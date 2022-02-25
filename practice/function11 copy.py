# coffee  order program 
coffee = """
        Espresso 
        Latte
        Cappuccino 
        Americano
        Cortado
        Mocca 
        Redeye
        Macchiato 
        Flat_White
        Irish
        """
customer_choice = []
# order will be received and stored for the purpose of making coffee 
print(coffee)
# order is also collected and stored for future decision making on  which coffee types are ordered most 
keep_asking= True
while keep_asking:
    coffee_choice = str(input("Please choose your coffee type or say custom:    ").lower())
    def coffee_make(coffee_choice):
        
        if coffee_choice == "espresso":
                    print("ground, extra-dark beans, that are run through a pressurized machine that produces only one, highly-concentrated shot at a time")
                    print("your espresso is being made") 
                    order_type = str(input("Do you want it here or to go?   "))
                    def order_Type(order_type):
                            if order_type  == "to go":
                                print("your coffee will be delivered in the plastic cup")
                            else:
                                 print("your coffee will be delivered in the glass cup")    
                    order_Type(order_type) 
        elif  coffee_choice == "latte":
                    print("heavy on steamed milk which is blended with rather than layered on top of the espresso and light on foam")
                    print("your latte is being made") 
        elif  coffee_choice == "cappuccino":
                    print("an even distribution of steamed milk, foamed milk, and espresso")
        elif  coffee_choice == "americano":
                    print("an espresso shot diluted with hot water")
                    print("your Americano is being made") 
        elif  coffee_choice == "cortado":
                    print("Equal parts espresso and steamed milk. The milk balances the sharp bitterness of the espresso")
                    print("your Cortado is being made")   
        elif  coffee_choice == "mocca":
                    print("Cocoa kick and creaminess from steamed milk")
                    print("your Mocca is being made")
        elif  coffee_choice == "redeye":
                print("this is a full cup of coffee with an espresso shot stirred in")
                print(" your Redeye is being made")
        elif coffee_choice == "macchiato":
                print("Combine three parts foam with one part espresso")
                print(" your Macchiato is being made")
        elif  coffee_choice == "flat_White":
                 print("a double shot of espresso with steamed milk")
        elif  coffee_choice == "irish":
                print("an Irish coffee is a combination of coffee, sugar, cream, and whiskey")
                print(" your Irish coffee is being made")
        elif coffee_choice == "custom":
                    print("sorry, we cannot do custom today")
                    keep_asking =False
                    
    coffee_make(coffee_choice)
    list_of_choice= customer_choice.append(coffee_choice)
    print(list_of_choice)        
                
         
             
    




         
    # order type function will take to delivery type and act accordingly 
 
     
    
       
# the print function eventually will display the orders that were made 
     
        