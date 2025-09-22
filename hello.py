print("Hello, World!")
print("Vad heter du?")
name = input()
print("Hej" + " " + name + "!")
print("Hur gammal är du?")
age = input()
print ("Du är" + " " + age + " " + "år gammal!")
print("Ange två tal:")
num1 = input("Tal 1: ")
num2 = input("Tal 2:")
sum = int(num1) + int(num2) #Måste göra om num1 & num2 till en int från en string då det läses som en string och lägger ihop talen endast utan att addera dom.
print("Summan av talen är:" + " " + str(sum)) #Måste här göra om int till en string för att kunna skriva ut.