import random

def mostrar_menu():
    print("\nBem vindos ao quiz sobre arduino!")
    print("1. Responder Quiz.")
    print("2. Exibir Regras.")
    print("2. Criadores.")
    print("4. Encerrar Programa.")

    while True:
        opcao = input("Escolha uma opção (1-4): ")
        if opcao in ['1', '2', '3', '4']:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")

def mostrar_regras():
    print("\nREGRAS DO QUIZ:")
    print("""
1. O quiz contém 20 perguntas variadas sobre arduino.
2. Cada questão vale 0,5 pontos.
3. Digite apenas a letra da resposta (A, B, C, D ou E).
4. Ao final do jogo é mostrada sua pontuação.
Bom jogo!
    """)
    
def mostrar_creditos():
    print("\nCriadores do jogo")
    print("""
Alex, Ana Carolina, Arthur, Bianca e Helena
Curso Técnico em Informática para Internet, 1°D
    """)
    
def sortear_questoes(banco):
    qtd = 20
    if len(banco) < 20:
        qtd = len(banco)
    return random.sample(banco, qtd)
    
def verificar_resposta(acertou):
    if acertou:
        return 0.5
    else:
        return 0
        
def exibir_questao(numero, questao):
    print(f"\nQuestão {numero}: {questao['pergunta']}")

    alternativas = questao['alternativas'][:]
    random.shuffle(alternativas)

    indice = 0
    while indice < len(alternativas):
        letra = chr(65 + indice)
        print(f"{letra}. {alternativas[indice]}")
        indice += 1

    resposta_usuario = input("Sua resposta: ").upper()
    while resposta_usuario not in ['A', 'B', 'C', 'D', 'E']:
        resposta_usuario = input("Digite apenas A, B, C, D ou E: ").upper()

    indice_resposta = ord(resposta_usuario) - 65
    return alternativas[indice_resposta] == questao['correta']

def exibir_resultado(pontos):
    print("\nPONTUAÇÃO FINAL")
    print(f"Sua pontuação total: {pontos:.1f} / 10.0")
    if pontos == 10:
        print("Parabens! Você acertou todas as perguntas!")
    elif pontos >= 7:
        print("Muito bem! Acertou a maioria!")
    elif pontos >= 5:
        print("Quase lá! Dá pra melhorar!")
    else:
        print("Não desista! Tente mais vezes!")

if __name__ == "__main__":
    main()
