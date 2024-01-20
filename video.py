from pytube import YouTube

# URL do vídeo
url = "https://www.youtube.com/watch?v=vTLRLusmYJ4&t=7s"

# Cria um objeto YouTube
yt = YouTube(url)

# Obtém a stream de maior resolução disponível
video_stream = yt.streams.get_highest_resolution()

# Baixa o vídeo
video_stream.download(output_path=r"C:\Users\leona\OneDrive\Área de Trabalho\downloadElisa")

print("Download concluído.")
