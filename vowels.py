vowels_and_constants=["a","e","i","o","u","r","t","w","A","P","E","X","U"]
print(vowels_and_constants)
vowels=["a","e","i","o","u"]
vowels_list=[]
constant_list=[]
for i in vowels_and_constants:
    i = i.lower()
    if i in vowels:
        vowels_list.append(i)
    else:
        constant_list.append(i)
print(vowels_list)
print(constant_list)


string="Luminar Is the Best iNstitUte"
print(string)
lower_count=0
upper_count=0
space_count=0
for i in string:
    if i.isspace():
        space_count+=1
    elif i.islower():
        lower_count+=1
    else:
        upper_count+=1
print("lower_count",lower_count)
print("upper_count",upper_count)
print("space_count",space_count)