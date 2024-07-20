ls=[2,6,95,24,23.76,24.987,23.97,True,False,'yes','no']

# counting boolean type elements
count_bool=0
for i in ls:
    if (i==True or i==False ):
        count_bool+=1
print(count_bool)    

# counting integer type elements
count_int=0
for i in ls:
    if type(i)==int:
        count_int+=1
print(count_int) 

# counting float type elements
count_float=0
for i in ls:
    if type(i)==float:
        count_float+=1
print(count_float)     

# counting string type elements
count_string=0
for i in ls:
    if type(i)==str:
        count_string+=1
print(count_string)    
         

   