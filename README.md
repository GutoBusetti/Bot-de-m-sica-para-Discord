# Bot de música para discord usando FFMpeg com Python
Bot de música simples para discord usando FFMpeg. Neste exemplo estou usando a lib do Disnake, mas pode se usar a do discord.py e dentre outras bibliotecas. Para este bot é crucial instalar o ffmpeg em seu computador, veja abaixo de forma descomplicada como fazer a instalação dele.

# Passos para Instalar o FFmpeg do Gyan.dev:
Baixar FFmpeg:

Vá para a página de builds do FFmpeg de Gyan.dev: [Click Aqui](https://www.gyan.dev/ffmpeg/builds/.)
Na seção "Release builds", clique no link ffmpeg-git-full.7z para baixar a versão completa.
Extrair os Arquivos:

Extraia o conteúdo do arquivo baixado (ffmpeg-git-full.7z) para uma pasta, por exemplo, C:\ffmpeg. Você pode usar um programa como 7-Zip para extrair arquivos .7z.
Adicionar FFmpeg ao PATH:

Abra o "Painel de Controle" > "Sistema e Segurança" > "Sistema" > "Configurações avançadas do sistema".
Clique no botão "Variáveis de ambiente".
Em "Variáveis do sistema", selecione a variável Path e clique em "Editar".
Clique em "Novo" e adicione o caminho para a pasta bin do FFmpeg, por exemplo, C:\ffmpeg\bin.
Clique em "OK" para fechar todas as janelas.
Verificar a Instalação:

Abra o Prompt de Comando (CMD) e digite ffmpeg -version. Você deve ver informações sobre a versão do FFmpeg instalada.
Verificação
Certifique-se de que a instalação está correta e que o FFmpeg está disponível no PATH do sistema. A saída do comando ffmpeg -version no CMD deve mostrar algo assim:
