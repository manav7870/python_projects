# Unit Converter

print("UNIT CONVERTER ")

def km_to_miles(km):
    return km * 0.612
def miles_to_km(m):
    return m / 0.612
def c_to_f(celcius):
    return (celcius*9/5)+32
def f_to_c(farhen):
    return (farhen - 32) * 5/9
while True:
    print("1. Kilomiles to Miles\n2. Miles to Kilomilesr\n3. Celcius to Fahrenheit\n4. Fahrenheit to Celcius\n")

    a = int(input("Enter your choice: "))
    try:
        if a == 1:
            km = float(input("Enter the kilomiles: "))
            print(f"{km} km = {km_to_miles(km)} miles")
        elif a == 2:
            m =  float(input("Enter the miles: "))
            print(f"{m} miles = {miles_to_km(m)} kilomiles") 
        elif a == 3:
            c = float(input("Enter the celcius: "))
            print(f"{c} celcius = {c_to_f(c)} fahrenheit") 
        elif a == 4:
            f = float(input("Enter the Fahrenheit: "))
            print(f"{f} fahrenheit = {f_to_c(f)} celcius")         
        else:
            print("Invalid Choice..")
    except ValueError:
        print("Please enter a valid number...") 
        break
