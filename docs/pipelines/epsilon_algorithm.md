---
status: working-definition
layer: docs/pipelines/
---

# ε-Filtration Algorithm

## Purpose

Defines the executable procedure for ε-filtration.

---

# Algorithm

Given:

- BC grid points b_i
- observable O_i
- epsilon set E

For each ε in E:

1. For each neighbor pair (i, i+1):
   compute ΔO = |O[i+1] - O[i]|

2. Compute threshold τ(ε)

3. If ΔO < τ:
   mark edge active

4. Assign membership:
   m[i] = 1 if any adjacent edge active

Aggregate:

- height[i] += m[i]

Track:

- ε_enter
- ε_leave

---

# Output

- height field
- entry scale
- persistence width
