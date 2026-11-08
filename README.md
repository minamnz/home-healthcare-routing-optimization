# Home Healthcare Routing Optimization

**Partial research reproduction | Operations Research in Healthcare | Python & Pyomo**

This repository contains a course-project implementation inspired by **Fathollahi-Fard, Hajiaghaei-Keshteli, and Mirjalili**, *A set of efficient heuristics for a home healthcare problem*. We explored mathematical modeling and heuristic approaches for a simplified home healthcare routing and scheduling problem using **synthetic data**.

> **Scope:** This is an educational **partial reproduction and implementation study**, not an official implementation of the paper or an exact reproduction of its published results. The mathematical model and tests were simplified to fit the available computing environment.

## Problem overview

Home healthcare planning involves assigning healthcare professionals to patient visits while considering travel costs, vehicle capacity, patient service requirements, and time constraints. The reference paper studies a mixed-integer linear programming (MILP) formulation and optimization heuristics for this problem.

## What we implemented

- A baseline **mixed-integer programming model** in Python with **Pyomo**, including routing, assignment, capacity, time-window and travel-distance components.
- A **synthetic instance generator** for small illustrative cases (three patients, two nurses, one transportation mode in the provided examples).
- A **simplified/relaxed model** solved using **CBC**, with a more permissive set of constraints.
- Three exploratory **constructive heuristics (H1, H2, H3)** for selecting patient-visit orders.
- A function for adding a **Lagrangian penalty** to a relaxed objective. Its full optimization procedure and performance were **not validated** in the supplied notebook runs.
- A step-by-step code explanation prepared for the course project (maintained separately from the published article).

## Repository structure

```text
notebooks/
  01_synthetic_data_generation.ipynb   # Generate illustrative problem instances
  02_baseline_milp.ipynb                # Original baseline formulation (infeasible in the saved run)
  03_relaxed_model_heuristics.ipynb     # Simplified model, CBC solver and H1-H3 heuristics
experiments/
  standalone_distance_constraint.py    # Separate draft constraint; not integrated into the main model
requirements.txt
README.md
```

## How to run

The notebooks were developed in **Google Colab**. To run them in a compatible Linux/Colab environment:

```bash
pip install -r requirements.txt
sudo apt-get update
sudo apt-get install -y glpk-utils coinor-cbc
```

Open the notebooks in numerical order and run their cells. The synthetic-data generator is an independent experiment: its generated instances are **not automatically passed to** the other notebooks, which use their own example parameter values.

## Observed results and limitations

| Notebook / experiment | Saved output | Interpretation |
|---|---|---|
| Baseline MILP (GLPK) | `infeasible` | The submitted baseline did not yield a feasible solution for its example data and constraints. |
| Simplified model (CBC) | `optimal`; objective value `437.5` | A solver result for a **modified model without the original time-sequencing constraint**, **not** the full formulation. |
| Constructive heuristics | H1: `[1,2,3]`; H2: `[2,1,3]`; H3: `[3,1,2]` | Example patient-visit sequences, not validated globally optimal routes. |

**Important interpretation:** The final optimization step uses heuristic values as variable initializations, not as fixed routing constraints. Consequently, the solver's printed route may differ from the H2 route. The notebooks do **not** establish that H2 improves the objective, nor do they demonstrate a complete Lagrangian-relaxation solution.

The notebooks contain exploratory modeling choices. Their outputs should not be interpreted as clinical deployment results or a rigorous benchmark against the original publication. All study inputs are synthetic; no real patient records are used.

## Reference

Fathollahi-Fard, A. M., Hajiaghaei-Keshteli, M., & Mirjalili, S. (2019). *A set of efficient heuristics for a home healthcare problem*. **Neural Computing and Applications**. https://doi.org/10.1007/s00521-019-04126-8

This repository is independent of the paper authors. Refer to the linked publication for the original mathematical model and evaluation.

## Academic context

Completed as a collaborative university course project in **Operations Research in Healthcare** at **Amirkabir University of Technology**. Acknowledgment of all student contributors should be added with their preferred English names before public release.
