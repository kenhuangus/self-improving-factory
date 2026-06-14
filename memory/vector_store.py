import json
from pathlib import Path

DB = Path("data/memory.json")

def _load():
    if not DB.exists():
        return []
    return json.loads(DB.read_text())

def _save(x):
    DB.parent.mkdir(parents=True, exist_ok=True)
    DB.write_text(json.dumps(x, indent=2))

def embed(text):
    return [len(text)]

def store(memory):
    db = _load()
    memory["embedding"] = embed(memory.get("content", ""))
    db.append(memory)
    _save(db)

def search(query, k=3):
    db = _load()
    return db[-k:]
