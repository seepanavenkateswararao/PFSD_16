import csv

with open("venkat.csv", "w") as v:
    file = csv.writer(v)
    file.writerow(["name", "place"])
    while True:
        name = input("enter your name")
        place = input("enter your area")
        file.writerow([name, place])
        opt = input("continue or stop")
        if opt.lower() == "no":
            break
