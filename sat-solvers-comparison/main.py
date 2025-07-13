import time
import matplotlib.pyplot as plt
from resolution import resolution
from dp import dp
from dpll import dpll

# Exemplu simplu: formula CNF (A ∨ ¬B) ∧ (B ∨ C) ∧ (¬A ∨ ¬C)
test_clauses = [
    {'A', '~B'},
    {'B', 'C'},
    {'~A', '~C'}
]

def measure_time(func, clauses):
    start = time.time()
    result = func(clauses)
    end = time.time()
    return result, end - start

def main():
    solvers = {'Resolution': resolution, 'DP': dp, 'DPLL': dpll}
    times = {}
    results = {}

    for name, solver in solvers.items():
        result, elapsed = measure_time(solver, test_clauses)
        results[name] = result
        times[name] = elapsed

    # Print results
    for name in solvers:
        print(f"{name}: SAT? {results[name]}, Time: {times[name]:.6f} seconds")

    # Grafic timp
    plt.bar(times.keys(), times.values())
    plt.ylabel("Execution time (s)")
    plt.title("SAT Solving Algorithms Runtime Comparison")
    plt.savefig("results/runtime_plot.png")
    plt.show()

if __name__ == "__main__":
    main()

