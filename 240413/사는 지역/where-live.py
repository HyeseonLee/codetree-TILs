import sys
n = int(sys.stdin.readline().strip())

class Person:
    def __init__(self, name,ad,place):
        self.name = name
        self.ad = ad
        self.place = place

people = []
for _ in range(n):
    name, ad, place = sys.stdin.readline().strip().split()
    people.append(Person(name, ad, place))

# 이름이 가장 느린 사람 ? 어떻게 구하지 ? 
sorted_people = sorted(people, key= lambda x:x.name)
print(f"name {sorted_people[-1].name}")
print(f"addr {sorted_people[-1].ad}")
print(f"city {sorted_people[-1].place}")