import sys

class Person:
    def __init__(self, _id, level):
        self._id = _id
        self.level=level

a,b = sys.stdin.readline().strip().split()
person1 = Person(_id="codetree", level="10")
person2 = Person(_id=a, level=b)

print(f"user {person1._id} lv {person1.level}")
print(f"user {person2._id} lv {person2.level}")