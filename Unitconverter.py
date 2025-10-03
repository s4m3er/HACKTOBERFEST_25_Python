def temperature_converter():
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    try:
        choice = int(input("Choose conversion type (1-6): "))
        value = float(input("Enter temperature value: "))
        
        if choice == 1:
            # Celsius to Fahrenheit
            result = (value * 9/5) + 32
            print(f"{value}°C = {result:.2f}°F")
        elif choice == 2:
            # Fahrenheit to Celsius
            result = (value - 32) * 5/9
            print(f"{value}°F = {result:.2f}°C")
        elif choice == 3:
            # Celsius to Kelvin
            result = value + 273.15
            print(f"{value}°C = {result:.2f}K")
        elif choice == 4:
            # Kelvin to Celsius
            result = value - 273.15
            print(f"{value}K = {result:.2f}°C")
        elif choice == 5:
            # Fahrenheit to Kelvin
            result = (value - 32) * 5/9 + 273.15
            print(f"{value}°F = {result:.2f}K")
        elif choice == 6:
            # Kelvin to Fahrenheit
            result = (value - 273.15) * 9/5 + 32
            print(f"{value}K = {result:.2f}°F")
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter valid numbers!")

def length_converter():
    print("\n=== Length Converter ===")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Centimeters to Inches")
    print("6. Inches to Centimeters")
    
    try:
        choice = int(input("Choose conversion type (1-6): "))
        value = float(input("Enter length value: "))
        
        if choice == 1:
            # Meters to Feet
            result = value * 3.28084
            print(f"{value} meters = {result:.2f} feet")
        elif choice == 2:
            # Feet to Meters
            result = value / 3.28084
            print(f"{value} feet = {result:.2f} meters")
        elif choice == 3:
            # Kilometers to Miles
            result = value * 0.621371
            print(f"{value} km = {result:.2f} miles")
        elif choice == 4:
            # Miles to Kilometers
            result = value / 0.621371
            print(f"{value} miles = {result:.2f} km")
        elif choice == 5:
            # Centimeters to Inches
            result = value * 0.393701
            print(f"{value} cm = {result:.2f} inches")
        elif choice == 6:
            # Inches to Centimeters
            result = value / 0.393701
            print(f"{value} inches = {result:.2f} cm")
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter valid numbers!")

def weight_converter():
    print("\n=== Weight Converter ===")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Kilograms to Ounces")
    print("4. Ounces to Kilograms")
    print("5. Pounds to Ounces")
    print("6. Ounces to Pounds")
    
    try:
        choice = int(input("Choose conversion type (1-6): "))
        value = float(input("Enter weight value: "))
        
        if choice == 1:
            # Kilograms to Pounds
            result = value * 2.20462
            print(f"{value} kg = {result:.2f} lbs")
        elif choice == 2:
            # Pounds to Kilograms
            result = value / 2.20462
            print(f"{value} lbs = {result:.2f} kg")
        elif choice == 3:
            # Kilograms to Ounces
            result = value * 35.274
            print(f"{value} kg = {result:.2f} oz")
        elif choice == 4:
            # Ounces to Kilograms
            result = value / 35.274
            print(f"{value} oz = {result:.2f} kg")
        elif choice == 5:
            # Pounds to Ounces
            result = value * 16
            print(f"{value} lbs = {result:.2f} oz")
        elif choice == 6:
            # Ounces to Pounds
            result = value / 16
            print(f"{value} oz = {result:.2f} lbs")
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter valid numbers!")

def main():
    print("🔢 UNIT CONVERTER")
    print("=" * 30)
    
    while True:
        print("\nSelect conversion type:")
        print("1. Temperature")
        print("2. Length")
        print("3. Weight")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                temperature_converter()
            elif choice == 2:
                length_converter()
            elif choice == 3:
                weight_converter()
            elif choice == 4:
                print("Thank you for using the Unit Converter! 👋")
                break
            else:
                print("Invalid choice! Please select 1-4.")
                
        except ValueError:
            print("Please enter a valid number!")

        # Ask if user wants another conversion
        if choice != 4:
            continue_choice = input("\nPerform another conversion? (y/n): ").lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Unit Converter! 👋")
                break

# Run the converter
if __name__ == "__main__":
    main()
