#Bruce Diaz 
# this program will multiply the numbers in the list
myList=(5,2,7,-1)
def multiplylist(myList):
    result=1
    for x in myList:
        result=result*x
        return result
print(multiplylist(myList))