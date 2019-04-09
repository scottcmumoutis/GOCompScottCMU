import os

filename = "case.raw"
os.chdir(r'C:\Users\yelca\PycharmProjects\GOCompScottCMU\scenario_1')
with open(filename, "r") as f:
    data = [[float(num) for num in line.split(',')] for line in f]
    print(data)

