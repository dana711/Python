Challenge: Multiples of 3 and 5
If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000. Afterward, write a brief explanation walking through your code's logic in markdown.


Challenge Explanation
First, I want to create a variable to keep track of the sum of the numbers that are divisible by 3 or 5 (meaning they are a multiple of 3 or 5). I called this sum_nums and set it = 0.

Then we want to iterate through the range of numbers between 1 and up to, but not including, 1000, since the problem asks for "below 1,000."

We can check both divisible by 3 and 5 in the same if statement by using an OR command. In either case, we want to add that number to the sum_nums variable and continue through the range until we get to 1,000.

Once we have iterated through all of the numbers, we want to print the value of the sum of all numbers that are a multiple of 3 or 5.