string_input = input('Enter a string (can be uppercase or lowercase letters): ')

comp_str_lower = ''
string_input_lower = string_input.lower()

count = 1
for x in range((len(string_input_lower) - 1)):
    if string_input_lower[x] == string_input_lower[x + 1]:
        count += 1
    else:
        comp_str_lower += string_input_lower[x] + str(count)
        count = 1
comp_str_lower += string_input_lower[x + 1] + str(count)


if len(string_input_lower) >= len(comp_str_lower):
    print(string_input_lower)
else:
    print(comp_str_lower)
