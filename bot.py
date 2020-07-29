#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import os
import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from telegram import ReplyKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")

update_id = None


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
     # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

     # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("yardim", start))
    dp.add_handler(CommandHandler("NedenGtu", nedenGtu))
    dp.add_handler(CommandHandler("ArastirmaOlanaklari", arastirmaOlanaklari))
    dp.add_handler(CommandHandler("MuhendisNedir", muhendisNedir))
    dp.add_handler(CommandHandler("BilgisayarMuhendisi", bilgisayarMuhendisi))
    
    dp.add_handler(CommandHandler("KimlerBMOlabilir", kimlerBMOlabilir))
    dp.add_handler(CommandHandler("EgitimSureci", egitimSureci))
    dp.add_handler(CommandHandler("CalismaOrtami", calismaOrtami))
    dp.add_handler(CommandHandler("BMIsImkanlari", isImkanlari))
    dp.add_handler(CommandHandler("GorevTanimlari", gorevTanimlari))

    dp.add_handler(CommandHandler("EgitimKadrosu", egitimKadrosu))
    dp.add_handler(CommandHandler("Lablar", lablar))
    dp.add_handler(CommandHandler("Burs", burs))
    dp.add_handler(CommandHandler("GTUIsImkanlari", gTUIsImkanlari))
    dp.add_handler(CommandHandler("Ulasim", ulasim))
    dp.add_handler(CommandHandler("Barinma", barinma))
    
    dp.add_handler(CommandHandler("Erasmus", erasmus))
    dp.add_handler(CommandHandler("Kulupler", kulupler))
    dp.add_handler(CommandHandler("OgrenciykenCalisma", ogrenciykenCalisma))
    dp.add_handler(CommandHandler("Basarilar", basarilar))
    dp.add_handler(CommandHandler("CiftveYanDal", ciftveYanDal))
    dp.add_handler(CommandHandler("EgitimDili", egitimDili))
    dp.add_handler(CommandHandler("Akreditasyon", Akreditasyon))
    dp.add_handler(CommandHandler("YurtDisi", YurtDisi))
    dp.add_handler(CommandHandler("KykYurt", KykYurt))
    dp.add_handler(CommandHandler("YapayZeka", YapayZeka))
    dp.add_handler(CommandHandler("YatayGecis", YatayGecis))
    dp.add_handler(CommandHandler("NasilBilgisayar", NasilBilgisayar))
    dp.add_handler(CommandHandler("HangiDiller", HangiDiller))
    dp.add_handler(CommandHandler("Siralama", Siralama))
    dp.add_handler(CommandHandler("KacYildaMezun", KacYildaMezun))
    dp.add_handler(CommandHandler("MuallimKoyKYK", MuallimKoyKYK))





    dp.add_handler(CommandHandler("PuanYetmiyor",puanYetmiyor))
    dp.add_handler(CommandHandler("UzmanlikAlanBelgesi", uzmanlikAlanBelgesi))
    dp.add_handler(CommandHandler("YokAtlas", yokAtlas))
    dp.add_handler(CommandHandler("GirisimciDestekleri", girisimciDestekleri))
    dp.add_handler(CommandHandler("IsBulmaOranlari", isBulmaOranlari))
    dp.add_handler(CommandHandler("KampusFotolari", kampusFotolari))
    dp.add_handler(CommandHandler("HangiBolumuSecmeliyim", hangiBolumuSecmeliyim))
    dp.add_handler(CommandHandler("GrupKurallari", grupKurallari))
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    PORT = int(os.environ.get('PORT', '8443')) 
    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN) 
    updater.bot.set_webhook("https://gtu-bilmuh-bot-2020.herokuapp.com/" + TOKEN) 
    updater.idle()

    # Start the Bot
    # updater.start_polling()
    # updater.idle()
   
def start(bot, update):
    update.message.reply_text(
        "Gebze Teknik Universitesi Bilgisayar Muhendisligi Botuna Hos Geldiniz.\
        \n /NedenGtu - Neden GTU Secmeliyim?\
        \n /MuhendisNedir - Mühendis Nedir?\
        \n /BilgisayarMuhendisi - Bilgisayar Mühendisi Nedir?\
        \n /KimlerBMOlabilir - Kimler Bilgisayar Mühendisi Olabilir?\
        \n /EgitimSureci - Eğitim Süreci\
        \n /CalismaOrtami - Çalışma ve İş Ortamları\
        \n /BMIsImkanlari - İş İmkanları\
        \n /GorevTanimlari - Görev ve İş Tanımları\
        \n /EgitimKadrosu - Eğitim Karosu\
        \n /Lablar - Araştıma Labratuarları\
        \n /ArastirmaOlanaklari - Araştırma Olanakları\
        \n /Burs - Burslar\
        \n /Barinma - Yurt Olanakları\
        \n /GTUIsImkanlari - GTU İş İmkanları\
        \n /Ulasim - Ulaşım\
        \n /Erasmus - Erasmus\
        \n /OgrenciykenCalisma - Öğrenciyken Çalışma\
        \n /Kulupler - Okulumuz Öğrenci Kulüpleri Hakkında\
        \n /Basarilar - Başarılarımız\
        \n /CiftveYanDal - Çift Dal ve Yan Dal Olanakları\
        \n /EgitimDili - Eğitim Dili\
        \n /YurtDisi - Yurt Dışında Doktora yapan eski mezunumuzdan\
        \n /Akreditasyon - Akreditasyon ve GTÜ hakkında\
        \n /YatayGecis - Yatay Geçişle İlgili Sorular\
        \n /KykYurt - KYK ve Genel Olarak Barınma için sorulan sorular\
        \n /YapayZeka - Yapay Zeka Nedir?\
        \n /HangiDiller - Bilgisayar bilmeden gelebilir miyim ? Hangi Programlama dilleri lazım\
        \n /NasilBilgisayar - Nasil Bilgisayar almalıyım ?\
        \n /UzmanlikAlanBelgesi - Diplomanın yanında herhangi bir ek belge veriliyor mu?\
        \n /YokAtlas - YÖK Atlas neden önceki yıllara ait başarı sıranızı göstermiyor? \
        \n /PuanYetmiyor - Puanım yetmiyor , GTU istiyorum ne yapmalıyım ? \
        \n /GirisimciDestekleri - Üniversitenin girişimci desteği var mı? \
        \n /MuallimKoyKYK - MuallimKoy Yurdu ile ilgili bilgiler \
        \n /IsBulmaOranlari - Mezunlarınızın iş bulma oranları ve süreleri nelerdir?\
        \n /KampusFotolari - Kampüsümüzden görüntüler\
        \n /HangiBolumuSecmeliyim - Bilgisayar Mühendisliğini mi seçmeliyim, XXXX Mühendisliğini mi seçmeliyim??\
        \n /Siralama - Yusuf Hoca'nın sıralama ile ilgili tahmin aralığı\
        \n /KacYildaMezun - Bilgisayar Mühendisliğinin meşhur zorluğu ile ilgili hocalarımızdan son senelerde ki pozitif değişme hakkında \
        \n /GrupKurallari - Grubumuzun ufak kuralları \
        \n Adayları Bilgilendirme Grubu - https://t.me/GTU_CSE_2020")
 
