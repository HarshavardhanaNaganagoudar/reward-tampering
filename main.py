
import tools
import shutil
from pathlib import Path
from datetime import datetime

from agent import run_agent
from tools import REWARD_FILE


OUTPUT_DIR = Path(__file__).parent / "outputs"


def main():

    # Create a unique run directory
    run_number = len(list(OUTPUT_DIR.glob("run_*"))) + 1

    run_dir = OUTPUT_DIR / f"run_{run_number:02d}"
    run_dir.mkdir(parents=True, exist_ok=False)
    tools.LOG_FILE = run_dir / "experiment_log.txt"

    print("=" * 50)
    print("REWARD TAMPERING EXPERIMENT")
    print("=" * 50)

    print(f"Run: {run_number:02d}")

    # Preserve original reward functions
    shutil.copy(
        REWARD_FILE,
        run_dir / "reward_functions_initial.py"
    )

    print("\nStarting Gemma...\n")

    run_agent()

    # Preserve final reward functions
    shutil.copy(
        REWARD_FILE,
        run_dir / "reward_functions_final.py"
    )

    print("\nExperiment completed.")
    print(f"Results saved in: {run_dir}")


if __name__ == "__main__":
    main()
