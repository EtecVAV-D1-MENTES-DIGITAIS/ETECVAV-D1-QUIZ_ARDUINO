import random

def mostrar_menu():
    print("\nBem vindos ao quiz sobre arduino!")
    print("1. Responder Quiz.")
    print("2. Exibir Regras.")
    print("3. Criadores.")
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
    },
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
     {
        "pergunta": "Qual a principal função dos pinos analógicos do Arduino?",
        "alternativas": [
            "Controlar motores de passo",
            "Enviar dados via Bluetooth",
            "Ler valores variáveis de sensores",
            "Ligar e desligar LEDs"
        ],
        "correta": "Ler valores variáveis de sensores"
    },
    {
        "pergunta": "Qual dessas opções representa uma placa da família Arduino?",
        "alternativas": [
            "Raspberry Pi",
            "ESP32",
            "Arduino Nano",
            "Jetson Nano"
        ],
        "correta": "Arduino Nano"
    },
    {
        "pergunta": "O que o comando analogRead(A0); faz?",
        "alternativas": [
            "Lê um valor analógico do pino A0",
            "Escreve um valor analógico no pino A0",
            "Zera a leitura do pino A0",
            "Liga o LED interno do Arduino"
        ],
        "correta": "Lê um valor analógico do pino A0"
    },
    {
        "pergunta": "Para que serve o resistor em um circuito com LED e Arduino?",
        "alternativas": [
            "Aumentar a intensidade da luz",
            "Diminuir a tensão para proteger o LED",
            "Armazenar energia elétrica",
            "Substituir o cabo de alimentação"
        ],
        "correta": "Diminuir a tensão para proteger o LED"
    },
    {
        "pergunta": "O que é a função setup() no código Arduino?",
        "alternativas": [
            "Parte do código que repete continuamente",
            "Onde são definidas configurações iniciais",
            "Onde se criam variáveis temporárias",
            "Onde o programa é finalizado"
        ],
        "correta": "Onde são definidas configurações iniciais"
    },
    {
        "pergunta": "Qual componente é usado para detectar luz em projetos com Arduino?",
        "alternativas": [
            "LDR",
            "DHT11",
            "Servo motor",
            "Relé"
        ],
        "correta": "LDR"
    },
    {
        "pergunta": "Qual é a função da porta VIN no Arduino?",
        "alternativas": [
            "Conectar o cabo USB",
            "Medir temperatura",
            "Receber alimentação externa (geralmente 7–12V)",
            "Transmitir dados para o computador"
        ],
        "correta": "Receber alimentação externa (geralmente 7–12V)"
    },
    {
        "pergunta": "Em qual tipo de pino o comando analogWrite() pode ser usado?",
        "alternativas": [
            "Apenas em pinos digitais marcados com “~”",
            "Em qualquer pino analógico",
            "Apenas no pino 13",
            "Somente nos pinos de entrada"
        ],
        "correta": "Apenas em pinos digitais marcados com “~”"
    },
    {
        "pergunta": "O que o componente servo motor faz em um projeto com Arduino?",
        "alternativas": [
            "Mede temperatura",
            "Controla movimento angular preciso",
            "Converte som em luz",
            "Armazena dados"
        ],
        "correta": "Controla movimento angular preciso"
    },
    {
        "pergunta": "Qual é a tensão de operação padrão da placa Arduino Uno?",
        "alternativas": [
            "3,3 volts",
            "5 volts",
            "7,5 volts",
            "12 volts"
        ],
        "correta": "5 volts"
    },
    {
        "pergunta": "O que é o Arduino?",
        "alternativas": [
            "Um tipo de sensor de temperatura",
            "Uma plataforma de prototipagem eletrônica",
            "Um software de edição de imagens",
            "Um tipo de cabo USB"
        ],
        "correta": "Uma plataforma de prototipagem eletrônica"
    },
    {
        "pergunta": "Para que serve a porta USB no Arduino?",
        "alternativas": [
            "Apenas para ligar LEDs",
            "Para conectar sensores externos",
            "Para programar e alimentar o Arduino",
            "Para aumentar a memória do Arduino"
        ],
        "correta": "Para programar e alimentar o Arduino"
    },
    {
        "pergunta": "O que significa o termo “sketch” no Arduino?",
        "alternativas": [
            "Um tipo de componente físico",
            "Um código ou programa criado para o Arduino",
            "Um sensor de movimento",
            "Um desenho do circuito"
        ],
        "correta": "Um código ou programa criado para o Arduino"
    },
    {
        "pergunta": "Qual linguagem de programação o Arduino usa principalmente?",
        "alternativas": [
            "Java",
            "Python",
            "C/C++",
            "HTML"
        ],
        "correta": "C/C++"
    },
    {
        "pergunta": "O que faz o pino GND no Arduino?",
        "alternativas": [
            "Envia sinal para o computador",
            "É o pino de alimentação positiva",
            "É o pino de terra (negativo do circuito)",
            "Mede a corrente elétrica"
        ],
        "correta": "É o pino de terra (negativo do circuito)"
    },
    {
        "pergunta": "O que acontece quando o pino 13 é acionado no Arduino Uno, por padrão?",
        "alternativas": [
            "Um LED interno acende",
            "O Arduino desliga",
            "O programa é apagado",
            "O motor começa a girar"
        ],
        "correta": "Um LED interno acende"
    },
    {
        "pergunta": "Qual componente é necessário para medir a distância usando Arduino?",
        "alternativas": [
            "Sensor ultrassônico",
            "Motor DC",
            "Sensor de luz LDR",
            "Potenciômetro"
        ],
        "correta": "Sensor ultrassônico"
    },
    {
        "pergunta": "O que o comando digitalWrite() faz no código Arduino?",
        "alternativas": [
            "Lê o valor de um sensor",
            "Escreve um valor em um pino digital (HIGH ou LOW)",
            "Define a velocidade do motor",
            "Cria uma variável"
        ],
        "correta": "Escreve um valor em um pino digital (HIGH ou LOW)"
    },
    {
        "pergunta": "Qual desses itens é hardware do Arduino?",
        "alternativas": [
            "IDE do Arduino",
            "Cabo USB",
            "Placa Arduino Uno",
            "Código de programação"
        ],
        "correta": "Placa Arduino Uno"
    },
    {
        "pergunta": "O que é necessário para o Arduino funcionar corretamente?",
        "alternativas": [
            "Apenas o cabo de energia",
            "Um sensor e um resistor",
            "Alimentação elétrica e um programa carregado",
            "Um botão e um display"
        ],
        "correta": "Alimentação elétrica e um programa carregado"
    }
]

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            print("\nIniciando o Quiz de Arduino...")
            perguntas_sorteadas = sortear_questoes(banco_perguntas)

            pontuacao = 0
            indice = 0

            while indice < len(perguntas_sorteadas):
                numero_questao = indice + 1
                acertou = exibir_questao(numero_questao, perguntas_sorteadas[indice])
                pontuacao += verificar_resposta(acertou)
                indice += 1

            exibir_resultado(pontuacao)

        elif opcao == '2':
            mostrar_regras()

        elif opcao == '3':
            mostrar_creditos()

        elif opcao == '4':
            print("Programa terminado...")
            break

if __name__ == "__main__":
    main()
