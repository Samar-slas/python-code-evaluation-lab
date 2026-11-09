def evaluate(expected, actual):
    if expected == actual:
        return "PASS"
    else:
        return "FAIL"


result = evaluate(30, 30)
print("Test Result:", result)
