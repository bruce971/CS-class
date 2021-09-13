#Bruce Diaz
# this function will take a year and reutn true if the year is a leap year, false if not.
def is_leap(n):
    if n %400==0:
     return True
    if n % 100 ==0:
     return False
    if n % 4 == 0 :
        return True
    return False
    
         
