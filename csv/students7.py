import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students7.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# یه مشکل به وجود اومد وقتی که به ته فایل سی‌اس‌وی اضاف می‌یشه یه خط اضافه بینشون میفته    