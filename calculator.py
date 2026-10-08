print("Welcome to the Engineering Calculator!")

# The 'while True' loop keeps the program running forever, 
# until we specifically tell it to 'break' (stop).
while True:
    print("\n--- Main Menu ---")
    print("1. Calculate Density (ρ = m/V)")
    print("2. Calculate Ideal Gas Volume (V = nRT/P)")
    print("3. Calculate Reynolds Number")
    print("4. Quit")
    
    # input() pauses the loop and waits for you to type something
    choice = input("Select an option (1, 2, 3 or 4): ")
    
    # if/elif routes the program based on what you typed
    if choice == '1':
        print("\n--- Density Calculator ---")
        # float() converts the text you type into a decimal number so Python can do math
        mass = float(input("Enter mass in kg: "))
        volume = float(input("Enter volume in m^3: "))
        
        density = mass / volume
        print(f"Result: The density is {density} kg/m^3")
        
    elif choice == '2':
        print("\n--- Ideal Gas Volume Calculator ---")
        Moles = float(input("enter moles: "))
        Temperature = float(input("enter Temperature in Kelvin ($T$): "))
        Pressure = float(input("enter Pressure in atm (P): "))
        R = 0.0821

        volume = (Moles * R *  Temperature ) / Pressure
        print(f"Result: the volume is {volume} in L: ")
        
    
    elif choice == '3':
        print("\n--- Reynolds Number Calculator ---")
        density = float(input("Enter fluid density in kg/m^3: "))
        velocity = float(input("Enter fluid velocity in m/s: "))
        diameter = float(input("Enter pipe diameter in m: "))
        viscosity = float(input("Enter dynamic viscosity in Pa·s: "))
        
        reynolds = (density * velocity * diameter) / viscosity
        print(f"Result: The Reynolds Number is {reynolds}")
        
        # This uses the if/elif logic you are learning!
        if reynolds < 2300:
            print("Flow State: Laminar")
        elif 2300 <= reynolds <= 4000:
            print("Flow State: Transitional")
        else:
            print("Flow State: Turbulent")
    
    
    elif choice == '4':
        print("Exiting the calculator. Goodbye!")
        break # This command shatters the 'while True' loop and ends the script
        
    else:
        # This catches any typos if you press '4' or a letter by mistake
        print("Invalid input. Please type 1, 2, or 3.")