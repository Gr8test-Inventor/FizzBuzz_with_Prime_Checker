def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
    if is_prime:
        return "This is a prime number."
    else:
        return "This is not a prime number."

game_on = True
while game_on:
    user_number = int(input("Enter a number:\t"))
    prime_result = prime_checker(user_number)

    if user_number % 5 == 0 and user_number % 3 == 0:
        fb_result = "FizzBuzz"
    elif user_number % 3 == 0:
        fb_result = "Fizz"
    elif user_number % 5 == 0:
        fb_result = "Buzz"
    else:
        fb_result = ""

    print(f"Number: {user_number}\nFizzBuzz: {fb_result}\nPrime Status: {prime_result}")
    restart = input("Enter another number? Y or N\t").lower()

    if restart == "n":
        game_on = False
    else:
        print("\n\n")
