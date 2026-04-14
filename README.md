# DPH Codex Prototype

Prototype for a coding-agent-assisted data product builder using DPH-style context:
- asset discovery
- lineage reasoning
- contract/template inheritance
- policy recommendation
- draft build bundle generation

## Goal
Given a request like:
"Create a new Customer 360 UK data product from existing GCP assets"

the prototype should:
1. discover candidate assets
2. inspect lineage
3. select a contract template
4. recommend data protection rules
5. produce:
   - output/build_bundle.json
   - output/draft_contract.yaml
   - output/policy_recommendations.json
   - output/prototype_plan.md

## Important constraints
- Start from checked-in fixtures, not live platform calls
- Treat contracts and protection rules as governed inputs
- Do not directly mutate GCP services
- Produce proposals and drafts first

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/build_bundle.py
python scripts/validate_contract.py
```

## Codex task pattern
Ask Codex to:
- read AGENTS.md
- read docs/tool-map.md
- use the dph-builder skill
- generate the build bundle from fixtures
- keep policy actions in recommendation form
