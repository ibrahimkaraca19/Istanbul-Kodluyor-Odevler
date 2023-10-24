maas = input("Lütfen maaşınızı giriniz: ")
zamOrani = input("Lütfen zam oranınızı giriniz: ")

maasAsFloat = float(maas)
zamOraniAsFloat = float(zamOrani)

zamliMaas = maas + ((maas*zamOrani)/100)
print(f"Zamlı maaşınız: {zamliMaas}")
