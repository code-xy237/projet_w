import cv2
import numpy as np
import pyautogui

# Définir la résolution de l'écran
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# Définir le nom du fichier de sortie
output_filename = "screen_recording.mp4"

# Définir les FPS
fps = 30.0

# Définir le codec et créer l'objet VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

# Durée de l'enregistrement en secondes
recording_duration = 15  # Modifier selon besoin

# Démarrer l'enregistrement
for _ in range(int(fps * recording_duration)):
    # Capturer l'écran
    screen = pyautogui.screenshot()
    
    # Convertir la capture en tableau numpy et changer le format en BGR pour OpenCV
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Écrire l'image dans la vidéo
    out.write(frame)

# Libérer la ressource de l'écriture vidéo
out.release()

print("Enregistrement terminé et sauvegardé sous 'screen_recording.mp4'")
