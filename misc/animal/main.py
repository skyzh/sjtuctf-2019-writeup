import base64
import pickle
import favorite
import pickletools
class Animal:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f'Animal(name={self.name!r}, category={self.category!r})'

    def __eq__(self, other):
        return type(other) is Animal and self.name == other.name and self.category == other.category

class IsTrue:
    def __eq__(self, other):
        return True

def test():
    return 233

x = pickle.dumps(Animal(favorite.name, favorite.category))
print(x)
print(pickletools.dis(x))
print(base64.b64encode(x))
