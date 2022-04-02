# number nomli ikki honali butun sonli o’zgaruvchi yarating.
# answer nomli o’zgaruvchiga number ning teskarisini taminlang.
# Natijani chop eting.

number = 52

x1 = number % 10
number //= 10

x2 = number % 10
number //= 10

answer = x1 * 10 + x2
print(answer)