def welcome(bot, update):
    for new_user_obj in update.message.new_chat_members:
        chat_id = update.message.chat.id
        new_user = ""
        try:
            new_user = "@" + new_user_obj['username']
        except Exception as e:
            new_user = new_user_obj['first_name'];

        WELCOME_MESSAGE = "Merhaba " + str(new_user) + ", Gebze Teknik Universitesi Bilgisayar Muhendisligi Grubuna Hos Geldin! Bize kendini tanitmak ister misin? Seni tanimaktan memnuniyet duyariz 🙂. Ayrica merak ettigin konularda bilgi almak icin botumuzu 🤖 buradan @GTUBilMuh2020Bot ziyaret edebilirsin veya  telefonla aranıp birebir iletişime geçilmesini istiyorsan bit.ly/gebzetanıtım sitesinden bilgilerini girebilirsin."

        bot.sendMessage(chat_id=chat_id, text=WELCOME_MESSAGE)

def NasilBilgisayar(bot, update):
    
    update.message.reply_text('Bilgisayar mühendisliğinde lisans eğitiminde bitirme projeniz haricinde çok ağır işlemler yapılmamaktadır. Bilgisayarınızın çok güçlü olmasından çok hafif ve taşınabilir olması daha önemlidir. Ekran çözünürlüğünün gözünüzü ağrıtmaması gece ödev yaparken size fayda sağlayacaktır.\
            i5 işlemcisi olan 8GB ram ve SSD(şart değil) içeren bir laptop işinizi görecektir.Ailelerinizi bu konuda ağır yük altına sokmamanız daha yararlı olacaktır çok güç gerektiren derin öğrenme ağları vb gibi işlemlerde okulun imkanlarını kullanabilirsiniz.')

def nedenGtu(bot, update):
    
    update.message.reply_text('GTU konumu itibari ile GOSB, TÜBİTAK Serbest Bölge, KOSGEB ve benzeri bir çok AR-GE Merkezi alanında bulunmaktadır. Bu durum staj, mezuniyet öncesi ve sonrası iş olanakları sağlamaktadır. İstanbul’a yakın olması nedeniyle İstanbul’da ikamet etme ve çalışma olanağı sağlamaktadır. Öğrencilere yaptırılan projelerle sadece teorik bilgide kalmayan bunun yanında saha tecrübesi kazandıran bir eğitim verilmektedir.')

def Siralama(bot, update):
    
    update.message.reply_text('Yusuf Sinan Akgül hocanın 2020 sıralama tahmini ile ilgili yazdığı yazı şöyledir \n https://t.me/GTU_CSE_2020/252')

def KacYildaMezun(bot, update):
    
    update.message.reply_text('Bu arada geçen sen bölümümüzün ortalama mezuniyet süresi 5.6 yıldı. Buna göre gelen kadar mezun olan var ama bazıları geç mezun oluyor.Mezun olma süresi Bugünlerde durum daha iyi olabilir çünkü son 4-5 yıldır öğrencilerin bölüme sahip olma seviyeleri artmaya başladı. Ama sonuç olarak GTÜ içerisinde mezun olma süresi BMden daha uzun bölüm olduğunu sanmıyorum. Bu istenilen bir durum değil tabi ki ama bu rakamı düşük tutmak için ders kalitesinden taviz vermemiz mümkün değil.')

def HangiDiller(bot, update):
    
    update.message.reply_text('Bilgisayar Mühendisliği lisans eğitimi boyunca C,C++,Java,Python,LISP,C#,Assembly(Makine Dili) gibi programlama dilleri gösterilmektedir.Onceden bilgisayar hakkında bir bilgi sahibi olmanıza gerek yoktur derslerinize zamanıda calisirsaniz dersleri geçebilecek kadar bilgi almaktasınız.')

