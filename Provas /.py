print('Código da região - Nome da região')

print('1 - Sul')

print('2 - Norte')

print('3 - Leste')

print('4 - Oeste')

print('5 - Noroeste')

print('6 - Sudeste')

print('7 - Centro-Oeste')

print('8 - Nordeste')

input('Digite seu nome: ')

regiao = int(input('Digite o código da sua região: '))

input('Digite o nome do vendedor: ')

pecas = int(input('Digite o número de peças vendidas: '))

CustoTotal = pecas7

ValorTotal = CustoTotal1.5

Comissao = ValorTotal0.065

Lucro = ValorTotal - CustoTotal - Comissao

if regiao == 1 and pecas <= 1000:

    frete = 1.00pecas

elif regiao == 1 and pecas > 1000:

    frete = (1.00pecas)0.9

if regiao == 2 and pecas <= 1000:

    frete = 1.10pecas

elif regiao == 2 and pecas > 1000:

    frete = (1.10pecas)0.92

if regiao == 3 and pecas <= 1000:

    frete = 1.15pecas 

elif regiao == 3 and pecas > 1000:

    frete = (1.15pecas)0.93

if regiao == 4 and pecas <= 1000:

    frete = 1.20pecas 

elif regiao == 4 and pecas > 1000:

    frete = (pecas1.20)0.89

if regiao == 5 and pecas <= 1000:

    frete = 1.25pecas

elif regiao == 5 and pecas > 1000:

    frete = (1.25pecas)0.85

if regiao == 6 and pecas <= 1000:

    frete = 1.30pecas

elif regiao == 6 and pecas > 1000:

    frete = (1.30pecas)0.88

if regiao == 7 and pecas <= 1000:

    frete = 1.40pecas

elif regiao == 7 and pecas > 1000:

    frete = (1.40pecas)0.82

if regiao == 8 and pecas <= 1000:

    frete = 1.35pecas

elif regiao == 8 and pecas > 1000:

    frete = (1.35pecas)*0.85

print(f'O valor do frete é R$ {frete}, a comissão do vendedor é R$ {Comissao} e o lucro obtido é R$ {Lucro}.')