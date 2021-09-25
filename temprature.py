
for i in range(11):
    a=int(input("Enter 1 to convert celsius to fahrenheit\n"
                "Enter 2 to convert fahrenheit to celsius\n"
                "Enter 3 to Exit\n"
                ": "))
    if a == 3:
        break

    elif a==1:
        c=float(input("Enter the temperature in celsius: "))
        f=(9/5 * c)+32
        print("The converted temperature is", f,"degree fahrenheit")

    else:
        f=float(input("Enter the temperature in fahrenheit: "))
        c=(f-32)*5/9
        print("The converted temperature is", c,"degree celsius")