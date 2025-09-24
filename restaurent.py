print("Welcome to Jindal Dhaba")
menu={
    'Dal Makhani': 7,
    'Shahi Paneer': 6,
    'Butter Roti': 2,
    'Butter Naan': 3,
    'Gulab Jamun': 2,
    'Malpuda': 2
}

print("Dal Makhani: $7\nShahi Panner: $6\nButter Roti: $2\nButter Naan: $3\nGulab Jamun: $2\nMalpuda: $2")

total=0

while True:
    item=input("Enter the item you want to order: ")
    if item in menu:
        total+=menu[item]
        print(f"Your item {item} is added to your order")
    else:
        print("This item is not available")

    another_order= input("Do you want to add another item to your order?(yes/no) ")
    if another_order.lower() != 'yes':
        break

print(f"Your total bill is {total} $")
