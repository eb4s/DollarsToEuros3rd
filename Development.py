US_Dollar = int(input("Enter dollar amount to be converted:"))

euro = US_Dollar *.94540

print("₤",euro)

Continue = input("Continue code?:")

while Continue == "Yes":
    US_Dollar = int(input("Enter dollar amount to be converted:"))
    print("₤",euro)
    Continue = input("Continue code?: ")
