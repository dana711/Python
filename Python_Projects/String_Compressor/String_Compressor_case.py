string_input = input('Enter a string (can be uppercase or lowercase letters): ')

comp_str = ''

count = 1
for x in range(len(string_input) - 1):
    if string_input[x] == string_input[x + 1]:
        count += 1
    else:
        comp_str += string_input[x] + str(count)
        count = 1
comp_str += string_input[x + 1] + str(count)

if len(string_input) >= len(comp_str):
    print(string_input)
else:
    print(comp_str)
