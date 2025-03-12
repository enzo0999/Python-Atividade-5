# Função para verificar se os lados formam um triângulo válido
def verifica_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Solicita os lados do triângulo
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados formam um triângulo válido
if not verifica_triangulo(a, b, c):
    print("Os valores informados não formam um triângulo válido.")
else:
    # Determina o tipo de triângulo
    if a == b == c:
        print("Triângulo Equilátero: Todos os três lados são iguais.")
    elif a == b or b == c or a == c:
        print("Triângulo Isósceles: Dois lados são iguais e um é diferente.")
    else:
        print("Triângulo Escaleno: Todos os lados possuem medidas diferentes.")