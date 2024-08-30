sayi_listesi=[10,9,8,7,6,5,4,3,2,1]
yeni_liste= list(filter(lambda x: (x % 2== 0), sayi_listesi))
print(yeni_liste)