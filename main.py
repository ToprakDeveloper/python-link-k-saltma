import pyshorteners

ulink = str(input("Uzun Linki Giriniz: "))

s = pyshorteners.Shortener()

klink = s.tinyurl.short(ulink)

print("Kısa Linkiniz: ", klink)