def MuallimKoyKYK(bot, update):
    
    update.message.reply_text('Gebze Muallimköy KYKdan biraz bahsetmek gerekirse en başta ülkemizdeki diğer KYK lara göre gayet iyi durumda olduğunu söyleyebiliriz. Yurdun kapasitesi yaklaşık 1000 kişilik ve ücreti aylık 280 liradır. Odaları 3 kişilik, banyo mutfak ve tuvalet odanın içindedir. Odaların hepsi balkonlu ve birçoğu deniz manzaralıdır. Yurdun bir adet kantini, kütüphanesi ve sosyal tesisi bulunmaktadır. Akşamları arkadaşlarınızla kantinde vakit geçirebilir ders çalışmak için kütüphaneyi kullanabilirsiniz. Kütüphanenin normal zamanlarda yeterli, final ve vize zamanı yetersiz geldiğini söyleyebilirim. Bunun yanı sıra sosyal tesislerde birçok kurs verilmekte. Gitar kursundan işaret diline, Almancadan çizim dersine kadar birçok kurstan faydalanabilirsiniz.Yurdun çevresinde temel ihtiyaçlarınızı giderebileceğiniz 2 adet market bulunmakta.Ek olarak bir tane çiğköfteci ve kıraathane den başka bir şey yok ama zaten belediye otobüsüyle Gebze Center a 20 dakika sürüyor. Yurdun dezavantajlarına gelecek olursak birincisi ulaşım. Yurttan okula özel servis ve belediye otobüsüyle ulaşabilirsiniz. Özel servis ile ulaşım 15 dakika sürmekte ve her saat servis bulunmakta fakat aylık 200 lira civarı ve her sene zamlanıyor. Belediye otobüsünde ise sabahları 3 tane akşamları 1 tane express bulunmakta. Express ile ulaşım da 15 dakika sürmekte fakat sıra bekleme ve kalabalık gibi problemler ortaya çıkabiliyor. Bunun dışındaki saatlerde 20 dakikada bir normal belediye otobüsleri var ve ortalama 50-55 dakika sürüyor. Ücreti ise bir öğrenci basımı 1.60 TL. Haftasonları ise belediye otobüsleri saatte bire özel servisler ise günde 3 taneye düşüyor. Diğer bir dezavantaj ise yedekler mevzusu. Erkeklerde ilk 40-50 yedek ilk bir ay içinde yerleşebiliyor fakat sonrasının çıkması 2. Dönemi bulabiliyor. Kızlarda ise bu durum çok daha yavaş ilerliyor ve hiç çıkmama durumu olabiliyor. Bu yüzden yedeklerde çok geride olan arkadaşların alternatif çözümler bulmasını tavsiye ediyorum.')

def arastirmaOlanaklari(bot, update):
    
    update.message.reply_text('Bilgisayar Mühendisliği bölümü olarak 11 adet laboratuvar ile araştırma çalışmalarını sürdürmekteyiz.\
            \n Ağ ve Bilgi Güvenliği Laboratuvarı \
            \n Bilgisayar Ağları Laboratuvarı \
            \n Bilgisayarla Görme Laboratuvarı \
            \n Çizge Teorisi ve Ağ Optimizasyonu Laboratuvarı \
            \n İnsan Bilgisayar Etkileşimi Laboratuvarı \
            \n Kablosuz Araştırma Laboratuvarı\
            \n Robotik ve Kontrol Laboratuvarı \
            \n Bilgisayar Ağları Laboratuvarı \
            \n Simulasyon ve Savunma Teknolojileri Laboratuvarı \
            \n Veri Madenciliği Laboratuvarı \
            \n Yüksek Başarımlı Hesaplama Laboratuvarı \
            \n Otonom Araç Laboratuvarı \
            \n Çalışma alanlarımız hakkında detaylı bilgi alabilmek için  : http://www.gtu.edu.tr/kategori/109/0/display.aspx?languageId=1 ')

def muhendisNedir(bot, update):
    
    update.message.reply_text('Mühendis; karmaşık yapıları, makineleri, ürünleri ve sistemleri tasarlayan, üreten ve test eden kişidir. Sistemlerin en verimli şekilde hizmet etmesi için gereksinimleri göz önüne alarak yeni yöntemler geliştirir.')

def bilgisayarMuhendisi(bot, update):
    
    update.message.reply_text('Bilgisayar Mühendisliği bilgisayar bilimleri ve elektronik-elektronik mühendisliği gibi birçok alanı birleştiren bir disiplindir. Bilgisayar Mühendisi çeşitli problemlere çözüm sağlamak amacı ile bilgisayardonanımı ve yazılımı içeren bilgi sistemlerinin analiz, tasarım, test ve geliştirme süreci ile ilgilenir.')

def kimlerBMOlabilir(bot, update):
    
    update.message.reply_text('Analitik problem çözme yeteneğine sahip, problemi doğru ve verimli bir şekilde çözmeye istekli, problem çözmede sabırlı ve hırslı davranan, teknolojiye ilgisi olan kişiler bilgisayar mühendisi olabilirler.')

def egitimSureci(bot, update):
    
    update.message.reply_text('Öğrencilere temel mühendislik disiplinleri olan programlama dilleri, bilgisayar mimarisi ve donanımı, veri yapıları, algoritmalar, işletim sistemleri, iletişim ağları ve kuramsal temellerin yanı sıra bilgisayar mühendisliği alanlarında özelleşmelerini sağlayan dersler verilmektedir.\
        \n GTU Bilgisayar Mühendisliği Bölümü, öğrencilerine üç farklı alandan birinde uzmanlaşma imkânı sunmaktadır.Öğrencilerin bir alanda uzmanlaşmaları profesyonel kariyerlerinde (özellikle iş hayatına atacakları ilk adımda) daha başarılı olmalarına yardımcı olacaktır. Öğrenciler aşağıdaki alanlardan ilgilerine göre bir tanesi seçerek başarıyla bitirdikleri takdirde ‘Uzmanlık Alanı Sertifikası’ almaya hak kazanacaklardır.\
        \n Detaylar için aşağıdaki sayfaları ziyaret edebilirsiniz. \
        \n Uzmanlık alan dersleri icin http://www.gyte.edu.tr/Files/UserFiles/85/kaynaklar/alandersleri.pdf ulaşabilirsiniz. \
        \n Tum dersler icin http://www.gtu.edu.tr/%20http:/anibal.gyte.edu.tr/ects/?dil=tr&amp;duzey=ucuncu&amp;modul=lisans_derskatalogu&amp;bolum=104&amp;tip=lisans ')


def calismaOrtami(bot, update):
    
    update.message.reply_text('Bilgisayar Mühendislerinin tek bir alanda çalıştığını söylemek zordur. Çünkü Bilgisayar mühendisleri yönetim, endüstri ve hizmet alanlarında değişik görevler üstlenebilirler. Günümüzde birçok meslek gibi; bilgisayar mühendisleri, genellikle yazılım ve donanım mühendisi olarak ofislerde ve araştırma-geliştirme laboratuvarlarda çalışmaktadırlar. Genellikle sessiz bir ortamda çalışmaktadırlar. Pazarlama alanında çalışanlar beraber çalıştıkları diğer ortamlarla etkileşim halinde olup daha sosyal bir iş ortamına sahiptirler. İş analistleri ise sahada gözlemler yapar. Akademisyenliği tercih eden bilgisayar mühendisleri bunlara ek olarak dersliklerde de görev yapabilmektedirler. Bilgisayar mühendisi çalışırken diğer meslektaşlarıyla ve iş sahipleriyle etkileşim halindedir.')

