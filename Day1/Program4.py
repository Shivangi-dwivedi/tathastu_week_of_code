cp=int(input("enter cost price: "))
sp=int(input("enter selling price: "))
p= float(sp) - float(cp)
print("profit = ", p)
# selling price if profit is increased by 5%
sp2=float((1.05*p) + cp)
print("the new selling price=", sp2)
