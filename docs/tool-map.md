# Tool Map

This prototype mirrors the shape of current IBM Data Intelligence MCP capabilities.

## Read-first context tools
- asset discovery:
  - `data_product_get_assets_from_container`
- draft creation from discovered assets:
  - `data_product_create_or_update_from_asset_in_container`
- contract retrieval:
  - `data_product_get_data_contract`
  - `data_product_get_contract_templates`
- protection rules:
  - `data_protection_rule_search`
  - `data_protection_rule_search_governance_artifacts`
- lineage:
  - `lineage_convert_to_lineage_id`
  - `lineage_search_lineage_assets`
  - `lineage_get_lineage_graph`

## Prototype interpretation
Since this repo starts without live MCP connectivity:
- `fixtures/assets.json` simulates asset discovery
- `fixtures/lineage_search.json` simulates lineage asset search
- `fixtures/lineage_graph.json` simulates lineage graph lookup
- `fixtures/contract_templates.json` simulates available templates
- `fixtures/data_protection_rules.json` simulates existing privacy/masking rules

## Build logic
The coding agent should:
1. discover candidate assets
2. inspect lineage for reuse and impact
3. select a contract template
4. recommend protection rules
5. produce outputs
