#sayı tahmin oyunu
import random as r
while True:
    s = r.randint(0,100)
    print('Sayı tahmin etme oyunuma hoşgeldiniz:)')
    print("Oyundan çıkıp yeni oyun başlatmak için '-1' giriniz.")
    print('Geçersiz girişlerde hakkınız düşecektir.')
    print('0-100 arasında bir sayı tahmin ediniz.')
    print(' ')
    x = 5
    for i in range(0,5):
        y = x-i
        print(f"{y} tahmin hakkınız kaldı.")
        t = int(input(' Tahmininiz nedir? \n '))
        if t == -1:
            print('Yeni oyuna geçiliyor.\n')
            break
        if t < -1 or t > 100:
            print('Lütfen 0-100 arasında bir sayı giriniz. \n')
        if t==s :
            print('Sayıyı doğru tahmin ettiniz.')
            print('Yeni oyun başlatılıyor... \n')
            break
        if t!=s and y!=1:
            if t > s:
                print('Daha küçük bir sayı deneyiniz.')
            elif t < s:
                print('Daha büyük bir sayı deneyiniz.')
        if y == 1 :
            print(f'Oyun bitti. Doğru sayı: {s}')
            print('Yeni oyun başlıyor...\n')
            break
