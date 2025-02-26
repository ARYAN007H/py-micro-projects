def unit_conversion(unit):
    try:
        if unit == 1:
            km = float(input("Enter kilometers: "))
            miles = km * 0.621371
            print(f"{km} km is approximately {miles:.2f} miles")
        elif unit == 2:
            m = float(input("Enter meters: "))
            feet = m * 3.28084
            inches = m * 39.3701
            print(f"{m} m is approximately {feet:.2f} feet or {inches:.2f} inches")
        elif unit == 3:
            kg = float(input("Enter kilograms: "))
            pounds = kg * 2.20462
            print(f"{kg} kg is approximately {pounds:.2f} pounds")
        elif unit == 4:
            celsius = float(input("Enter Celsius temperature: "))
            fahrenheit = (celsius * 9/5) + 32
            kelvin = celsius + 273.15
            print(f"{celsius}°C is approximately {fahrenheit:.2f}°F or {kelvin:.2f}K")
        elif unit == 5:
            liters = float(input("Enter liters: "))
            gallons = liters * 0.264172
            quarts = liters * 1.05669
            print(f"{liters} liters is approximately {gallons:.2f} gallons or {quarts:.2f} quarts")
        elif unit == 6:
            acres = float(input("Enter acres: "))
            hectares = acres * 0.404686
            square_meters = acres * 4046.86
            print(f"{acres} acres is approximately {hectares:.2f} hectares or {square_meters:.2f} square meters")
        elif unit == 7:
            inches = float(input("Enter inches: "))
            centimeters = inches * 2.54
            print(f"{inches} inches is approximately {centimeters:.2f} centimeters")
        elif unit == 8:
            pounds = float(input("Enter pounds: "))
            kilograms = pounds * 0.453592
            print(f"{pounds} pounds is approximately {kilograms:.2f} kilograms")
        elif unit == 9:
            miles_per_hour = float(input("Enter miles per hour: "))
            kilometers_per_hour = miles_per_hour * 1.60934
            print(f"{miles_per_hour} mph is approximately {kilometers_per_hour:.2f} km/h")
        elif unit == 10:
            feet_per_second = float(input("Enter feet per second: "))
            meters_per_second = feet_per_second * 0.3048
            print(f"{feet_per_second} ft/s is approximately {meters_per_second:.2f} m/s")
        else:
            print("Invalid unit choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def menu():
    print("Menu")
    print("Unit conversion:")
    print()
    print("[1] Kilometers to Miles")
    print("[2] Meters to Feet and Inches")
    print("[3] Kilograms to Pounds")
    print("[4] Celsius to Fahrenheit and Kelvin")
    print("[5] Liters to Gallons and Quarts")
    print("[6] Acres to Hectares and Square Meters")
    print("[7] Inches to Centimeters")
    print("[8] Pounds to Kilograms")
    print("[9] Miles per Hour to Kilometers per Hour")
    print("[10] Feet per Second to Meters per Second")
    print("[0] Exit")

def main():
    while True:
        menu()
        try:
            unit = int(input("Enter your choice: "))
            if unit == 0:
                break
            unit_conversion(unit)
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()