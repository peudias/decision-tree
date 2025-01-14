def perguntar_1():
    print("1. Você prefere praticar esportes individuais ou em equipe?")
    resposta = input("Digite 'individuais' ou 'em equipe': ").strip().lower()
    if resposta == "individuais":
        return perguntar_2()
    elif resposta == "em equipe":
        return perguntar_6()
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_1()

def perguntar_2():
    print("2. Você prefere esportes de alta intensidade ou mais tranquilos?")
    resposta = input("Digite 'alta intensidade' ou 'mais tranquilos': ").strip().lower()
    if resposta == "alta intensidade":
        return perguntar_3()
    elif resposta == "mais tranquilos":
        return perguntar_4()
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_2()

def perguntar_3():
    print("3. Você gosta de esportes com contato físico?")
    resposta = input("Digite 'sim' ou 'não': ").strip().lower()
    if resposta == "sim":
        return perguntar_5()
    elif resposta == "não":
        return perguntar_4()
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_3()

def perguntar_4():
    print("4. Você prefere praticar esportes ao ar livre ou em ambientes fechados?")
    resposta = input("Digite 'ao ar livre' ou 'em ambientes fechados': ").strip().lower()
    if resposta == "ao ar livre":
        return "Sugestões: Caminhada, Corrida, Ciclismo"
    elif resposta == "em ambientes fechados":
        return "Sugestões: Tênis, Natação, Yoga"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_4()

def perguntar_5():
    print("5. Você tem interesse em esportes aquáticos?")
    resposta = input("Digite 'sim' ou 'não': ").strip().lower()
    if resposta == "sim":
        return "Sugestões: Natação, Polo aquático, Surfe"
    elif resposta == "não":
        return "Sugestões: Luta (Boxe, Judô, Muay Thai), Ciclismo"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_5()

def perguntar_6():
    print("6. Você prefere esportes com bola ou sem bola?")
    resposta = input("Digite 'com bola' ou 'sem bola': ").strip().lower()
    if resposta == "com bola":
        return perguntar_7()
    elif resposta == "sem bola":
        return perguntar_8()
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_6()

def perguntar_7():
    print("7. Você prefere esportes com mais ação e rapidez ou mais estratégia?")
    resposta = input("Digite 'mais ação e rapidez' ou 'mais estratégia': ").strip().lower()
    if resposta == "mais ação e rapidez":
        return "Sugestões: Futebol, Basquete, Vôlei"
    elif resposta == "mais estratégia":
        return "Sugestões: Tênis, Tênis de mesa, Peteca"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_7()

def perguntar_8():
    print("8. Você prefere esportes que exigem agilidade ou mais força física?")
    resposta = input("Digite 'agilidade' ou 'força física': ").strip().lower()
    if resposta == "agilidade":
        return "Sugestões: Tênis, Peteca, Corrida"
    elif resposta == "força física":
        return "Sugestões: Levantamento de peso, Luta, Ciclismo"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_8()

def perguntar_9():
    print("9. Você se sente confortável com esportes radicais ou prefere algo mais tradicional?")
    resposta = input("Digite 'radicais' ou 'tradicionais': ").strip().lower()
    if resposta == "radicais":
        return "Sugestões: Escalada, Skate, Surfe"
    elif resposta == "tradicionais":
        return "Sugestões: Natação, Futebol, Vôlei"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_9()

def perguntar_10():
    print("10. Você prefere esportes com mais interação social ou mais independentes?")
    resposta = input("Digite 'mais interação social' ou 'mais independentes': ").strip().lower()
    if resposta == "mais interação social":
        return "Sugestões: Futebol, Vôlei, Basquete"
    elif resposta == "mais independentes":
        return "Sugestões: Natação, Corrida, Tênis"
    else:
        print("Resposta inválida. Tente novamente.")
        return perguntar_10()

# Função principal para começar o jogo de perguntas
def iniciar_jogo():
    print("Bem-vindo à árvore de decisão para sugestão de esportes!")
    resultado = perguntar_1()
    print(resultado)

# Inicia o jogo
iniciar_jogo()