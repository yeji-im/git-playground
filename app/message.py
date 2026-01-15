def render_message(name: str) -> str:
    name = (name or "").strip()
    if not name:
        name = "anonymous"
    return f"Hello, {name}!"
