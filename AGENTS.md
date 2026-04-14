# AGENTS.md

## Repo purpose
This repo prototypes a DPH-style build workflow for new data products using a coding agent.

## Required workflow
Before changing code, always:
1. Read `docs/prototype-goal.md`
2. Read `docs/tool-map.md`
3. Read `.agents/skills/dph-builder/SKILL.md`

## Working rules
- Prefer fixture-driven development before live integration
- Use lineage and asset discovery as read-first context
- Treat contracts and protection rules as governed inputs
- Do not directly implement live GCP mutations in this prototype
- Produce machine-readable outputs in `output/`

## Deliverables
For the main workflow, maintain:
- `output/build_bundle.json`
- `output/draft_contract.yaml`
- `output/policy_recommendations.json`
- `output/prototype_plan.md`

## Coding style
- Python 3.11+
- Small pure functions
- JSON/YAML outputs should be deterministic
- Add comments only where they clarify behavior
