import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "build_local_media_library.py"
SPEC = importlib.util.spec_from_file_location("build_local_media_library", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_extracts_only_bracketed_eleven_character_video_id():
    assert MODULE.extract_video_id(Path("A title [mNLNb-Z4T0M].mp4")) == (
        "mNLNb-Z4T0M",
        "HIGH",
        "FILENAME_BRACKETED_YOUTUBE_ID",
    )
    assert MODULE.extract_video_id(Path("A title without id.mp4")) == (
        "",
        "UNKNOWN",
        "NO_RELIABLE_ID_IN_FILENAME",
    )


def test_atomic_copy_is_idempotent_and_detects_conflict(tmp_path):
    source = tmp_path / "source.mp4"
    destination = tmp_path / "nested" / "destination.mp4"
    source.write_bytes(b"source bytes")
    digest = MODULE.sha256_file(source)
    assert MODULE.atomic_copy(source, destination, digest) == ("COPIED_VERIFIED", "")
    assert MODULE.atomic_copy(source, destination, digest) == ("VERIFIED_EXISTING", "")
    destination.write_bytes(b"different bytes")
    status, error = MODULE.atomic_copy(source, destination, digest)
    assert status == "DESTINATION_CONFLICT"
    assert "does not match source" in error
