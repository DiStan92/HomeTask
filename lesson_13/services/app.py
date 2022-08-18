from annotation import HouseAnnotation, ConsumerAnnotation
from consts import house_gener, consumer_gener


def get_recommendations(house_lst: list[HouseAnnotation], consumer: ConsumerAnnotation) -> dict[
    ConsumerAnnotation, HouseAnnotation]:
    rec_house = [house for house in house_lst if house.price < consumer.account]
    rec_house.sort(key=lambda x: x.square)
    return {"Consumer": consumer, "Recommendations": rec_house[::-1]}


print((get_recommendations(house_gener(10), consumer_gener())))
