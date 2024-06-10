import disnake
import json

from disnake.ext import commands

# Configurar o bot com intents
intents = disnake.Intents.default()
bot = commands.Bot(intents=intents)

# Evento de inicialização do bot
@bot.event
async def on_ready():
    print(f"Bot está online como {bot.user}")

import yt_dlp
import asyncio
import re
import os
from pytube import YouTube

# Diretório para armazenar arquivos de áudio temporariamente
audio_dir = "audio_cache"
if not os.path.exists(audio_dir):
    os.makedirs(audio_dir)

# Caminho do executável do FFmpeg
FFMPEG_PATH = r"C:\caminho\bin\ffmpeg.exe" # subistitua pelo caminho da sua pasta ffmpeg, não esqueça de colocar a pasta bin e o ffmpeg.exe no final

def sanitize_filename(filename):
    # Remove caracteres inválidos para nomes de arquivos no Windows
    return re.sub(r'[\\/*?:"<>|]', "", filename)

@bot.slash_command(description="Reproduz uma música do YouTube")
async def play(inter: disnake.ApplicationCommandInteraction, url: str):
    await inter.response.send_message(f"Baixando a música...")

    try:
        # Extrair informações do YouTube
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Sanitize the filename
        sanitized_title = sanitize_filename(yt.title)
        audio_path = os.path.join(audio_dir, f"{sanitized_title}.mp3")

        # Baixar o áudio
        audio_stream.download(output_path=audio_dir, filename=f"{sanitized_title}.mp3")

        # Entrar no canal de voz
        if inter.author.voice is not None:
            voice_channel = inter.author.voice.channel
            if not inter.guild.voice_client:
                await voice_channel.connect()

            voice_client = inter.guild.voice_client

            # Tocar o áudio
            if voice_client.is_playing():
                voice_client.stop()
            
            def after_playing(error):
                if error:
                    print(f"Player error: {error}")
                # Desconectar após a reprodução
                coro = voice_client.disconnect()
                fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
                try:
                    fut.result()
                except Exception as e:
                    print(f"Error disconnecting: {e}")

            voice_client.play(disnake.FFmpegPCMAudio(audio_path, executable=FFMPEG_PATH), after=after_playing)
            await inter.edit_original_message(content=f"Tocando: {yt.title}")

        else:
            await inter.edit_original_message(content="Você precisa estar em um canal de voz para usar esse comando.")
    
    except Exception as e:
        await inter.edit_original_message(content=f"Erro ao tentar reproduzir a música: {str(e)}")

@bot.slash_command(description="Para a música atual e limpa o cache")
async def stop(inter: disnake.ApplicationCommandInteraction):
    if inter.guild.voice_client:
        inter.guild.voice_client.stop()
        await inter.guild.voice_client.disconnect()
        await inter.response.send_message("A música foi parada e o bot saiu do canal de voz.")
    else:
        await inter.response.send_message("Não estou tocando nenhuma música no momento.")

# Rodar o bot   
bot.run(TOKEN)
