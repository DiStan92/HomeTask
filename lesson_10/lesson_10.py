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
    def __init__(self, syrname, name, age, father_name, mother_name):
        super().__init__(syrname)
        self.name = name
        self.age = age
        self.father_name = father_name
        self.mother_name = mother_name

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father_name}, my mother is {self.mother_name}'

class Dougther(Father, Mother):
    def __init__(self, syrname, name, age, father_name, mother_name):
        super().__init__(syrname)
        self.name = name
        self.age = age
        self.father_name = father_name
        self.mother_name = mother_name

    def __str__(self):
        return f'{self.syrname} {self.name}, my father is {self.father_name}, my mother is {self.mother_name}'

family = Family('Stantsel')
father = Father('Stantsel', 'Dima', 30)
print(father)
mother = Mother('Stantsel', 'Diana', 28)
print(mother)
son = Son('Stantsel', 'Kirill', 1, 'Dima', 'Diana')
print(son)
doughter = Dougther('Stantsel', 'Alene', 5, 'Dima', 'Diana')
