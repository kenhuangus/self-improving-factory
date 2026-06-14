from .vector_store import search

def retrieve_context(spec):
    mem = search(spec)
    return "\n".join(m.get("content","" ) for m in mem)
