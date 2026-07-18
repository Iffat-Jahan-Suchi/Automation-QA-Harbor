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
    print(f"{count} nota(s) de R$ {coin}.00")
    amount%=val