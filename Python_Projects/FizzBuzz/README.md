Challenge: FizzBuzz
Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz;" for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." Afterward, write a brief explanation walking through your code's logic in markdown.


Explination
We need to iterate through the numbers 1 to 100, including 100, so the range needs to be from 0 to 101, since we do not include the last number (101).

Since there are some numbers that are divisible by both 3 and 5, we need to check that first with an AND statement. From there, we check if they are divisible by 3 or 5 and print the expected wording.