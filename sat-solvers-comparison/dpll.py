def dpll(clauses, assignment={}):
    """
    DPLL SAT Solver.
    clauses: list of sets of literals
    assignment: dict of variable assignments
    Returns True if satisfiable, False otherwise.
    """
    clauses = [set(c) for c in clauses]

    if not clauses:
        return True
    if any(len(c) == 0 for c in clauses):
        return False

    # Unit Propagation
    unit_clauses = [c for c in clauses if len(c) == 1]
    while unit_clauses:
        unit = next(iter(unit_clauses[0]))
        var = unit.strip('~')
        val = not unit.startswith('~')
        assignment[var] = val
        new_clauses = []
        for c in clauses:
            if unit in c:
                continue
            if (f"~{var}" if val else var) in c:
                new_c = c - {f"~{var}" if val else var}
                if not new_c:
                    return False
                new_clauses.append(new_c)
            else:
                new_clauses.append(c)
        clauses = new_clauses
        unit_clauses = [c for c in clauses if len(c) == 1]

    # Choose literal
    for c in clauses:
        for lit in c:
            var = lit.strip('~')
            if var not in assignment:
                break
        break
    else:
        return True

    var = lit.strip('~')

    # Try True
    new_assignment = assignment.copy()
    new_assignment[var] = True
    new_clauses = []
    for c in clauses:
        if var in c:
            continue
        if f"~{var}" in c:
            new_clauses.append(c - {f"~{var}"})
        else:
            new_clauses.append(c)
    if dpll(new_clauses, new_assignment):
        return True

    # Try False
    new_assignment = assignment.copy()
    new_assignment[var] = False
    new_clauses = []
    for c in clauses:
        if f"~{var}" in c:
            continue
        if var in c:
            new_clauses.append(c - {var})
        else:
            new_clauses.append(c)
    return dpll(new_clauses, new_assignment)
