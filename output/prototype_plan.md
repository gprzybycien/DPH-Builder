# Prototype Plan

## Selected product
- `customer_360_uk`

## Asset selection reasoning
### Selection criteria
1. **Market fit**: keep only assets with `market=UK` to avoid cross-market data mixing.
2. **Domain relevance**: prioritize assets tagged `customer` for Customer 360 scope.
3. **Reusability maturity**: prefer curated layers (`gold` first, then `silver`) to reduce transformation risk.
4. **Governance readiness**: prioritize assets already carrying PII-related tags so contract/policy inheritance is explicit.

### Selected assets and rationale
- `bq.customer_master` (`gold`, owner: `customer_platform`): chosen as the anchor record because it is curated, has the highest lineage confidence (`0.96`), and is described as a stable source.
- `bq.customer_interactions` (`silver`, owner: `engagement_team`): included to provide behavioral/event context; lineage confidence is high (`0.91`).
- `bq.customer_preferences` (`silver`, owner: `crm_team`): included for consent/preference enrichment; lineage confidence is acceptable (`0.88`) and carries PII context needed for policy mapping.

## Lineage interpretation and risk
### Observed lineage context
- **Root asset**: `bq.customer_master`
- **Upstream dependencies (2)**: `bq.raw_customer_profile`, `bq.raw_customer_consent`
- **Downstream consumers (2)**: `dashboard.customer_retention`, `ml.churn_features`
- **Lineage notes** indicate `customer_master` is stable and a downstream dashboard is business-critical.

### Risk assessment
| Risk area | Why it matters | Risk level | Mitigation for prototype/live handoff |
|---|---|---|---|
| Upstream schema drift | Raw profile/consent changes can silently break joins and consent semantics. | Medium | Add schema + contract compatibility checks before each build run. |
| Consent data integrity | Activation logic depends on accurate consent propagation from upstream. | High | Gate activation use cases on `consent_status` and add contract assertions. |
| Downstream blast radius | Changes to `customer_master` can impact retention dashboard and churn features. | High | Require impact review and versioned output before promoting contract changes. |
| Multi-owner coordination | Selected assets span 3 owners, increasing coordination latency. | Medium | Assign explicit owner approvals in build checklist before implementation stage. |

### Lineage-based decision
Use `bq.customer_master` as the canonical join spine, and treat the two `silver` assets as enrichments. This minimizes ambiguity in identity resolution while keeping behavior and preference coverage.

## Contract inheritance
- **Template used**: `customer360-market-template-v1`
- **Reasoning**: the template already encodes country-scoped fields (`country_code`), consent gating (`consent_status`), and UK-friendly privacy defaults (masking + in-market residency), so the draft can start from governed defaults instead of custom policy invention.

## Policy recommendation approach
- Apply existing UK defaults first (`email` hash, `phone` partial mask, `consent_status` activation gate).
- Keep recommendations declarative in outputs only; do not execute live platform mutations in this prototype.

## Next step in live MCP version
1. Replace fixture reads with MCP discovery + lineage calls.
2. Add automated lineage risk checks (schema drift, downstream impact scoring).
3. Run template inheritance and policy lookup as pre-build validation gates.
4. Generate implementation scaffolds only after governance/owner sign-off.
