from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"


def main() -> None:
    contract_path = OUTPUT / "draft_contract.yaml"
    if not contract_path.exists():
        raise FileNotFoundError("draft_contract.yaml not found. Run build_bundle.py first.")

    with open(contract_path, "r", encoding="utf-8") as f:
        contract = yaml.safe_load(f)

    required_top_level = ["data_product", "contract_template_id", "required_fields", "sla", "privacy_defaults", "source_assets"]
    missing = [key for key in required_top_level if key not in contract]

    if missing:
        raise ValueError(f"Contract missing required keys: {missing}")

    print("Contract validation passed.")


if __name__ == "__main__":
    main()
