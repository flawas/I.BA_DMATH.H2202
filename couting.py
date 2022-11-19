count = 0
for number in range(1000000):
    prod_digits = 1
    saved_number = number
    while number:
        number, digit = divmod(number, 10) 
        prod_digits *= digit
    if prod_digits == 49: 
        count += 1
        print(saved_number)
print("Anzahl: ",count)