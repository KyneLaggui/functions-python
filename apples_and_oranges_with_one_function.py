print("The price of Apple is 20 pesos")
print("The price of Oranges is 25 pesos")

def QuantityofFruits():
    ApplePrice= 20
    OrangePrice=25
    Quantity_of_A=int(input("How many apples you want to buy? "))
    Quantity_of_O= int(input("How many oranges you want to buy? "))
    TotalApples= Quantity_of_A * ApplePrice
    TotalOranges= Quantity_of_O * OrangePrice
    TotalAmount= TotalApples + TotalOranges
    return ApplePrice, OrangePrice, Quantity_of_A, Quantity_of_O, TotalApples, TotalOranges, TotalAmount

def display(AmountT_):
    print(f"The total amount is {AmountT_}")






AppleP, OrangeP, AppleF, OrangeF,AppleT,OrangeT, AmountT= QuantityofFruits()
display(AmountT)