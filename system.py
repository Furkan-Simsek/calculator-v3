import os
import time

i=0
a=0
def soru_error():
    print("Hata!")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
def soru():
    global soru
    print("-----------------Kayıt Sistemi-----------------")
    soru = input("1) Yeni öğrenci kaydı \n2) Yeni öğretmen kaydı \n3) Tüm öğrencileri Gösterir\n4) Tüm öğretmenleri gösterir\n5) Sistemi kapat\n \n>:  ")
def login_error():
    os.system('cls' if os.name=='nt' else 'clear')
    print("-----------------Hata-----------------")
    print("Kullanıcı adı yada şifre hatalı")
    print("--------------------------------------")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
def login():
    global username, password
    print("-----------------Giriş-----------------")
    username = input("Kullanıcı Adı giriniz:")
    password = input("Şifre Giriniz: ")
    os.system('cls' if os.name=='nt' else 'clear')
def student_register():
     print("-----------------Öğrenci Kayıt-----------------")
     students = open("students.txt", "a",encoding="utf-8")
     name = input("Öğrenci Adı: ")
     lastname = input("Öğrenci Soyadı: ")
     dad = input("Baba adı: ")
     mother = input("Anne Adı: ")
     birthday = input("Doğum tarihi: ")
     classroom = input("Öğrencinin okuduğu sınıf: ")
     school = input("Öğrencinin bulunduğu okul: ")
     cartno = input("Öğrencinin T.C kimlik nosu: ")
     schoolNumber = input("Öğrencinin okul numarası: ")
     students.write("Ad: " + name + " - Soyadı: " + lastname + " - Baba adı: " + dad + " - Anne adı: " + mother + " - Kimlik numarası: " + " - Sınıfı" + classroom + " - Okulu: "+ school +" - Okul numarası: " + schoolNumber +  "\n" )
     students.close()
     os.system('cls' if os.name=='nt' else 'clear')
def teacher_register():
     print("-----------------Öğretmen Kayıt-----------------")
     teachers = open("teachers.txt", "a",encoding="utf-8")
     name = input("Öğretmen Adı: ")
     lastname = input("Öğretmen Soyadı: ")
     branch = input("Öğretmenin Branşı: ")
     teachers.write("Ad: " + name + " - Soyadı: " + lastname + " - Branşı: " + branch + "\n")
     os.system('cls' if os.name=='nt' else 'clear')
def read_student():
     print("-----------------Tüm Öğrenciler-----------------")
     reads = open("students.txt",encoding="utf-8")
     print(reads.read())
     reads.close()
def read_teacher():
     print("-----------------Tüm Öğretmenler-----------------")
     readt = open("teachers.txt",encoding="utf-8")
     print(readt.read())
     readt.close()
while i==0:
    while a==0:
        login()
        if password == "123" and username == "Admin":
            a=a+1
        else:
            login_error()
    if password == "123" and username == "Admin":
        soru()
        if soru == "1":
            student_register()
        elif soru == "2":
            teacher_register()
        elif soru == "3":
            read_student()
        elif soru == "4":
            read_teacher()
        elif soru == "5":
            break
        else:
            soru_error()
            
      
