Challenge: Largest Palindrome
A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers. Afterward, write a brief explanation walking through your code's logic in markdown.


Challenge explination:
First, we need to create a list to store the product of our multiplication. I called this palindromes.

Then we need to iterate through two variables, x and i, where we are multipliying from 100 to 999 in each.

While x and i are < 1000, we want to check if the product is a palindrome using if (num[::-1] == num).

If it is a palindrome, add the product to the list we created and the continue through the for loop until X >= 100 and i >= 1000).

If it is NOT a palindrome, continue through the for loop.

Since the palindrome list has many values, we want to print the largest value since that is what was asked in the question.

If you wanted the smallest value, you could add: print(min(palindromes)) and get 10201.