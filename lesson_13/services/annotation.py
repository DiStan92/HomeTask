from dataclasses import dataclass

@dataclass
class ConsumerAnnotation:
    name: str
    account: float


@dataclass
class HouseAnnotation:
    price: float
    square: float