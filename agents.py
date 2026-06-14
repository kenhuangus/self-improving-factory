def llm(prompt):
    # stub model
    return "def sort_list(x): return sorted(x)"

def critic(spec, result):
    return f"Issue: {result}"

def edit(spec, critique):
    return spec + "\nConstraint: " + critique

def evolve_multi(spec, result):
    c = critic(spec, result)
    return edit(spec, c)
