"""Export the FastAPI OpenAPI schema to packages/contracts/openapi.json.

Run from the repo root via `npm run contracts:export`, or directly from apps/api.
"""

import json
import sys
from pathlib import Path

API_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = API_DIR.parents[1]
sys.path.insert(0, str(API_DIR))

from app.main import app

OUT = REPO_ROOT / "packages" / "contracts" / "openapi.json"


def main() -> None:
    OUT.write_text(json.dumps(app.openapi(), indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
