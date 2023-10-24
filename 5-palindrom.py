# Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Lütfen bir doğal sayı giriniz: ")
revsayi = sayi[::-1]

if sayi == revsayi:
    print("Girdiğiniz sayı bir palindrom sayıdır.")
else:
    print("Girdiğiniz sayı bir palindrom sayı değildir.")
