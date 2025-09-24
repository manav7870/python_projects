#Task
input("Enter the Product Name: ")
a=int(input("Enter the Product ID: "))
b=int(input("Enter the Product Price: "))
c=int(input("Enter the Product Quantity: "))
print(f"Total Price: {b*c}")
e=b*c
choice=int(input("Enter you choice: "))
if choice ==1:
    print("The GST imposed is 5 percent")
    gst=(5*e)/100
elif choice ==2:
    print("The GST imposed is 12 percent")
    gst=(12*e)/100
elif choice ==3:
    print("The GST imposed is 18 percent")
    gst=(18*e)/100
else:
    print("Invalid Choice..")            
print(f"Total GST: {gst}")
print(f"Grand Total: {e+gst}")