const EXPLICIT_OFFSET = /(Z|[+-]\d{2}:?\d{2})$/i;

export function publicationDateForUtcDisplay(value) {
  if (typeof value !== 'string' || !EXPLICIT_OFFSET.test(value)) return value;
  const instant = new Date(value);
  if (Number.isNaN(instant.getTime())) return value;
  return instant;
}

function readableValue(value) {
  if (value === null || value === undefined || value === '') return '';
  if (Array.isArray(value)) return value.map(readableValue).filter(Boolean).join(', ');
  if (typeof value === 'object') {
    return Object.entries(value)
      .map(([key, item]) => {
        const rendered = readableValue(item);
        return rendered ? `${key.replaceAll('_', ' ')}: ${rendered}` : '';
      })
      .filter(Boolean)
      .join('; ');
  }
  return String(value);
}

export function structuredValueForDisplay(value, fallback = 'PENDING') {
  const rendered = readableValue(value);
  return rendered || fallback;
}

export function beatMapForDisplay(beatMap, legacyNarrativeChain) {
  if (beatMap === null || beatMap === undefined || beatMap === '') {
    return legacyNarrativeChain || 'PENDING';
  }
  const beats = Array.isArray(beatMap) ? beatMap : [beatMap];
  const rendered = beats.map((item) => {
    if (item === null || item === undefined || item === '') return '';
    if (typeof item !== 'object') return String(item);
    const label = readableValue(item.beat ?? item.title ?? item.label ?? item.description);
    const range = Array.isArray(item.character_range) && item.character_range.length === 2
      ? `${item.character_range[0].toLocaleString('en-US')}–${item.character_range[1].toLocaleString('en-US')} chars`
      : '';
    if (label) return range ? `${range}: ${label}` : label;
    return structuredValueForDisplay(item, '');
  }).filter(Boolean);
  return rendered.length ? rendered.join(' → ') : (legacyNarrativeChain || 'PENDING');
}
