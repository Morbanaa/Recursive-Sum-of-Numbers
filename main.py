#Teddy Rodd
#Morbanaa Studios
#Sum of Numbers

def main():
    total = 0
    while True:
        try:
            number = int(input("Enter a number to get the sum from 1 to that number: "))
            if number < 1:
                print("The number must be greater than zero")
                continue
            break
        except ValueError:
            print("You must enter a number")

    # Recives and prints results
    total = sum_of_number(number,total)
    print(f"Total sum of 1-{number}: {total}")

# Counts sum from 1 to given number
def sum_of_number(number,total):
    if number == 0:
        return total
    else:
        return sum_of_number(number - 1,total + number)

# Program Entry Point
if __name__ == "__main__":
    main()