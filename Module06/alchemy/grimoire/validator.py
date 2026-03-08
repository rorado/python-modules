def validate_ingredients(ingredients: str) -> str:
    valid_tokens = ["fire", "water", "earth", "air"]
    words = ingredients.lower().split()

    is_valid = False
    for token in valid_tokens:
        if token in words:
            is_valid = True
            break

    if is_valid:
        return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
