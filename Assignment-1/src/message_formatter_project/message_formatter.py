def leafy_border(func):
    def wrapper(message):
        border = "🍃" * (len(message) + 8)
        return f"{border}\n🌿  {func(message)}  🌿\n{border}"
    return wrapper

def butterfly_effect(func):
    def wrapper(message):
        return f"🦋 {func(message)} 🦋"
    return wrapper
