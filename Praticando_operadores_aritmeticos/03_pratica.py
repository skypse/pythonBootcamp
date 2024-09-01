import os
import time


def limpar_console():
    os.environ['TERM'] = 'xterm'

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("Bem-Vindo a um criador de personagem! (RPG)")

while True:
    print("\nVocê deseja criar seu personagem?")
    print("'Y' = Sim")
    print("'N' = Não")
    limpar_console()

    escolha = input("Digite aqui: ")

    if escolha == "Y" or escolha == "y":
        print("---------------------------------------------")
        print("A Criação de boneco tem às seguintes etapas:")
        print("1- Nome & Sexo")
        print("2- Origem & Raça")
        print("3- Arma")
        print("---------------------------------------------")

        print("\nEntão vamos para etapa: 1- Nome!")
        personagem_nome = input("Qual o nome do seu personagem?: ")
        if personagem_nome == "":
            print("Digite um nome válido!")
            break

        personagem_sexo = input("Qual o seu sexo? (M), (F) ou (OUTROS): ")
        if personagem_sexo not in ["M", "m", "F", "f", "OUTROS", "outros"]:
            print("Digite um sexo válido!")
            break

        # Inicializa as variáveis para armazenar o nome da origem, raça e arma
        nome_origem = ""
        nome_raca = ""
        nome_arma = ""

        print("-------------------------------------------------------------------------------------------------------------------------")
        print(f"Olá '{personagem_nome}'! Que tal escolher sua origem? Abaixo contém nossas principais cidades do game:")
        print("1- Euldaria")
        print("2- Criúnas")
        print("3- Klavyus")
        print("4- Óberion")
        print("-------------------------------------------------------------------------------------------------------------------------")

        personagem_cidade = input(f"\nOlá '{personagem_nome}', qual cidade você deseja ter como origem?:  ")
        INTELIGENCIA_PADRAO = 10
        FORCA_PADRAO = 10
        AGILIDADE_PADRAO = 10
        DEFESA_PADRAO = 10

        if personagem_cidade == "1":
            nome_origem = "Euldaria"
            print("\nBem-vindo à 'Euldaria!'")
            print("Irei mostrar uma lista de raças disponíveis nesta cidade:")
            print("1- Humano")
            print("2- Anão")
            print("3- Elfo")
            print("4- Druída")

            personagem_raca = input("\nDigite aqui sua escolha: ")
            if personagem_raca == "1":
                nome_raca = "Humano"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Humano'!")
                HUMAN_RACA_BUFF_INTELIGENCIA = 2
                HUMAN_RACA_BUFF_AGILIDADE = 4
                HUMAN_RACA_BUFF_FORCA = 4
                INTELIGENCIA_PADRAO += HUMAN_RACA_BUFF_INTELIGENCIA
                AGILIDADE_PADRAO += HUMAN_RACA_BUFF_AGILIDADE
                FORCA_PADRAO += HUMAN_RACA_BUFF_FORCA

            elif personagem_raca == "2":
                nome_raca = "Anão"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Anão'!")
                ANAO_RACA_BUFF_AGILIDADE = 2
                ANAO_RACA_BUFF_INTELIGENCIA = 6
                AGILIDADE_PADRAO += ANAO_RACA_BUFF_AGILIDADE
                INTELIGENCIA_PADRAO += ANAO_RACA_BUFF_INTELIGENCIA

            elif personagem_raca == "3":
                nome_raca = "Elfo"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Elfo'!")
                ELF_RACA_BUFF_INTELIGENCIA = 8
                ELF_RACA_BUFF_AGILIDADE = -4
                ELF_RACA_BUFF_ALCANCE = 4
                INTELIGENCIA_PADRAO += ELF_RACA_BUFF_INTELIGENCIA
                AGILIDADE_PADRAO += ELF_RACA_BUFF_AGILIDADE

            elif personagem_raca == "4":
                nome_raca = "Druída"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Druída'!")
                DRUID_RACA_BUFF_INTELIGENCIA = 10
                INTELIGENCIA_PADRAO += DRUID_RACA_BUFF_INTELIGENCIA

        elif personagem_cidade == "2":
            nome_origem = "Criúnas"
            print("\nBem-vindo à 'Criúnas!'")
            print("Irei mostrar uma lista de raças disponíveis nesta cidade:")
            print("1- Goblin")
            print("2- Murlock")
            print("3- Druída")

            personagem_raca = input("\nDigite aqui sua escolha: ")
            if personagem_raca == "1":
                nome_raca = "Goblin"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Goblin'!")
                GOBLIN_RACA_BUFF_FORCA = 4
                FORCA_PADRAO += GOBLIN_RACA_BUFF_FORCA

            elif personagem_raca == "2":
                nome_raca = "Murlock"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Murlock'!")
                MURLOCK_RACA_BUFF_FORCA = 4
                FORCA_PADRAO += MURLOCK_RACA_BUFF_FORCA

            elif personagem_raca == "3":
                nome_raca = "Druída"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Druída'!")
                DRUID_RACA_BUFF_INTELIGENCIA = 10
                INTELIGENCIA_PADRAO += DRUID_RACA_BUFF_INTELIGENCIA

        elif personagem_cidade == "3":
            nome_origem = "Klavyus"
            print("\nBem-vindo à 'Klavyus!'")
            print("Irei mostrar uma lista de raças disponíveis nesta cidade:")
            print("1- Gigante da Nevoa")
            print("2- Troll")

            personagem_raca = input("\nDigite aqui sua escolha: ")
            if personagem_raca == "1":
                nome_raca = "Gigante da Nevoa"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Gigante da Nevoa'!")
                GIGANTE_NEVOA_RACA_BUFF_INTELIGENCIA = -6
                GIGANTE_NEVOA_RACA_BUFF_AGILIDADE = -4
                GIGANTE_NEVOA_RACA_BUFF_DEFESA = 8
                GIGANTE_NEVOA_RACA_BUFF_FORCA = 4
                INTELIGENCIA_PADRAO += GIGANTE_NEVOA_RACA_BUFF_INTELIGENCIA
                AGILIDADE_PADRAO += GIGANTE_NEVOA_RACA_BUFF_AGILIDADE
                DEFESA_PADRAO += GIGANTE_NEVOA_RACA_BUFF_DEFESA
                FORCA_PADRAO += GIGANTE_NEVOA_RACA_BUFF_FORCA

            elif personagem_raca == "2":
                nome_raca = "Troll"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Troll'!")
                TROLL_RACA_BUFF_INTELIGENCIA = -8
                TROLL_RACA_BUFF_DEFESA = 4
                TROLL_RACA_BUFF_FORCA = 8
                INTELIGENCIA_PADRAO += TROLL_RACA_BUFF_INTELIGENCIA
                DEFESA_PADRAO += TROLL_RACA_BUFF_DEFESA
                FORCA_PADRAO += TROLL_RACA_BUFF_FORCA

        elif personagem_cidade == "4":
            nome_origem = "Óberion"
            print("\nBem-vindo à 'Óberion!'")
            print("Irei mostrar uma lista de raças disponíveis nesta cidade:")
            print("1- Berserker")
            print("2- Kronviking")

            personagem_raca = input("\nDigite aqui sua escolha: ")
            if personagem_raca == "1":
                nome_raca = "Berserker"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Berserker'!")
                BERSERK_RACA_BUFF_FORCA = 10
                BERSERK_RACA_BUFF_DEFESA = 4
                BERSERK_RACA_BUFF_AGILIDADE = 2
                FORCA_PADRAO += BERSERK_RACA_BUFF_FORCA
                DEFESA_PADRAO += BERSERK_RACA_BUFF_DEFESA
                AGILIDADE_PADRAO += BERSERK_RACA_BUFF_AGILIDADE

            elif personagem_raca == "2":
                nome_raca = "Kronviking"
                print(f"\n'{personagem_nome}', a partir de agora você é um 'Kronviking'!")
                BERSERK_RACA_BUFF_FORCA = 8
                BERSERK_RACA_BUFF_INTELIGENCIA = 4
                BERSERK_RACA_BUFF_AGILIDADE = 2
                FORCA_PADRAO += BERSERK_RACA_BUFF_FORCA
                INTELIGENCIA_PADRAO += BERSERK_RACA_BUFF_INTELIGENCIA
                AGILIDADE_PADRAO += BERSERK_RACA_BUFF_AGILIDADE

        else:
            print("Digite uma origem válida!")
            break

        print("-------------------------------------------------------------------------------------------------------------------------")
        print(f"Olá '{personagem_nome}'! Que tal escolher sua arma?")
        print("1- Adaga")
        print("2- Pistola")
        print("3- Lança")
        print("4- Espada")
        print("5- Machado")
        print("6- Greatsword")
        print("-------------------------------------------------------------------------------------------------------------------------")

        personagem_arma = input(f"\nOlá '{personagem_nome}', qual arma você deseja equipar?: ")
        if personagem_arma == "1":
            nome_arma = "Adaga"
            print(f"Uma adaga foi escolhida, '{personagem_nome}'!")
            ARMA_ADAGA_BUFF_AGILIDADE = 6
            AGILIDADE_PADRAO += ARMA_ADAGA_BUFF_AGILIDADE

        elif personagem_arma == "2":
            nome_arma = "Pistola"
            print(f"Uma pistola foi escolhida, '{personagem_nome}'!")
            ARMA_PISTOLA_BUFF_AGILIDADE = 6
            ARMA_PISTOLA_BUFF_INTELIGENCIA = 4
            AGILIDADE_PADRAO += ARMA_PISTOLA_BUFF_AGILIDADE
            INTELIGENCIA_PADRAO += ARMA_PISTOLA_BUFF_INTELIGENCIA

        elif personagem_arma == "3":
            nome_arma = "Lança"
            print(f"Uma lança foi escolhida, '{personagem_nome}'!")
            ARMA_LANCA_BUFF_DEFESA = 8
            DEFESA_PADRAO += ARMA_LANCA_BUFF_DEFESA

        elif personagem_arma == "4":
            nome_arma = "Espada"
            print(f"Uma espada foi escolhida, '{personagem_nome}'!")
            ARMA_ESPADA_BUFF_FORCA = 8
            ARMA_ESPADA_BUFF_AGILIDADE = 2
            FORCA_PADRAO += ARMA_ESPADA_BUFF_FORCA
            AGILIDADE_PADRAO += ARMA_ESPADA_BUFF_AGILIDADE

        elif personagem_arma == "5":
            nome_arma = "Machado"
            print(f"Um machado foi escolhido, '{personagem_nome}'!")
            ARMA_MACHADO_BUFF_FORCA = 10
            FORCA_PADRAO += ARMA_MACHADO_BUFF_FORCA

        elif personagem_arma == "6":
            nome_arma = "Greatsword"
            print(f"Uma greatsword foi escolhida, '{personagem_nome}'!")
            ARMA_GREATSWORD_BUFF_FORCA = 8
            ARMA_GREATSWORD_BUFF_DEFESA = 6
            FORCA_PADRAO += ARMA_GREATSWORD_BUFF_FORCA
            DEFESA_PADRAO += ARMA_GREATSWORD_BUFF_DEFESA

        else:
            print("Digite uma escolha válida!")
            break

        print("---------------------------------------------------")
        print(f"\nStatus Final do personagem '{personagem_nome}':")
        print(f"Origem: {nome_origem}")
        print(f"Raça: {nome_raca}")
        print(f"Arma: {nome_arma}")
        print(f"Inteligência: {INTELIGENCIA_PADRAO}")
        print(f"Força: {FORCA_PADRAO}")
        print(f"Agilidade: {AGILIDADE_PADRAO}")
        print(f"Defesa: {DEFESA_PADRAO}")

        break

    elif escolha == "N" or escolha == "n":
        print("Até mais!")
        break

    else:
        print("Escolha inválida! Por favor, digite 'Y' para sim ou 'N' para não.")
        time.sleep(2)
        limpar_console()