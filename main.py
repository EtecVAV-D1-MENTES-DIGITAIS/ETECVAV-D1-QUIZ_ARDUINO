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

banco_perguntas = [
    {
        "pergunta": "Qual é a principal função do Arduino?",
        "alternativas": ["Controlar dispositivos eletrônicos de forma programável", "Reproduzir arquivos de áudio",
        "Criar modelos 3D", "Servir como roteador de internet", "Desenvolver sites WEB"],
        "correta": "Controlar dispositivos eletrônicos de forma programável"
    },
    {
        "pergunta": "Qual linguagem de programação é usada no Arduino IDE?",
        "alternativas": ["Python", "C/C++", "Java", "Ruby", "CSS"],
        "correta": "C/C++"
    },
    {
        "pergunta": "O pino digital 13 do Arduino Uno é frequentemente usado porque:",
        "alternativas": ["Está conectado a um LED interno", "É o único que pode enviar sinal analógico", 
        "É reservado para comunicação I2C", "Não pode ser usado como saída", "É o único que ativa movimentos"],
        "correta": "Está conectado a um LED interno"
    }
    {
        "pergunta": "O que significa “IDE” em Arduino IDE?",
        "alternativas": ["Integrated Development Environment", "Internal Device Emulator", 
        "Input Data Encoder", "Interactive Design Editor", "Interactive Development Encoder"],
        "correta": "Integrated Development Environment"
    },
    {
        "pergunta": "Qual é o componente responsável por processar as instruções no Arduino Uno?",
        "alternativas": ["Sensor de temperatura", "Microcontrolador", 
        "Resistor", "Potenciômetro", "Transistor"],
        "correta": "Microcontrolador"
    },
    {
        "pergunta": "Qual destes sensores pode ser usado com Arduino para medir distância?",
        "alternativas": ["LDR", "Ultrassônico HC-SR04", 
        "DHT11", "MPU6050", "DS18B20"],
        "correta": "Ultrassônico HC-SR04"
    },
    {
        "pergunta": "Qual destes componentes armazenam energia elétrica em um circuito Arduino?",
        "alternativas": ["LED", "Resistor", "Capacitor", "Sensor", "Transistor"],
        "correta": "Capacitor"
    },
    {
        "pergunta": "A função pinMode(13, OUTPUT); serve para:",
        "alternativas": ["Definir o pino 13 como entrada digital", "Definir o pino 13 como saída digital", 
        "Ligar o LED no pino 13 automaticamente", "Resetar o microcontrolador", "Verificar e exibir movimento"],
        "correta": "Definir o pino 13 como saída digital"
    },
    {
        "pergunta": "O comando delay(1000); faz o Arduino:",
        "alternativas": ["Pausar por 1 segundo", "Enviar sinal por 1 segundo", "Reiniciar o programa", 
        "Pausar por 100 segundos", "Enviar sinal por 10 segundos"],
        "correta": "Pausar por 1 segundo"
    },
    {
        "pergunta": "Qual desses Arduinos possui conexão Wi-Fi integrada?",
        "alternativas": ["Arduino Uno", "Arduino Nano", "Arduino Mega", "Arduino Uno Wifi Rev2", "Arduino Uno Wifi Integrated"],
        "correta": "Arduino Uno Wifi Rev2"
    },
]

if __name__ == "__main__":
    main()
