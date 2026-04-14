---
name: dph-builder
description: Use this skill when building or refining a DPH-style governed data product from fixtures or MCP-shaped inputs.
---

# DPH Builder Skill

## When to use
Use this skill when the task involves:
- building a new data product draft
- asset discovery
- lineage reasoning
- contract inheritance
- policy recommendation
- generating build bundles

## Required reading
Before doing any work:
1. Read `AGENTS.md`
2. Read `docs/prototype-goal.md`
3. Read `docs/tool-map.md`

## Workflow
1. Inspect `fixtures/assets.json`
2. Inspect `fixtures/lineage_search.json`
3. Inspect `fixtures/lineage_graph.json`
4. Inspect `fixtures/contract_templates.json`
5. Inspect `fixtures/data_protection_rules.json`
6. Generate:
   - `output/build_bundle.json`
   - `output/draft_contract.yaml`
   - `output/policy_recommendations.json`
   - `output/prototype_plan.md`

## Rules
- Prefer reuse over invention
- Keep outputs machine-readable
- Recommend policies; do not directly execute platform mutations
- Treat lineage as dependency context, not as executable logic
- Treat source code as implementation detail after product context is assembled

## Output expectations
### build_bundle.json
Should contain:
- requested product id/name
- market
- domain
- candidate source assets
- lineage summary
- selected contract template
- recommended rules
- next build actions
