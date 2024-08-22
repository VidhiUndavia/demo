fruit=["apple","banana","mango","pineapple","watermelon","apple","apple"]
vegies=["potato","tomato","onion"]

print(fruit)
fruit.append("strawberry")
print(fruit)
vegies.extend(fruit)
print(vegies)

fruit.insert(3,"apple")
print(fruit)

print(fruit.count("apple"))
fruit.remove("apple")
print(fruit)
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)
mix=fruit.copy()
print(mix)
print(fruit.index("apple"))
print(fruit.pop(0))
print(fruit)
fruit.clear()
print(vegies)
vegies.clear()

print(vegies)
print(fruit)
