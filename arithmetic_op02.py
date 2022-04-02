# number nomli o’zgaruvchi yarating va 43 ni taminlang.
# answer nomli o’zgaruvchi yarating va number ning raqamlari yig’indisini
# taminlang.
# Natijani chop eting.

number = 43

x1 = number % 10
number //= 10

x2 = number % 10
number //= 10

answer = x1 + x2
print(answer)
