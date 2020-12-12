import decimal
from decimal import Decimal

x = Decimal('0.01') + Decimal('0.02')
decimal.getcontext().prec = 4
print(x)
