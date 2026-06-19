# Food Menu App

print("Welcome to Food App")

print("\nMenu")
print("1. Pizza - ₹150")
print("2. Burger - ₹100")
print("3. Sandwich - ₹80")

choice = int(input("\nEnter item number (1-3): "))

if choice == 1:
    print("You selected Pizza. Price: ₹150")
elif choice == 2:
    print("You selected Burger. Price: ₹100")
elif choice == 3:
    print("You selected Sandwich. Price: ₹80")
else:
    print("Invalid choice")