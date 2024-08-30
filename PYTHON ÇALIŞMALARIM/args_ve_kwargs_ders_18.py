def toplama(*args,**kwargs):
  toplam=0
  for eleman in args:
    toplam= toplam+ eleman
  return toplam
toplam= toplama(1,2,3,4,5,6)
print(toplam)
      