def isImkanlari(bot, update):
    
    update.message.reply_text('Bilişim teknolojileri hızla gelişmekte ve günümüzde sağlık, eğitim, haberleşme, savunma, eğlence ve bankacılık gibi birçok alanda önemli bir yere sahip olmaktadır. Bu nedenle Bilgisayar Mühendisliği bölümü birçok alanda iş bulma kolaylığı sunmaktadır. Çalışanlarının büyük bir bölümü bilgisayar mühendislerinden oluşan ve temel işi mühendislik olan yazılım şirketlerinde, farklı alanlarda çalışan birçok şirketin bilişim bölümlerinde, devlet bünyesinde proje odaklı çalışan araştırma-geliştirme bölümlerinde, kamu sektöründe ve üniversitelerde bilgisayar mühendisliği bilgisayar mühendisi istihdam edilmektedir. Bilgisayar mühendisleri birçok mesleğe kıyasla yüksek rağbet görmektedirler ve yüksek ücretler alırlar. Buna bağlı olarak iş değiştirme oranları bilgisayar mühendislerinde yüksek seviyelerdedir ve işsiz kalma süreleri oldukça azdır. Özellikle devletin de desteklediği bir çok kobi projesiyle ile kendi girişimlerini kurabilme şansları da bilgisayar mühendislerinin yüksek kazanç elde edebilmelerine olanak sağlamaktadır.')

def KykYurt(bot, update):
    
    update.message.reply_text('Kyk yurduna çıkma ihtimali zor mudur? = Değildir KYK yurtlarında yer bulunmaktadır 3 kişilik odalara getirildi kontenjan artırılması için. Kyk Yurtları dışında Şifa mahallesi öğrencie evleri 2+1/3+1 650-750 lira arasındadır.\
            KYK yurdundan devlet otobüsyle ulaşım 45 dakika sürmekte ve aylık 70-80 lira tutmaktadır. Özel servis ile ulaşım 15 dakika sürmekte ve ücreti 150-160 lira arası değişmektedir.')
def YapayZeka(bot, update):
    
    update.message.reply_text('Yapay Zeka nedir? Yapay zekâ, bir bilgisayarın veya bilgisayar kontrolündeki bir robotun çeşitli faaliyetleri zeki canlılara benzer şekilde yerine getirme kabiliyeti.İngilizce artificial intelligence kavramının akronimi olan AI sözcüğü de bilişimde sıklıkla kullanılır. Yapay zekâ çalışmaları genellikle insanın düşünme yöntemlerini analiz ederek bunların benzeri yapay yönergeleri geliştirmeye yöneliktir.\
        Okulumuzda neredeyse tüm hocalarımız yapay zekanın bir alanında çalışma yapmış ve yapmaya devam etmektedirler.Çalışma konuları arasında Makine Zekası,Yapay Sinir Ağları,Doğal Dil İşleme,\
        Konuşma Sentezi,Uzman Sistemler,Örüntü Tanıma,Genetik Algoritmalar,Bulanık Mantık,Pekiştirmeli Öğrenme gibi alanlar bulunmaktadır.Çalışma alanlarıyla ilgili detaylı video için \
            https://www.youtube.com/watch?v=ZJixNvx9BAc izleyebilirsiniz')

def gorevTanimlari(bot, update):
    
    update.message.reply_text('Sistem Çözümleyici: Bilgi işlem sistemlerini kuran ve yeni bilgi toplayan, sistemlerin kurulmaları ve çalışmaları için gerekli yöntemleri tanımlayan, kurulumlarını yapan, denetleyen ve gelişmeleri için önerilerde bulunan nitelikli kişidir. \
        \n*Sistem Programcısı*: Bilgisayarın sistem yazılımını tasarlayan, programlayan ve bakımını yapan, yapımcı firma tarafından verilen yazılımı inceleyerek gerekli optimum yapıyı kararlaştıran, yapımcının yazılımda yaptığı değişiklikleri inceleyerek mevcut işletim sistemleri, sistem tasarımı, programlama ve işletme yöntemlerine etkilerini belirleyen, yeni yada değiştirilmiş yazılımları kurmadan önce deneyerek sistem yazılımının kullanımı ve uygulama programlarına bağlantısı konularında sistem çözümleyicilere ve programcılara yol gösteren kişidir. \
        \nUygulama Programcısı: Programın mantığını tasarlayan, deneyen ve hazır hale getirerek bilgiyi işlemek için gerekli olan program akış şemalarını ve alt programları hazırlayan, dizi ve kütük gereksinimlerinin belirlenmesi için sistem tasarımcısına yardımcı olan, programlama standartlarına göre tamamlanmış olan programların işlemesini ve diğer programlara bağlantısını deneyen nitelikli kişidir.  \
        \nVeri Tabanı Yöneticisi: Bir veri tabanı yöneticisi mantıksal data modelleme, fiziksel veritabanı dizaynı çıkarma, fiziksel olarak veritabanı oluşturma, güvenlik yönetimi ve konfigürasyonu, veritabanı yönetimi ve bakımı, veritabanı denetleme ve optimize etme işlerini üstlenir.\
        \nVeri İletişim Uzmanı: Veri madenciliği ile ilgilenen, büyük verilerin daha efektif nasıl kullanılabileceği sorusuna çözümler geliştiren ve bunları raporlayan uzmanlardır.\
        \nBilgi İşlem Yöneticisi: Çalışanlar için gereken yazılım, donanım ve network araçlarının oluşturulması, kurulumu, yönetimi ve bakımı gibi işler ile ilgilenir.\
        \nEğitmen: Üniversitelerde yeni bilgisayar mühendislerinin yetişmesi için çalışırlar.\
        \nDanışman: Şirketlere bilişim teknolojileri ile ilgili gerekli konularda danışmanlık yaparlar.\
        \nBilgisayar Donanımı Tasarımcısı: Bilgisayarların fiziksel parçalarının tasarlanmasında ve geliştirilmesinde görev alırlar.\
        \nBilgisayar Donanımı Tasarımcısı: Bilgisayarların fiziksel parçalarının tasarlanmasında ve geliştirilmesinde görev alırlar.')

