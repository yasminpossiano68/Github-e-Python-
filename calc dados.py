def validar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError("Os vetores devem ter o mesmo tamanho!")
    return True


# Distância Euclidiana
def euclidiana(v1, v2):
    validar_vetores(v1, v2)
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(v1, v2))
    return soma_quadrados ** 0.5


# Produto Escalar
def produto_escalar(v1, v2):
    validar_vetores(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))

# MAE - Erro Médio Absoluto
def mae(v1, v2):
    validar_vetores(v1, v2)
    return sum(abs(a - b) for a, b in zip(v1, v2)) / len(v1)


# MSE - Erro Quadrático Médio
def mse(v1, v2):
    validar_vetores(v1, v2)
    return sum((a - b) ** 2 for a, b in zip(v1, v2)) / len(v1)
    
if __name__ == "_main_":
    obs = [1.2, 2.5, 3.8]
    pred = [1.0, 2.7, 4.0]

    print("Sistema iniciado com sucesso.")
