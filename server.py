from fastapi import FastAPI
from runner import run_factory
from openspec_graph import load_graph

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/run")
def run():
    return {"result": run_factory()}

@app.get("/graph")
def graph():
    g = load_graph()
    nodes = []
    edges = []
    for sid, n in g.items():
        nodes.append({"id": sid, "label": f"{sid[:4]} ({n.get('score',0)})"})
        if n.get("parent"):
            edges.append({"from": n["parent"], "to": sid})
    return {"nodes": nodes, "edges": edges}
