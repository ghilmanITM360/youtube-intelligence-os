import test from 'node:test';
import assert from 'node:assert/strict';
import { beatMapForDisplay, publicationDateForUtcDisplay, structuredValueForDisplay } from './workbook_formatting.mjs';

test('publication timestamp with an offset displays as the same UTC instant near a date boundary', () => {
  const displayed = publicationDateForUtcDisplay('2025-12-31T23:30:00-02:00');
  assert.equal(displayed.getUTCFullYear(), 2026);
  assert.equal(displayed.getUTCMonth(), 0);
  assert.equal(displayed.getUTCDate(), 1);
  assert.equal(displayed.getUTCHours(), 1);
  assert.equal(displayed.getUTCMinutes(), 30);
  assert.equal(publicationDateForUtcDisplay('2025-12-31'), '2025-12-31');
});

test('structured, scalar, empty and null beat maps have readable displays', () => {
  const structured = beatMapForDisplay([
    { character_range: [0, 5000], beat: 'Opening promise' },
    { character_range: [5000, 10000], beat: 'Worked example' },
  ]);
  assert.equal(structured, '0–5,000 chars: Opening promise → 5,000–10,000 chars: Worked example');
  assert.equal(beatMapForDisplay(['Hook', 'Payoff']), 'Hook → Payoff');
  assert.equal(beatMapForDisplay([], 'Legacy chain'), 'Legacy chain');
  assert.equal(beatMapForDisplay(null, ''), 'PENDING');
  assert.doesNotMatch(structured, /\[object Object\]/);
  assert.equal(
    structuredValueForDisplay([{ claim: 'Fee claim', status: 'Needs source' }]),
    'claim: Fee claim; status: Needs source',
  );
});
