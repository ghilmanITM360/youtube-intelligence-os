"""Portable validated packaging research must not depend on local raw image bytes."""
import copy
import json
from pathlib import Path

import pytest
from scripts.validate_packaging_research import validate

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / 'docs/research/packaging-validated-2026-10-11/records.json'


def test_genius_history_packet_is_complete_and_portable():
    packet = json.loads(PACKET.read_text())
    assert validate(packet) == []
    assert len(packet['records']) == 10
    assert all(row['qa']['status'] in {'PASS', 'PASS_WITH_CORRECTIONS', 'HISTORICAL_SAMPLE'} for row in packet['records'])


@pytest.mark.parametrize('mutation', ['identity', 'hash', 'duplicate', 'qa', 'score'])
def test_invalid_packet_is_rejected(mutation):
    packet = copy.deepcopy(json.loads(PACKET.read_text()))
    row = packet['records'][0]
    if mutation == 'identity':
        row['package_audit']['Video_ID'] = 'wrongvideo1'
    elif mutation == 'hash':
        row['provenance']['source_sha256'] = 'bad'
    elif mutation == 'duplicate':
        packet['records'].append(copy.deepcopy(row))
    elif mutation == 'qa':
        row['qa']['status'] = 'NOT_STARTED'
    else:
        row['thumbnail_audit']['score_100'] += 1
    assert validate(packet)
