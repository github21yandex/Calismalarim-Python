

metin ="""Pratiklik açısından bakarsak, append() metodununu kullanmanın + "işlecini kullanmaya
kıyasla daha kolay olduğunu herhalde kimse reddetmeyecektir. Bu iki yöntem işleyiş
bakımından da birbirinden ayrılıyor. Zira + işlecini kullandığımızda listeye yeni bir öğe
eklerken aslında liste adlı başka bir liste daha oluşturmuş oluyoruz. Hatırlarsanız önceki
bölümlerde listelerin değiştirilebilir (mutable ) veri tipleri olduğunu söylemiştik. İşte append()
metodu sayesinde listelerin bu özelliğinden sonuna kadar yararlanabiliyoruz. + işlecini
kullandığımızda ise, orijinal listeyi değiştirmek yerine yeni bir liste oluşturduğumuz için, sanki
listelere karakter dizisi muamelesi yapmış gibi oluyoruz. Gördüğünüz gibi, listeye append()
metodunu uyguladıktan sonra bunu bir değişkene atamamıza gerek kalmıyor. append()
metodu orijinal liste üzerinde doğrudan değişiklik yapmamıza izin verdiği için daha az kod
yazmamızı ve programımızın daha performanslı çalışmasını sağlıyor.
Python3, Python2’ye göre hem çok daha güçlüdür, hem de Python2’nin hatalarından
arındırılmıştır. Python3’teki büyük değişikliklerden ötürü, Python2 ile yazılmış bir program
Python3 altında çalışmayacaktır. Aynı durum bunun tersi için de geçerlidir. Yani Python3
kullanarak yazdığınız bir program Python2 altında çalışmaz.
Dediğimiz gibi, piyasada Python2 ile yazılmış çok sayıda program var. İşte bu sebeple Python
geliştiricileri uzun bir süre daha Python2’yi geliştirmeye devam edecek. Elbette geliştiriciler
bir yandan da Python3 üzerinde çalışmayı ve bu yeni seriyi geliştirmeyi sürdürecek.
Farklı Python serilerinin var olmasından ötürü, Python ile program yazarken hangi seriye
ait sürümlerden birini kullandığınızı bilmeniz, yazacağınız programın kaderi açısından büyük
önem taşır.
Dediğimiz gibi, şu anda piyasada iki farklı Python serisi var: Python3 ve Python2. Peki acaba
hangi seriye ait bir sürümü öğrenmelisiniz?
[Kısa cevap]
Python3’ü öğrenmelisiniz.
[Uzun cevap]
Eğer Python programlama diline yeni başlıyorsanız Python3’ü öğrenmeniz daha doğru
olacaktır.
Ama eğer Python programlama dilini belirli bir proje üzerinde çalışmak
üzere öğreniyorsanız, hangi sürümü öğrenmeniz gerektiği, projede kullanacağınız yardımcı
modüllerin durumuna bağlıdır.
Zira şu anda piyasada bulunan bütün Python
modülleri/programları henüz Python3’e aktarılmış değil.
Eğer projenizde kullanmayı planladığınız yardımcı modüller halihazırda Python3’e
aktarılmışsa Python3’ü öğrenebilirsiniz. Ancak eğer bu modüllerin henüz Python3 sürümü
çıkmamışsa sizin de Python2 ile devam etmeniz daha uygun olabilir. Ama her halükarda
Python3’ün bu dilin geleceği olduğunu ve günün birinde Python2’nin tamamen tedavülden
kalkacağını da aklınızın bir köşesinde bulundurun.
Python’ı root haklarıyla kurduğunuzda Python /usr dizini altına kurulacaktır. Ancak siz
yetkisiz kullanıcı olduğunuz için /usr dizinine herhangi bir şey kuramazsınız. İşte bu yüzden,
configure betiğine verdiğimiz –prefix parametresi yardımıyla Python’ı, yazma yetkimiz olan
bir dizine kuruyoruz. Mesela yukarıdaki komut Python’ın /usr dizinine değil, ev dizininiz içinde
python adlı bir klasöre kurulmasını sağlayacaktır. Elbette siz python yerine farklı bir dizin
adı da belirleyebilirsiniz. Burada önemli olan nokta, –prefix parametresine vereceğiniz dizin
adının, sizin yazmaya yetkili olduğunuz bir dizin olmasıdır.
Bu komutu çalıştırdıktan sonra make komutunu normal bir şekilde veriyoruz. Bunun ardından
da make install (veya duruma göre make altinstall) komutuyla Python’ı ev dizinimize
kuruyoruz. Burada make install komutunu sudo‘suz kullandığımıza dikkat edin. Çünkü,
dediğimiz gibi, siz yetkili kullanıcı olmadığınız için sudo komutunu kullanamazsınız.
Python’ı bu şekilde ev dizininiz altında bir klasöre kurduğunuzda Python ile ilgili bütün
dosyaların bu klasör içinde yer aldığını göreceksiniz. Bu klasörü dikkatlice inceleyip neyin
nerede olduğuna aşinalık kazanmaya çalışın. Eğer mümkünse root hakları ile kurulmuş bir
Python sürümünü inceleyerek, dosyaların iki farklı kurulum türünde nerelere kopyalandığını
karşılaştırın.
Böylece Python programlama dilini bilgisayarımıza nasıl kuracağımızı öğrenmiş olduk.
Ama bu noktada bir uyarı yapmadan geçmeyelim: Python özellikle bazı GNU/Linux
dağıtımlarında pek çok sistem aracıyla sıkı sıkıya bağlantılıdır. Yani Python, kullandığınız
dağıtımın belkemiği durumunda olabilir. Bu yüzden Python’ı kaynaktan derlemek bazı
riskler taşıyabilir. Eğer yukarıda anlatıldığı şekilde, kaynaktan Python derleyecekseniz, karşı
karşıya olduğunuz risklerin farkında olmalısınız. Ayrıca GNU/Linux üzerinde kaynaktan
program derlemek konusunda tecrübeli değilseniz ve eğer yukarıdaki açıklamalar size kafa
karıştırıcı geliyorsa, mesela ‘Ben bu komutları nereye yazacağım?’ diye bir soru geçiyorsa
aklınızdan, kesinlikle dağıtımınızla birlikte gelen Python sürümünü kullanmalısınız. Python
sürümlerini başa baş takip ettiği için, ben size Ubuntu GNU/Linux’u denemenizi önerebilirim.
Ubuntu’nun depolarında Python’ın en yeni sürümlerini rahatlıkla bulabilirsiniz. Ubuntu’nun
resmi sitesine ubuntu.com adresinden, yerel Türkiye sitesine ise forum.ubuntu-tr.net
adresinden ulaşabilirsiniz. Eğer şu anda kullandığınız GNU/Linux dağıtımından vazgeçmek
istemiyorsanız, sabit diskinizden küçük bir bölüm ayırıp bu bölüme sadece Python
çalışmalarınız için Ubuntu dağıtımını da kurmayı tercih edebilirsiniz.
Yalnız küçük bir uyarı daha yapalım. Kaynaktan kurulum ile ilgili bu söylediklerimizden,
Python’ın GNU/Linux’a kesinlikle kaynaktan derlenerek kurulmaması gerektiği anlamı
çıkmamalı. Yukarıdaki uyarıların amacı, kullanıcının Python’ı kaynaktan derlerken sadece
biraz daha dikkatli olması gerektiğini hatırlatmaktır. Örneğin bu satırların yazarı, kullandığı
Ubuntu sisteminde Python3’ü kaynaktan derleyerek kullanmayı tercih ediyor ve herhangi bir
problem yaşamıyor.
Bu önemli uyarıları da yaptığımıza göre gönül rahatlığıyla yolumuza devam edebiliriz.
Kurduğumuz yeni Python’ı nasıl çalıştıracağımızı biraz sonra göreceğiz. Ama önce Windows
kullanıcılarının Python3’ü nasıl kuracaklarına ' bakalım."""

