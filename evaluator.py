def evaluate(code):
    try:
        env = {}
        exec(code, {}, env)
        fn = env.get("sort_list")
        if not fn: return "missing function"
        assert fn([3,1,2]) == [1,2,3]
        return "success"
    except Exception as e:
        return str(e)

def score(result):
    if result == "success": return 1.0
    if "missing" in result: return 0.3
    return 0.0
