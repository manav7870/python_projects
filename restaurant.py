print("Welcome to punjabi Dhaba")
menu={
    'pizza': 6,
    'burger': 5,
    'noodles': 4,
    'manchorian': 3,
    'soup': 2
}

print("pizza: $6\nburger: $5\nnoodles: $4\nmanchorian: $3\nsoup: $2")

total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        total += menu[item]
        print(f"Your item {item} is added to your order")
    else:
        print("Sorry this item is not available")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {total} $")            