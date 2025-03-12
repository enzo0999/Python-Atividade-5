# Função para verificar se o número é par e positivo
def par_positivo(numero):
    if numero > 0 and numero % 2 == 0:
        return True
    else:
        return False

# Função principal para rodar o programa
def main():
    try:
        # Solicita um número ao usuário
        numero = float(input("Digite um número: "))
        
        # Verificar se o número é par e positivo
        if par_positivo(numero):
            print("True")  # Se for par e positivo
        else:
            print("False")  # Caso contrário
    except ValueError:
        print("Por favor, insira um número válido.")

# Chama a função principal
if _name_ == '_main_':
    main()