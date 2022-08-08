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

class Mother(Family):
    def __init__(self, syrname, name, age):
        super().__init__(syrname)
        self.name = name
        self.age = age

    def __str__(self):
        return f'Mother: {self.syrname} {self.name} is {self.age} years'

class Son(Father, Mother):
    def __init__(self, syrname, name, age, father, mother):
        self.syrname = syrname
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father}, my mother is {self.mother}'

class Dougther(Father, Mother):
    def __init__(self, syrname, name, age, father, mother):
        self.syrname = syrname
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father}, my mother is {self.mother}'

family = Family('Stantsel')
father = Father(family.syrname, 'Dima', 30)
print(father)
mother = Mother(family.syrname, 'Diana', 28)
print(mother)
son = Son(family.syrname, 'Kirill', 1, father.name, mother.name)
print(son)
doughter = Dougther(family.syrname, 'Alene', 5, father.name, mother.name)
print(doughter.father)
