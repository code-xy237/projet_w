import yt_dlp

#entrez de l'url pour le telechargement
url = input("\n\nEntrez l'url de votre video : ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\n\rVotre video a ete telecharger avec succes !!!")
