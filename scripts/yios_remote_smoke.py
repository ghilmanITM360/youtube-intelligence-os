"""Explicitly authorized live smoke test in a unique, non-production Git namespace.

Two independent local Git clients share the existing remote. This proves remote
protocol behavior, never two actual Macs or accepted production research. Ref and
client histories are retained even after success; failed ownership is not stolen.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
from pathlib import Path
import socket
import subprocess
import tempfile
import threading
import uuid

from scripts.yios import Workflow, write_json
from scripts.yios_coordination import Coordination, CoordinationError, Git, utc
from scripts.yios_workspace import check_safety, sha256


PROTECTED = (
    "main", "research/finance-economics-intelligence",
    "research/casually-finance-editing-forensics", "codex/casually-finance-forensic-research",
    "codex/what-if-archive-main-integration", "codex/casually-finance-knowledge-navigation",
)


def run_smoke(repo: Path, output: Path, five_hour: float, weekly: float) -> dict:
    source = Git(repo)
    safety = dict(checked_utc=utc(), five_hour=five_hour, weekly=weekly,
                  context_reserve="AVAILABLE_UNMETERED", paid_credits=0,
                  source="OPERATOR_CURRENT_METER_READING; NO_CREDITS_REDEEMED")
    check_safety(safety, repo)
    operation = uuid.uuid4().hex
    namespace = "yios-test/" + operation + "/claims"
    workspace = Path(tempfile.mkdtemp(prefix="yios-remote-smoke-"))
    receipt = dict(status="IN_PROGRESS", started_utc=utc(), namespace=namespace,
                   real_host=socket.gethostname(), real_two_mac_testing="NOT_TESTED",
                   simulated_clients=True, preserved_workspace=str(workspace),
                   canonical_mutations="NONE", safety=safety, checks=[], refs={})
    write_json(output, receipt)

    def checked(name, **detail):
        receipt["checks"].append({"check": name, "result": "PASS", **detail})
        write_json(output, receipt)

    try:
        before = {branch: source.head("refs/heads/" + branch) for branch in PROTECTED}
        receipt["protected_heads_before"] = before
        remote = source.run("remote", "get-url", "origin")
        name = source.run("config", "user.name")
        email = source.run("config", "user.email")
        clients = []
        for label in ("simulated-client-a", "simulated-client-b"):
            path = workspace / label
            subprocess.run(["git", "init", str(path)], check=True, capture_output=True)
            git = Git(path)
            git.run("config", "user.name", name)
            git.run("config", "user.email", email)
            git.run("config", "commit.gpgsign", "false")
            git.run("remote", "add", "origin", remote)
            clients.append(Coordination(git, namespace=namespace, machine=label))
        task, separate = "finance/TEST0000001", "finance/TEST0000002"
        barrier = threading.Barrier(2)

        def claim(client):
            barrier.wait()
            try:
                return client.acquire(task, None, channel_id="NON_PRODUCTION_TEST_CHANNEL")
            except CoordinationError as exc:
                return {"rejected": str(exc)}

        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(claim, clients))
        winners = [i for i, value in enumerate(results) if isinstance(value, tuple)]
        if len(winners) != 1:
            raise CoordinationError("Live simultaneous claim did not yield exactly one writer: " + str(results))
        index = winners[0]
        winner, other = clients[index], clients[1 - index]
        claim_sha, state = results[index]
        if other.read(task)[0] != claim_sha:
            raise CoordinationError("Independent client could not reconcile winning remote claim")
        checked("LIVE_SAME_VIDEO_DOUBLE_WRITER_EXCLUDED", winner=winner.machine,
                winning_sha=claim_sha, loser=results[1 - index])
        second_sha, second = other.acquire(separate, None, channel_id="NON_PRODUCTION_TEST_CHANNEL")
        checked("LIVE_DIFFERENT_VIDEO_INDEPENDENT_CLAIM", remote_sha=second_sha)
        try:
            other.transition(task, claim_sha, state["token"], "RELEASED")
        except CoordinationError:
            if winner.read(task)[0] != claim_sha:
                raise CoordinationError("Wrong-owner attempt changed remote state")
            checked("LIVE_WRONG_OWNER_RELEASE_REJECTED")
        else:
            raise CoordinationError("Wrong-owner release unexpectedly succeeded")

        git = winner.git
        git.run("commit", "--allow-empty", "-m", "test: non-production checkpoint seed")
        branch = "yios-test/" + operation + "/checkpoint"
        git.run("switch", "-c", branch)
        base = git.run("rev-parse", "HEAD")
        workflow = Workflow(git.repo, winner.machine, namespace=namespace)
        write_json(workflow.local / "safety.json", safety)
        write_json(workflow.local / "session.json", {
            "task": task, "claim_sha": claim_sha, "token": state["token"], "branch": branch,
            "source_base": base, "machine": winner.machine,
        })
        folder = git.repo / "research/tasks" / task
        folder.mkdir(parents=True)
        note = folder / "notes.md"
        note.write_text("NON-PRODUCTION PARTIAL PROTOCOL FIXTURE. No accepted audit.\n")
        write_json(folder / "CHECKPOINT.json", {
            "task": task, "video_id": "TEST0000001", "channel_id": "NON_PRODUCTION_TEST_CHANNEL",
            "status": "PARTIAL", "source_base": base, "completed_stages": ["fixture-checkpoint"],
            "remaining_stages": ["fixture-review-not-performed"],
            "continuation": "Protocol fixture only; no production research to continue.",
            "source_fingerprints": {"fixture-note": sha256(note)}, "media": [], "artifacts": [],
        })
        saved = workflow.save([str(note.relative_to(git.repo))])
        checkpoint = saved["checkpoint_commit"]
        receipt["refs"]["refs/heads/" + branch] = checkpoint
        checked("LIVE_PARTIAL_CHECKPOINT_PUBLISHED", checkpoint=checkpoint)
        release = workflow.switch_to(other.machine)
        released_sha, released = other.read(task)
        if released_sha != release["release_sha"] or released["status"] != "RELEASED":
            raise CoordinationError("Explicit writer release unverified")
        other.git.fetch("refs/heads/" + branch, checkpoint)
        other.git.run("switch", "-c", "restored-fixture", checkpoint)
        restored = json.loads((other.git.repo / "research/tasks" / task / "CHECKPOINT.json").read_text())
        if restored["status"] != "PARTIAL" or not restored["remaining_stages"]:
            raise CoordinationError("Restored unfinished checkpoint changed its acceptance status")
        for artifact in restored["artifacts"]:
            path = other.git.repo / artifact["path"]
            if path.stat().st_size != artifact["bytes"] or sha256(path) != artifact["sha256"]:
                raise CoordinationError("Independent checkpoint restore hash mismatch")
        if other.git.run("rev-parse", "HEAD") != checkpoint:
            raise CoordinationError("Independent restored HEAD mismatch")
        checked("LIVE_INDEPENDENT_CONTEXT_PARTIAL_RESTORE_SHA256", checkpoint=checkpoint)
        acquired_sha, acquired = other.acquire(task, released_sha, channel_id="NON_PRODUCTION_TEST_CHANNEL")
        checked("LIVE_EXPLICIT_RELEASE_AND_REACQUISITION", acquired_sha=acquired_sha)
        end, _ = other.transition(task, acquired_sha, acquired["token"], "RELEASED",
                                  checkpoint=checkpoint, task_branch=branch,
                                  acceptance="PARTIAL", continuation="Remote smoke fixture complete; retained for inspection")
        end_second, _ = other.transition(separate, second_sha, second["token"], "RELEASED",
                                         acceptance="PARTIAL", continuation="Remote smoke fixture complete; no research started")
        receipt["refs"][other.ref(task)] = end
        receipt["refs"][other.ref(separate)] = end_second
        for ref, expected in receipt["refs"].items():
            if source.head(ref) != expected:
                raise CoordinationError("Final remote fixture SHA mismatch: " + ref)
        after = {branch: source.head("refs/heads/" + branch) for branch in PROTECTED}
        receipt["protected_heads_after"] = after
        if before != after:
            raise CoordinationError("Protected branch changed during smoke; inspect before claiming preservation")
        checked("LIVE_FINAL_REFS_RELEASED_AND_PROTECTED_HEADS_UNCHANGED")
        receipt.update(status="REMOTELY_VERIFIED", finished_utc=utc(),
                       active_test_writers=0, production_acceptance="NOT_CLAIMED")
    except Exception as exc:
        receipt.update(status="BLOCKED_PRESERVED", finished_utc=utc(), error=str(exc),
                       recovery="Retain local contexts and remote refs; inspect exact owners before any release")
        write_json(output, receipt)
        raise
    write_json(output, receipt)
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--five-hour", type=float, required=True)
    parser.add_argument("--weekly", type=float, required=True)
    args = parser.parse_args(argv)
    try:
        receipt = run_smoke(args.repo, args.output, args.five_hour, args.weekly)
        print(json.dumps({"status": receipt["status"], "receipt": str(args.output),
                          "namespace": receipt["namespace"], "checks": len(receipt["checks"])}))
        return 0
    except (CoordinationError, OSError, ValueError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "BLOCKED_PRESERVED", "receipt": str(args.output), "error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
