#Bruce Diaz
# this program will take a list of numbers and returns with a new list

def unique_list():
    x=[]
    for a in 1:
        if a not in x:
            x.append(a)
            return x
print(unique_list([1,3,3,3,6,2,3,5]))