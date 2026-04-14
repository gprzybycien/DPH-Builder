Create a prototype data product build bundle for `customer_360_uk`.

Requirements:
- Use the checked-in fixtures only
- Reuse candidate assets from `fixtures/assets.json`
- Use lineage information from `fixtures/lineage_graph.json`
- Select the best matching contract template
- Recommend masking/privacy rules
- Produce:
  - `output/build_bundle.json`
  - `output/draft_contract.yaml`
  - `output/policy_recommendations.json`
  - `output/prototype_plan.md`

Constraints:
- Do not add live integrations
- Do not mutate external systems
- Keep outputs deterministic and easy to inspect
