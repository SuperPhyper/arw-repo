---
status: note
---

# Research Journal — Session 2026-03-18: Observable Decomposition

### Context

Starting point: the observation that a formalized observable must be
decomposable into combinations of basis relations between parameters —
and these can be traced back to independent BC classes, possibly outside
the original scope (latent degrees of freedom).

Conducted for: r_ss (Kuramoto), var_rel (double pendulum),
lambda_proxy (double pendulum), σ²(θ) (Kuramoto).

---

### Finding 1: Pre-scope substrate [claim]

Every non-trivial observable π carries a hierarchical substrate of
assumptions serving its algebraic and topological well-definedness,
which precedes the scope definition S = (B, Π, Δ, ε).

For r_ss, ~25 assumptions across 7 levels (A0–A6) were identified.
Exactly one (A5.2: phase ψ discarded) is an explicit scope decision.
All others are pre-scope.

Reference: `docs/advanced/observable_decomposition.md`

---

### Finding 2: Observable range R(π) [claim]

The subset of parameter space on which all pre-scope assumptions are
stable under Δ defines the observable range R(π). Z(π) is the exclusion
zone — structurally unreliable not due to scope failure but substrate violation.

```
R(r_ss)         = { κ ≪ κ_c } ∪ { κ ≫ κ_c }       Z: κ ≈ κ_c
R(var_rel)      = { E < E_diff, |Δθ| ≪ 2π }        Z: diffusion + phase wrapping
R(lambda_proxy) = { λ_true ≫ 0 } ∪ { λ_true ≪ 0 }  Z: transitions, weak chaos
R(σ²(θ))        = { σ(θ) ≪ π, P(θ) unimodal }      Z: Z_shared + wrap + multi
```

Reference: `docs/glossary/observable_range.md`

---

### Finding 3: BC structure of observables [claim]

```
r_ss         = Dissipation ∘ Restriction³ ∘ Aggregation
var_rel      = Scaling ∘ Aggregation² ∘ Restriction³
lambda_proxy = Approximation ∘ Dissipation³ ∘ Restriction²
σ²(θ)        = Dissipation ∘ Aggregation² ∘ Restriction³
```

All four are Restriction-dominated. All four blind to higher moments of P(θ).

---

### Finding 4: S¹ embedding as two-layer structure [interpretation]

φ: R → R/2πZ ≅ S¹ carries:
- Topological layer: π₁(S¹) = Z → winding numbers as latent DOF
- Algebraic layer: group structure + Haar measure → prerequisite for S5

Both are meta-assumptions about X, prior to scope. Whether this belongs
to Restriction BC or a meta-layer is open (Q_NEW_1).

---

### Finding 5: lambda_proxy structurally insufficient by construction [claim]

A6.1 and A6.2 are violated by construction — not fixable by better
measurement. Confirms primary: false in CASE-0003 with structural justification.

---

### Finding 6: F0 as new falsification category [hypothesis]

```
F0: R(π) ∩ B ≠ B
    Severity: observable_replacement
    Distinct from: scope_rejection, observable_insufficiency
```

Not yet integrated into falsification schema.

---

### Finding 7: Product scope admissibility [interpretation]

S_joint = S_1 ×_B S_2 is admissible by definition of the scope tuple.
No proof needed. Open question is empirical: does it carry a robust plateau?

---

### Finding 8: σ²(θ) — no genuine complementarity to r_ss at κ_c [claim]

σ²(θ) shares Z_shared entirely with r_ss. Both collapse at κ ≈ κ_c
from identical dynamic reasons. No complementarity at κ_c.

Additional own exclusion zones: Z_wrap (phase wrapping), Z_multi (bimodal P(θ)).

---

### Finding 9: Z_shared as dynamic universal zone [claim]

```
∀ π ∈ E:  Z(π) ⊇ Z_shared
```

Z_shared is enforced by system dynamics — not by observable structure.
No scope with π ∈ E can have κ_c in its observable range.

Reference: `docs/advanced/observable_consequences.md` — K1

---

### Finding 10: Phase transition κ_c is scope transition, not regime boundary [interpretation]

θ* ≈ 1.475 in CASE-0001 is more precisely a scope transition (observable
leaves R(π)) than a regime boundary (observable changes within R(π)).
Framework needs formal distinction. CASE-0001 remains valid.

Reference: `docs/advanced/observable_consequences.md` — K3

---

### Finding 11: Φ measures observable transfer, not system transfer [claim]

Φ = f(S_A, S_B), not f(System_A, System_B). Transfer reports should
document observable BC structures of both scopes.

Reference: `docs/advanced/observable_consequences.md` — K4

---

### Finding 12: Fluctuation observables as structural solution [hypothesis]

χ = ∂r_ss/∂κ diverges at κ_c rather than collapsing. R(χ) ∋ κ_c.
First candidate of a new observable class (fluctuation observables)
structurally suited for phase transitions / scope transitions.

Reference: `docs/advanced/observable_consequences.md` — K6

---

### Open questions raised

Q_NEW_1–12: see `docs/notes/open_questions_session_2026-03-18.md`
