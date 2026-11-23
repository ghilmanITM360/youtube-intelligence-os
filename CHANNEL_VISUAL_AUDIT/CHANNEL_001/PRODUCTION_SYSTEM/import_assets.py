"""Deprecated entry point. Validation is now type-aware and never writes the registry: use pipeline.py (validate / review / approve / rollback)."""
import sys, pipeline
sys.exit(pipeline.main(['validate'] + sys.argv[1:]))
