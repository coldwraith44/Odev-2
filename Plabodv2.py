

#liman otomasyonu
#Anıl Erdoğan Bilgisayar Mühendisliği 220501006
#Akın Turan   Bilgisayar Mühendisliği 220501013


# -*- coding: utf-8 -*-
import pandas as pd
import tkinter as tk  #Gerekli kütüphaneler eklenir
from tkinter import messagebox
from tkinter import simpledialog
from termcolor import colored

dosya=open("gemiler.csv","r")
liste1=dosya.readlines()
liste2=[]
dosya.close()
liste1=liste1[1:]

stringecevir=""



for i in liste1:

    x=i.replace("\n", " ")
    y=x.replace(",", " ")
    liste2.append(y)

for i in liste2:

    stringecevir=stringecevir+i




liste3=stringecevir.split(" ")
liste3=liste3[:-1]#Liste istediğimiz forma geldi gemiler dosyasındaki elemanlar listeye eklenerek her 4 elemanda 1 geminin bilgisinin bulunması sağlandı



dosya1=open("olaylar.csv","r")
liste4=dosya1.readlines()
dosya1.close()
liste5=[]
liste4=liste4[1:]
stringecevir1=""


for i in liste4:

    x=i.replace("\n", " ")
    y=x.replace(",", " ")
    liste5.append(y)

for i in liste5:

    stringecevir1=stringecevir1+i

liste6=stringecevir1.split(" ")
liste6=liste6[:-1]  #Aynı işlem olaylar.csv dosyası içinde gerçekleştirildi her 7 elemanda 1 tır bilgisi bulunması sağlandı





