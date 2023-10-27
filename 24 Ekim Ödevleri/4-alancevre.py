# Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
import math
yaricap = input("Dairenin yarıçapını girin: ")
yaricapAsFloat = float(yaricap)

alan = math.pi * (yaricapAsFloat*yaricapAsFloat)
cevre = 2 * math.pi * yaricapAsFloat
print(f"Dairenin alanı: {alan}, çevresi ise: {cevre}")
