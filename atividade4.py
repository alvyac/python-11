compra = float(input("Qual o valor da compra?(em reais): "))
cliente = (input("É cliente vip?(s/n): "))
if compra >= 100 or cliente == "s":
    print("Ganhou frete grátis!")
else:
    print("Não ganhou frete grátis, vai ter que pagar o frete.")
