
# the purpose of this program is to print all prime numbers between 1 and 100
def main():
    #create list of numbers
    numbers = list(range(1,101))
    #create list of prime numbers
    prime_numbers = []
    #loop through numbers
    for number in numbers:
        #check if number is prime
        if number > 1:
            for i in range(2,number):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)
    #print prime numbers
    print(prime_numbers)

if __name__ == '__main__':
    main()