def egitimKadrosu(bot, update):
    
    update.message.reply_text('Yurtdışında eğitim almış ve farklı ekollerden gelen öğretim üyelerine sahiptir. http://www.gtu.edu.tr/kategori/98/12/display.aspx?languageId=1 linkinde detaylı bir şekilde öğretim üyelerine ait bilgiler verilmektedir.')


def lablar(bot, update):
    
    update.message.reply_text('GTÜ Bilgisayar Bölümü bünyesinde 10 farklı alanda araştırmaların yürütüldüğü araştırma laboratuvarları bulunmaktadır.\
    \nAğ ve Bilgi Güvenliği Laboratuvarı \
    \nBilgisayar Ağları Laboratuvarı \
    \nBilgisayarla Görme Laboratuvarı \
    \nÇizge Teorisi ve Ağ Optimizasyonu Laboratuvarı \
    \nİnsan Bilgisayar Etkileşimi Laboratuvarı \
    \nKablosuz Araştırma Laboratuvarı \
    \nRobotik ve Kontrol Laboratuvarı \
    \nSimülasyon ve Savunma Teknolojileri Laboratuvarı \
    \nVeri Madenciliği Laboratuvarı \
    \nYüksek Başarımlı Hesaplama Laboratuvarı\
    \nAyrıntılı bilgi için http://www.gyte.edu.tr/icerik/109/670/laboratuvarlar.aspx')


def burs(bot, update):
    
    update.message.reply_text('Net bir sayı verememekle birlikte çevredeki firmalar tarafından okul yönetiminin belirlediği öğrencilere burs imkânı sağlanmaktadır. \
        Detaylar icin: http://www.gtu.edu.tr/kategori/2460/0/display.aspx?languageId=1')

def barinma(bot, update):
    
    update.message.reply_text('Muallimköy Yerleşkesi’nin batısında Yükseköğrenim Kredi ve Yurtlar Kurumu’na tahsis edilen yerde yurdumuz 320 kız 440 erkek olmak üzere toplam 760 öğrenci kapasitesiyle hizmet vermektedir.\
        \nAyrıca üniversiteye yürüme mesafesinde öğrencilerin ev tutabileceği siteler bulunmaktadır. Aşağıdaki resimde mavi ile çizilmiş yerler İstanbul ve Gebze bölgesinde öğrencilerin yoğunlukla yaşadıkları yerlerdir.\
        \n Detaylar icin: http://www.gtu.edu.tr/kategori/2328/0/barinma-ve-yurtlar.aspx')

def gTUIsImkanlari(bot, update):
    
    update.message.reply_text('Üniversitemiz birçok Teknopark ve ARGE merkezine yakın olduğundan, bu çevredeki firmaların ilgi odağı halindedir. Birçok mezunumuz bu çevredeki firmalarda yarı-zamanlı veya tam-zamanlı olarak çalışmakta, yeni mezunlara da ön ayak olmaktadırlar.')


def ulasim(bot, update):
    
    update.message.reply_text('Ulasim imkanlarini gormek icin: http://www.gtu.edu.tr/icerik/926/629/ulasim-ve-iletisim.aspx')


def erasmus(bot, update):
    
    update.message.reply_text('Üniversitemiz Erasmus öğrenim hareketliliği programına dahildir ve en az 3 ay en fazla 12 ay olacak şekilde öğrencilere yurt dışı deneyimi, çok kültürlü ortamda ders işleme, değişik kültürleri tanıma, Türk kültürünü tanıtma, yeni arkadaşlar edinme, farklı bir okulda öğrenci olabilme ve farklı bir sistem görebilme olanakları kazandırır. GTU Bilgisayar Mühendisliği Fransa, İspanya, Almanya, Belçika, Polonya gibi bir çok farklı ülkedeki üniversitelere bu program ile öğrenciler göndermektedir.\
            Erasmus değişim programı olduğu için bölümün ile ilgili ders alıp 1 dönem veya 2 dönem farklı bir ülkede ve okulda eğitim görme fırsatı buluyorsun. Ülkede kaldığın süre zarfında gittiğin okulun eğitiminin yaninda geziyorsun farkı kültür görüyorsun, o ülkenin dilini ve kulturunu kendine katiyorsun ve büyük tecrübeler edinmiş oluyorsun. \
                    Dil konusunda gideceğin okula göre değişen bir durum oluyor bu. Bazı okullar kendi bulundukları ülkenin dilinde belirli bir seviyede olmanı isteyebiliyorlar ama bazı okullar için eğitim dilleri %100 ingilizce olduğundan dolayı sadece İngilizce yeterli olabiliyor. Benim gideceğim okulda Fransızca zorunluluğu yok mesela ben de bilmiyorum. Bu sayede hem Fransızca öğrenip kendimi geliştireceğim hem de İngilizcemi üst kademeye taşımış olacağım.\
Bunun yanında Erasmus stajı denen bir ayrı durum daha var burada da belirli bir süreliğine farklı bir ülkede stajini yapıyorsun. Bu programların hepsi devlet destekli oluyor. Gittiğin ülkeye göre ve erasmus için gireceğin sıralamana göre belirli bir miktar aylık hesaplama ile hibe aliyorsun. Genelde bizim okulda hibe almayan öğrenci kalmıyor.')


def ogrenciykenCalisma(bot, update):
    
    update.message.reply_text('GTU Bilgisayar Mühendisliği İstanbul-Kocaeli il sınırında bulunan bir üniversite olduğu için hem İstanbul hem de Kocaeli ilinde bulunan şirketlere yakınlığı nedeniyle özellikle 3.sınıftan sonra üniversite de öğrenilen bilgileri iş hayatında uygulamaya koymak isteyen öğrencilere avantaj sağlamaktadır. Öğrenciler için ders programında boş gün ve saatler ayarlanarak kısa zamanlı çalışmak isteyen öğrencilere kolaylıklar sunulmaktadır. Ayrıca bölümün dış destekli araştırma projelerinde öğrencilere çalışma fırsatları verilmektedir.')

