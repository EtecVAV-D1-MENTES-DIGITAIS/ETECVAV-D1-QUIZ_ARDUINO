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
        "pergunta": "O comando Serial.begin(9600); serve para:",
        "alternativas": ["Iniciar a comunicação serial a 9600 bps", "Ativar o pino digital 13", "Controlar o servo motor", "Definir modo analógico", "Encerrar o programa"],
        "correta": "Iniciar a comunicação serial a 9600 bps"
    },
    {
        "pergunta": "Qual biblioteca é usada para controlar servos no Arduino?",
        "alternativas": ["Servo.h", "Motor.h", "PWM.h", "Stepper.h", "Serial.h"],
        "correta": "Servo.h"
    },
    {
        "pergunta": "O comando digitalRead(2); faz o quê?",
        "alternativas": ["Lê o estado (HIGH ou LOW) do pino 2", "Ativa o LED interno", "Lê um valor analógico", "Define o pino 2 como saída", "Reinicia o código"],
        "correta": "Lê o estado (HIGH ou LOW) do pino 2"
    },
    {
        "pergunta": "O símbolo “~” nos pinos do Arduino indica:",
        "alternativas": ["Pinos com função PWM", "Pinos analógicos", "Pinos reservados para GND", "Pinos de alimentação", "Pinos RX/TX"],
        "correta": "Pinos com função PWM"
    },
    {
        "pergunta": "Qual a voltagem máxima suportada na entrada analógica do Arduino Uno?",
        "alternativas": ["3,3V", "5V", "7V", "9V", "12V"],
        "correta": "5V"
    },
    {
        "pergunta": "O comando tone(8, 1000); faz o quê?",
        "alternativas": ["Gera um som de 1000 Hz no pino 8", "Lê o som do pino 8", "Liga o LED do pino 8", "Desativa o buzzer", "Ativa o motor"],
        "correta": "Gera um som de 1000 Hz no pino 8"
    },
    {
        "pergunta": "Qual o nome do software usado para programar o Arduino?",
        "alternativas": ["Arduino IDE", "Tinkercad", "MATLAB", "Proteus", "Code::Blocks"],
        "correta": "Arduino IDE"
    },
    {
        "pergunta": "Qual a principal função do GND?",
        "alternativas": ["Fornecer corrente positiva", "Atuar como terra (retorno de corrente)", "Medir tensão", "Enviar dados", "Regular energia"],
        "correta": "Atuar como terra (retorno de corrente)"
    },
    {
        "pergunta": "O comando noTone(8); serve para:",
        "alternativas": ["Parar o som gerado no pino 8", "Iniciar som no pino 8", "Ativar LED no pino 8", "Enviar sinal HIGH", "Reiniciar o Arduino"],
        "correta": "Parar o som gerado no pino 8"
    },
    {
        "pergunta": "O que significa PWM?",
        "alternativas": ["Pulse Width Modulation", "Power Wave Mode", "Positive Wave Mechanism", "Parallel Write Memory", "Programmable Wave Mode"],
        "correta": "Pulse Width Modulation"
    },
    {
        "pergunta": "Qual comando envia mensagens ao monitor serial?",
        "alternativas": ["Serial.print()", "digitalWrite()", "analogRead()", "tone()", "pinMode()"],
        "correta": "Serial.print()"
    },
    {
        "pergunta": "O que o comando millis() retorna?",
        "alternativas": ["Tempo em milissegundos desde o início do programa", "Número de ciclos do processador", "Valor de leitura do pino A0", "Contagem de loops", "Tempo do delay"],
        "correta": "Tempo em milissegundos desde o início do programa"
    },
    {
        "pergunta": "Qual componente converte energia elétrica em movimento rotacional?",
        "alternativas": ["Motor DC", "Resistor", "Capacitor", "LDR", "Diodo"],
        "correta": "Motor DC"
    },
    {
        "pergunta": "O que é o Tinkercad?",
        "alternativas": ["Um simulador de circuitos e Arduino online", "Um tipo de Arduino físico", "Uma placa controladora", "Um microcontrolador", "Um aplicativo de celular"],
        "correta": "Um simulador de circuitos e Arduino online"
    },
    {
        "pergunta": "O comando map(valor, 0, 1023, 0, 255); faz o quê?",
        "alternativas": ["Converte a faixa de leitura analógica (0–1023) para 0–255", "Liga o pino 13", "Envia sinal digital", "Zera o programa", "Lê o pino 0"],
        "correta": "Converte a faixa de leitura analógica (0–1023) para 0–255"
    },
    {
        "pergunta": "O que o sensor DHT11 mede?",
        "alternativas": ["Temperatura e umidade", "Distância e luz", "Som e vibração", "Movimento e cor", "Pressão e altitude"],
        "correta": "Temperatura e umidade"
    },
    {
        "pergunta": "O que é o RX/TX no Arduino?",
        "alternativas": ["Pinos de comunicação serial (receber e transmitir)", "Sensores de luz", "Entradas analógicas", "Saídas PWM", "Linhas de alimentação"],
        "correta": "Pinos de comunicação serial (receber e transmitir)"
    },
    {
        "pergunta": "O que faz a função random(10)?",
        "alternativas": ["Gera um número aleatório de 0 a 9", "Reinicia o programa", "Lê um sensor", "Ativa um LED", "Cria uma variável"],
        "correta": "Gera um número aleatório de 0 a 9"
    },
    {
        "pergunta": "Qual é o valor lógico de HIGH no Arduino?",
        "alternativas": ["1 (ou 5V)", "0 (ou 0V)", "3.3V", "7V", "10V"],
        "correta": "1 (ou 5V)"
    },
    {
        "pergunta": "Qual é o valor lógico de LOW no Arduino?",
        "alternativas": ["0 (ou 0V)", "1 (ou 5V)", "3.3V", "9V", "10V"],
        "correta": "0 (ou 0V)"
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
