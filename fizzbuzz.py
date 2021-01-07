def fizzbuzz(n):
    for x in range(n):
        if x % 5 == 0 and x % 3 == 0:
            print('fizzbuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        print(x)


print(fizzbuzz(20))
