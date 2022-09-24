
my_ascii_dict_loweralpha= {}  # creating empty dict for lower and upper alpha
my_ascii_dict_upperalpha= {}

ascii_value_of_a = ord("a")   # knowing ascii value of first character fo lower and upper alpha
print(ascii_value_of_a)
ascii_value_of_A = ord("A")
print(ascii_value_of_A)

for i in range(97, 97 + 26):   # populating and printing ascii dictionary of lower alpha
    my_ascii_dict_loweralpha[chr(i)] = i
print("lower alpha dictionary = ", my_ascii_dict_loweralpha) 

for i in range(65, 65 + 26):   # populating and printing ascii dictionary of lower alpha
    my_ascii_dict_upperalpha[chr(i)] = i
print("lower alpha dictionary = ", my_ascii_dict_upperalpha)  