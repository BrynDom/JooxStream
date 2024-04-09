# helper for strings

class Helper(object):
    HELP_M = '''Dibawah ini adalah menu bantuan manage : /'''
    
    HELP_ChatGPT = '''ChatGPT

Commands:

⦿ /ask
➠ Ajukan pertanyaan contoh /ask dimanakah letak antartika
'''

    HELP_Sticker = '''Stickers

Stickers Commands:

⦿ /packkang
➠ Buat paket stiker dari paket lain.

⦿ /stickerid
➠ Mendapatkan id stiker dari sebuah stiker
'''

    HELP_TagAll = '''Tag

Tag Commands:
Panggil semua anggota di group.
๏ Mention Panggil semua anggota.
➠ Stop mention /alloff

๏ /gmtag Pesan selamat pagi
➠ Tag stop /gmstop

๏ /gntag Pesan selamat malam  
➠ Tag Stop /gnstop

๏ /tagall Panggil anggota random
➠ Tag stop /tagoff /tagstop

๏ /hitag Pesan untuk sapa anggota 
➠ Tag Stop /histop

๏ /shayari Pesan mesra
➠ Tag stop /shstop

๏ /utag Pesan random
➠ Tag stop /cancel 

๏ /vctag Invite anggota ke obrolan suara
➠ /vcstop
'''

    HELP_Info = '''Info

Info Commands:

๏ /id
➠ Replay ke pasan cek id users digroup maupun dibot.
๏ /info
➠ Lihat informasi users.
๏ /github <Username>
➠ lihat informasi github dengan username.
'''
    HELP_Group = '''Group

Group Commands:
⦿ /pin 
➠ Menyematkan pesan di grup.
⦿ /pinned
➠ Menampilkan pesan yang disematkan dalam grup.
⦿ /unpin
➠ Melepas pin pesan yang saat ini dipasangi pin.
⦿ /staff
➠ Menampilkan daftar anggota staf.
⦿ /bots
➠ Menampilkan daftar bot di grup.
⦿ /settitle
➠ Menentukan judul grup.
⦿ /setdiscription
➠ Menetapkan deskripsi grup.
⦿ /setphoto
➠ Mengatur Photo Group.
⦿ /removephoto
➠ Hapus Photo group.
⦿ /zombies 
➠ Hapus akun yang sudah terhapus dari group.
⦿ /imposter ON/OFF 
➠ Mengaktifkan atau menonaktifkan pengamat grup Anda, yang memberi tahu tentang pengguna yang mengubah nama atau nama pengguna mereka.
'''

    HELP_Extra = '''Extra

Extra Commands:
⦿ /math 
➠ Memecahkan masalah matematika dan persamaan.
⦿ /blackpink 
➠ Menghasilkan logo gaya blackpink.
⦿ /carbon
➠ Hasilkan kode gambar kode karbon dari cuplikan kode.
⦿ /speedtest
➠ Lihat seberapa cepat server bot
⦿ /reverse
➠ Membalikkan teks tertentu.
⦿ /webss
➠ Salin link web dan screenshot website.
⦿ /paste
➠ Tempelkan teks berupa link.
⦿ /tgm 
➠ Upload photo agar saya bisa membuat link.
⦿ /tr
➠ Translate bahasa replay teks (id) Indonesia 
⦿ /google
➠ Cari informasi lewat google.
⦿ /stack 
➠ Untuk programming informasi.
'''

    HELP_Image = '''Image

Image Commands:

⦿ /draw
➠ Menghasilkan gambar berdasarkan perintah yang diberikan.

⦿ /image
➠ Mencari gambar berdasarkan kata kunci tertentu.

⦿ /upscale
➠ Replay ke gambar untuk meningkatkan dan memperbaiki kualitasnya.
'''
    HELP_Action = '''Tindakan

Action Commands:

Command khusus untuk ban/mute.
⦿ /kickme
➠ kicks the user who issued the command

Admins only:
⦿ /ban <userhandle>
➠ bans a user. (via handle, or reply)
⦿ /sban <userhandle>
➠ Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
⦿ /tban <userhandle>
➠ x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
⦿ /unban <userhandle>
➠ unbans a user. (via handle, or reply)
⦿ /kick <userhandle>
➠ kicks a user out of the groueply)
⦿ /mute <userhandle>
➠ silences a user. Can also be used as a reply, muting the replied to user.
⦿ /tmute <userhandle>
➠ x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
⦿ /unmute <userhandle>
➠ unmutes a user. Can also be used as a reply, muting the replied to user.
'''
    HELP_Search = '''Pencarian

Search Commands;

⦿ /google <query>
➠ Cari di Google untuk permintaan yang diberikan.

⦿ /anime <query>
➠ Telusuri animelist untuk kueri yang diberikan.

⦿ /stack <query>
➠ Telusuri stackoverflow untuk kueri yang diberikan.

⦿ /image (/imgs) <query>
➠ Dapatkan gambar mengenai permintaan Anda.

Example:
/google pyrogram: return top 5 reuslts.
'''

    HELP_Font = '''Font

Font Commands:

⦿ /font [Text]
➠ Contoh /font Hallo.

Note: pilih karakter font yang anda inginkan.
'''
    HELP_Game = '''Games

Games Commands:

⦿ /toss
➠ [Tos Action]
⦿ /roll
➠ [Game roll]
⦿ /dart
➠ [Game Dart]
⦿ /slot
➠ [Game slot]
⦿ /bowling
➠ [Game bowling]
⦿ /basket
➠ [Game basket]
⦿ /football
➠ [Game bola]
'''
    HELP_TG = '''Tele

T-Graph Commands:

⦿ /tgm
➠ [Replay ke media]

⦿ /tgt
➠ [Putar ulang ke media apa pun]
'''
    HELP_Imposter = '''Imposter

Imposter Commands:
Untuk menandai anggota yang mengubah nama digroup!

⦿ /imposter
➠ on/menghidupkan 
⦿ /imposter
➠ off/mematikan
'''
    HELP_TD = '''Truth-Dare

Command:
Kejujuran & Tantangan.

⦿ /truth
➠ Kirim teks beberapa pertanyaan untuk memulai games.
⦿ /dare 
➠ Kirim teks beberapa tantangan untuk memulai games.
'''
    HELP_HT = '''HasTag

HasTag Commands:

⦿ /hastag
➠ [Text]
'''
    HELP_TTS = '''Tts

Tts Commands:

Untuk membuat teks menjadi voice.
⦿ /tts
➠ [Text] Contoh /tts Saya ganteng.

'''
    HELP_Fun = '''Fun

Fun Commands:

⦿ /wish
➠ Tambahkan keinginan kamu.
⦿ /cute
➠ [Cek berapa nilai kecantikan kamu]
⦿ /horny
➠ [Cek apakah kamu horny apa tidak]
⦿ /lesbi
➠ [Cek apakah kamu lesbi]
⦿ /depressed
➠ [Cek berapa persen kamu depresi]
⦿ /gay
➠ [Cek apakah kamu gay atau tidak]
'''
    HELP_Q = '''Quotly

Membuat stickers besar dan kecil.

⦿ /q 
➠ Replay ke pesan agar bisa membuat stickers.

⦿ /q r
➠ Buat Stickers kecil
'''
    HELP_SangMata = '''Sang mata

/sg Cari tau riwayat nama pengguna sebelumnya.
'''

    HELP_Bot = '''Bot

Bot Commands:   
Hanya berlaku untuk developer.

⦿ /cekbot
➠ lihat bot mana saja yang online/masih hidup.
'''

    HELP_Filters = '''Filters

Filters Commands:   
⦿ /filters
➠ Buat filter digrup 
Contoh: /filters hallo replay pesan.

⦿ /stop
➠ Menghapus filter
Contoh: /stop hallo
'''   
    
    fullpromote = {
    'can_change_info': True,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': True,
    'can_invite_users': True,
    'can_restrict_members': True,
    'can_pin_messages': True,
    'can_promote_members': True,
    'can_manage_chat': True,
}

    promoteuser = {
    'can_change_info': False,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': False,
    'can_invite_users': True,
    'can_restrict_members': False,
    'can_pin_messages': False,
    'can_promote_members': False,
    'can_manage_chat': True,
}
