import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)


foods = ["Meat", "Cheese"]
print("Welcome to the Grocery List App")
print(f"Current Date and Time: {month}/{day}/\t{hour}:{minute}")
print(f"Your currently have {foods[0]} and {foods[1]} in your list")

food = input("\nType of food to add to the grocery list: ")
foods.append(food.title())
food = input("Type of food to add to the grocery list: ")
foods.append(food.title())
food = input("Type of food to add to the grocery list: ")
foods.append(food.title())

print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("\nHere is your grocery list sorted: ")
print(foods)

print("\nSimulating grocery shopping...")
print(f"\nCurrent grocery list: {len(foods)} items")
print(foods)
buyfood = input("What food did you just buy: ").title()
foods.remove(buyfood)
print(f"Removing {buyfood} from the list...")

print(f"\nCurrent grocery list: {len(foods)} items")
print(foods)
buyfood = input("What food did you just buy: ").title()
foods.remove(buyfood)
print(f"Removing {buyfood} from the list...")

print(f"\nCurrent grocery list: {len(foods)} items")
print(foods)
buyfood = input("What food did you just buy: ").title()
foods.remove(buyfood)
print(f"Removing {buyfood} from the list...")

print(f"\nCurrent grocery list: {len(foods)} itemns")
print(foods)
noitem = foods.pop()
print(f"\nSorry, the store is out of {noitem}")
newfood = input("What food would you like instead: ").title()
foods.insert(0, newfood)

print("\nHere is what remains on your grocery list: ")
print(foods)