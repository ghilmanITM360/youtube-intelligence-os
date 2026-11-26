"""Phase 7 holdout: the 12 long videos NOT in the coding sample (odd positions), same selection rule, same frozen scheme."""
import re,sys,runpy
src=open('/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/scripts/phase7_sample.py').read()
src=src.replace("[::2]","[1::2]").replace("phase7_frames/","holdout7/").replace("07_SAMPLE_FRAMES.csv","07_HOLDOUT_FRAMES.csv")
exec(compile(src,'phase7_holdout','exec'))
