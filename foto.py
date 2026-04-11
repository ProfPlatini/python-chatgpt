# ==============================================================================
# PASSO 1: IMPORTAÇÃO E PREPARAÇÃO
# ==============================================================================

# Importa a biblioteca OpenCV (que no Python se chama cv2). 
# É ela que tem os "poderes" de conversar com a câmera e entender as imagens.
# Lembrete para os alunos: Vocês precisam rodar 'pip install opencv-python' no terminal antes!
import cv2 

# O comando VideoCapture é como "pedir a chave" da câmera para o computador.
# O número (0) indica qual câmera queremos. 
# Se você tiver uma webcam USB conectada além da do notebook, ela seria a (1).
cap = cv2.VideoCapture(0)

# Imprime instruções claras no terminal para o usuário não ficar perdido.
print("Aperte 'F' para tirar a foto ou 'Q' para fechar.")

# ==============================================================================
# PASSO 2: O LOOP DE VÍDEO (A MÁGICA ACONTECE AQUI)
# ==============================================================================

# O computador não entende o que é "vídeo". Ele só entende "fotos em sequência".
# O 'while True' cria um loop infinito que obriga o Python a tirar fotos sem parar.
while True:
    
    # O comando cap.read() tira a foto daquele exato milissegundo.
    # Ele nos devolve duas coisas:
    # 1. 'sucesso': Uma variável Verdadeiro/Falso que diz se a câmera funcionou.
    # 2. 'frame': A foto em si (os pixels coloridos que formam a imagem).
    sucesso, frame = cap.read() 
    
    # Abre uma janela visual no sistema operacional (Windows/Mac).
    # O primeiro texto ("Minha Camera") é o título que vai aparecer na barra da janela.
    # O 'frame' é a imagem que será pintada dentro dessa janela.
    cv2.imshow("Minha Camera", frame)
    
    # ==========================================================================
    # PASSO 3: ESCUTANDO O TECLADO (O TRADUTOR UNIVERSAL)
    # ==========================================================================
    
    # cv2.waitKey(1): Congela o programa por 1 milissegundo para ouvir o teclado.
    # & 0xFF: É um "filtro de limpeza". Ele remove códigos estranhos que o 
    # Windows ou Mac possam enviar, garantindo que o Python receba a letra pura.
    tecla = cv2.waitKey(1) & 0xFF
    
    # A função ord() pega a letra 'f' e descobre qual é o número oficial dela no teclado.
    if tecla == ord('f'): 
        # cv2.imwrite cria um arquivo de imagem no seu HD (Disco Rígido).
        # Ele pega o 'frame' atual e salva com o nome "minha_foto.jpg".
        cv2.imwrite("minha_foto.jpg", frame)
        print("📸 Foto salva com sucesso na pasta!")
        
    # Verifica se a tecla apertada foi a letra 'q' (de Quit/Sair)
    elif tecla == ord('q'):
        # O comando 'break' destrói o 'while True', encerrando o loop infinito.
        break

# ==============================================================================
# PASSO 4: LIMPEZA E BOAS PRÁTICAS (NUNCA ESQUECER)
# ==============================================================================

# cap.release() "devolve a chave" da câmera para o computador. 
# Se não fizermos isso, a luz da webcam fica acesa e nenhum outro programa 
# (como Zoom ou Teams) conseguirá usar a câmera até você reiniciar o PC.
cap.release()

# Destrói todas as janelas ("Minha Camera") que o OpenCV criou na tela,
# liberando a memória RAM do computador.
cv2.destroyAllWindows()