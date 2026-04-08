def grade_data(response: str):
    if "Bob" in response:
        return 0.2

    if "Alice" in response and "Charlie" in response:
        return 1.0

    return 0.5
