print("The price of Apple is 20 pesos")
print("The price of Oranges is 25 pesos")

def User_Input_Fruits():
    Quantity_of_A=int(input("How many apples you want to buy? "))
    Quantity_of_O= int(input("How many oranges you want to buy? "))
    return Quantity_of_A, Quantity_of_O

def Calculations_of_Fruits(UserApple, UserOranges): 
    ApplePrice= 20
    OrangePrice=25
    TotalApples= UserApple * ApplePrice
    TotalOranges= UserOranges * OrangePrice
    TotalAmount= TotalApples + TotalOranges
    return TotalAmount
def display():
    print(f"The total amount is {TotalAmount}")






Quantity_of_A, Quantity_of_O= User_Input_Fruits()
TotalAmount= Calculations_of_Fruits(Quantity_of_A, Quantity_of_O)
display()