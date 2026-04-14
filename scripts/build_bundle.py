from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"
OUTPUT = ROOT / "output"


def load_json(name: str) -> Any:
    with open(FIXTURES / name, "r", encoding="utf-8") as f:
        return json.load(f)


def ensure_output_dir() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)


def choose_assets(assets_payload: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        asset
        for asset in assets_payload["assets"]
        if "customer" in asset.get("tags", []) and asset.get("market") == "UK"
    ]


def choose_template(templates_payload: dict[str, Any]) -> dict[str, Any]:
    for template in templates_payload["templates"]:
        if template.get("domain") == "customer":
            return template
    raise ValueError("No suitable template found")


def choose_rules(rules_payload: dict[str, Any]) -> list[dict[str, Any]]:
    return [rule for rule in rules_payload["rules"] if rule.get("market") == "UK"]


def build_bundle() -> dict[str, Any]:
    assets_payload = load_json("assets.json")
    lineage_search = load_json("lineage_search.json")
    lineage_graph = load_json("lineage_graph.json")
    templates_payload = load_json("contract_templates.json")
    rules_payload = load_json("data_protection_rules.json")

    selected_assets = choose_assets(assets_payload)
    selected_template = choose_template(templates_payload)
    selected_rules = choose_rules(rules_payload)

    return {
        "data_product": {
            "id": "customer_360_uk",
            "name": "Customer 360 UK",
            "domain": "customer",
            "market": "UK",
            "platform": "GCP"
        },
        "candidate_assets": selected_assets,
        "lineage_search_matches": lineage_search["matches"],
        "lineage_summary": {
            "root": lineage_graph["root"],
            "upstream": lineage_graph["upstream"],
            "downstream": lineage_graph["downstream"],
            "notes": lineage_graph["notes"]
        },
        "selected_contract_template": selected_template,
        "recommended_protection_rules": selected_rules,
        "next_actions": [
            "Draft contract from selected template",
            "Review lineage risks and downstream dependencies",
            "Confirm masking rules with governance owner",
            "Generate SQL/dbt implementation scaffold",
            "Replace fixtures with live MCP adapter"
        ]
    }


def write_outputs(bundle: dict[str, Any]) -> None:
    ensure_output_dir()

    with open(OUTPUT / "build_bundle.json", "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)

    contract_yaml = {
        "data_product": bundle["data_product"],
        "contract_template_id": bundle["selected_contract_template"]["template_id"],
        "required_fields": bundle["selected_contract_template"]["required_fields"],
        "sla": bundle["selected_contract_template"]["sla"],
        "privacy_defaults": bundle["selected_contract_template"]["privacy_defaults"],
        "source_assets": [a["asset_id"] for a in bundle["candidate_assets"]]
    }
    with open(OUTPUT / "draft_contract.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(contract_yaml, f, sort_keys=False)

    policy_recommendations = {
        "data_product_id": bundle["data_product"]["id"],
        "market": "UK",
        "recommendations": bundle["recommended_protection_rules"]
    }
    with open(OUTPUT / "policy_recommendations.json", "w", encoding="utf-8") as f:
        json.dump(policy_recommendations, f, indent=2)

    plan = f"""# Prototype Plan

## Selected product
- {bundle["data_product"]["id"]}

## Why these assets
- Customer-tagged UK assets were selected from the discovered container.

## What lineage says
- Root asset: {bundle["lineage_summary"]["root"]}
- Upstream count: {len(bundle["lineage_summary"]["upstream"])}
- Downstream count: {len(bundle["lineage_summary"]["downstream"])}

## Contract inheritance
- Template used: {bundle["selected_contract_template"]["template_id"]}

## Policy recommendation approach
- Recommend existing UK protection defaults before any live platform action.

## Next step in live MCP version
- Replace fixtures with MCP-backed calls for discovery, lineage, contract templates, and governance rule lookup.
"""
    with open(OUTPUT / "prototype_plan.md", "w", encoding="utf-8") as f:
        f.write(plan)


if __name__ == "__main__":
    bundle = build_bundle()
    write_outputs(bundle)
    print("Prototype outputs written to output/")
