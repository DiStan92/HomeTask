class Family:
    def __init__(self, syrname):
        self.syrname = syrname

    def __str__(self):
        return f'{self.syrname} family'

class Father(Family):
    def __init__(self, syrname, name, age):
        super().__init__(syrname)
        self.name = name
        self.age = age

    def __str__(self):
        return f'Father: {self.syrname} {self.name} is {self.age} years'

    def __sub__(self, other):
        return f'{self.name} older {mother.name} on {self.age - other.age} years'

    def __repr__(self):
        return f'{self.name}, {self.age}'

class Mother(Family):
    def __init__(self, syrname, name, age):
        super().__init__(syrname)
        self.name = name
        self.age = age

    def __str__(self):
        return f'Mother: {self.syrname} {self.name} is {self.age} years'

    def __repr__(self):
        return f'{self.name}, {self.age}'

class Son(Father, Mother):
    def __init__(self, syrname, name, age, father, mother):
        self.syrname = syrname
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father}, my mother is {self.mother}'

    def __repr__(self):
        return f'{self.name}, {self.age}'

class Dougther(Father, Mother):
    def __init__(self, syrname, name, age, father, mother):
        self.syrname = syrname
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father}, my mother is {self.mother}'

    def __sub__(self, other):
        return f'{self.name} older {son.name} on {self.age - other.age} years'

    def __repr__(self):
        return f'{self.name}, {self.age}'

family = Family('Stantsel')
father = Father(family.syrname, 'Dima', 30)
mother = Mother(family.syrname, 'Diana', 28)
son = Son(family.syrname, 'Kirill', 1, father.name, mother.name)
doughter = Dougther(family.syrname, 'Alene', 5, father.name, mother.name)
print(father)
print(mother)
print(son)
print(doughter.father)
print(father - mother)
print(doughter - son)
print(repr(father))
print(repr(mother))
print(repr(son))
print(repr(doughter))