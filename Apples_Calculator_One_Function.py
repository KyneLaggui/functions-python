def UserInput_Money_and_Apple():
    money_of_user= int(input("Amount of Money you have?: "))
    amount_of_apple= int(input("How much does an apple cost?: "))
    return money_of_user, amount_of_apple

def CalculatorApples(MoneyU, AmountA):
    user_can_buy= MoneyU//AmountA
    user_change= MoneyU%AmountA
    return user_can_buy, user_change

def display():
    print(f"You can buy {user_can_buy} apples and your change is {user_change} pesos")
         
money_of_user, amount_of_apple= UserInput_Money_and_Apple()
user_can_buy, user_change= CalculatorApples(money_of_user,amount_of_apple)
display()