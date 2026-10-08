def calculate_density():
    print("\n--- Density Calculator ---")
    try:
        mass = float(input("Enter mass in kg: "))
        volume = float(input("Enter volume in m^3: "))
        density = mass / volume
        print(f"Result: The density is {density} kg/m^3")
    except ValueError:
        print("Error: Please enter a valid number, not letters.")

def calculate_ideal_gas():
    print("\n--- Ideal Gas Volume Calculator ---")
    try:
        moles = float(input("Enter moles: "))
        temperature = float(input("Enter Temperature in Kelvin (T): "))
        pressure = float(input("Enter Pressure in atm (P): "))
        r = 0.0821
        volume = (moles * r * temperature) / pressure
        print(f"Result: The volume is {volume} L")
    except ValueError:
        print("Error: Please enter a valid number, not letters.")

def calculate_reynolds():
    print("\n--- Reynolds Number Calculator ---")
    try:
        density = float(input("Enter fluid density in kg/m^3: "))
        velocity = float(input("Enter fluid velocity in m/s: "))
        diameter = float(input("Enter pipe diameter in m: "))
        viscosity = float(input("Enter dynamic viscosity in Pa·s: "))
        
        reynolds = (density * velocity * diameter) / viscosity
        print(f"Result: The Reynolds Number is {reynolds}")
        
        if reynolds < 2300:
            print("Flow State: Laminar")
        elif 2300 <= reynolds <= 4000:
            print("Flow State: Transitional")
        else:
            print("Flow State: Turbulent")
    except ValueError:
        print("Error: Please enter a valid number, not letters.")

print("Welcome to the Engineering Calculator!")

while True:
    print("\n--- Main Menu ---")
    print("1. Calculate Density (ρ = m/V)")
    print("2. Calculate Ideal Gas Volume (V = nRT/P)")
    print("3. Calculate Reynolds Number")
    print("4. Quit")
    
    choice = input("Select an option (1, 2, 3, or 4): ")
    
    if choice == '1':
        calculate_density() # Calls the function above!
        
    elif choice == '2':
        calculate_ideal_gas()
        
    elif choice == '3':
        calculate_reynolds()
        
    elif choice == '4':
        print("Exiting the calculator. Goodbye!")
        break
        
    else:
        print("Invalid input. Please type 1, 2, 3, or 4.")