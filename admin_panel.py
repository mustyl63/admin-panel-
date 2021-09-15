from urllib.request import urlopen 
import Request , URLError, HTTPError

def Space(j):
    i = 0
    while i<=j:
        print= " ",
        i+=1

def AdminPanel():
    f =open("link.txt","r");
    link = raw_input("Lütfen Siteye Giriniz: ")
    print ="\n\nPanel Aranıyor...: \n"
    while True:
        sub_link = f.readline()
        if not sub_link:
            break
        req_link= "http://"+link+"/"+sub_link
        req = Request(req_link)
        try:
            response =urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print =" Tamam =>", req_link

def Yapanlar():
    Space(9); print = "#############################"
    Space(9); print = "#    Yazan Mustafa Yüksel   #"
    Space(9); print = "#    Yardımcı Ahmet Yüksel  #"
    Space(9); print = "#    Türk Hack Team Türkiye #"

Yapanlar()
AdminPanel()

