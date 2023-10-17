from my_package import add # I can write the import like this because I imported the add function in the __init__ file in the my_package folder.
from my_package.module_a import add # otherwise I would have to import it like this.

if __name__ == "__main__":
    print("The main.py file is the entry point to your program.")