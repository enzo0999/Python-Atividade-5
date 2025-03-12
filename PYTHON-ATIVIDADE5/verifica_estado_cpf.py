import re

# Função para remover caracteres não numéricos
def limpar_cpf(cpf):
    return re.sub(r'\D', '', cpf)

# Função para verificar o estado baseado no primeiro dígito do CPF
def estado_do_cpf(cpf):
    if len(cpf) != 11:
        return 'CPF INVÁLIDO'

    # Dicionário com os estados e seus respectivos dígitos
    estados = {
        '1': 'Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul',
        '2': 'Minas Gerais',
        '3': 'Espírito Santo, Rio de Janeiro',
        '4': 'São Paulo',
        '5': 'Paraná',
        '6': 'Santa Catarina',
        '7': 'Rio Grande do Sul',
        '8': 'São Paulo',
        '9': 'São Paulo'
    }

    # O primeiro dígito do CPF, que é o indicativo do estado
    primeiro_digito = cpf[0]

    # Verificar se o primeiro dígito existe no dicionário
    if primeiro_digito in estados:
        return f'O CPF pertence ao(s) estado(s): {estados[primeiro_digito]}'
    else:
        return 'Estado desconhecido'

# Função principal para rodar o programa
def main():
    cpf = input('Digite o CPF (com ou sem pontuação): ')
    
    # Limpar o CPF
    cpf_limpado = limpar_cpf(cpf)

    # Verificar se o CPF tem exatamente 11 dígitos
    if len(cpf_limpado) != 11:
        print('CPF INVÁLIDO')
    else:
        # Verificar o estado com base no CPF
        resultado = estado_do_cpf(cpf_limpado)
        print(resultado)

if _name_ == '_main_':
    main()