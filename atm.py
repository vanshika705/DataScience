name=input(" plz enter your name :")
print("hello",name,"!")
message="""
How may i help you sir/mam .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL."""

print(message)

task=int(input("pls enter your option:"))
available_amount=5000
 
if (task>=1 and task<=3):
    print("welcome to you in our virtual bank !")
    # check balance
    if task== 1:
        print("your avaliable amount is :-",available_amount)
    # deposit
    elif task ==2:
        deposit_amount=int(input("pls enter amount deposit amount:-"))
        if deposit_amount>500:
            available_amount+=deposit_amount
            print("you have successfully deposit amount .")
            print("your available_amount is ",available_amount)
        else:
            print("pls enter more than 500 !")
    
    # withdrawl 
    else:
       withdrawl_amount=int(input("pls enter amount to withdraw :-"))
       if withdrawl_amount>5000:
           print("pls withdraw less than 5000")
       else:
           available_amount-=withdrawl_amount
           print("your available_amount is ",available_amount)  
           
else:
    print("pls select valid option !")
    
  
         





