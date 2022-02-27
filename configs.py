# copyright ©️ 2021 nabilanavab
# fileName: configs.py
# Total time wasted ~ 250 hrs



import os
    
    
    
    
    
# Config Variables
class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    API_TOKEN = os.environ.get("API_TOKEN")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL")
    CONVERT_API = os.environ.get("CONVERT_API")
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE")
    OWNER_ID = os.environ.get("OWNER_ID")
    BANNED_USER = os.environ.get("BANNED_USER")
    PDF_THUMBNAIL = "./tmb.jpg"
    
    
    
    
    
# Message Variables
class Msgs(object):
    
    
    welcomeMsg = """Halo [{}](tg://user?id={}) 👋 Bot ini akan membantu Anda melakukan banyak hal dengan pdf 

Fitur utama :
➤ `Convert images to PDF`
➤ `Convert PDF to images` (On Develop)
➤ `Convert files to pdf` (On Develop)
"""
    
    
    feedbackMsg = """
[Tulis feedback 📋](https://tellonym.me/Developer_InHame)
"""

    menuMsg = """Halo [{}](tg://user?id={}) 👋 terimakasih sudah menggunakan InHame PDF Bot, berikut perintah yang tersedia 

`Umum`
/start - memulai bot
/id - melihat id telegram Anda
/feedback - memberikan saran kepada dev untuk bot
/menu - menampilkan menu perintah yang tersedia
/dev - informasi tentang developer(pengembang) bot ini
/report - melaporkan bug/error pada bot

`Image to PDF`
/buat - membuat file pdf
/hapus - menghapus antrian sebelumnya

`PDF to ..`
(On Develop)
"""

    caraMsg = """
[Cara Menyimpan PDF 💾](https://telegra.ph/Cara-Menyimpan-PDF-ke-Storage-02-20-2)
"""
    
    
    forceSubMsg = """Tunggu [{}](tg://user?id={})..!!

Karena alasan traffic server maka hanya Anggota channel yang Dapat Menggunakan
    
Anda diwajibkan untuk bergabung kedalam channel.

Klik "refresh" jika sudah bergabung.. 
"""
    
    
    foolRefresh = """Cie boong, masuk channel dulu baru bisa gunain yaa... 😐"""
    
    
    fullPdfSplit = """Jika Anda ingin membagi pdf,

Anda perlu mengirim limit juga..
"""
    
    
    bigFileUnSupport = """Karena Overload, bot hanya mendukung file {}mb

`silahkan kirim file kurang dari {}mb`
"""
    
    
    encryptedFileCaption = """Nomer halaman: {}
key 🔐: `{}`"""
    
    
    imageAdded = """`✅ - Berhasil Menambahkan {} halaman ke pdf`
"""

    gmbrAlrt = """`*⏱️pesan akan terhapus dalam 8s
    Note : Jika ingin menambahkan foto lainnya dalam satu pdf silahkan kirim foto sebelum melakukan /buat`

/buat [Nama Filemu Bebas] - untuk membuat nama pdf
/hapus - untuk menghapus semua halaman
"""
    
    
    errorEditMsg = """⛔️ - Something went wrong

ERROR: `{}`
"""
    
    
    pdfReplyMsg = """`Total : {}halaman`

balas:
/extract - _ untuk mendapatkan seluruh halaman _
/extract `pgNo` - __ untuk mendapatkan halaman tertentu __
/extract `start:end` - __untuk mendapatkan semua gambar b/w_


/encrypt `password` - untuk mengatur password
/text - untuk mengekstrak teks dari pdf
"""
    
    
    aboutDev = """About Dev: males ngisinya, ntaran ae
"""
    
    
    I2PMsg = """Images to pdf :

 ➤ Urutan gambar akan dipertimbangkan 
 ➤ Kirim gambar tanpa dikompres (for better quality) 
 
 ➤ `/hapus` - Delete antrian saat ini 
 ➤ `/id` - mendapatkan telegram ID-mu                                                      
 
 ➤ GANTI NAMA PDF ANDA:
 
    - Secara default, ID telegram Anda akan diperlakukan sebagai nama pdf Anda..
    - `/buat fileName` - untuk mengubah nama pdf menjadi nama file
    - `/buat name` - untuk mendapatkan pdf dengan nama telegram Anda
"""
    
    
    P2IMsg = """PDF to images:

        Just Kirim/teruskan file pdf kepada saya.

 ➤ Saya akan mengonversinya menjadi gambar ️
 ➤ jika Beberapa halaman dalam pdf (kirim sebagai album)
 ➤ Nomor halaman diurutkan secara berurutan
 ➤ Kirim gambar lebih cepat dari bot lain (klo hoax keplak palanya ilham)
 ➤ /cancel : kensel
"""
    
    
    F2PMsg = """Files to PDF:

       Just Kirim/teruskan file yang Didukung.. Saya akan mengonversinya ke pdf dan mengirimkannya kepada Anda..

➤ Supported files(.epub, .xps, .oxps, .cbz, .fb2) 
➤ Tidak perlu menentukan ekstensi file telegram Anda
➤ Hanya Gambar & karakter ASCII yang Didukung
➤ menambahkan 30+ format file baru yang dapat dikonversi ke pdf
API LIMITS.. (gapunya duid buat beli yg premi wakwaow)
"""
    
    
    warningMessage = """PESAN PERINGATAN ️:

Bot ini sepenuhnya gratis untuk digunakan jadi tolong jangan spam di sini 

Tolong jangan mencoba menyebarkan konten 18+

JIKA ADA JENIS LAPORAN, BUGS, PERMINTAAN, DAN SARAN SILAHKAN HUBUNGI @hamshff
"""
    
    
    back2Start = """Hai..!! Bot ini akan membantu Anda melakukan banyak hal dengan pdf

Beberapa fitur utama adalah :
➤ `Convert images to PDF`
➤ `Convert PDF to images`
➤ `Convert files to pdf`
"""