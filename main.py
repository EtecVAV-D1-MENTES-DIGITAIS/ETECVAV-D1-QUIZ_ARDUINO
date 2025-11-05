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

if __name__ == "__main__":
    main()
