from pyrogram import Client, filters
import random
from Musikbot import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "Cinta sedang mengudara tetapi membutuhkan sedikit percikan..",
            "Awal yang baik tetapi masih ada ruang untuk berkembang.",
            "Itu hanyalah awal dari sesuatu yang indah."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "Ada hubungan yang kuat di sana. Terus peliharalah itu.",
            "Anda punya peluang bagus. Sedang dikerjakan.",
            "Cinta sedang mekar, teruskan."
        ])
    else:
        return random.choice([
            "Wow! Ini adalah pasangan yang dibuat di surga!",
            "Pasangan sempurna! Hargai ikatan ini.",
            "Ditakdirkan untuk bersama. Selamat!"
        ])
        
@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    else:
        response = "Silakan masukkan dua nama setelah perintah /love."
    app.send_message(message.chat.id, response)
