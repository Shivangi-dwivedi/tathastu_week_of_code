
a = int(input("enter runs of player 1: "))
b = int(input("enter runs of player 2: "))
c = int(input("enter runs of player 3: "))

sa = (a/60)*100
sb = (b/60)*100
sc = (c/60)*100

print("Strike rate of player 1: ",sa)
print("Strike rate of player 2: ",sb)
print("Strike rate of player 3: ",sc)

print("Score after next 60 balls: ")
print("Player 1: ", (a +(sa/100)*60))
print("Player 2: ", (b +(sb/100)*60))
print("Player 3: ", (c +(sc/100)*60))

print("Maximum sixes each player could have hit: ")
print("Player 1: ",(a +(sa/100)*60)/6)
print("Player 2: ",(b +(sb/100)*60)/6)
print("Player 3: ",(c +(sc/100)*60)/6)
