def test_function():
    try:
        return "The block result"
    finally:
        return "Finally block result"
print(test_function())