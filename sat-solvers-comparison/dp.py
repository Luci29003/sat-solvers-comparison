def dp(clauses):
    """
    Davis–Putnam algorithm for SAT.
    clauses: list of sets of literals
    Returns True if satisfiable, False otherwise.
    """
    clauses = [set(c) for c in clauses]

    if not clauses:
        return True
    if any(len(c) == 0 for c in clauses):
        return False

    # Choose a literal to eliminate
    literal = next(iter(next(iter(clauses))))

    pos_clauses = [c for c in clauses if literal in c]
    neg_clauses = [c for c in clauses if f"~{literal}" in c]

    new_clauses = [c for c in clauses if literal not in c and f"~{literal}" not in c]

    for pc in pos_clauses:
        for nc in neg_clauses:
            resolvent = (pc - {literal}) | (nc - {f"~{literal}"})
            if not resolvent:
                return False
            new_clauses.append(resolvent)

    return dp(new_clauses)
