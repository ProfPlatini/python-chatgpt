import cv2
from ultralytics import YOLO

modelo = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)

cv2.namedWindow("Radar móvel", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Radar móvel", 1280, 720)

print("Sistema de Automação e Controle de Processos!")

while True:
    sucesso, frame = cap.read()
    if not sucesso: break

    resultados = modelo(frame, verbose=False)
    frame_com_ia = resultados[0].plot(line_width=2)

    tem_celular_na_tela = False

    for box in resultados[0].boxes:
        classe_id = int(box.cls[0]) 
        
        if classe_id == 39:
            tem_celular_na_tela = True
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            centro_x = int((x1 + x2) / 2)
            centro_y = int((y1 + y2) / 2)
            
            cv2.circle(frame_com_ia, (centro_x, centro_y), 60, (0, 0, 255), 5)
            cv2.line(frame_com_ia, (centro_x-80, centro_y), (centro_x+80, centro_y), (0, 0, 255), 2)
            cv2.line(frame_com_ia, (centro_x, centro_y-80), (centro_x, centro_y+80), (0, 0, 255), 2)

    if tem_celular_na_tela:
        altura, largura, _ = frame_com_ia.shape
        cv2.rectangle(frame_com_ia, (0, 0), (largura, altura), (0, 0, 255), 40)
        cv2.putText(frame_com_ia, "Garrafa Detectada!", (100, 150), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 5)
        cv2.putText(frame_com_ia, "Inciando processo de envase!", (100, 220), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 255), 4)

    cv2.imshow("Visão computacional - Operação de Máquinas", frame_com_ia)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()