my_list=[]
swap=0

while True:
    val_str = input('Enter the list:')
    swap = int(input('Enter the position to swap the value to last:'))
    if swap > len(my_list):
        print('Please enter the correct position\n')
        my_list = val_str.split(',')
        print (my_list)

    for val in range(swap):
        my_list.append(my_list.pop(0))

    print (my_list)

