# Exploratory scratch fragment from the course project.
# Not integrated into notebooks/03_relaxed_model_heuristics.ipynb.
# This creates a separate Pyomo model and defines one distance-violation constraint;
# it is NOT an end-to-end runnable solution of the original article.

from pyomo.environ import ConcreteModel, Var, Param, RangeSet, NonNegativeReals, Constraint, Binary

model = ConcreteModel()
#Maximum allowable distance constraint (13)
# 1) Define sets ---
N = 2  # Number of nurses
K = 1  # Number of vehicles
M = 3  # Number of patients

model.Nurses = RangeSet(1, N)
model.Kv     = RangeSet(1, K)
model.P      = RangeSet(1, M)

model.Dij = Param(model.P, model.P, default=10)

model.MDIS = Param(model.Nurses, model.Kv, default=100)

#  3) Define variables ---
model.X = Var(model.Kv, model.P, model.P, model.Nurses, domain=Binary)
model.O = Var(model.Nurses, model.Kv, domain=NonNegativeReals)

#  4) Define constraint ---
def max_distance_violation_rule(m, n, k):
    total_dist = sum(m.Dij[i,j] * m.X[k, i, j, n] for i in m.P for j in m.P)
    return m.O[n, k] >= total_dist - m.MDIS[n, k]

model.MaxDistanceViolation = Constraint(model.Nurses, model.Kv,
                                        rule=max_distance_violation_rule)


