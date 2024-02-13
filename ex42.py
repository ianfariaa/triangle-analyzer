m1 = float(input('Primeiro segmento:'))
m2 = float(input('Segundo segmento:'))
m3 = float(input('Terceiro segmento:'))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Os seguimentos pode formar um triangulo', end='')
    if m1 == m2 == m3:
        print('EQUILATERO!')
    elif m1 != m2 != m3 != m1:
        print(' ESCALENO!')
    else:
        print(' ISÓSCELES!')
else:
    print('Os seguimentos não pode formar um triangulo')

# Isso é uma forma diferente de usar as condições alinhadas.É possível colocar um if dentro de outro if.
# Como se fossem dois caminhos, um é sem saída (else), e o outro tem como prosseguir de várias maneiras(if).
