prompt = """
1. Single
2. Married filed jointly
3. Married filed  separately 
4. Heads of the household 
"""
print(prompt)

income = int(input("Enter your income:   "))
status = int(input("Enter the number for your respective marital  status: "))
if status ==1:
        if 0 <= income <= 9875:
            print(income*0.1)
        elif 9876 <= income <= 40125:
            print(987.50 + (0.12 * (income - 9875)))
        elif  40126 <= income <= 85525:
            print(4617.50 + (0.22 * (income - 40125)))
        elif 85526 <= income <= 163300:
            print(14605.50 + (0.24 * (income - 85525)))
        elif 163301 <= income <= 207350:
            print(33271.50 + (0.32 * (income - 163300)))
        elif 207351 <= income <= 518400:
            print(47367.50 + (0.35 * (income - 207350)))
        elif income >= 518401:
            print(156235 + (0.37 * (income - 518400))) 
if status == 2:
    if 0 <= income <= 19750:
        print(income*0.1)
    elif  19751 <= income <= 80250:
        print(1975 + (0.12 * (income - 19750)))
    elif 80251 <= income <= 171050:
        print(9235 + (0.22 * (income - 80250)))
    elif 171051 <= income <= 326600:
        print(29211 + (0.24 * (income - 171050)))
    elif 326601 <= income <= 414700:
        print(66543 + (0.32 * (income - 326600)))
    elif 414701 <= income <= 622050:
        print(94735 + (0.35 * (income - 414700)))
    elif income >= 622051:
        print(167307.50 + (0.37 * (income - 622050))) 
if status == 3:
    if 0 <= income <= 9875:
        print(income*0.1)
    elif 9876 <= income <= 40125:
        print(98750 + (0.12 * (income - 9875)))
    elif 40126 <= income <= 85525:
        print(4617.50 + (0.22 * (income - 40125))) 
    elif 85526 <= income <= 163300:
        print(14605.50 + (0.24 * (income - 85525)))
