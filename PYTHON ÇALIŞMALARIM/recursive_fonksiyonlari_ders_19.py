def faktoriyel(x):
  if x== 1:
    return 1
  else:
   return (x*faktoriyel(x-1))
sonuc= faktoriyel(6)
print(sonuc)
