import keyword

def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True
    return False

# Example usage
print(contains_keyword("hello", "goodbye"))  # Should print: False
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))  # Should print: True
print(contains_keyword("four", "for", "if"))  # Should print: True
print(contains_keyword("blah", "doggo", "crab", "anchor"))  # Should print: False
print(contains_keyword("grizzly", "ignore", "return", "False"))  # Should print: True
