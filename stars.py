print('não coloque letras, evite numeros grandes.')
print(' ')
print('exemplo (10 mil): 10000, não coloque assim, para facilitar sua leitura. coloque no máximo até centena (1-999).')
print(' ')
e=int(input('quantas estrelas você abre por vez? '))
print(' ')
s1=input('você roleta em numero quebrados?\npor exemplo: roleto em 4.5s ou 4.25s (4.5 é um numero quebrado)\n[S/S1/N]\n(S) para 4.5 e etc\n(S1) para 4.25 e etc\n(N) para 5 e etc ').upper()
print(' ')
if s1=='S':
    tm=int(input('quantos segundos você demora para roletar cada estrela? coloque em decimal\nexemplo: roleto a cada 4.5s, então coloque 45\n(sera divido por 10) '))
    t=tm/10
elif s1=='S1':
    tm=int(input('quantos segundos você demora para roletar cada estrela? coloque em centena\nexemplo: roleto a cada 4.25s, então coloque 425\n(sera divido por 100) '))
    t=tm/100
elif s1=='N':
    t=int(input('quantos segundos você demora para roletar cada estrela?'))
print(' ')
h=int(input('quantas horas você vai deixar roletando? '))
print(' ')
d=int(input('quanto custa cada estrela/para roletar? '))
print(' ')
h1=h*3600
ht=h1/t
hte=ht*e
hted=hte*d
print('vamos com calma agora.')
print(' ')
print('você roleta {} por vez'.format(e))
print(' ')
print('demora {} segundos para abrir cada estrela'.format(t))
print(' ')
print('você vai roletar por {} horas'.format(h))
print(' ')
print('e custa {} para roletar'.format(d))
print(' ')
print('em {} horas, você vai roletar {} vezes'.format(h , ht))
print(' ')
print('abrindo {} estrelas por vez, você vai roletar {} estrelas em {} horas'.format(e , hte , h))
print(' ')
print('tudo isso vai custar {}'.format(hted))
print(' ')
n=input('leia tudo e digite "727"')
if n==727:
    print('blue zenith')
else:
    print('paia')
