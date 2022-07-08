1import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
import cv2
if __name__ == '__main__':
    print("1 - FACE RECOGNITION")
    print("2 - TRANSLATOR")
    val = input("Enter your CHOICE: ")
    if val==1:

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        cap = cv2.VideoCapture(0)
        while 1:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
                    cv2.imshow('img',img)
                    k = cv2.waitKey(30) & 0xff
                    if k == 27:
                        break
                        
        cap.release() 
        cv2.destroyAllWindows()

    elif val==2:
        # Importing necessary modules required
        import speech_recognition as spr
        from googletrans import Translator
        from gtts import gTTS
        import os


        # Creating Recogniser() class object
        recog1 = spr.Recognizer()

        # Creating microphone instance
        mc = spr.Microphone()


        # Capture Voice
        with mc as source:
            print("Speak 'hello' to initiate the Translation !")
            print("~~~~~~~~~~~~~~~~")
            recog1.adjust_for_ambient_noise(source, duration=0.2)
            audio = recog1.listen(source)
            MyText = recog1.recognize_google(audio)
            MyText = MyText.lower()

        # Here initialising the recorder with
        # hello, whatever after that hello it
        # will recognise it.
        if 'hello' in MyText:
            
            # Translator method for translation
            translator = Translator()
            
            # short form of english in which
            # you will speak
            from_lang = 'en'
            
            # In which we want to convert, short
            # form of hindi
            to_lang = 'hi'
            
            with mc as source:
                
                print("Speak a stentence...")
                recog1.adjust_for_ambient_noise(source, duration=0.2)
                
                # Storing the speech into audio variable
                audio = recog1.listen(source)
                
                # Using recognize.google() method to
                # convert audio into text
                get_sentence = recog1.recognize_google(audio)

                # Using try and except block to improve
                # its efficiency.
                try:
                    
                    # Printing Speech which need to
                    # be translated.
                    print("Phase to be Translated :"+ get_sentence)

                    # Using translate() method which requires
                    # three arguments, 1st the sentence which
                    # needs to be translated 2nd source language
                    # and 3rd to which we need to translate in
                    text_to_translate = translator.translate(get_sentence,
                                                            src= from_lang,
                                                            dest= to_lang)
                    
                    # Storing the translated text in text
                    # variable
                    text = text_to_translate.text

                    # Using Google-Text-to-Speech ie, gTTS() method
                    # to speak the translated text into the
                    # destination language which is stored in to_lang.
                    # Also, we have given 3rd argument as False because
                    # by default it speaks very slowly
                    speak = gTTS(text=text, lang=to_lang, slow= False)

                    # Using save() method to save the translated
                    # speech in capture_voice.mp3
                    speak.save("captured_voice.mp3")	
                    
                    # Using OS module to run the translated voice.
                    os.system("start captured_voice.mp3")

                # Here we are using except block for UnknownValue
                # and Request Error and printing the same to
                # provide better service to the user.
                except spr.UnknownValueError:
                    print("Unable to Understand the Input")
                    
                except spr.RequestError as e:
                    print("Unable to provide Required Output".format(e))

    elif val==3:
        print("Invalid Input")