def kulupler(bot, update):
    
    update.message.reply_text('Üniversite içinde ki kulüpler teknik kulüpler ve sosyal kulüpler olmak üzere iki alanda çalışmalarını sürdürmektedirler. \
            \n Her bölümün kendine ait topluluğu bulunmakla beraber Robotik ve Otomasyon, Havacılık ve Uzay, SEDS Uzay ve Fizik , Savunma Teknolojileri, IEEE,Sosyal Yaşam ve Medya, Latin Dans Topluluğu, Fotoğrafçılık ve Kısa Film, Siber Güvenlik,MITA gibi kulüpler ile üyelerine ders dışı vakitlerini değerlendirme olanağı sağlamaktadır.\
            \n Kulüplerin kendi içlerinde oluşturduğu topluluklar sayesinde uluslarası yarışmalara katılım ve uluslararası TEKNOFEST,TUBITAK yarışmalarına katılım sağlanmaktadır. \
            \n Havacılık ve Uzay kulübü  ve Robotik kulüpleri içerisinde oluşan Model Uydu Takımları 2018 yılından beri NASA dahil olmak üzere Amerikan ve Avrupa yarışlarına katılmaktadır. Havacılık kulübünün IHA , Model Uçak takımları 2013 yılından beri çeşitli yarışmalarda sayısız ödül kazanmıştır.  Robotik otomasyon kulübü her sene değişik alanlarda eğitimler düzenlemek ve nisan aylarında geleneksel Robot olimpiyatları düzenlemektedir. Okul içerisinde GTU Roket kulübü adlı model roketçilik kulübü bulunmakta ve Türkiye Tayyare Derneği tarafından desteklenmektedir. Otonom Araç geliştirmek üzerine kurulan GTU HAZINE OTONOM araç takımı ise birebir boyut otonom araç tasarlamak ve bu konular üzerine çalışmaktadır. IEEE olarak sosyal yardımlaşma amaçlı robotlar tasarlanmaktadır. Ayrıca bu etkinlikler yanı sıra haftalık latin dans geceleri ve fotoğrafçılık gezileri olmaktadır. ')

def basarilar(bot, update):
    
    update.message.reply_text('Basarilarimi gormek icin: http://www.gtu.edu.tr/icerik/8/4200/display.aspx?languageId=1')

def YurtDisi(bot, update):
    
    update.message.reply_text('Merhaba, ben Şeyma Yucer. GTU 2015 lisans, 2018 yüksek lisans mezunuyum. Şuan Kuzey İngilterede bulunan Durham Üniversitesinde doktora yapıyorum. Geçen yıl akreditasyonla ilgili çok fazla soru sorulduğu için kendi doktora başvuru sürecimden bahsedip, soruların akademik olan kısmına cevap vermek istiyorum. 2019 başında, İngiltere başta olmak üzere, Güney Kore, Finlandiya, Almanya gibi farklı ülkelere doktora başvurusu yaptım. Aranan şeylerin ortak olanları: IELTS, iyi bir ortalama (min. 3.00), mezuniyet derecesi, yaptığın projeler, bu projelerden çıkan yayınlar, bunları anlatabiliyor olman, mülakatlarda sorulan veri yapıları ve lineer cebir sorularına yaklaşımın ve yanıtlarını nasıl kodladığın idi. Ancak hiçbir başvurumda akreditasyon sorulmadı, başvurularımı ilerlettiğim, belgelerini tamamladığım Güney Koredeki üniversiteö ailemle ilgili nüfus kayıt noter tasdikli çeviri bile istedi ama akreditasyon istemedi. Okulun size sağlayacağı en önemli belge, İngilizce mezuniyet belgesi ve sınıf sıralama belgesi. Sıralama veriliyor lisans için, mezuniyet de İngilizce-Türkçe beraber zaten. Başvuru zamanı geldiğinde akreditasyonun sorun olmayacağını, İngilizce, not ortalaması ve veri yapılarının çok daha fazla önemli olduğunu bir kez daha adaylara belirtmek isterim')

def puanYetmiyor(bot,update):

    update.message.reply_text('GTU Bilgisayar Mühendisliğine puanım yetmiyor, üzülmeli miyim? \
             \n Arkadaşlar, GTÜ BM olarak iyi bir lisans eğitimi verdiğimize inanıyoruz, bizim programımızı bilen ve isteyen adayların tabi ki bizde öğrenci olmasını isteriz ancak alabileceğimiz öğrenci sayısı belli, aşmamız mümkün değil. Eğer puanınız bu bölüm için yetmiyorsa, üzülmeyin, \
             \n Türkiyede çok sayıda BM bölümü mevcut, araştırın, sizin istediğinize en uygun bölümü bulun ve ondan sonra yapacağınız tek şey derslerinize dikkat etmek, sürekli olarak başka kaynaklardan BMnin temelleri ve yeni gelişen teknolojileri hakkında bilgi edinmek olsun. Bunu yaparsanız, sizin ne GTÜ BMye ne de MIT CSe ihtiyacınız var, zaten iyi bir mühendis olacaksınız. Bir bölüm sizin iyi bir mühendis olmanız için bir araçtır, bölümlere kabul edilmeyi amaç olarak almayın kendinize. Ülkemizde uygulanan üniversite öğrenci seçme sistemi maalesef çok başarılı değil, sınav hazırlık süreci çok uzun ve hazırlık sürecinden elde edilen birikimlerin sonradan işe yaraması beklenmiyor. Bu sınav sonucunu kendinize sınır çekmek için kullanmayın, kendinizi diğer adaylardan daha az puan aldığınız için yetersiz görmeyin aynı şekilde yüksek puan almanız da diğerlerinden farklı olduğunuzu göstermez. Bu sınav bir üniversiteye yerleşmek için bir aşamadır. Esas çalışma, kendinizi yetiştirme, geliştirme bu aşamadan sonra başlar. GTÜ BMnin diğer üniversitelerden farklı yaptığı tek şey belki biraz fazla ödev ve proje verip, bunların yapıldığından emin olmaya çalışmasıdır. Aynı disiplini kendiniz başka üniversitelerde uygulamamanız için bir neden yok. Defalarca söylediğim gibi iş sizde bitiyor, iyi bir mühendis olmak için bölüm sadece yardımcı bir araçtır ama tek başına sizi iyi bir mühendis yapmaz. Gayret eden, sürekli araştıran ve ileride kalan birisi için hangi bölümde okuduğun çok bir önemi yoktur.')

