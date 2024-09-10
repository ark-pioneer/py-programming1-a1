file = open("./shop_items.txt")
data = file.read().splitlines()
items = {}
for line in data:
  [item, price] = line.split(", ")
  items[item] = float(price)


def add(basket, item, quantity):
  return "fix me"

def remove(basket, item, quantity):
  return "fix me"

def show(basket):
  return "fix me"

def checkout(basket):
  return "fix me"
