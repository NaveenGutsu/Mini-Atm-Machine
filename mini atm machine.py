balance = 1000  
is_running = True

print("Welcome to Hasili Bank!")


while is_running:
    print("\n--- What would you like to do? ---")
    print("1. Check Balance 💰")
    print("2. Deposit Money 📥")
    print("3. Withdraw Money 📤")
    print("4. Exit 🚪")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ₹{balance}")

    elif choice == "2":
        amount = int(input("How much do you want to deposit? ₹"))
        if amount > 0:
            balance += amount
            print(f"Awesome! ₹{amount} added. New balance: ₹{balance}")
        else:
            print("You must deposit more than ₹0!")

    elif choice == "3":
        amount = int(input("How much do you want to withdraw? ₹"))
        if amount > balance:
            print(" Alert! You don't have enough money in your account!")
        elif amount <= 0:
            print("Please enter a valid amount!")
        else:
            balance -= amount
            print(f"Cha-ching! Take your cash. Remaining balance: ₹{balance}")

    elif choice == "4":
        print("Thank you for using Hasili Bank! Goodbye! ")
        is_running = False  

    else:
        print("Invalid option! Please pick a number from 1 to 4.")