def ciftveYanDal(bot, update):
    
    update.message.reply_text('Üniversitemiz belirli not ortalamasını sağlayan öğrencilere çift anadal ve yandal programları ile ikinci bir diploma veya sertifika olanağı sağlanmaktadır. Öğrenciler ilan edilen (Elektronik Mühendisliği, Malzeme Bilimi ve Mühendisliği gibi) yandal ve çiftanadal programına anadal lisans programının 3. ve 5. döneminde başvurabilir.')

def egitimDili(bot, update):
    
    update.message.reply_text('Bilgisayar Mühendisliğinde eğitim dili %100 İngilizcedir. Öğrenciler eğitime başlamadan önce 1 yıl İngilizce hazırlık kursu görmektedirler. İngilizceleri yeterli olan öğrenciler kursa başlamadan önce İngilizce hazırlık geçiş sınavına girerek, bu kurstan muaf olarak eğitime başlama hakkına sahiptir.')

def Akreditasyon(bot, update):
    
    update.message.reply_text('Akreditasyon alınmak üzereyken yüzde otuzdan yüzde yüz ingilizce eğitime  geçildiği için \
            Akreditasyon MÜDEK alacaktık vazgeçtik anlamlı olmadığına karar verdik şimdi ABET alınacak, ancak bunlar bizim gibi bölümler için sadece ekstra bir etiketten öteye gitmiyor. Ama işte bazı velileri tatmin ediyor.\
        Siz mezun olduğunuzda zaten birkaç yıllık ABET akreditasyonumuz olmuş olacaktır.')

def YatayGecis(bot, update):
    
    update.message.reply_text('Merhabalar ben yatay geçiş süreciyle yerleşen bir arkadaşım , merkezi yerleştirme puanı ile yatay geçiş yapacaklar için yaşadığım süreçten ve Gtü bilgisayarı neden tercih ettiğimden kısaca bahsedeceğim. Benim zamanımda Lys ve Ygs olduğu için puan türü farklı olabilir ancak MF-4 ile geçiş yapmıştım, okulun açtığı kontenjan kadar kişi puan sıralaması doğrultusunda kabul ediliyor. Benimle beraber 2015 senesinde 3 kişi daha geçiş yapmıştı yani kontenjan 4 diye düşünüyorum. Hazırlık okuma durumu-Eğer okulunuzdan geçerli bir yabancı dil belgeniz var ise yani daha önce hazırlık okuyup başarı ile geçtiyseniz burada hazırlık okumanıza gerek kalmıyor. Ancak Türkçe bir bölümden geçiyorsanız, maalesef GTÜ’de hazırlık sınavını geçmelisiniz. Ders saydırma - Okulunuzun size verdiği havuz derslerinin(Mat,Fizik,Türkçe vb.) CC ve daha üstü olanlarını geçiş yaptığınızda saydırabilirsiniz.\
    \n Yatay geçiş yaparken istenen belgeler içerisinde, önceki okulunuzdan başarı ile geçtiğiniz derslerin dökümünü çıkartmanız istenmektedir. Bölüm dersleri için ise tavsiyem, tamamını GTÜ’den almanızdır. İki üniversite görmüş biri olarak söylemeliyim ki, ders içerikleri ve niteliği çok farklı oluyor. Neden GTÜ bilgisayar -Eğitiminiz sadece derste kalmıyor, verilen ödevler ve projeler ile hem derste işlenen konu pekişmiş oluyor hem de sizi iş hayatının yoğunluğuna hazırlanmış oluyorsunuz. Belki okul eğitiminde ağırlıklı olarak console eğitimi verilse de, öğrencilerin çoğu yaz tatillerinde ya da mezun olduktan sonra web, mobil gibi popüler alanlara kolaylıkla kayabilecek yeterlilikte ve özgüvende oluyorlar.\
    \n Ayrıca öğrenciler çok rahat bir biçimde 3. ve 4. sınıfta okurken çalışabilecekleri gibi, mezun olur olmaz rahatlıkla iş bulabiliyorlar. Kötü yanları peki? -Gerçekten vaktinizin çoğunu okul alacak, bunu göze almalısınız. Ben çok hafta biliyorum, 4 ödev teslim ettiğim oldu bu da neredeyse hiçbir günün bana kalmaması anlamına geliyordu. Ayrıca okulun Gebze’de olması da bir dezavantaj olarak görülebilir ancak şanslısınız ki Marmaray açıldı :) . Nasıl Girebiliriz - \
    \n Arkadaşlar yatay geçiş her üniversiteden yapılabilir fakat 2 çeşit yatay geçiş var biri önceki seneler puanı tuttuğu halde yazmayıp sonradan geçmeyi düşünenler için(merkezi yatay geçiş) diğeri ortalama ile yatay geçiş bunun içinde belli bir ortalamanın üstünde olup başvuruyorsunuz tabi başka kriterlere de bakılabilir o dönem başvuranlar arasında listeye alınıyorsunuz eğer şartları(yaptığınız GNO,girdiğiniz sene ki sınav puanı gibi katmanların belli katsayılarla çarpılıp size puan çıkarılması) sağlarsanız ve kontenjana girerseniz geçebilirsiniz . Tüm üniversitelerde böyle bu olay , ders denklik olayı ayrı bir olay tabi')

