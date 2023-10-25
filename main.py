n = int(input("Unesite broj:"))



def fib(n):
    f0 = 0
    f1 = 1
    for i in range(n):
        yield f0 , f1
        ff = f0
        f0 = f1
        f1 = ff + f1




def parovi(n):
    for i, (fi, fii) in enumerate(fib(n)):
        i = i + 1
        try:
            kolicnik=float(fii)/ float(fi)
            print("Za par:" ,"(",i - 1, i,")","Rezultat je", kolicnik)
        except ZeroDivisionError:
            print("Za par:" ,"(",i - 1, i,")","Rezultat je", "∞")

"Prvi način  ispisa Fibonacijevog niza"
print("Fibonacijev niz je:")
print(list(fib(n)))
"Drugi način  ispisa Fibonacijevog niza"
for x in fib(n):
    print(x)


print(parovi(n))
