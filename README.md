# Guardrail Composition Theory

Guardrail Composition Theory collects the notes, proofs, and reference implementations used in the
research program on adversarially robust guardrail composition. The repository is intended to be a
one-stop starting point for readers who want to study the theory, run the supporting code, and build
the PDF thesis.

## Project Overview

The project provides three complementary artifacts:

1. **Theory (LaTeX)** – the manuscript located in `theory/` formalises the main theorems about
   Fréchet–Hoeffding envelopes, the guardrail composition trilemma, Lipschitz robustness taxes,
   PAC-robust confidence intervals, and causal reintroduction diagnostics.
2. **Python reference implementation** – modules under `src/certify/` mirror the theoretical
   constructs. They expose helpers for computing FH intervals, evaluating the trilemma trade-off,
   applying Lipschitz penalties, forming PAC-style half-widths, and running causal reintroduction
   tests.
3. **Validation assets** – tests under `tests/` ensure the helpers satisfy their invariants, while
   `examples/experiment_synthetic.py` demonstrates the full workflow on a toy dataset.

All components are designed to be lightweight and dependency-minimal so they can be inspected and
modified easily.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
make test
python examples/experiment_synthetic.py
```

To build the PDF you will also need a LaTeX distribution with `latexmk` available in your `$PATH`.

## Repository Layout

```
guardrail-comp-theory/
├── theory/                 # Thesis sources (preamble, main driver, chapters)
├── src/certify/            # Python reference modules
├── tests/                  # Pytest suite covering each module
├── examples/               # Synthetic experiment harness
├── Makefile                # Common entry points (PDF, tests, coverage, clean)
└── pyproject.toml          # Project metadata and pytest configuration
```

### Components in Detail

- `src/certify/fh.py` defines the `FHInterval` data class and helpers for AND/OR FH bounds plus a
  variance envelope used by concentration inequalities.
- `src/certify/trilemma.py` packages the FH calculations into a `TrilemmaEnvelope` to highlight the
  impossibility of simultaneously optimising precision, recall, and false-positive guarantees.
- `src/certify/lipschitz.py` models the additive "tax" introduced by adversarial Wasserstein shifts
  on Lipschitz-continuous rails.
- `src/certify/pac.py` provides conservative Bernstein-style half-widths and domain adaptation
  inflation terms for guardrail performance intervals.
- `src/certify/causal.py` implements a simple reintroduction statistic and a permutation-style test
  to flag causal feedback loops.

### Running the Tests

The repo ships with a focused test suite that validates algebraic properties and monotonicity of the
helpers. Run the suite via:

```bash
make test
```

For coverage details, execute:

```bash
make cov
```

### Building the PDF Thesis

The thesis is built with `latexmk`. Invoke:

```bash
make pdf
```

The generated PDF will be located at `theory/main.pdf`. If you need to clean auxiliary files, run:

```bash
make clean
```

## Synthetic Experiment

The script `examples/experiment_synthetic.py` draws synthetic rails under fixed marginals, estimates
empirical joints, evaluates FH envelopes, and prints a summary report including PAC half-widths and
whether the trilemma flag is triggered. The script can be run directly:

```bash
python examples/experiment_synthetic.py
```

## Contributing

Contributions are welcome. Please ensure any pull request includes updated theory references where
appropriate, passes `make test`, and keeps the documentation consistent with new features.
