# create file logic.py
#  create file solve.py
# min , max , sort() without sort fuction -----> inside logic.py
# import in solve.py
ls=[65,85,24,6,35,98,64,23,96,90,245,86,48]
#  finding maximum element
def find_max(ls):
    max=0
    for i in  ls:
        if i>max:
            max=i
    return max         


#  finding minimum element 
def find_min(ls):
    min=ls[0]
    for i in  ls:
        if i<min:
            min=i
    return min     
    
# sorting 
def sort_list(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):

            if ls[i]<ls[j]:
                ls[i],ls[j]=ls[j],ls[i]
    return ls      
            
        
        