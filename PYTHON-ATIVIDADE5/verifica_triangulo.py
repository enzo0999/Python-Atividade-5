# Função para verificar se é um triângulo válido
def verifica_triangulo(a, b, c):
    # Verificando as condições de um triângulo válido
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Função principal para rodar o programa
def main():
    try:
        # Entrada de dados
        a = float(input("Digite o comprimento do primeiro lado: "))
        b = float(input("Digite o comprimento do segundo lado: "))
        c = float(input("Digite o comprimento do terceiro lado: "))
        
        # Verificar se forma um triângulo válido
        if verifica_triangulo(a, b, c):
            print("True")  # Se for um triângulo válido
        else:
            print("False")  # Se não for um triângulo válido
    except ValueError:
        print("Por favor, insira apenas números válidos.")

# Chama a função principal
if _name_ == '_main_':
    main()