#smtp kütüphanesini import ettik
import smtplib

#Mail başlığı için isim belirledik ve title değişkenine atadık
title="Subject:Deneme"

#Göndereceğimiz maili yazdık ve message değişkenine atadık
message="Mail gönderme denemesi"

#başlık ve mesajı content değşkenine atadık
content=title+'\n'+message

#Mail göndereceğimiz adresi sender değişkenine atadık
sender="hasn56gd@gmail.com"

#Mail göndereceğimiz adresin uygulama şifresini passworld değişkenine atadık
#Önemli kısımlardan biri de uygulama şifresine ulaşmak.Bunun için olan adımlara png olarak ulaşabilirsiniz
password="Buraya mail adresimizden aldığımız uygulama şifresini giriyoruz"

#Maili göndereceğimiz adresi to değişkenine atadık
to="oguzzh4nn@gmail.com"


# SMTP sunucusuna bağlanma
server = smtplib.SMTP("smtp.gmail.com", 587)

# Sunucu ile el sıkışma işlemi
server.ehlo()

# Güvenli bağlantı başlatma (TLS)
server.starttls()

# Gmail hesabına giriş yapma
server.login(sender, password)

# E-posta gönderme
server.sendmail(sender, to, content.encode("utf-8"))

# SMTP bağlantısını kapatma
server.close()