def uzmanlikAlanBelgesi(bot, update):
    
    update.message.reply_text('GTÜ Bilgisayar Mühendisliği Bölümü öğrencilerine üç alanda uzmanlaşma imkanı sunmaktadır. Öğrenciler gerekli şartları sağlarlarsa Uzmanlık Alanı Sertifikası almaya hak kazanacaklardır. [Sistem Mühendisliği, Yazılım Mühendisliği ve Bilgisayar Ağları ve Bilgi Güvenliği]')

def yokAtlas(bot, update):
    
    update.message.reply_text('Bölümümüz 2018 yılında Ingilizce eğitime başladığı için daha önceki yıllarda elde edilen başarı sıralamaları tercih kılavuzunda yer almamaktadır. Bölümümüz başarı sıralamaları için http://www.gtu.edu.tr/kategori/1730/0/display.aspx?languageId=1 adresindeki yıllara göre başarı sıralamaları grafiğini inceleyebilirsiniz.')

def girisimciDestekleri(bot, update):
    
    update.message.reply_text('GTÜ Teknoloji Transfer Merkezi bu konuda hizmet vermektedir http://gebzettm.com/birimler/girisimcilik-ve-kulucka Ilgili haber için http://www.sanayigazetesi.com.tr/ar-ge/tirtil-girisimci-kelebege-donusuyor-h17468.html')

def isBulmaOranlari(bot, update):
    
    update.message.reply_text('Bu konuda yapılmış bazı anketlere göre Türkiye\'nin en iyileri arasındayız. Ilgili bağlantı http://calibre.kyyd.org.tr/EniyiUniversiteler.aspx')

def hocalarimizAyriliyormu(bot, update):
    
    update.message.reply_text('Hayır değil. Son 4 yıldır ayrılan bir hocamız olmadı hatta yeni hocalar aramıza katıldı.')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def grupKurallari(bot, update):
     update.message.reply_text('1) İlk olarak kendinizi lütfen tanıtınız. Aday iseniz, isim sıralama bizim için yeterlidir.\
                                \n2) Üniversite öğrencisi/görevlisi iseniz, isim sınıf veya göreviniz vs. (esktralar sizden 🙂)\
                                \n3) Üniversite mezunu iseniz, çalıştığınız kurum ve pozisyon (ekstralar sizden 🙂)\
                                \n4) Mesajlarımızı yazarken lütfen bir metin halinde gönderelim. Bir kaç kelime yazıp "enter" basmak gruptaki çalışanları düşününce çok hoş bir durum olmuyor, grubun sessize alınmasını istemeyiz 🙂\
                                \n5) Grupta profesöründen bölüm öğrencisine kadar insanlar olduğunu unutmayıp saygı ve sevgi çerçevesini bozmayalım. (Bozanlar gruptan 1. uyarıdan sonra nazikçe çıkarılacaktır.)\
                                \n6) Grupta sizleri bilgilendirmek için varız. Grup kurulduğu günden itibaren mesajları görmeniz mümkündür. Bu yüzden aratma opsiyonunu kullanarak tek kelimelik aramalar ile sorunuzun cevabına ulaşabilirsiniz. Bulamazsanız cevaplamak için buradayız zaten 🙂')

def kampusFotolari(bot,update):
    update.message.reply_text('Kampus fotolarını sitemizden görmek icin: http://www.gtu.edu.tr/kategori/2362/0/display.aspx?languageId=1 \n')

def hangiBolumuSecmeliyim(bot,update):

    update.message.reply_text("Bu soru bana çok soruluyor ve cevaplaması gerçekten çok zor. İyi bir eğitim almış bilgisayar mühendisinin hem Türkiye'de hem de yurt dışında iyi iş bulacağı herkes tarafından kabul ediliyor. Bu konuda yapılan istatistikler hep bu yönde. \
        \nFakat bu herkes bilgisayar mühendisi olmalıdır manasına gelmiyor tabi ki, eğer yetenekleriniz ve planlarınınız XXXX mühendisliği yönünde ise tabi ki XXXX mühendisi olun derim. Ancak kararınız bilinçli olmalı, iyi bir araştırmaya dayalı olmalı. Üniversite tercih aşamasında bu türlü bir kararı vermek hiç te kolay değil, bunu herkes biliyor. O nedenle bu ikilemde kalan adaylara şunu öneriyorum. Eğer bilgisayar mühendisliği ve XXXX mühendisliği arasında ikilemdeyseniz, GTÜ Bilgisayar Mühendisliği bölümünü tercih edin. \
        \nİlk yıl okuyun, size çok iyi temel mühendislik ve programlama dersleri vereceğiz. Bu arada bir bilgisayar mühendisinin ne yaptığını yavaş yavaş anlamış olacaksınız. Eğer yıl sonunda hala XXXX mühendisi olmak istiyorsanız, o zaman hemen dilekçenizi vererek merkezi yatay geçiş (http://www.yok.gov.tr/documents/7701936/7719456/yataygeci%C5%9Fpdf.pdf/) kontenjanlarından Türkiye'de istediğiniz üniversiteye yatay geçiş yapabilirsiniz, tabi ki tercih yaptığınız dönemde o bölüme YKS puanınızın yetmesi gerekiyor. \
        \nBu şekilde eğer bilgisayar mühendisi olmak isterseniz bir kaybınız olmaz, eğer XXXX olmak isterseniz, temel bilim dersleriniz yeni bölümünüzde saydırırsınız, yıl kaybınız olmaz ve sağlam C programlama ve temel bilgisayar bilginiz olur. Bu bilgiler her türlü mühendislik için gereklidir. \
        \nMerkezi yatay geçiş için herhangi bir sınırlama yok (ortalama, not ve devam durumu, sınıf, kontenjan, fakülte farkı vb.) Sadece söylediğim gibi tercih yaptığınız dönemde o bölüme YKS puanınızın yetmesi gerekiyor. Bölümüze her sene çok sayıda merkezi yatay geçiş öğrencisi geliyor ve aynı zamanda çok sayıda öğrenci de ayrılıyor. Merkezi yatay geçiş bence YÖK'ün son yıllarda devreye aldığı en güzel uygulama. Başlangıçta yapılan tercih yanlışlıklarının büyük kısmını gideriyor.")


if __name__ == '__main__':
    main()
