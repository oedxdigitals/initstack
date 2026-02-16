# initstack/core/environment.py
import os
import platform

def detect_environment():
    if "TERMUX_VERSION" in os.environ or os.path.exists("/data/data/com.termux"):
        return "termux"
    if os.environ.get("RNX_WORKSPACE"):
        return "rnx"
    system = platform.system().lower()
    return system
