#!/bin/bash
#Autor: Renato Vasconcelos
#Data: 09/11/2024
#Algoritmo que calcula: soma, subtração, multiplicação,divisão
#Converta os valores recebidos pelo usuário para um ponto flutuante (float)
#Converta os valores recebidos pelo usuário para (int)
#faz um loop com os números digitados


clear
# visual do script

echo "  _____________________________________"
echo
echo "              CALCULADORA "
echo "               Versão 1"
echo "  Desenvolvido por Renato Vasconcelos"
echo "  _____________________________________"

# Dados do usuario

echo "Digite seu Nome de usuário"
read nom
echo "digite sua senha"
read sen
if [ "$sen" = "1234" ]
then
clear
echo "Seja bem vindo $nom !!!"
echo
#execução do arquivo prova.py
python3 /home/renato/modulo1/python/calculadora.py
fi
