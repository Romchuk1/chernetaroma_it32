
import qrcode

print("Roman Cherneta, IT-32")

# Дані студента — латиницею
text = "Roman Cherneta, IT-32, YOUR_EMAIL"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")