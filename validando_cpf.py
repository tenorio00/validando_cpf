#calculo do primeiro digito do CPF

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado = 0
for digito in nove_digitos:
    resultado += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)