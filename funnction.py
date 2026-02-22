

def take_numbers():
    l = []

    while True:
        a = input("give input until stop:")
        if a =='stop':
            break
        
        l.append(int(a))
    return l
        #

def calculate(l):
    if len(l) == 0:
        print("enter list numbers")
        return
    print("sum :",sum(l))
    print("maximum number :",max(l))
    average = (sum(l))/(len(l))
    print("average: ", average)
    print("minimum number:", min(l))

exp = take_numbers()
calculate(exp)

