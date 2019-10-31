A,B,C,X,Y = input('Digite A,B,C,X,Y entre 1 e 52> ').split()
baralho = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
baralho[int(A)] = int(A)
baralho[int(B)] = int(B)
baralho[int(C)] = int(C)
baralho[int(X)] = int(X)
baralho[int(Y)] = int(Y)

mao1 = [int(A),int(B),int(C)]
mao2 = [int(X),int(Y)]
contador1 = 0
carta2 = 0
carta3 = 0

for i in range(1, len(mao1)):
    chave = mao1[i]
    k = i
    while k > 0 and chave > mao1[k - 1]:
        mao1[k] = mao1[k - 1]
        k -= 1
    mao1[k] = chave

for i in range( 1, len( mao2 ) ):
    chave = mao2[i]
    k = i
    while k > 0 and chave > mao2[k - 1]:
        mao2[k] = mao2[k - 1]
        k -= 1
    mao2[k] = chave

for i in range(len(mao2)):
    for j in range(len(mao1)):
        if mao2[i]>mao1[j]:
            contador1 = contador1 + 1
            if(len(mao1)==3):
                del(mao1[j])
            else:
                carta3 = mao1[j]
            break
        else:
            carta2 = mao1[j]

if contador1 == 2:
    carta = int(carta3) + 1
    if baralho[carta]==0:
        valor = carta
    else:
        while baralho[carta]!=0:
            carta += 1
        valor = carta
elif contador1 == 1:
    carta = int(carta2) + 1
    if baralho[carta]==0:
        valor = carta
    else:
        while baralho[carta]!=0:
            carta += 1
        valor = carta
else:
    valor = -1


print(valor)
# if(contador2>=1):
#     while mao1[]
#     valor = mao2[-1] + 1

# else:
#     valor = -1

# print(valor)