import cv2
from ultralytics import YOLO #You Only Look Once

print("Visão computacional ativada 👁️‍🗨️")

modelo = YOLO("yolov8n.pt") #yolov8n-seg.pt, yolov8n-pose.pt, yolov8n.pt

cap = cv2.VideoCapture("video.mp4")

print("Câmera ligada! Aperte 'Q' para sair! ")

while True:
    
    sucesso,frame = cap.read()
    
    if not sucesso:
        break
    resultados = modelo(frame, stream=True, verbose=False)
    
    for resultado in resultados:
        imagem_com_quadrados = resultado.plot()
        imagem_menor = cv2.resize(imagem_com_quadrados,(0,0), fx=0.05, fy=0.05)
        
    cv2.imshow("Radar Computacional", imagem_menor)
    
    if cv2.waitKey(1) == ord('Q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        
    
    