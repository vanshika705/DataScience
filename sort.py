ls=[65,85,24,6,35,98,64,23,96,90,245,86,48]

def sort_list(ls):
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            
            if ls[i]<ls[j]:
                ls[i],ls[j]=ls[j],ls[i]
    return ls            
print(sort_list(ls))           
        