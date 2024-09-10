from shop.shop import add, remove, show, checkout

# this should run without error once your tests are passing
basket = {}

add(basket, "pizza", 3)
add(basket, "lemonade", 2)
add(basket, "cookie", 2)

remove(basket, "pizza", 1)
remove(basket, "cookie", 2)

print(show(basket))

print(checkout(basket))
