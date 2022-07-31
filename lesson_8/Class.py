class Car():
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Car is started')

    def stop(self):
        print('Car is stoped')

    def __str__(self):
        return f'color is {self.color}\ntype is {self.type}\nyear is {self.year}'

car_1 = Car('black', 'sedan', 2018)
car_1.start()
car_1.stop()
print(car_1)
