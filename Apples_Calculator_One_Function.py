def Calculator_of_Apples():
    money_of_user= int(input("Amount of Money you have?: "))
    amount_of_apple= int(input("How much does an apple cost?: "))
    user_can_buy= money_of_user//amount_of_apple
    user_change= money_of_user%amount_of_apple
    return money_of_user, amount_of_apple, user_can_buy,user_change

def display(UserCanBuy, User_Change):
    print(f"You can buy {UserCanBuy} apples and your change is {User_Change} pesos")
    
    
    
MoneyU,AppleAmount,UserBuy,UserChange =Calculator_of_Apples()
display(UserBuy,UserChange)