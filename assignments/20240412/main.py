def fizzbuzz(n: int) -> None:
    "Prints n lines of the FizzBuzz game."

    if n < 1:
        print('InputError, input natural numbers')
        exit()
    try:
        for index in range(1,n+1):
            if index % 5 == 0 and index % 3 == 0:
                print('FizzBuzz')

            elif index % 5 == 0:
                print('Buzz')

            elif index % 3 == 0:
                print('Fizz')

            else:
                print(index)
    except TypeError:
        print('TypeError, input natural numbers')

if __name__ == '__main__':
    fizzbuzz(30)
    fizzbuzz(1)
    fizzbuzz(5.8)
    fizzbuzz(-3)