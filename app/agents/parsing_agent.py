def return_standard_response():
    return {"status": "success", "data": None}

def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(return_standard_response())
    print(say_hello("Alice"))