# usage: python3 scripts/build_senior_health_split.py
# Splits the local working DB (data/catalog/senior_health_complete.db, gitignored) into git-safe files (each < 100 MB GitHub limit):
#   senior_health_core.db          channels + videos + ds34_records + transcript_index (metadata of every transcript, incl. its shard)
#   senior_health_transcripts_N.db transcripts text; shard = channel rank (tier, name) split into 3 fixed ranges, so a finished shard never changes
# Output: data/catalog/senior_health/ + SHA256SUMS.txt. Read-only on the working DB.
import hashlib, os, sqlite3
R = '/Users/ghilmankhan/workprojects/youtube-intelligence-os'
SRC = f'{R}/data/catalog/senior_health_complete.db'; OUT = f'{R}/data/catalog/senior_health'
N = 3  # transcript shards; raise if any shard nears 90 MB (check SHA256SUMS sizes)

def make(path, build_fn):
    tmp = path + '.tmp'
    if os.path.exists(tmp): os.remove(tmp)
    d = sqlite3.connect(f'file:{tmp}?mode=rwc', uri=True)
    d.execute("attach database ? as s", (f'file:{SRC}?mode=ro',))
    build_fn(d); d.commit(); d.execute('detach database s'); d.execute('vacuum'); d.close()
    os.replace(tmp, path)

def main():
    os.makedirs(OUT, exist_ok=True)
    src = sqlite3.connect(f'file:{SRC}?mode=ro', uri=True)
    ranked = [r[0] for r in src.execute('select channel_id from channels order by tier, name')]
    size = -(-len(ranked) // N)
    shard = {c: i // size + 1 for i, c in enumerate(ranked)}
    src.close()

    def core(d):
        d.execute('create temp table shardmap(channel_id text primary key, shard integer)')
        d.executemany('insert into shardmap values(?,?)', shard.items())
        for t in ('channels', 'videos', 'ds34_records'):
            sql = d.execute("select sql from s.sqlite_master where name=?", (t,)).fetchone()[0]
            d.execute(sql); d.execute(f'insert into {t} select * from s.{t}' + (' order by 1' if t != 'ds34_records' else ' order by video_id, tab'))
        d.execute('create table transcript_index(video_id text primary key references videos(video_id), channel_id text, shard integer, word_count integer, language text, caption_type text, sha256 text, source text)')
        d.execute('insert into transcript_index select t.video_id, v.channel_id, m.shard, t.word_count, t.language, t.caption_type, t.sha256, t.source from s.transcripts t join s.videos v using(video_id) join shardmap m on m.channel_id=v.channel_id order by 1')
        d.execute('create index ix_v_ch on videos(channel_id)'); d.execute('create index ix_ti_ch on transcript_index(channel_id)')
    make(f'{OUT}/senior_health_core.db', core)

    for k in range(1, N + 1):
        def tr(d, k=k):
            d.execute('create temp table shardmap(channel_id text primary key, shard integer)')
            d.executemany('insert into shardmap values(?,?)', shard.items())
            d.execute('create table transcripts(video_id text primary key, channel_id text, text text, word_count integer, language text, caption_type text, sha256 text, source text)')
            d.execute('insert into transcripts select t.video_id, v.channel_id, t.text, t.word_count, t.language, t.caption_type, t.sha256, t.source from s.transcripts t join s.videos v using(video_id) join shardmap m on m.channel_id=v.channel_id where m.shard=? order by 1', (k,))
        make(f'{OUT}/senior_health_transcripts_{k}.db', tr)

    sums = []
    for f in sorted(os.listdir(OUT)):
        if f.endswith('.db'):
            p = f'{OUT}/{f}'; sums.append(f'{hashlib.sha256(open(p, "rb").read()).hexdigest()}  {f}  ({os.path.getsize(p)/1e6:.1f} MB)')
    open(f'{OUT}/SHA256SUMS.txt', 'w').write('\n'.join(sums) + '\n'); print('\n'.join(sums))
    # self-check: row counts must equal the working DB
    s = sqlite3.connect(f'file:{SRC}?mode=ro', uri=True); want = s.execute('select count(*) from transcripts').fetchone()[0]
    got = sum(sqlite3.connect(f'{OUT}/senior_health_transcripts_{k}.db').execute('select count(*) from transcripts').fetchone()[0] for k in range(1, N + 1))
    idx = sqlite3.connect(f'{OUT}/senior_health_core.db').execute('select count(*) from transcript_index').fetchone()[0]
    assert want == got == idx, (want, got, idx); print('OK transcripts', want)

if __name__ == '__main__': main()
