from random import randint

a = randint(0,100)

if a>0 and a<=50:
    print("Слаб 2.")
elif a>50 and a<=60:
    print("Среден 3.")
elif a>60 and a<=70:
    print("Добър 4.")
elif a>70 and a<=80:
    print("Много добър 5.")
elif a>80 and a<100:
    print("Отличен 6.")
else:
    print("Много Отличен 7.")

