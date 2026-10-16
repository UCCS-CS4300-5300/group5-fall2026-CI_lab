# CI Practice Lab — Behavioral Contract

This is a **teaching example**, not the HW3 PeakPass specification.

## Shipping
- Shipping costs $7 when the order total is **$50 or less**.
- Shipping is free only when the total is **greater than $50**.

## Age validation
- `visitor_age` must be a **non-negative integer** (zero is permitted by the age constraint).
- Negative ages are invalid and must raise `ValueError`.
- This simple practice function has no additional age-related eligibility rules.

Do not infer these rules apply to a team's Sprint 2 project.
