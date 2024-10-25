# Importando bibliotecas essenciais
import cv2
import mediapipe as mp

# Inicializando o MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)  # 0 refere-se à webcam padrão

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Converter o frame para RGB, pois o MediaPipe usa imagens RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Processar a imagem para detectar poses
    results = pose.process(frame_rgb)

    # Desenhar os pontos do corpo e as conexões na imagem original
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=2, circle_radius=3),
                                  mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))
    if results.pose_landmarks:
        label = "Pessoa detectada"
        color = (0, 255, 0)
    else:
        label = "Sem pessoa detectada"
        color = (0, 0, 255)
    # Mostrar a imagem
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Detecção de Esqueleto em Tempo Real - MediaPipe", frame)


    # Tecla para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
