import turtle
import random
import time

# Pencere ayarları
pencere = turtle.Screen()
pencere.title("Kaplumbağa Yakalama Oyunu")
pencere.bgcolor("white")
pencere.setup(width=600, height=600)

# Skor
skor = 0

# Kaplumbağa nesnesi
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()
kaplumbaga.speed(0)
kaplumbaga.hideturtle()  # Kaplumbağayı başlangıçta gizle

# Zaman sınırlaması
oyun_suresi = 10

# Skor yazısı
skor_yazisi = turtle.Turtle()
skor_yazisi.speed(0)
skor_yazisi.color("black")
skor_yazisi.penup()
skor_yazisi.hideturtle()
skor_yazisi.goto(0, 260)
skor_yazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

# Süre yazısı
sure_yazisi = turtle.Turtle()
sure_yazisi.speed(0)
sure_yazisi.color("black")
sure_yazisi.penup()
sure_yazisi.hideturtle()
sure_yazisi.goto(0, -260)
sure_yazisi.write("Süre: {} saniye".format(oyun_suresi), align="center", font=("Courier", 18, "normal"))


# Yeni kaplumbağa pozisyonu belirleme
def yeni_pozisyon():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    kaplumbaga.goto(x, y)
    kaplumbaga.showturtle()  # Kaplumbağayı yeni pozisyonda göster


# Kaplumbağayı yeni pozisyona taşıma
def pozisyon_guncelle():
    yeni_pozisyon()
    if time.time() - baslangic_zamani < oyun_suresi:
        pencere.ontimer(pozisyon_guncelle, 1000)  # 1 saniye


# Fare tıklamasını yakalama
def kaplumbaga_tiklama(x, y):
    global skor
    if kaplumbaga.distance(x, y) < 20:
        skor += 1
        skor_yazisi.clear()
        skor_yazisi.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))
        yeni_pozisyon()


pencere.onclick(kaplumbaga_tiklama)
baslangic_zamani = time.time()
pozisyon_guncelle()

# Ana oyun döngüsü
while time.time() - baslangic_zamani < oyun_suresi:
    kalan_sure = int(oyun_suresi - (time.time() - baslangic_zamani))
    sure_yazisi.clear()
    sure_yazisi.write("Süre: {} saniye".format(kalan_sure), align="center", font=("Courier", 18, "normal"))
    pencere.update()

# Oyun bittiğinde sonuçları gösterme
kaplumbaga.hideturtle()  # Oyun bittiğinde kaplumbağayı gizle
sure_yazisi.clear()
sure_yazisi.goto(0, -260)
sure_yazisi.write("Süre Bitti!", align="center", font=("Courier", 18, "normal"))
skor_yazisi.clear()
skor_yazisi.goto(0, 0)
skor_yazisi.write("Oyun Bitti!\nSkor: {}".format(skor), align="center", font=("Courier", 36, "normal"))

turtle.mainloop()
