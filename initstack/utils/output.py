# initstack/utils/output.py
import os

PLAIN = os.environ.get("INITSTACK_PLAIN") == "1"

def info(msg):
    print(msg if PLAIN else f"ℹ {msg}")

def success(msg):
    print(msg if PLAIN else f"✅ {msg}")

def error(msg):
    print(msg if PLAIN else f"❌ {msg}")
