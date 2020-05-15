

with open("file.txt", 'r') as fh:
    data = fh.readline()

lis= data.split(' ')
my_dict={}

for key in lis:
    if key in my_dict.keys():
        my_dict[key] += 1
    else:
        my_dict[key] = 1

print(my_dict)
