def get_numbers():
nunbers_input = input(" Enter numbers separeated by commas: ")
number = [float(num) for num in numbers_input.split(",")
return number

def square_numbers(numbers):
def display_numbers(numbers):


def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

main()
