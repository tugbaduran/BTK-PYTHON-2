"""
AND:
True and True= True
True and False= False
False and True= False
False and False= False

OR:
True or True= True
True or False= True
False or True= True
False or False= False

NOT: 
Boolean değerin başına girildiğinde otomatik olarak o değerin tersi alınacaktır.

"""

kullanici_adi= input("Kullanici Adı:")
sifre= input("Şifre Giriniz:")
print(kullanici_adi == "Tuğba" and sifre == "123456")

"""
kullanici_adi= input("Kullanici Adı:")
sifre= input("Şifre Giriniz:")
print(kullanici_adi == "Tuğba" or sifre == "123456")
"""
"""
kullanici_adi= input("Kullanici Adı:")
sifre= input("Şifre Giriniz:")
print(not (kullanici_adi == "Tuğba") )
"""