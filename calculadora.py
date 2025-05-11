import os
import time
from colorama import Fore, Back, Style, init

# Inicializa o colorama para usar cores no terminal
init(autoreset=True)

def calcular_imc(peso, altura):
    """
    Função para calcular o IMC.
    """
    return peso / (altura ** 2)

def classificacao_imc(imc):
    """
    Função para classificar o IMC de acordo com as categorias padrão da OMS.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def limpar_tela():
    """
    Função para limpar a tela do console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_resultados(nome, idade, imc, classificacao):
    """
    Função para exibir os resultados do cálculo de IMC com mais estilo.
    """
    limpar_tela()
    print(Fore.CYAN + "="*40)
    print(Fore.YELLOW + f"  CALCULADORA DE IMC - {nome.upper()}")
    print(Fore.CYAN + "="*40)
    print(Fore.MAGENTA + f"\nOlá {nome}, de {idade} anos!")
    print(Fore.CYAN + "="*40)
    print(Fore.GREEN + f"\nSeu IMC é: {imc:.2f}")
    print(Fore.RED + f"Classificação: {classificacao}")
    print(Fore.CYAN + "="*40)

def animacao_loading():
    """
    Função de animação para dar um efeito de "carregamento".
    """
    loading_text = "Calculando"
    for i in range(3):
        print(loading_text + "." * (i + 1), end='\r')
        time.sleep(0.5)
    print("Calculando... concluído!\n")

def saudacao_inicial():
    """
    Função de saudação inicial com efeito.
    """
    limpar_tela()
    print(Fore.CYAN + "="*40)
    print(Fore.YELLOW + "  BEM-VINDO À CALCULADORA DE IMC  ")
    print(Fore.CYAN + "="*40)
    time.sleep(1)

def main():
    """
    Função principal que executa a calculadora de IMC com nome e idade.
    """
    while True:
        saudacao_inicial()

        nome = input(Fore.MAGENTA + "Digite seu nome: ").strip()
        idade = input(Fore.MAGENTA + "Digite sua idade: ").strip()

        try:
            peso = float(input(Fore.GREEN + "Digite seu peso em kg: "))
            altura = float(input(Fore.GREEN + "Digite sua altura em metros: "))
            
            if peso <= 0 or altura <= 0:
                print(Fore.RED + "\nPeso e altura devem ser valores positivos!")
                time.sleep(2)
                continue
            
            animacao_loading()  # Animação de carregamento

            imc = calcular_imc(peso, altura)
            classificacao = classificacao_imc(imc)
            exibir_resultados(nome, idade, imc, classificacao)

            continuar = input(Fore.YELLOW + "\nDeseja calcular novamente? (s/n): ").lower()
            if continuar != 's':
                print(Fore.GREEN + "\nObrigado por usar a calculadora de IMC!")
                time.sleep(2)
                break
        except ValueError:
            print(Fore.RED + "\nPor favor, insira valores válidos para peso e altura.")
            time.sleep(2)

# Executa o programa
if __name__ == "__main__":
    main()
