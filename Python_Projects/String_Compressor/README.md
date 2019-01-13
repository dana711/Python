Challenge: String Compressor
Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown.


Challenge Explanation
First, I have created a variable that will be assigned based on what the user enters.

The first set of code will count based on a mixed case (case sensitive) - "a" and "A" will be counted as two different values.

If we want to make the code case insestive ("a" and "A" would count towards the same value), we would need to run the 2nd set of code where we set the input string to be all lower case and then count.

In the code that does the counting, we need to create a variable called compr_str to hold the values we want to compare with in the for loop.

Since we don't know the length of the input string, we need to dynamically set the values in the range based on the length of the string.

We can't do x + 1 and get a number greater than the length of the indexed word, so I have created a range of the length of the string - 1 so I can do my compare +1 and not hit any errors.

Since we are looking at length - 1, we need to then do a final addition to the comp_str value to get the last character evaluated.