# Define a operação

operação = input('''
Por favor escolha uma operação:
1 Para Adição
2 Para subtração
3 Para Multiplicação
4 Para Divisão
''')

numero_1 = int(input('Entre com o primeiro número: '))
numero_2 =int(input('Entre com o primeiro número: ')) 

#Adição
if operação == '1':
  print('{} + {} = '.format(numero_1, numero_2))
  print("Resultado da operação é: ",numero_1 + numero_2)

# Subtração
elif operação == '2':
  print('{} - {} = '.format(numero_1, numero_2))
  print("Resultado da operação é: ",numero_1 - numero_2)

# Multiplicação
elif operação == '3':
  print('{} x {} = '.format(numero_1, numero_2))
  print("Resultado da operação é: ",numero_1 * numero_2)

# Divisão
elif operação == '4':
  print('{} / {} = '.format(numero_1, numero_2))
  print("Resultado da operação é: ",numero_1 / numero_2)

else:
   print('Você inseriu um numrero incorreto.Por favor execute o programa novamente.')
