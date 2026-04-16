import cv2

cap = cv2.VideoCapture(0)

print("Aperte F para tirar a foto ou Q para fechar")

while True:
    sucesso, frame = cap.read()
    
    cv2.imshow("Minha Câmera", frame)
    
    tecla = cv2.waitKey(1) #Espera um  milisegundo
    
    if tecla == ord('f'):
        cv2.imwrite("minha_foto.jpg",frame)
        print("Foto salva com sucesso 🎥")
        
    elif tecla == ord('q'):
        break
    