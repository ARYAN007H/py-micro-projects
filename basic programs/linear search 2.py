def get_integer_input(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    elements = []
    num_elements = get_integer_input("How many numbers do you want to add to the list? ")

    for i in range(num_elements):
        element = get_integer_input(f"Element {i + 1}: ")
        elements.append(element)

    print("\nOriginal list:", elements)
    search_element = get_integer_input("Enter an element you want to search for: ")
    positions = [index for index, value in enumerate(elements) if value == search_element]

    if positions:
        print(f"Element found at positions: {', '.join(map(str, positions))}")
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