def main():



    class Gemi:                                                 #istenilen classlar oluşturuldu
        def __init__(self,ad,zaman,kapasite,gidilecek_ulke,depo):
            self.ad=ad
            self.zaman=zaman
            self.kapasite=kapasite
            self.gidilecek_ulke=gidilecek_ulke
            self.depo=depo


    class TIR:

        def __init__(self,plaka,zaman,ulke, _20_t_a_,_30_t_a_,yuk,maliyet):
            self.plaka=plaka
            self.zaman=zaman
            self.ulke=ulke
            self._20_t_a_=_20_t_a_
            self._30_t_a_=_30_t_a_
            self.yuk=yuk
            self.maliyet=maliyet




    yuk_indirme_alani1=list()       #Gereken değişkenler oluşturuldu
    yuk_indirme_alani2=list()


    tir_indirme=[]
    gemi_yukleme=[]
    sayac=0
    yuk_sayaci=0
    yuk_sayaci_2=0
    sozluk={}
    sozluk1={}
    gemi_gun_listesi=[]
    tir_gun_listesi=[]
    temizlik_listesi2=[]
    temizlik_listesi3=[]
    tir_arastirma_sozlugu={}
    gemi_arastirma_sozlugu={}
    temizlik_listesi4=[]
    gun=0


    a=0
    b=0
    sozluk2={}
    as_secim=-1


    for i in range(0,len(liste3),4):            #Döngü için gereken listeler oluşturuldu
        gemi_gun_listesi.append(liste3[i])




    for i in range(0,len(liste6),7):
        tir_gun_listesi.append(liste6[i])


    print("Liman Otomasyonu Menüsüne hoşgeldiniz")
    print("┌──────────────────────────────────────────────────────┐") #Menü Oluşturuldu
    print("│                         Menü                         │")
    print("├──────────────────────────────────────────────────────┤")
    print("│ 1-Otomasyonu Başlat                                  │")
    print("│ 2-Otomasyonu Seçtiğin Gün İle Başlat                 │")
    print("│ 3-Tır Sorgulama                                      │")
    print("│ 4-Gemi Sorgulama                                     │")
    print("│ 5-Çıkış                                              │")
    print("└──────────────────────────────────────────────────────┘")
    x6=0
    x6=input("Lütfen bir seçenek seçiniz:")
    if x6=="1":

            if len(tir_gun_listesi)>len(gemi_gun_listesi):
                as_secim=len(tir_gun_listesi)+5
            elif len(gemi_gun_listesi)>len(tir_gun_listesi):
                as_secim=len(gemi_gun_listesi)+5

    elif x6=="2":
            a7=input("Lütfen günü giriniz:")

            as_secim=int(a7)+1

    elif x6=="3":
            if tir_arastirma_sozlugu=={}:
                print("Sorgu Listesi Boş!")
            else:
                pass
    elif x6=="4":

            if gemi_arastirma_sozlugu=={}:
                print("Sorgu Listesi Boş!")
            else:
                k5=input("Gemi Adını Girin:")
                for i in gemi_arastirma_sozlugu:
                    if i==k5:
                        print(gemi_arastirma_sozlugu[i])
    elif x6=="5":
            print("İyi Günler Dileriz!")
            m1=2
    else:
            print("Böyle bir seçenek bulunmamaktadır")





    while gun<as_secim:                 #otomasyon döngüsü başladı
            sayac=0
            print(gun,".gün")
            if str(gun) in gemi_gun_listesi:

                for i in range(0,len(liste3),4):

                    if liste3[i]==str(gun):
                        gemi_yukleme.append(liste3[i])
                        gemi_yukleme.append(liste3[i+1])
                        gemi_yukleme.append(liste3[i+2])
                        gemi_yukleme.append(liste3[i+3])



            if str(gun) in tir_gun_listesi:


                for i in range(0,len(liste6),7):

                    if liste6[i]==str(gun):

                        tir_indirme.append(liste6[i])
                        tir_indirme.append(liste6[i+1])
                        tir_indirme.append(liste6[i+2])
                        tir_indirme.append(liste6[i+3])
                        tir_indirme.append(liste6[i+4])
                        tir_indirme.append(liste6[i+5])
                        tir_indirme.append(liste6[i+6])

            for i in range(0,len(gemi_yukleme),4):

                gemi_adi=gemi_yukleme[i+1]
                zaman=gemi_yukleme[i]
                gemi_kapasite=int(gemi_yukleme[i+2])
                gidilecek_ulke=gemi_yukleme[i+3]
                depo=0


                gemi=Gemi(gemi_adi,zaman,gemi_kapasite,gidilecek_ulke,depo) #gemi nesneleri oluşturuldu

                anahtar=gemi.ad
                deger=[gemi.zaman,gemi.kapasite,gemi.gidilecek_ulke,gemi.depo]
                sozluk[anahtar]=deger
                anahtar3=gemi.ad
                deger3=[gemi.zaman,gemi.kapasite,gemi.gidilecek_ulke,gemi.depo]
                gemi_arastirma_sozlugu[anahtar3]=deger3



            for i in range(0,len(tir_indirme),7):

                if tir_indirme[i+1] in tir_indirme[i+2:]:
                    tir_plaka=tir_indirme[i+1]+"_1"
                else:
                    tir_plaka=tir_indirme[i+1]

                zaman=tir_indirme[i]
                ulke=tir_indirme[i+2]
                _20_t_a_=tir_indirme[i+3]
                _30_t_a_=tir_indirme[i+4]
                yuk=int(tir_indirme[i+5])
                maliyet=tir_indirme[i+6]

                tir=TIR(tir_plaka,zaman,ulke,_20_t_a_,_30_t_a_,yuk,maliyet) #tır nesneleri oluşturuldu





                tir.plaka=tir.plaka
                anahtar1=tir.plaka


                deger1=[tir.zaman,tir.ulke,tir._20_t_a_,tir._30_t_a_,tir.yuk,tir.maliyet]
                sozluk1[anahtar1]=deger1







                anahtar2=tir.plaka
                deger2=[tir.zaman,tir.ulke,tir._20_t_a_,tir._30_t_a_,tir.yuk,tir.maliyet]
                if anahtar2 not in tir_arastirma_sozlugu:
                     tir_arastirma_sozlugu[anahtar2]=deger2
                else:
                    eklenen_surler = [k for k in sozluk if k.startswith(anahtar2)]

                    if not eklenen_surler:
                          tir_arastirma_sozlugu[anahtar2 + '_1'] = deger2

                    else:
                            son_sayi = max([int(s.split('_')[-1]) for s in eklenen_surler])
                            yeni_sayi = son_sayi + 1
                            yeni_anahtar = f"{anahtar2}_{yeni_sayi}"
                            sozluk[yeni_anahtar] = deger2






            sirali_sozluk1 = dict(sorted(sozluk1.items(), key=lambda x: x[0][-3:]))



            for i in temizlik_listesi2:

                if i in sirali_sozluk1:         #Sözlük Temizlikleri

                    del sirali_sozluk1[i]

            for i in temizlik_listesi3:

                if i in sirali_sozluk1:

                    del sirali_sozluk1[i]

            for i,j in sozluk.items():
                if i not in sozluk2:
                    sozluk2[i]=j





            if yuk_sayaci<1:

                for i in sirali_sozluk1:


                    if sayac>20 or yuk_sayaci>0:
                        break

                    z1=sirali_sozluk1[i]
                    a=0
                    for j in yuk_indirme_alani1:            #Tır yük indirmesi
                        a=a+int(j[4])
                    if int(z1[4])+a>750:
                        print(colored("Yükleme Alanı-1 Dolu!",'red'))
                        yuk_sayaci+=1
                        break
                    else:
                        yuk_indirme_alani1.append(sirali_sozluk1[i])
                        print(i,("plakalı tır yükünü indirdi."))
                        temizlik_listesi2.append(i)
                        sayac+=1











            if yuk_sayaci>0 and yuk_sayaci_2<1:
                for i in sirali_sozluk1:

                    if sayac>20 or yuk_sayaci_2>0:
                        break

                    z1=sirali_sozluk1[i]
                    b=0
                    for j in yuk_indirme_alani2:
                        b=b+int(j[4])

                    if int(z1[4])+b>750:
                        print(colored("Yükleme Alanı-2 Dolu!",'red'))
                        yuk_sayaci_2+=1
                        break
                    else:
                        yuk_indirme_alani2.append(sirali_sozluk1[i])
                        print(i,("plakalı tır yükünü indirdi."))
                        sayac+=1
                        temizlik_listesi2.append(i)






            if yuk_sayaci>0:
                print(colored("Yükleme Alanı-1 Dolu!",'red'))   #Geri bildirim kısmı

            if yuk_sayaci_2>0:
                print(colored("Yükleme Alanı-2 Dolu!",'red'))
            if yuk_sayaci>0 and yuk_sayaci_2>0:
                print(colored("Yükleme Alanları Dolu!",'red'))








            for i in sozluk2:
                a1=sozluk2[i][3]
                b1=int(sozluk2[i][1])
                c1=95
                d1=100                              #Gemi kontrolü
                f1=b1*(c1/d1)
                if a1>f1:
                    temizlik_listesi4.append(i)
                    print(i,"numaralı gemi yola çıktı")



            for i in temizlik_listesi4:

                if i in sozluk2:

                    del sozluk[i]




            if sayac<20 and sozluk2!={}:


                    for i in sozluk2:

                        for j in yuk_indirme_alani1:    #Gemilerin yüklenmesi

                            if sozluk2[i][2]==j[1] and sozluk2[i][3]+j[4]<=sozluk2[i][1] and sayac<20 :

                                sozluk2[i][3]=sozluk2[i][3]+j[4]

                                n1=yuk_indirme_alani1.index(j)
                                yuk_indirme_alani1[n1]=['0', 'Minas Trith', '0', '0', 0, '0']




            if sayac<20 and sozluk2!={}:


                    for i in sozluk2:

                        for j in yuk_indirme_alani2:

                            if sozluk2[i][2]==j[1] and sozluk2[i][3]+j[4]<=sozluk2[i][1] and sayac<20 :

                                sozluk2[i][3]=sozluk2[i][3]+j[4]

                                n1=yuk_indirme_alani2.index(j)
                                yuk_indirme_alani2[n1]=['0', 'Minas Trith', '0', '0', 0, '0']




            for i in sozluk2:
                a1=sozluk2[i][3]
                b1=int(sozluk2[i][1])
                c1=95                   #Gemi kontrolü
                d1=100
                f1=b1*(c1/d1)
                if a1>f1:
                    temizlik_listesi4.append(i)
                    print(i,"numaralı gemi yola çıktı")



            for i in temizlik_listesi4:

                if i in sozluk2:

                    del sozluk2[i]




            if yuk_indirme_alani1==[]:
                print(colored("Yükleme Alanı-1 Boş!",'green'))

            if yuk_indirme_alani2==[]:                              #Geri bildirim kısmı
                print(colored("Yükleme Alanı-2 Boş!",'green'))

            if yuk_indirme_alani1==[] and yuk_indirme_alani2==[]:
                print(colored("Yükleme Alanları Boş!",'green'))


            gun=gun+1

    x9=1
    while x9==1:
        print("Liman Otomasyonu Menüsüne hoşgeldiniz")
        print("┌──────────────────────────────────────────────────────┐") #Menü Oluşturuldu
        print("│                         Menü                         │")
        print("├──────────────────────────────────────────────────────┤")
        print("│ 1-Tır Sorgulama                                      │")
        print("│ 2-Gemi Sorgulama                                     │")
        print("│ 3-Çıkış                                              │")
        print("└──────────────────────────────────────────────────────┘")
        x6=0
        x6=input("Lütfen bir seçenek seçiniz:")
        if x6=="1":

                if tir_arastirma_sozlugu=={}:
                    print("Sorgu Listesi Boş!")
                else:
                    k8=input("Tır Adını Girin:")
                    for i in tir_arastirma_sozlugu:
                         if i==k8:
                              print(tir_arastirma_sozlugu[i])

        elif x6=="2":
            if gemi_arastirma_sozlugu=={}:
                    print("Sorgu Listesi Boş!")
            else:
                    k5=input("Gemi Adını Girin:")
                    for i in gemi_arastirma_sozlugu:
                        if i==k5:
                            print(gemi_arastirma_sozlugu[i])

        elif x6=="3":
                print("İyi Günler Dileriz!")
                x9=2

        else:
                print("Böyle bir seçenek bulunmamaktadır")



    x19=input("Eğer guiye girmek istiyorsanız 1'e basın:")

    if x19== "1":
        #Görsel arayüz ekleme kısmı tkinter ve onun özellikleri import edilerek yazıldı
            def yuk_tasima_baslat():
                    tur_bilgisi = tk.simpledialog.askstring("Otomasyon Başlat","İstediğiniz günü girin:")
                    tur_bilgisi=int(tur_bilgisi)

                    messagebox.showinfo("Bilgi", "Yük taşıma işlemi başlatıldı.")

                    dosya=open("gemiler.csv","r")
                    liste1=dosya.readlines()
                    liste2=[]
                    dosya.close
                    liste1=liste1[1:]

                    stringecevir=""



                    for i in liste1:

                        x=i.replace("\n", " ")
                        y=x.replace(",", " ")
                        liste2.append(y)

                    for i in liste2:

                        stringecevir=stringecevir+i




                    liste3=stringecevir.split(" ")
                    liste3=liste3[:-1]#Liste istediğimiz forma geldi gemiler dosyasındaki elemanlar listeye eklenerek her 4 elemanda 1 geminin bilgisinin bulunması sağlandı



                    dosya1=open("olaylar.csv","r")
                    liste4=dosya1.readlines()
                    dosya1.close()
                    liste5=[]
                    liste4=liste4[1:]
                    stringecevir1=""



                    for i in liste4:

                        x=i.replace("\n", " ")
                        y=x.replace(",", " ")
                        liste5.append(y)

                    for i in liste5:

                        stringecevir1=stringecevir1+i

                    liste6=stringecevir1.split(" ")
                    liste6=liste6[:-1]  #Aynı işlem olaylar.csv dosyası içinde gerçekleştirildi her 7 elemanda 1 tır bilgisi bulunması sağlandı









                    class Gemi:                                                 #istenilen classlar oluşturuldu
                        def __init__(self,ad,zaman,kapasite,gidilecek_ulke,depo):
                            self.ad=ad
                            self.zaman=zaman
                            self.kapasite=kapasite
                            self.gidilecek_ulke=gidilecek_ulke
                            self.depo=depo


                    class TIR:

                        def __init__(self,plaka,zaman,ulke, _20_t_a_,_30_t_a_,yuk,maliyet):
                            self.plaka=plaka
                            self.zaman=zaman
                            self.ulke=ulke
                            self._20_t_a_=_20_t_a_
                            self._30_t_a_=_30_t_a_
                            self.yuk=yuk
                            self.maliyet=maliyet




                    yuk_indirme_alani1=list()       #Gereken değişkenler oluşturuldu
                    yuk_indirme_alani2=list()


                    tir_indirme=[]
                    gemi_yukleme=[]
                    sayac=0
                    yuk_sayaci=0
                    yuk_sayaci_2=0
                    sozluk={}
                    sozluk1={}
                    gemi_gun_listesi=[]
                    tir_gun_listesi=[]
                    temizlik_listesi2=[]
                    temizlik_listesi3=[]
                    tir_arastirma_sozlugu={}
                    gemi_arastirma_sozlugu={}
                    temizlik_listesi4=[]
                    gun=0


                    a=0
                    b=0
                    sozluk2={}
                    as_secim=-1


                    for i in range(0,len(liste3),4):            #Döngü için gereken listeler oluşturuldu
                        gemi_gun_listesi.append(liste3[i])




                    for i in range(0,len(liste6),7):
                        tir_gun_listesi.append(liste6[i])








                    while gun<tur_bilgisi+1:                 #otomasyon döngüsü başladı
                            sayac=0

                            messagebox.showinfo("Bilgi",(gun,".gün"))
                            if str(gun) in gemi_gun_listesi:

                                for i in range(0,len(liste3),4):

                                    if liste3[i]==str(gun):
                                        gemi_yukleme.append(liste3[i])
                                        gemi_yukleme.append(liste3[i+1])
                                        gemi_yukleme.append(liste3[i+2])
                                        gemi_yukleme.append(liste3[i+3])



                            if str(gun) in tir_gun_listesi:


                                for i in range(0,len(liste6),7):

                                    if liste6[i]==str(gun):

                                        tir_indirme.append(liste6[i])
                                        tir_indirme.append(liste6[i+1])
                                        tir_indirme.append(liste6[i+2])
                                        tir_indirme.append(liste6[i+3])
                                        tir_indirme.append(liste6[i+4])
                                        tir_indirme.append(liste6[i+5])
                                        tir_indirme.append(liste6[i+6])

                            for i in range(0,len(gemi_yukleme),4):

                                gemi_adi=gemi_yukleme[i+1]
                                zaman=gemi_yukleme[i]
                                gemi_kapasite=int(gemi_yukleme[i+2])
                                gidilecek_ulke=gemi_yukleme[i+3]
                                depo=0


                                gemi=Gemi(gemi_adi,zaman,gemi_kapasite,gidilecek_ulke,depo) #gemi nesneleri oluşturuldu

                                anahtar=gemi.ad
                                deger=[gemi.zaman,gemi.kapasite,gemi.gidilecek_ulke,gemi.depo]
                                sozluk[anahtar]=deger
                                anahtar3=gemi.ad
                                deger3=[gemi.zaman,gemi.kapasite,gemi.gidilecek_ulke,gemi.depo]
                                gemi_arastirma_sozlugu[anahtar3]=deger3



                            for i in range(0,len(tir_indirme),7):

                                if tir_indirme[i+1] in tir_indirme[i+2:]:
                                    tir_plaka=tir_indirme[i+1]+"_1"
                                else:
                                    tir_plaka=tir_indirme[i+1]

                                zaman=tir_indirme[i]
                                ulke=tir_indirme[i+2]
                                _20_t_a_=tir_indirme[i+3]
                                _30_t_a_=tir_indirme[i+4]
                                yuk=int(tir_indirme[i+5])
                                maliyet=tir_indirme[i+6]

                                tir=TIR(tir_plaka,zaman,ulke,_20_t_a_,_30_t_a_,yuk,maliyet) #tır nesneleri oluşturuldu





                                tir.plaka=tir.plaka
                                anahtar1=tir.plaka


                                deger1=[tir.zaman,tir.ulke,tir._20_t_a_,tir._30_t_a_,tir.yuk,tir.maliyet]
                                sozluk1[anahtar1]=deger1







                                anahtar2=tir.plaka
                                deger2=[tir.zaman,tir.ulke,tir._20_t_a_,tir._30_t_a_,tir.yuk,tir.maliyet]
                                if anahtar2 not in tir_arastirma_sozlugu:
                                    tir_arastirma_sozlugu[anahtar2]=deger2
                                else:
                                    eklenen_surler = [k for k in sozluk if k.startswith(anahtar2)]

                                    if not eklenen_surler:
                                        tir_arastirma_sozlugu[anahtar2 + '_1'] = deger2

                                    else:
                                            son_sayi = max([int(s.split('_')[-1]) for s in eklenen_surler])
                                            yeni_sayi = son_sayi + 1
                                            yeni_anahtar = f"{anahtar2}_{yeni_sayi}"
                                            sozluk[yeni_anahtar] = deger2






                            sirali_sozluk1 = dict(sorted(sozluk1.items(), key=lambda x: x[0][-3:]))



                            for i in temizlik_listesi2:

                                if i in sirali_sozluk1:         #Sözlük Temizlikleri

                                    del sirali_sozluk1[i]

                            for i in temizlik_listesi3:

                                if i in sirali_sozluk1:

                                    del sirali_sozluk1[i]

                            for i,j in sozluk.items():
                                if i not in sozluk2:
                                    sozluk2[i]=j





                            if yuk_sayaci<1:

                                for i in sirali_sozluk1:


                                    if sayac>20 or yuk_sayaci>0:
                                        break

                                    z1=sirali_sozluk1[i]
                                    a=0
                                    for j in yuk_indirme_alani1:            #Tır yük indirmesi
                                        a=a+int(j[4])
                                    if int(z1[4])+a>750:

                                        messagebox.showinfo("Bilgi", "Yükleme Alanı-1 Dolu!")

                                        yuk_sayaci+=1
                                        break
                                    else:
                                        yuk_indirme_alani1.append(sirali_sozluk1[i])

                                        messagebox.showinfo("Bilgi",(i, "plakalı tır yükünü indirdi."))
                                        temizlik_listesi2.append(i)
                                        sayac+=1











                            if yuk_sayaci>0 and yuk_sayaci_2<1:
                                for i in sirali_sozluk1:

                                    if sayac>20 or yuk_sayaci_2>0:
                                        break

                                    z1=sirali_sozluk1[i]
                                    b=0
                                    for j in yuk_indirme_alani2:
                                        b=b+int(j[4])

                                    if int(z1[4])+b>750:

                                        messagebox.showinfo("Bilgi", "Yükleme Alanı-2 Dolu!")
                                        yuk_sayaci_2+=1
                                        break
                                    else:
                                        yuk_indirme_alani2.append(sirali_sozluk1[i])
                                        messagebox.showinfo("Bilgi",(i, "plakalı tır yükünü indirdi."))


                                        sayac+=1
                                        temizlik_listesi2.append(i)






                            if yuk_sayaci>0:
                                #Geri bildirim kısmı
                                messagebox.showinfo("Bilgi", "Yükleme Alanı-1 Dolu!")

                            if yuk_sayaci_2>0:
                                messagebox.showinfo("Bilgi", "Yükleme Alanı-2 Dolu!")
                            if yuk_sayaci>0 and yuk_sayaci_2>0:
                                messagebox.showinfo("Bilgi", "Yükleme Alanları Dolu!")







                            for i in sozluk2:
                                a1=sozluk2[i][3]
                                b1=int(sozluk2[i][1])
                                c1=95
                                d1=100                              #Gemi kontrolü
                                f1=b1*(c1/d1)
                                if a1>f1:
                                    temizlik_listesi4.append(i)

                                    messagebox.showinfo("Bilgi" ,(i,"numaralı gemi yola çıktı"))



                            for i in temizlik_listesi4:

                                if i in sozluk2:

                                    del sozluk[i]




                            if sayac<20 and sozluk2!={}:


                                    for i in sozluk2:

                                        for j in yuk_indirme_alani1:    #Gemilerin yüklenmesi

                                            if sozluk2[i][2]==j[1] and sozluk2[i][3]+j[4]<=sozluk2[i][1] and sayac<20 :

                                                sozluk2[i][3]=sozluk2[i][3]+j[4]

                                                n1=yuk_indirme_alani1.index(j)
                                                yuk_indirme_alani1[n1]=['0', 'Minas Trith', '0', '0', 0, '0']




                            if sayac<20 and sozluk2!={}:


                                    for i in sozluk2:

                                        for j in yuk_indirme_alani2:

                                            if sozluk2[i][2]==j[1] and sozluk2[i][3]+j[4]<=sozluk2[i][1] and sayac<20 :

                                                sozluk2[i][3]=sozluk2[i][3]+j[4]

                                                n1=yuk_indirme_alani2.index(j)
                                                yuk_indirme_alani2[n1]=['0', 'Minas Trith', '0', '0', 0, '0']




                            for i in sozluk2:
                                a1=sozluk2[i][3]
                                b1=int(sozluk2[i][1])
                                c1=95                   #Gemi kontrolü
                                d1=100
                                f1=b1*(c1/d1)
                                if a1>f1:
                                    temizlik_listesi4.append(i)

                                    messagebox.showinfo("Bilgi" ,(i,"numaralı gemi yola çıktı"))



                            for i in temizlik_listesi4:

                                if i in sozluk2:

                                    del sozluk2[i]




                            if yuk_indirme_alani1==[]:

                                messagebox.showinfo("Bilgi", "Yükleme Alanı-1 Boş!")

                            if yuk_indirme_alani2==[]:                              #Geri bildirim kısmı

                                messagebox.showinfo("Bilgi", "Yükleme Alanı-2 Boş!")

                            if yuk_indirme_alani1==[] and yuk_indirme_alani2==[]:

                                messagebox.showinfo("Bilgi", "Yükleme Alanları Boş!")


                            gun=gun+1











            def gemi_sorgula():

                gemi_bilgisi = tk.simpledialog.askstring("Gemi Sorgula", "Gemi Numarasını Girin:")

                as_uzunluk=3

                if len(gemi_bilgisi)<as_uzunluk:

                    gemi_bilgisi="0"*(as_uzunluk-len(gemi_bilgisi))+gemi_bilgisi

                if gemi_bilgisi in gemi_arastirma_sozlugu:
                    bilgi=gemi_arastirma_sozlugu[gemi_bilgisi]
                    messagebox.showinfo(f"{gemi_bilgisi} adlı geminin bilgileri",
                            f"Varış zamanı: {bilgi[0]}\n"
                            f"Geminin kapasitesi: {bilgi[1]}\n"
                            f"Gideceği ülke: {bilgi[2]}")

                else:
                    messagebox.showinfo("Bilgi", f"{gemi_bilgisi} adlı gemi bilgisi bulunamadı!")

            def tir_sorgula():

                tir_bilgisi = tk.simpledialog.askstring("Tır Sorgula", "Tır Plakasını Girin:")


                if tir_bilgisi in tir_arastirma_sozlugu:
                    bilgi1=tir_arastirma_sozlugu[tir_bilgisi]
                    messagebox.showinfo(f"{tir_bilgisi} adlı tırın bilgileri",
                            f"Varış zamanı: {bilgi1[0]}\n"
                            f"Gideceği ülke: {bilgi1[1]}\n"
                            f"20 Ton Adet: {bilgi1[2]}\n"
                            f"30 Ton Adet: {bilgi1[3]}\n"
                            f"Toplam Yük Miktarı: {bilgi1[4]}\n"
                            f"Maliyet: {bilgi1[5]}")
                else:
                    messagebox.showinfo("Bilgi", f"{tir_bilgisi} adlı tır bilgisi bulunamadı!")

            def cikis():
                root.destroy()

            root = tk.Tk()
            root.title("Liman Otomasyonu")




            baslik= tk.Label(root, text="Liman Otomasyonu", font=("Verdana", 24))
            baslik.pack(pady=20)


            yuk_tasima_butonu=tk.Button(root, text="Yük Taşıma İşlemini Başlat",command=yuk_tasima_baslat)
            gemi_sorgulama_butonu= tk.Button(root, text="Gemi Sorgula",command=gemi_sorgula)
            tir_sorgulama_butonu=btn_tir_sorgula = tk.Button(root, text="Tır Sorgula",command=tir_sorgula)
            cikis_butonu = tk.Button(root, text="Çıkış", command=cikis)


            yuk_tasima_butonu.pack(pady=35)
            gemi_sorgulama_butonu.pack(pady=35)
            tir_sorgulama_butonu.pack(pady=35)
            cikis_butonu.pack(pady=35)


            pencere_genislik = 840
            pencere_yukseklik = 620
            ekran_genislik = root.winfo_screenwidth()
            ekran_yukseklik = root.winfo_screenheight()
            x_pozisyon = (ekran_genislik - pencere_genislik) // 2
            y_pozisyon = (ekran_yukseklik - pencere_yukseklik) // 2

            root.geometry(f"{pencere_genislik}x{pencere_yukseklik}+{x_pozisyon}+{y_pozisyon}")



            ana_menu = tk.Menu(root)
            root.mainloop()



if __name__ == "__main__":
    main()