metin.replace("-", " ", len(metin))
silinecek = ",.;:<>+*!^$%&\'’‘()=?_/+{[]}\""

temp = ""

for i in metin:
    if i not in silinecek:

        if i == "I":
            temp += "ı"
        
        if i == "İ":
            temp += "i"
        else:
            temp += i.lower()

    elif i in "-\'’‘\\":
        temp += " "

    else:
        pass




sozluk ={}

for j in temp.split(sep = "\n"):
    for i in j.split(sep = " "):
        if i in sozluk:
            sozluk[i] = sozluk[i] + 1
        else:
            sozluk[i] = 1


try:
    sozluk.pop("")
except:
    pass


kelimeler = [["#",0],["#",0],["#",0],["#",0],]


for anahtar, deger  in sozluk.items():

    if deger >= kelimeler[0][1]:

        kelimeler[3]=kelimeler[2]
        kelimeler[2]=kelimeler[1]
        kelimeler[1]=kelimeler[0]
        kelimeler[0]=[anahtar,deger]

    elif deger >= kelimeler[1][1]:
        kelimeler[3]=kelimeler[2]
        kelimeler[2]=kelimeler[1]
        kelimeler[1]=[anahtar,deger]

    elif deger >= kelimeler[2][1]:
        kelimeler[3]=kelimeler[2]
        kelimeler[2]=[anahtar,deger]

    elif deger >= kelimeler[3][1]:
        kelimeler[3]=[anahtar,deger]

    else:
        pass

    



print(*kelimeler)
    
        
