# number nomli uch honali butun sonli o’zgaruvchi yarating.
# number o’zgaruvchining birinchi raqamini toping va x1 ga taminlang.
# number o’zgaruvchining ikkinchi raqamini toping va x2 ga taminlang.
# number o’zgaruvchining uchunchi raqamini toping va x3 ga taminlang.
# Ularning yig’indisini answer nomli o’zgaruchiga taminlang va natijani
# chop eting.

number = 184
x1 = number // 100
x2 = number % 100 // 10
x3 = number % 10
answer = x1 + x2 + x3
print(answer)
