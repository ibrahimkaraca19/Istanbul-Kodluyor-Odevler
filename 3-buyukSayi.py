# Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = input("Sayı giriniz: ")
sayi2 = input("Sayı giriniz: ")
sayi3 = input("Sayı giriniz: ")

sayi1AsFloat = float(sayi1)
sayi2AsFloat = float(sayi2)
sayi3AsFloat = float(sayi3)

if sayi1AsFloat > sayi2AsFloat and sayi1AsFloat > sayi3AsFloat:
    print(f"En büyük sayı: {sayi1AsFloat}")
elif sayi2AsFloat > sayi1AsFloat and sayi2AsFloat > sayi3AsFloat:
    print(f"En büyük sayı: {sayi2AsFloat}")
else:
    print(f"En büyük sayı: {sayi3AsFloat}")
