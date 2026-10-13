// String-level edits of library markup: lets a shot animate a named sub-group of an approved
// asset (lever, fill bar, chart bar, clock hand) without redrawing it.

/** Add attributes to the first `<g id="id"` tag (transform, opacity, style...). */
export function setGroup(m: string, id: string, attrs: Record<string, string | number>): string {
  const tag = `<g id="${id}"`;
  const i = m.indexOf(tag);
  if (i < 0) throw new Error(`group ${id} not found`);
  const extra = Object.entries(attrs).map(([k, v]) => ` ${k}="${v}"`).join("");
  return m.slice(0, i + tag.length) + extra + m.slice(i + tag.length);
}

/** Apply setGroup for several ids. */
export const setGroups = (m: string, groups: Record<string, Record<string, string | number>>) =>
  Object.entries(groups).reduce((acc, [id, a]) => setGroup(acc, id, a), m);

/** Remove an exact substring that must exist (used to take a mark off an asset so it can be drawn live). */
export function without(m: string, part: string): string {
  if (!m.includes(part)) throw new Error(`fragment not found: ${part.slice(0, 60)}`);
  return m.replace(part, "");
}

/** Scale about a point, as an SVG transform string. */
export const scaleAbout = (x: number, y: number, sx: number, sy = sx) =>
  `translate(${x} ${y}) scale(${sx} ${sy}) translate(${-x} ${-y})`;
export const rotateAbout = (deg: number, x: number, y: number) => `rotate(${deg} ${x} ${y})`;
