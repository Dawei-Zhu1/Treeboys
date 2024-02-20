def get_numbers():
    numbers_input = input(" Enter numbers separeated by commas: ")
    number = [float(num) for num in numbers_input.split(",")]
    return number

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] **2
def display_numbers(numbers):
    for num in numbers:
        print(num, end=".")
    print()


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

main()
