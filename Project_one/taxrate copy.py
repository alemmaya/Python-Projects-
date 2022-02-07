#calaculating income after tax 
# first diplay list of numbers related to filing statuses  
prompt = """
1. Single
2. Married filed jointly
3. Married filed  separately 
4. Heads of the household 
"""
print(prompt)

income = int(input("Enter Taxable Income:   "))
status = int(input("Enter Filing Status: "))
#writing conditonal statements for each filing status and tax ranges within them using nested statments 
if status ==1:
        if 0 <= income <= 9875:
             tax= income*0.1
             income_after_tax = income-tax
             print(f"Your Taxable Income is {income}")
             print(f"Your Tax Bill is {tax}")
             print(f"Your Income after Tax is {income_after_tax}")

        elif 9876 <= income <= 40125:
            tax=987.50 + (0.12 * (income - 9875))
            income_after_tax = income-tax
            print(f"Your Taxable Income is {income}")
            print(f"Your Tax Bill is {tax}")
            print(f"Your Income after Tax is {income_after_tax}")
            
        elif  40126 <= income <= 85525:
            tax=4617.50 + (0.22 * (income - 40125))
            income_after_tax = income-tax
            print(f"Your Taxable Income is {income}")
            print(f"Your Tax Bill is {tax}")
            print(f"Your Income after Tax is {income_after_tax}")
        elif 85526 <= income <= 163300:
           tax=14605.50 + (0.24 * (income - 85525))
           income_after_tax = income-tax
           print(f"Your Taxable Income is {income}")
           print(f"Your Tax Bill is {tax}")
           print(f"Your Income after Tax is {income_after_tax}")
        elif 163301 <= income <= 207350:
            tax=33271.50 + (0.32 * (income - 163300))
            income_after_tax = income-tax
            print(f"Your Taxable Income is {income}")
            print(f"Your Tax Bill is {tax}")
            print(f"Your Income after Tax is {income_after_tax}")
        elif 207351 <= income <= 518400:
            tax=47367.50 + (0.35 * (income - 207350))
            income_after_tax = income-tax
            print(f"Your Taxable Income is {income}")
            print(f"Your Tax Bill is {tax}")
            print(f"Your Income after Tax is {income_after_tax}")
        elif income >= 518401:
            tax=156235 + (0.37 * (income - 518400)) 
            income_after_tax = income-tax
            print(f"Your Taxable Income is {income}")
            print(f"Your Tax Bill is {tax}")
            print(f"Your Income after Tax is {income_after_tax}")
if status == 2:
    if 0 <= income <= 19750:
        tax=income*0.1
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif  19751 <= income <= 80250:
        tax=1975 + (0.12 * (income - 19750))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 80251 <= income <= 171050:
        tax=9235 + (0.22 * (income - 80250))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 171051 <= income <= 326600:
        tax=29211 + (0.24 * (income - 171050))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 326601 <= income <= 414700:
       tax=66543 + (0.32 * (income - 326600))
       income_after_tax = income-tax
       print(f"Your Taxable Income is {income}")
       print(f"Your Tax Bill is {tax}")
       print(f"Your Income after Tax is {income_after_tax}")
    elif 414701 <= income <= 622050:
        tax=94735 + (0.35 * (income - 414700))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif income >= 622051:
        tax=167307.50 + (0.37 * (income - 622050))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
if status == 3:
    if 0 <= income <= 9875:
        tax=income*0.1
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 9876 <= income <= 40125:
        tax=98750 + (0.12 * (income - 9875))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 40126 <= income <= 85525:
        tax=4617.50 + (0.22 * (income - 40125))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
    elif 85526 <= income <= 163300:
        tax=14605.50 + (0.24 * (income - 85525))
        income_after_tax = income-tax
        print(f"Your Taxable Income is {income}")
        print(f"Your Tax Bill is {tax}")
        print(f"Your Income after Tax is {income_after_tax}")
