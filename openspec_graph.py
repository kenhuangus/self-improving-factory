import json, uuid
from pathlib import Path

DB = Path("data/spec_graph.json")

def _load():
    if not DB.exists(): return {}
    return json.loads(DB.read_text())

def _save(g):
    DB.parent.mkdir(parents=True, exist_ok=True)
    DB.write_text(json.dumps(g, indent=2))

def new_spec(content, parent=None):
    g = _load()
    sid = str(uuid.uuid4())
    g[sid] = {"id": sid, "content": content, "parent": parent, "children": [], "score": 0, "insights": []}
    if parent: g[parent]["children"].append(sid)
    _save(g)
    return sid

def set_score(sid, score):
    g = _load(); g[sid]["score"] = score; _save(g)

def add_insight(sid, txt):
    g = _load(); g[sid]["insights"].append(txt); _save(g)

def select_best():
    g = _load(); return max(g, key=lambda k: g[k].get("score",0)) if g else None

def load_graph(): return _load()
