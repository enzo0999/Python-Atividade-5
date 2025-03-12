# Acesso ao sistema de login para o administrador

# Definindo as credenciais corretas
login_correto = "admin"
senha_correta = "1234"

# Solicitando as credenciais do usuário
login_usuario = input("Digite o login: ")
senha_usuario = input("Digite a senha: ")

# Verificando se as credenciais estão corretas
if login_usuario == login_correto and senha_usuario == senha_correta:
    print("Acesso Permitido")
else:
    print("Acesso Negado")