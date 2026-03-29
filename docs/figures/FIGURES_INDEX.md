---
status: note
layer: docs/figures/
last_updated: 2026-03-29
---

# FIGURES_INDEX — ARW/ART Figure Registry

Registry of all visual artifacts in `figures/` (top-level).
Every figure file must have an entry here and a corresponding description
document in `docs/figures/`.

**Rules:**
- After generating a figure: add a row here and create or extend the relevant `docs/figures/*.md`.
- Description documents group related figures (one `.md` per thematic group).
- `description_doc` column: path to the `docs/figures/` file that describes this figure.
- Status `described` = has a full description. `stub` = placeholder only. `pending` = no description yet.

---

## Group A — Kuramoto ε-Sweep and Partition Invariants

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/epsilon_sweep_kuramoto.png` | CASE-20260311-0001 | described | `docs/figures/epsilon_sweep_kuramoto.md` |
| `figures/epsilon_kappa_robustness.png` | CASE-20260311-0001 | described | `docs/figures/epsilon_kappa_robustness.md` |
| `figures/r_ss_vs_kappa.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_observables.md` |
| `figures/chi_vs_kappa.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_observables.md` |
| `figures/bc_sweep_lambda.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_observables.md` |
| `figures/fig1_kappa_sweep.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/fig2_bc_heatmaps.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/fig3_regime_failure.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/fig4_bc_timeline.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/time_series_strong.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/time_series_weak.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/metrics_vs_coupling.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/epsilon_window.png` | CASE-20260311-0001 | stub | `docs/figures/kuramoto_paper_figures.md` |
| `figures/kuramoto_sync_transition.png` | CASE-20260311-0001 | described | `docs/figures/kuramoto_sync_transition.md` |
| `figures/kuramoto_2d_observable_heatmap.png` | CASE-20260311-0001 | described | `docs/figures/kuramoto_2d_cover_height.md` |

---

## Group B — Cover Height Analysis (Multi-Case)

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/cover2d_0002_varrel_panel.png` | CASE-20260311-0002 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0002_varrel_overlay.png` | CASE-20260311-0002 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0002_lambdaproxy_panel.png` | CASE-20260311-0002 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0002_lambdaproxy_overlay.png` | CASE-20260311-0002 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0003_varrel_panel.png` | CASE-20260311-0003 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0003_varrel_overlay.png` | CASE-20260311-0003 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0003_lambdaproxy_panel.png` | CASE-20260311-0003 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0003_lambdaproxy_overlay.png` | CASE-20260311-0003 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0004_plv_panel.png` | CASE-20260318-0004 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0004_plv_overlay.png` | CASE-20260318-0004 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0004_ampasym_panel.png` | CASE-20260318-0004 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_0004_ampasym_overlay.png` | CASE-20260318-0004 | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover2d_dr_comparison.png` | multi-case | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover_height_contrast_panel.png` | multi-case | described | `docs/figures/cover_2d_all_cases.md` |
| `figures/cover_height_all_cases.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_height_map.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_height_dr_comparison.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_height_all_cases_stats.json` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_cp_pi1_panel.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_cp_pi_comp_panel.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_cp_N_alpha.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover_cp_dr_comparison.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/cover2d_stats.json` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/obs_cover_count_curve.png` | multi-case | described | `docs/figures/scope_completeness.md` |
| `figures/obs_height_overlay.png` | multi-case | described | `docs/figures/scope_completeness.md` |
| `figures/obs_space_cover_height_panel.png` | multi-case | described | `docs/figures/scope_completeness.md` |
| `figures/cover_height_all_cases.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/fiber_N_comparison.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |
| `figures/fiber_scatter_by_alpha.png` | multi-case | stub | `docs/figures/cover_height_analysis.md` |

---

## Group C — Observable Decomposition and Empirical Validation

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/fig_emp1_gradient_rank.png` | CASE-20260311-0001 | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_emp2_sensitivity.png` | CASE-20260311-0001 | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_emp3_zdim_counter.png` | CASE-20260311-0001 | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_ext1_three_systems.png` | multi-case | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_ext2_dim_theorem.png` | multi-case | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_ext3_validity_maps.png` | multi-case | stub | `docs/figures/observable_decomposition_figures.md` |
| `figures/fig_ext4_assumption_heatmap.png` | multi-case | stub | `docs/figures/observable_decomposition_figures.md` |

---

## Group D — IVA and H2' Theorem

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/fig_iva1_geometry.png` | theory | stub | `docs/figures/iva_h2prime_figures.md` |
| `figures/fig_iva2_bc_mapping.png` | theory | stub | `docs/figures/iva_h2prime_figures.md` |
| `figures/fig_iva3_h2prime.png` | theory | stub | `docs/figures/iva_h2prime_figures.md` |

---

## Group E — Transfer, PCI, and Multi-Observable

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/pci_scaling.png` | multi-case | described | `docs/figures/pci_scaling.md` |
| `figures/multi_observable_agreement.png` | CASE-20260311-0003 | described | `docs/figures/multi_observable_agreement.md` |
| `figures/boundary_shift.png` | theory | described | `docs/figures/boundary_shift.md` |

---

## Group F — Scope Completeness and Sigma Figures

| File | Case | Status | Description doc |
|---|---|---|---|
| `figures/scope_completeness.png` | multi-case | described | `docs/figures/scope_completeness.md` |

---

## Group G — Structural Diagrams (non-PNG)

| File | Type | Status | Description doc |
|---|---|---|---|
| `figures/arw_signature_graph.mmd` | Mermaid | stub | `docs/figures/structural_diagrams.md` |

---

## Summary

| Status | Count |
|---|---|
| described | 22 |
| stub | 35 |
| pending | 0 |
| **Total** | **57** |

Stub files are listed in `docs/figures/` and require description content to be filled in by the researcher who generated the figures.
