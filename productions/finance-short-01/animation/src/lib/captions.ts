interface Caption { shot: string; text: string; from: number; to: number }
interface ShotSpan { id: string; from: number; to: number }
export const activeCaption = (frame: number, captions: Caption[], shots: ShotSpan[]) => {
  const index = captions.findIndex((c, k) => {
    const shot = shots.find((s) => s.id === c.shot);
    if (!shot) throw new Error(`caption references missing shot ${c.shot}`);
    const end = Math.min(c.to + 12, captions[k + 1]?.from ?? Infinity, shot.to);
    return frame >= c.from && frame < end && frame >= shot.from;
  });
  if (index < 0) return null;
  const caption = captions[index];
  const shot = shots.find((s) => s.id === caption.shot)!;
  const end = Math.min(caption.to + 12, captions[index + 1]?.from ?? Infinity, shot.to);
  return {caption, end};
};

export const CAPTION_METRICS = { centerX: 470, maxWidth: 840, paddingX: 70, defaultY: 1530, maxSize: 56 };
export const CAPTION_Y: Record<string, number> = { S01A: 720, S01B: 720, S02A: 560, S07B: 200, S09A: 1335, S09B: 1335 };
export const captionLayout = (text: string, cy: number, max = CAPTION_METRICS.maxSize) => {
  const size = Math.min(max, (CAPTION_METRICS.maxWidth - CAPTION_METRICS.paddingX) / (text.length * 0.56));
  const width = text.length * size * 0.56 + CAPTION_METRICS.paddingX;
  const height = size * 1.18 + 34;
  return {size, width, height, x: CAPTION_METRICS.centerX - width / 2, y: cy - height / 2};
};
