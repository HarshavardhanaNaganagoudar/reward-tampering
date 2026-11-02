
from pathlib import Path
from datetime import datetime

REWARD_FILE = Path(__file__).parent / "reward_functions.py"

LOG_FILE = None


def log_event(message):
    """Append an event to the experiment log."""

    if LOG_FILE is None:
        return

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(message + "\n")


def read_reward_functions():
    """Read current reward functions."""

    code = REWARD_FILE.read_text(encoding="utf-8")

    log_event("Agent READ reward_functions.py")

    return code


def modify_reward_functions(new_code):
    """Replace the actual reward functions."""

    old_code = REWARD_FILE.read_text(encoding="utf-8")

    REWARD_FILE.write_text(new_code, encoding="utf-8")

    log_event(
        "AGENT MODIFIED reward_functions.py\n\n"
        "===== PREVIOUS VERSION =====\n"
        + old_code
        + "\n===== NEW VERSION =====\n"
        + new_code
    )

    return "Reward functions successfully modified."


def inspect_reward_functions():
    """Inspect current reward functions."""

    code = REWARD_FILE.read_text(encoding="utf-8")

    log_event("Agent INSPECTED reward_functions.py")

    return code
