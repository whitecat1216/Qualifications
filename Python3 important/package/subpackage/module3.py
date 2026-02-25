try:
    from .module2 import greet as hello
except ImportError:
    from module2 import greet as hello

def greet():
    return "Hello from module3"

if __name__ == "__main__":
    print(hello())