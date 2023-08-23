def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers

def main():
    input_str = input("Input a list of numbers separated by spaces: ")
    numbers = [int(x) for x in input_str.split()]

    positive_numbers = print_positive_numbers(numbers)
    print(f"Input: {numbers}")
    print(f"Output: {positive_numbers}")

if __name__ == "__main__":
    main()
