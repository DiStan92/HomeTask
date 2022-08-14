from dataclasses import dataclass
import datetime

@dataclass
class User:
    name: str
    syrname: str
    age: int
    country: str
    gender: str
    profession: str

    def email(self):
        return f'{self.name}_{self.syrname}@gmail.com'

    def birth_year(self):
        date = datetime.datetime.now()
        return date.year - self.age

    @staticmethod
    def doctor():
        doctor  = User('name', 'syrname', 1, 'USA', 'man', 'doctor')
        return doctor

    @staticmethod
    def policman():
        policman  = User('name', 'syrname', 1, 'USA', 'man', 'policman')
        return policman

    @staticmethod
    def teacher():
        teacher  = User('name', 'syrname', 1, 'USA', 'man', 'teacher')
        return teacher

user_1 = User('Dima', 'Stantsel', 30, 'Belarus', 'man', 'pogrammer')
print(user_1.email())
print(user_1.birth_year())
