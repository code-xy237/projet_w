from pytube import YouTube

def download_video(url, save_path="./"):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Téléchargement de : {yt.title} ...")
        video_stream.download(output_path=save_path)
        print("Téléchargement terminé !")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    video_url = input("Entrez l'URL de la vidéo YouTube : ")
    destination = input("Entrez le chemin de sauvegarde (laisser vide pour l'actuel) : ") or "./"
    download_video(video_url, destination)
