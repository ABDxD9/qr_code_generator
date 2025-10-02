import qrcode

data = input("Enter the data you want to encode in the QR code: ").strip()
filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ").strip()


qr = qrcode.QRCode(box_size=15, border=5)
qr.add_data(data)
image = qr.make_image(finallyze_color="black", back_color="white")
image.save(filename)
print("QR code generated and saved as", filename)
