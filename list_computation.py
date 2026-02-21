list = []

while True:
    a = input("enter nuber stop : ")

    if a == 'stop':
        break
    
    list.append(int(a))

print(list)
#print(max(list))
length_list = len(list)
average_list= sum(list)/length_list
print(average_list)