from random import randint
from classes import House, Consumer
from annotation import ConsumerAnnotation, HouseAnnotation

NAMES = ["Alex", "Jhon", "Peter", "Victor", "James", "Oliver"]
NAMES_COUNT = len(NAMES)


def house_gener(house_count: int) -> list[HouseAnnotation]:
    house_lst = [House(price=randint(10_000, 250_000), square=randint(25, 200)) for _ in range(house_count)]
    return house_lst


def consumer_gener() -> ConsumerAnnotation:
    consumer = Consumer(name=NAMES[randint(0, NAMES_COUNT - 1)], account=randint(10_000, 250_000))
    return consumer
