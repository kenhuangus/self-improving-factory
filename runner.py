from openspec_graph import new_spec, load_graph, set_score, add_insight, select_best
from evaluator import evaluate, score
from agents import evolve_multi, llm
from memory.hybrid import retrieve_context
from memory.vector_store import store

def run_factory():
    sid = new_spec("Write a sorting function")
    for i in range(10):
        g = load_graph()
        spec = g[sid]["content"]

        ctx = retrieve_context(spec)
        code = llm(ctx + "\n" + spec)
        result = evaluate(code)

        sc = score(result)
        set_score(sid, sc)
        add_insight(sid, result)
        store({"type":"run","content":result,"score":sc})

        new_content = evolve_multi(spec, result)
        sid = new_spec(new_content, parent=sid)
        best = select_best()
        if best: sid = best

        print({"iter": i, "score": sc, "result": result})
        if sc == 1.0: break
    return "done"
