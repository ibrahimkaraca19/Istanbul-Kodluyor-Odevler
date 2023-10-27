# Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = input("Lütfen maaşınızı giriniz: ")
zamOrani = input("Lütfen zam oranınızı giriniz: ")

maasAsFloat = float(maas)
zamOraniAsFloat = float(zamOrani)

zamliMaas = maasAsFloat + ((maasAsFloat*zamOraniAsFloat)/100)
print(f"Zamlı maaşınız: {zamliMaas}")
