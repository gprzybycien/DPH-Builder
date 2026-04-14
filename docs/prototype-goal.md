# Prototype Goal

Prototype a coding-agent workflow that can draft a new data product using DPH-like context.

## Main scenario
Create `customer_360_uk` from existing GCP assets while:
- reusing discovered source assets
- using lineage to understand dependencies
- inheriting a contract template
- recommending masking/privacy rules
- avoiding direct platform mutation

## Success criteria
A successful run produces:
1. `build_bundle.json`
2. `draft_contract.yaml`
3. `policy_recommendations.json`
4. `prototype_plan.md`

## Out of scope
- live GCP writes
- direct BigQuery masking updates
- full graph database
- full MCP runtime integration
