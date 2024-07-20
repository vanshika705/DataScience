
ls=[65,85,24,6,35,98,64,23,96,90,245,86,48]
#  finding maximum element
def find_max(ls):
    max=0
    for i in  ls:
        if i>max:
            max=i
    return max         
print("maximum is-->",find_max(ls))

#  finding minimum element 
def find_min(ls):
    min=ls[0]
    for i in  ls:
        if i<min:
            min=i
    return min            
print("minimum is-->",find_min(ls))
        
