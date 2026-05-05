#Teddy Rodd
#Morbanaa Studios
#Sum of Numbers

def main():
    while True:
        try:
            number = int(input("Enter a number to get the sum from 1 to that number: "))
            if number < 1:
                print("The number must be greater than zero")
                continue
            break
        except ValueError:
            print("You must enter a number")
    sum_of_number(number)

def sum_of_number(number):
    total = 0
    for num in range(number + 1):
        total+= num

    print(f"Total: {total}")

if __name__ == "__main__":
    main()