import re


# first = 0
# second = 1

# while counter < 100:
#     print(first)
#     temp = first
#     first = first + second
#     second = temp
#     counter += 1


# characters = "abcdefghijklmnopqrstuvwxyz"

# for index, _char in enumerate(characters):
#     added_string = ""
#     for added in characters[index:] + characters[:index]:
#         added_string += added
#         print (added_string)

# l m n o

# input = "lmno"
# regex_string = r'\w+(?=l)|(?<=l)\w+(?=m)|(?<=m)\w+(?=n)|(?<=n)\w+(?=o)|(?<=o)\w+'
# #                aaaaaa1bbbbbb1ccccccc2bbbbbb2ccccccc3bbbbbb3ccccccc4bbbbbb4dddd

# a_component = r'\w+(?='
# b_component = r')|(?<='
# c_component = r')\w+(?='
# d_component = r')\w+'

# output = a_component
# for index, char in enumerate(input):
#     output += char + b_component + char
#     if index != len(input) - 1:
#         output += c_component
# output += d_component
# print(output)
# print(regex_string)

# reg_obj = re.compile(output)
# mo = reg_obj.findall("flamingos")

# print(mo)


import itertools
input = "abc"
vectors = list(itertools.product([0, 1], repeat=len(input) + 1))
vectors += list(itertools.product([0, 2], repeat=len(input) + 1))[1:]

print(vectors)

for group in vectors:
    counter = 0
    output = "" + str(counter) * group[counter]
    counter += 1
    for char in input:
        output += char + str(counter) * group[counter]
        counter += 1
    print (output)