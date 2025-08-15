cpf = "49303621808"
cpf_list = []
soma = 0
total = 0
list_total = []
total1 = 0
total2 = 0

# SEPARAR O CPF NA LISTA
for indice in cpf:
    cpf_list.append(int(indice))

# MULTIPLICAÇÃO EM CADA VALOR DA LISTA PARA O PRIMEIRO DÍGITO
i = 10
for indice in range(9):  # Agora consideramos apenas os primeiros 9 dígitos
    soma = cpf_list[indice] * i
    list_total.append(soma)
    i -= 1

# SOMA DOS RESULTADOS
total = sum(list_total)

# CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR
total1 = (total * 10) % 11
if total1 > 9:
    total1 = 0

# MULTIPLICAÇÃO PARA O SEGUNDO DÍGITO
i = 11
list_total.clear()
for indice in range(10):  # Agora consideramos os primeiros 10 dígitos
    soma = cpf_list[indice] * i
    list_total.append(soma)
    i -= 1

# SOMA DOS RESULTADOS PARA O SEGUNDO DÍGITO
total = sum(list_total)

# CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR
total2 = (total * 10) % 11
if total2 > 9:
    total2 = 0

# VERIFICAÇÃO FINAL
if cpf_list[9] == total1 and cpf_list[10] == total2:
    print("CPF VÁLIDO")
else:
    print("CPF INVÁLIDO")
