import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

şifre_uzunluğu = int(input("Şifre Uzunluğunu Giriniz"))

şifre =""

for i in range(şifre_uzunluğu):
    şifre += random.choice(karakterler)
    print(şifre)


