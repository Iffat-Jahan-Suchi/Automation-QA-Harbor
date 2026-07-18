amount = float(input("Enter any number: "))
amount = round(amount * 100)
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01 ]
print("NOTAS:")
for note in notes:
    value = note * 100
    count = amount // value
    print(f"{count} nota(s) de R$ {note}.00")
    amount %= value
print("MOEDAS:")

for coin in coins:
    val=coin*100
    count = amount // val
    if val == 100:
        print(f"{count} moeda(s) de R$ 1.00")
    elif val == 50:
        print(f"{count} moeda(s) de R$ 0.50")
    elif val == 25:
        print(f"{count} moeda(s) de R$ 0.25")
    elif val == 10:
        print(f"{count} moeda(s) de R$ 0.10")
    elif val == 5:
        print(f"{count} moeda(s) de R$ 0.05")
    else:
        print(f"{count} moeda(s) de R$ 0.01")

    amount%=val