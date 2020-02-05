from googletrans import Translator
import speech_recognition as ss
import socket
import os

def ihbar():

	host = "localhost"
	port = 4646

	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	my_socket.connect((host, 2346))

	data = my_socket.recv(1024)

	print(data.decode())
	my_socket.send(b"\n\n   tehdit var port = 4646 !!!!!")

def satirlar(satir):

	satir=satir[:-1]
	liste= satir.split(" ")

	i=0
	kontrol = 0

	a = len(liste)

	while i<a:

		if str(liste[i])== "help" or str(liste[i])== "rescue" or str(liste[i])== "succor" or str(liste[i])== "ambulance" or str(liste[i])== "police" or str(liste[i])== "fire":
			kontrol = kontrol+1
			i=i+1
		
		i=i+1

	return kontrol


def ses_al():

    kayit = ss.Recognizer()

    print("\n\n  ---- DEMIR DEsecurity ----")

    with ss.Microphone() as mic:
        kayit.adjust_for_ambient_noise(mic)
        print("\n\n   Seni dinliyorum...")
        ses = kayit.listen(mic)
    
        try:
            print("\n\n   ="+kayit.recognize_google(ses))
        except Exception as e:

            print("" + str(e))
        
        with open("kayit.wav", "wb") as f:
            f.write(ses.get_wav_data())

        return kayit.recognize_google(ses)



while True:

	os.system("cls")

	asd = ses_al()

	kontrol = satirlar(asd)

	if kontrol!=0:
		
		ihbar()
