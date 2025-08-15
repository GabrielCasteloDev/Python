#split cut string in words ////// variavel_list = variavel.split('')
#strip cut de space in start and end of string
#rstrip - right / ltrip - left ////// print(variavel[i].strip())
#join - string together ////// variavel = '#passa algum valor para separar#'.join(variavel)




test = "This is a test, this is a test, thist is a test"
#separando a string em lista, separando em (, )
test_list = test.split(', ')

test_join = []

#criando a repetição para passar de item em item na lista
for i, test in enumerate(test_list):
    #append para adicionar na nova lista e strip para cortar os espaços
    test_join.append(test_list[i].strip())

#juntando a lista em outra variável
list_together = ' '.join(test_join)

print(list_together)
print(test_list)

