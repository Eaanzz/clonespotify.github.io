import qrcode

# Data untuk QR Code (URL atau teks)
data_qris = "https://example.com/path-to-your-image.jpg"  # Ganti dengan URL Anda

# Membuat objek QRCode
qr = qrcode.QRCode(
    version=1,  # Versi QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Koreksi kesalahan
    box_size=10,  # Ukuran tiap kotak QR Code
    border=4,  # Lebar border (min 4)
)

# Menambahkan data ke QR Code
qr.add_data(data_qris)
qr.make(fit=True)

# Membuat gambar QR Code
img = qr.make_image(fill="black", back_color="white")

# Menyimpan dan menampilkan gambar QR Code
img.save("qris_example.png")  # Simpan sebagai file
img.show()  # Tampilkan
