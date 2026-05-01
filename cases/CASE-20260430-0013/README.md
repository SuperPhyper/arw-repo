# CASE-20260430-0013 — Vertical Spring-Mass Chain: Multi-Scale Observable Scope

**System:** Vertical N-mass spring chain with periodic pivot excitation  
**BC Classes:** Forcing (primary), Restriction (conditioned parameters)  
**Observable hierarchy:** π_micro (spring-extension variance) · π_meso (COM variance) · π_macro (end-mass variance)  
**Active BC domain:** 2D sweep over (A, Ω/ω₁)  
**Status:** pre-pipeline (ScopeSpec_signature_first stage)

## Key Documents

| File | Purpose |
|---|---|
| `ScopeSpec_signature_first.md` | Active ScopeSpec v3 — spring-mass chain (supersedes pendulum drafts) |
| `consistency_check.md` | Pre-ScopeSpec physical model and BC class verification |

## Evolution

This case evolved through three ScopeSpec iterations:
- v1 / v2: Multi-link pendulum (angular DOF) — archived at `archive/cases/CASE-20260430-0013_pendulum_drafts/`
- v3 (current): Vertical spring-mass chain — simpler observable hierarchy, no coordinate transformation needed

## Related

- CASE-20260311-0002 (Multi-Link Pendulum, single-observable scope — predecessor system)
- `docs/advanced/multi_scale_observables_and_latent_regime_formation.md`
- `docs/advanced/multi_scale_sweep_protocol.md`
- `experiments/spring_mass_chain/` (simulation scripts)
