from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


# Mulai buat gambar
sertif_base = Image.open("Sertifikat_SGT_2021.jpg")
SB_W, SB_H  = sertif_base.size


# Masukan dari input
nama_jabatan = []
f = open("input.txt", "r")
for entry in f:
    nama_jabatan.append(entry.split(","))
f.close()

# Nulis ke text
for data in nama_jabatan:
    # inisialisasi ulang tiap data
    sertif_edit = sertif_base.copy()
    sertif_draw = ImageDraw.Draw(sertif_edit)
    nama, jabatan = data
    

    # drawing text
    Font = ImageFont.truetype("font.ttf", 212)

    NW, NH = Font.getsize(nama)
    JW, JH = Font.getsize(jabatan)

    buffer_error = 68

    sertif_draw.text(((SB_W-NW)/2-buffer_error,1000), nama, fill="black", font= Font)
    sertif_draw.text(((SB_W-JW)/2-buffer_error,1320), jabatan, fill="black", font= Font)

    # save
    sertif_edit.save(f"jadi\sertif_{nama}.jpg")