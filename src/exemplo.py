def arvore_decisao():
    equipe = input("Você gosta de trabalhar em equipe? (sim/não): ").strip().lower()
    if equipe == "sim":
        ar_livre = input("Prefere atividades ao ar livre? (sim/não): ").strip().lower()
        if ar_livre == "sim":
            print("Sugestão: Explore atividades como esportes coletivos ou jardinagem.")
        else:
            tecnologia = input("Sente-se confortável trabalhando com tecnologia? (sim/não): ").strip().lower()
            if tecnologia == "sim":
                print("Sugestão: Considere áreas de tecnologia ou programação.")
            else:
                print("Sugestão: Experimente hobbies criativos como pintura ou música.")
    else:
        numeros = input("Gosta de lidar com números? (sim/não): ").strip().lower()
        if numeros == "sim":
            print("Sugestão: Áreas como finanças ou engenharia podem ser interessantes.")
        else:
            print("Sugestão: Considere hobbies individuais como leitura ou fotografia.")

arvore_decisao()
