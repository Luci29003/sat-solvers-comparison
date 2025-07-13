def resolution(clauses):
    """
    Simple resolution-based SAT solver.
    clauses: list of sets of literals (e.g. [{'A', '~B'}, {'B'}])
    Returns True if satisfiable, False otherwise.
    """
    def pl_resolve(ci, cj):
        resolvents = set()
        for di in ci:
            for dj in cj:
                if di == f"~{dj}" or dj == f"~{di}":
                    resolvent = (ci - {di}) | (cj - {dj})
                    resolvents.add(frozenset(resolvent))
        return resolvents

    clauses = set(frozenset(c) for c in clauses)
    new = set()
    while True:
        pairs = [(ci, cj) for ci in clauses for cj in clauses if ci != cj]
        for (ci, cj) in pairs:
            resolvents = pl_resolve(ci, cj)
            if frozenset() in resolvents:
                return False  # Unsatisfiable
            new = new.union(resolvents)
        if new.issubset(clauses):
            return True  # Satisfiable
        clauses = clauses.union(new)
