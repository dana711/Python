Challenge: Summation of Primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000. Afterward, write a brief explanation walking through your code's logic in markdown.



Challenge Explanation
First, I want to create a variable called primes to add up each number that the codes identifies as a prime number.

Then the code iterates through a range of 2 up to, but not including, 2000, since the problem asks for "all primes below 2,000." We start at 2 because we know that the number 1 is not a prime number based on the definition of a prime number.

Create the isPrime variable and initiate it too True.

Work through the range and divide by every number up to, but not including, the number in question.

If that number can be divided by other numbers other than 1 or itself, then the number is NOT prime. The program sets the isPrime variable to False and then breaks/exits the for loop for that number. There is no reason to keep checking if other numbers are divisible into the number in question - once we know one other number can used to divide, then we know the number is not prime and we don't need to use system resources to keep checking the math.

If that number can't be divided by any other number, then we set isPrime to True and add that number to the primes variable.

Once the code has iterated through 1999, the code stops and prints out the sum of all the prime numbers.