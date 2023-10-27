# Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
kisiKilo = input("Lütfen kilonuzu giriniz: ")
kisiBoy = input("Lütfen boyunuzu giriniz(metre cinsinde): ")

kisiKiloAsFloat = float(kisiKilo)
kisiBoyAsFloat = float(kisiBoy)

vkindeks = kisiKiloAsFloat/(kisiBoyAsFloat*kisiBoyAsFloat)

print(f"Vücut kitle indeksiniz: {vkindeks}")
