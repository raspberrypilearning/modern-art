## Dikdörtgenlerle modern sanat eseri yaratın

Şimdi farklı boyut ve renklerde çok sayıda dikdörtgen çizerek modern bir sanat eseri yaratalım.

+ İlk önce aşağıdaki kodu, kaplumbağa sanatınızdan sonra ekranı temizleyen ve kaplumbağayı her zamanki baktığı yöne alan, meydan okuduğunuz kodlamanın en altına ekleyin:
    
    ![ekran görüntüsü](images/modern-reset.png)

+ Kaplumbağa sanatı kodunuzun her satırının başına `#` işareti ekleyerek onu yorum haline getirebilirsiniz böylece dikdörtgen sanatı üzerinde çalışırken bu şekildeki kodlar çalışmayacak ve işlevsiz hale gelecektir. (Sonrasında bu işaretleri kaldırarak tüm çalışmanızı gösterebilirsiniz.)
    
    ![ekran görüntüsü](images/modern-comment.png)

+ Şimdi rastgele bir yerde, rastgele boyutlu, rastgele renkli dikdörtgen çizmek için bir işlev ekleyelim!
    
    Diğer işlevlerinizden sonra bir `drawrectangle()` işlevi ekleyin:
    
    ![ekran görüntüsü](images/modern-rect-function.png)
    
    Eğer zamandan tasarruf etmek istiyorsanız bazı yardımcı kodlamalar için `snippets.py` dosyasının içine bakın.

+ Yeni işlevinizi çağırmak için aşağıdaki kodu `main.py` kod bloğunuzun en sonuna ekleyin:
    
    ![ekran görüntüsü](images/modern-call-rect.png)
    
    Yükseklik ve genişlik değişikliğini görmek için komut dosyanızı birkaç kez çalıştırın.

+ Dikdörtgen her zaman aynı renkte ve aynı yerde başlıyor.
    
    Şimdi kaplumbağayı rastgele bir renge ayarlamanız ve ardından rastgele bir yere taşımanız gerekir. Hey, zaten bunu yapmak için işlevler oluşturmamış mıydın? Harika. Öyleyse bunları sadece dikdörtgen çiz fonkiyonundan önce çağırabilirsin:
    
    ![ekran görüntüsü](images/modern-random-rect.png)
    
    Vay canına bu çok daha az iş gerektirdi ve okuması çok daha kolay oldu.

+ Şimdi `drawrectangle()` işlevini bir döngü içinde çağırarak biraz daha havalı modern sanat eseri oluşturalım:
    
    ![ekran görüntüsü](images/modern-rect-art.png)

+ Tanrım, bu biraz yavaştı değil mi! Neyse ki turtle modülünü hızlandırabilirsin.
    
    'Kaplumbağa' şeklini ayarladığın kod satırını bul ve vurgulanmış kodu ekle:
    
    ![ekran görüntüsü](images/modern-speed.png)
    
    `speed(0)` değeri en hızlısıdır ya da 1 (yavaş) ile 10 (hızlı) arasında bir sayı kullanabilirsin. Hoşuna gidecek hızı bulana kadar deneyimle.