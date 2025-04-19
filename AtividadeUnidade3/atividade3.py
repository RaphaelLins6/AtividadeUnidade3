# Cenário: Você está no comando de uma nave espacial em uma batalha intergaláctica.
# Você tem um número limitado de mísseis e precisa usá-los estrategicamente para
# destruir naves inimigas.
# Tarefa:
# 1. Dena o número inicial de mísseis (um número inteiro positivo).
# 2. Crie uma lista com os nomes de pelo menos 3 naves inimigas.
# 3. Utilize um loop while para simular a batalha. O loop deve continuar enquanto você
# tiver mísseis E houver naves inimigas na lista.
# 4. Dentro do loop:
# ○ Imprima o número de mísseis restantes e a lista de naves inimigas.
# ○ Solicite ao usuário que escolha qual nave inimiga atacar (usando o índice da
# lista).
# ○ Implemente tratamento de erros para garantir que o usuário digite um índice
# válido.
# ○ Se o usuário digitar um índice inválido, exiba uma mensagem de erro e
# continue para a próxima iteração do loop usando continue.
# ○ Se o usuário digitar um índice válido:
# ■ Remova a nave inimiga da lista.
# ■ Diminua o número de mísseis em 1.
# ■ Imprima uma mensagem informando qual nave foi destruída.
# ○ Se o número de mísseis chegar a zero, imprima uma mensagem de "Sem
# mísseis! Retirada estratégica!".
# ○ Se todas as naves inimigas forem destruídas, imprima uma mensagem de
# "Vitória! Todas as naves inimigas foram destruídas!".

misseis = 5 
naves_inimigas = ["Nave A", "Nave B", "Nave C"]
while True:
    print(f"Número de mísseis restantes: {misseis}")
    print("Naves inimigas:", naves_inimigas)

    # Verifica se ainda há naves inimigas e mísseis
    if not naves_inimigas:
        print("Vitória! Todas as naves inimigas foram destruídas!")
        break
    if misseis <= 0:
        print("Sem mísseis! Retirada estratégica!")
        break

    # Usuario ataca maquina
    try:
        escolha = int(input("Escolha uma nave inimiga para atacar (0, 1 ou 2): "))
        if escolha < 0 or escolha >= len(naves_inimigas):
            # Perde um míssil se errar o tiro (indice invalido)
            misseis -= 1
            raise ValueError("Índice inválido. Tente novamente.")
    except ValueError as e:
        print(e)
        continue

    # Remove a nave inimiga
    naves_inimigas.pop(escolha)
    misseis -= 1
    print(f"Nave {escolha} destruida")