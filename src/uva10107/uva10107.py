lista = []
while True:
    try:
        num = int(input())
    except EOFError:
        break
    lista.append(num)
    lista.sort()
    if(len(lista)%2==1):
        print(lista[len(lista)//2])
    else:
        print(((lista[(len(lista)//2)-1] + lista[len(lista)//2]))//2)
