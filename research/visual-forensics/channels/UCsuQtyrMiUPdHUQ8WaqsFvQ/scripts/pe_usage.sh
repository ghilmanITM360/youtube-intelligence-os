#!/bin/zsh
# Reads the provider meter from the headless CLI's rate_limit_event (one tiny Haiku call, no tools). Prints JSON or UNKNOWN.
cd $HOME/YIOS-local-audits/primitive-education
perl -e 'alarm 120; exec @ARGV' claude -p "reply ok" --model haiku --output-format stream-json --verbose --max-turns 1 --strict-mcp-config --mcp-config '{"mcpServers":{}}' --setting-sources "" < /dev/null 2>/dev/null | /usr/bin/python3 -c '
import sys,json,datetime
for l in sys.stdin:
    try: d=json.loads(l)
    except Exception: continue
    if d.get("type")=="rate_limit_event":
        u=d["rate_limit_info"].get("unifiedWindows",{}); f=u.get("five_hour",{}); w=u.get("seven_day",{})
        print(json.dumps(dict(five_hour=f.get("utilization"),five_hour_reset=f.get("resetsAt"),seven_day=w.get("utilization"),seven_day_reset=w.get("resetsAt"),overage=d["rate_limit_info"].get("isUsingOverage"),read_utc=datetime.datetime.utcnow().isoformat()+"Z"))); sys.exit(0)
print("UNKNOWN"); sys.exit(1)'
