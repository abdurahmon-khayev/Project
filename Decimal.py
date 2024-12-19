from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 5

a = Decimal('0.1')
b = Decimal('0.2')
result1 = a + b

c = Decimal('1')
d = Decimal('3')
result2 = c / d

e = Decimal('2.675')
result3 = e.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

price = Decimal('19.99')
quantity = Decimal('3')
result4 = price * quantity

float_sum = 0.1 + 0.2
decimal_sum = Decimal('0.1') + Decimal('0.2')

print(result1, result2, result3, result4, float_sum, decimal_sum)
