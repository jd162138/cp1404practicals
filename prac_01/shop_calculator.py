number_of_items = int(input("Number of Items: "))
total_price = 0
while number_of_items <= 0:
    print("Invalid input")
    number_of_items = int(input("Number of Items: "))
for i in range(number_of_items):
    price = float(input("Price of item: $"))
    total_price = total_price + price
print(f"Total price for items is ${total_price:.2f}")

