'''files = open("numbers.txt","w")
files.write("hello jai shree ram \n")
files.write("jai bhavani")
files.close()'''

def list_number():
    list =[]

    while True:
        ip = input("enter the number \(s: stop): \n")
        if ip == 's':
            break
        d = int(ip)
        list.append(d)

    return list
   

def calculate(list):
    print("totall sum of list: ", sum(list))
    return

a = list_number()
calculate(a)

'''filess = open("numbers.txt", "w")
for i in list :
    filess.write(str(i)+ "\n")
filess.close()'''
with open("number.txt",'w') as file:
    for i in a:
        file.write(str(i) + "\n")
