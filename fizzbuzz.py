def fizzbuzz(number): 
    result = []
    for n in range(1, number + 1):
        if n % 3 == 0 and n % 5 == 0: 
            result.append('FizzBuzz')
        elif n % 3 == 0:
            result.append('Fizz')
        elif n % 5 == 0:
            result.append('Buzz')
        else:
            result.append(n) 
    return result