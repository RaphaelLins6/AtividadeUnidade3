import random

# Definir a distância inicial segura
distancia_segura = 5  # Você pode ajustar esse valor se quiser
incremento_seguro = 2  # Valor que aumenta a distância segura a cada iteração

print("Iniciando navegação pelo campo de asteroides...\n")

# Loop para simular a navegação
while True:
    # Gera distância aleatória entre 1 e 10
    distancia_asteroide = random.randint(1, 10)
    print(f"Distância do asteroide mais próximo: {distancia_asteroide}")

    #Se a distância for menor que 3, perigo!
    if distancia_asteroide < 3:
        print("PERIGO! Asteroide muito próximo!")
        break

    # Se a distância for menor que a metade da distância segura, emitir aviso
    if distancia_asteroide < distancia_segura / 2:
        print("Aproximando-se de asteroide!")

    # Aumenta a distância segura
    distancia_segura += incremento_seguro
    print(f"Distância segura agora é: {distancia_segura}\n")

    # Verifica se ainda deve continuar
    if distancia_asteroide >= distancia_segura:
        break

# 4. Mensagem final, se não houve break
else:
    print("Navegação concluída com segurança!")

# Como usamos break para sair em caso de perigo, a mensagem abaixo será exibida
# apenas se a nave sair do loop por segurança
if distancia_asteroide >= distancia_segura:
    print("Navegação concluída com segurança!")
