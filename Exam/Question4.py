amount = float(input("Enter any number: "))
amount = round(amount * 100)
notes = [100, 50, 20, 10, 5, 2]
coins = [100, 50, 25, 10, 5, 1]
print("NOTAS:")
for note in notes:
    value = note * 100
    count = amount // value
    print(f"{count} nota(s) de R$ {note}.00")
    amount %= value
print("MOEDAS:")

for coin in coins:
    count = amount // coin
    if coin == 100:
        print(f"{count} moeda(s) de R$ 1.00")
    elif coin == 50:
        print(f"{count} moeda(s) de R$ 0.50")
    elif coin == 25:
        print(f"{count} moeda(s) de R$ 0.25")
    elif coin == 10:
        print(f"{count} moeda(s) de R$ 0.10")
    elif coin == 5:
        print(f"{count} moeda(s) de R$ 0.05")
    else:
        print(f"{count} moeda(s) de R$ 0.01")

    amount %= coin