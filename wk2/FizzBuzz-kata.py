# The Fizzbuzzkataunittest.py file should be able to achieve the following tests:
    # Get “1” when I pass in 1
    # Get “2” when I pass in 2
    # Get “Fizz” when I pass in 3
    # Get “Buzz” when I pass in 5
    # Get “Fizz” when I pass in 6 (a multiple of 3)
    # Get “Buzz” wen I pass in 10 (a multiple of 5)
    # Get “FizzBuzz” when I pass in 15 (a multiple of 3 and 5)
# In the fizzbuzzkataunittest.py file, write a code that should achieve above tests through failing test, production test and the refractor test. 


for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)