
from dataclasses import dataclass


def sol(s1:str , s2:str) -> bool:
    return bool(set(s1) & set(s2))



# print(sol("bank","kanb"))




@dataclass
class Person:
    name: str
    age: int
    city: str

    def __str__(self):
        return f"{self.name}, {self.age}, {self.city}"  
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age and self.city == other.city
    def __hash__(self):
        return hash((self.name, self.age, self.city))
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

res= Person("John", 30, "New York")

print(res.__repr__)