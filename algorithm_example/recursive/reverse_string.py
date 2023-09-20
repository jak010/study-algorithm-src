def reverse_string(string):
    if len(string) == 1:
        return string[0]

    return reverse_string(string[1:len(string)]) + string[0]


print(reverse_string("abcde"))
