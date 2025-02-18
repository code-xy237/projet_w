import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERTE !!!",
            message="Faites une pause ! Cela fait une minute que vous travaillez.",
            timeout=10
        )
        time.sleep(60)  # Pause de 60 secondes (1 min )