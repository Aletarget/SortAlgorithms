import json
import random
import os

def numbers(quantiti):
    return [random.randint(-5000, 5000) for i in range (quantiti)]

hundred = numbers(100)
thousand = numbers(1000)
ten_thousand = numbers(10000)

rawdata = {
    "cien": hundred,
    "mil": thousand,
    "diezmil": ten_thousand
}

actual_folder = os.path.dirname(os.path.abspath(__file__))
file_patch = os.path.join(actual_folder, "test_Data.json")


with open(file_patch, "w") as file:
    json.dump(rawdata, file)

