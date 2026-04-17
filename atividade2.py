nota = float(input("Qual sua NOTA?: "))
if nota >= 9:
    print("PARABÉNS! Tirou nota A!")
elif nota >= 7 and nota < 9:
    print("PARABÉNS! Tirou nota B!")
elif nota >= 5 and nota < 7:
    print("Tirou nota C!")
else:
    print("Tirou nota D!")
