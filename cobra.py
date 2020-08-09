"""
-------------------------------------------------
Cobra Module 🐍
The main target of this module is to help
users do large things in some lines of codes
It contains many useful functions below
This module automatically installes some
module which are necessary, sometimes the cmd
may open, please don't mind it
If any problems are encountered contact
me on github LissanKoirala
-------------------------------------------------
"""

import os
import time

def encrypt(message):
  """-------------------------------------------------\nThis is a unique Encryption,\nThis is used to Encrypt datas,\nThis function Encrypts your message and provides\nyou a key which will be needed to decrypt the \nEncrypted Message\n-------------------------------------------------"""
  import random
  key_num = ""
  numbers_code = ['1','2','3','4','5','6','7','8','9'] # This are the possible numbers in the key
  for i in range(5):
    index = random.randint(0,8) # Generates the random number
    key_num += numbers_code[index]  # And adds the number into the key

  key_alpha = ""
  alpha_code = ['A','a','@','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']  # This are the possible alphabets in to key
  for i in range(5):
    index = random.randint(0,52) # Generates a random number
    key_alpha += alpha_code[index] # Adds the random alphabets into the key

  key_print = key_num[0] + key_alpha[0] + key_num[1] + key_alpha[1] + key_num[2] + '//' + key_alpha[2] + key_num[3] + key_alpha[3] + key_num[4] + key_alpha[4]                     

  key_stage_1 = int(key_print[0]) 
  key_stage_2 = int(key_print[2])
  key_stage_3 = int(key_print[4]) # Takes out the real key form the key that is printed out
  key_stage_4 = int(key_print[8])
  key_stage_5 = int(key_print[10])

  # Encryption Level 1
  encrypted_stage_1 = ""
  for letter in message: 
    encrypted_stage_1 += chr(ord(letter)+ key_stage_1) 
  # Encryption Level 2
  encrypted_stage_2 = ""
  for letter in encrypted_stage_1: 
    encrypted_stage_2 += chr(ord(letter)+ key_stage_2) 
  # Encryption Level 3
  encrypted_stage_3 = ""
  for letter in encrypted_stage_2: 
    encrypted_stage_3 += chr(ord(letter)+ key_stage_3) 
  # Encryption Level 4
  encrypted_stage_4 = ""
  for letter in encrypted_stage_3: 
    encrypted_stage_4 += chr(ord(letter)+ key_stage_4) 
  # Encryption Level 1
  encrypted_stage_5 = ""
  for letter in encrypted_stage_4: 
    encrypted_stage_5 += chr(ord(letter)+ key_stage_5) 
  # Final Substracting, Adding, Multiplying, Dividing all the key_Stages
  final_stage_key = key_stage_1 + key_stage_2 - key_stage_3 * key_stage_4 // key_stage_5
  final_stage = ""
  for letter in encrypted_stage_5: 
    final_stage += chr(ord(letter)+ final_stage_key) 
  encrypted = final_stage

  return encrypted, key_print

def decrypt(encrypted_message, key_user):
  """----------------------------------------------\nThis is a unique Decryption,\nThis Decrypts your Encrypted Message, but the\nEncryption should be done from his software\n----------------------------------------------"""
  # Key Distributer
  key_stage_1 = int(key_user[0])
  key_stage_2 = int(key_user[2])
  key_stage_3 = int(key_user[4])   # The real keys are taken from the input, some of them are just to look attractive
  key_stage_4 = int(key_user[8])
  key_stage_5 = int(key_user[10])

  # Final Substracting, Adding, Multiplying, Dividing all the key_Stages
  final_stage_key = key_stage_1 + key_stage_2 - key_stage_3 * key_stage_4 // key_stage_5
  final_stage = ""
  for letter in encrypted_message: 
    final_stage += chr(ord(letter)- final_stage_key) 
  # Decrypted Message Level 5
  decryption_stage_5 = ""
  for letter in final_stage: 
    decryption_stage_5 += chr(ord(letter)- key_stage_5) 
  # Encryption Level 4
  decryption_stage_4 = ""
  for letter in decryption_stage_5: 
    decryption_stage_4 += chr(ord(letter)- key_stage_4) 
  # Encryption Level 3
  decryption_stage_3 = ""
  for letter in decryption_stage_4: 
    decryption_stage_3 += chr(ord(letter)- key_stage_3) 
  # Encryption Level 2
  decryption_stage_2 = ""
  for letter in decryption_stage_3: 
    decryption_stage_2 += chr(ord(letter)- key_stage_2) 
  # Encryption Level 1
  decryption_stage_1 = ""
  for letter in decryption_stage_2: 
    decryption_stage_1 += chr(ord(letter)- key_stage_1) 
  decrypted_message = decryption_stage_1
  
  return decrypted_message

def send_email(from_email, from_password, to_email, title, message):
  """------------------------------------------------------------------\nThis is a function which sends email\nThe Requirments are as follows:\n- from_email : This is the email address of who is sending the email\n- from_password : This is the password of who is sending the email\n- to_email : This is the email of the receiver\n- title : This is the Subject of the Email\n- message : This is the Body of the Email\nYour Email ID or Password will not be saved!\n------------------------------------------------------------------"""
  try:
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
  except:
    os.system('cmd /c "pip install email"')
  try:
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = from_password
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = title
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    info.destroy()
    return "Email Sucessfully sent to " + to_email + " from " + from_email

  except:
    return "Sending email to " + to_email + " from " + from_email + " Uncessfull"

def get_time():
  """-------------------------------------------------\nThis is a function that gives you the time and date\n-------------------------------------------------"""
  import datetime
  all_time = datetime.datetime.now()
  all_time = all_time.strftime("%d %B %Y - %H:%M:%S")
  return all_time

def make_qr(information):
  """-------------------------------------------------------------\nThis is a function that make a Qr code\nThe requirments are as follows:\n- information : This contains the inforamtion of what is going\nto be converted to Qr Code\n- path : This is the path where your Qr image will be saved\nExample : 'D:/Python - Lissan'\n-------------------------------------------------------------"""
  try:
    import qrcode
  except:
    os.system('cmd /c "pip install qrcode"')
  try:
    img = qrcode.make(information)
    img.save('qr_code.png')
    return "Qr Code Made Sucessfully"
  except:
    return "Error Occured"

def speak(text):
  """------------------------------------------------------------\nThis is a function which transfers a text provided into speech\nThe requirements are as follows:\n- text : This is the text that is going to be converted\n- path: This is the path where your Qr image will be saved\nExample : 'D:/Python - Lissan'\n------------------------------------------------------------"""
  try:
    from gtts import gTTS
  except:
    os.system('cmd /c "pip install gtts"')
  try:
    speech = gTTS(text = text, lang = 'en', slow=False)
    speech.save('audio.mp3')
    return "Sucessfully made a audio file of the text " + text + " and saved with the file name audio.mp3" 
  except:
    return "Error while converting the text - " + text + " to audio"

def speech_to_text():
  """---------------------------------------------------------------\nThis is a function that takes your audio and transfers it to audio\n---------------------------------------------------------------"""
  try:
    import speech_recognition as sr
  except:
    os.system('cmd /c "pip install speech_recognition"')
  r = sr.Recognizer()
  with sr.Microphone() as source:
      audio = r.listen(source)
      try:
          said = r.recognize_google(audio)   # This takes the audio and transfers it to the text [User]
      except:
          said = "I didn't Hear that, Please try again"
  return said

def os_info():
  """---------------------------------------\nThis function returns the following:\n- The Current Operating System\n- Numbers of CPU\n- Actual Login Name of the Device\n- Current Working Directory\n---------------------------------------"""
  cpu = os.cpu_count()
  current_path = os.getcwd()
  all_comb = "Operating System - " + os.name + "\nNumbers of CPU - " + str(cpu) + "\nLogin Name - " + os.getlogin() + "\nCurrent working directory - " + current_path
  return all_comb

def create_folder(name, path):
  """---------------------------------------------\nThis function makes a folder in the path given\n---------------------------------------------"""
  try:
    os.chdir(path)
    os.mkdir(name)
    return "Folder name " + name + " was created in the path : " + path
  except:
    return "Error while creating Folder named " + name + " in the path : " + path

def rename(real_name,new_name):
  """----------------------------------\nThis function renames a file\nProvide the full path name of the file----------------------------------"""
  os.rename(real_name, new_name)
  return "File name : " + real_name + " changed to : " + new_name

def delete_folder(name, path):
  """---------------------------------------------\nThis function deletes a folder in the path given\n---------------------------------------------"""
  try:
    os.chdir(path)
    os.rmdir(name)
    return "The Folder named " + name + " was deleted in the path : " + path
  except:
    return "Error while deleting file named " + name + " in the path : " + path 

def make_file(name, information, path):
  """-------------------------------\nThis function makes a file,\nIn the path provided\nwith the information given\n-------------------------------"""
  try:
    os.chdir(path)
    f = open(name,'w')
    f.write(information)
    f.close()
    return "The file named " + name + " was creted in the path : " + path + " with [ " + information + " ] in it"
  except:
    return "Error while Creating file name " + f + "in the path : " + path

def delete_file(name):
  """---------------------------------------\nThis function deletes a file\nPlease provide the full address of a file\n---------------------------------------"""
  try:
    os.remove(name)
    return "File named " + name + " was Sucessfully deleted"
  except:
    return "Error while Deleting file named : " + name 

def time_file_created(name):
  """-----------------------------------------------------------\nThis funciton returns the time when the file was created\nEnter the full address of the file\nExample : D:/Python - Lissan/Login Portal/example.png\n-----------------------------------------------------------"""
  import time
  try: 
    mtime = os.path.getmtime(name)
    time_created = time.ctime(mtime)
    return "The file named " + name + " was created on " + time_created
  except:
    return "Error, seems that you didn't provide the full address of the file"

def delay(seconds):
  """---------------------------------\nThis function delays the program\n---------------------------------"""
  import time
  try:
    time.sleep(int(seconds))
  except:
    time.sleep(float(seconds))

def read(file):
  """----------------------------------------\nThis function reads a file and returns\nthe informations in it\n----------------------------------------"""
  try:
    f = open(file, 'r')
    info = f.read()
    f.close()
    return info
  except:
    return "The file provided was incorrect"

def write(file, information):
  """----------------------------------\nThis function writes in to a file\n----------------------------------"""
  try:
    f = open(file, 'w')
    f.write(information)
    f.close()
    return "Wrote [ " + inforamtion + " ] into the file named : " + file
  except:
    return "Error while writing [ " + information + " ] into the file named : " + file

def read_bytes(file):
  """----------------------------------------\nThis function reads a file and returns\nthe informations in it in bytes format\n----------------------------------------"""
  try:
    f = open(file, 'rb')
    info = f.read()
    f.close()
    return info
  except:
    return "The file provided was incorrect"

def write_bytes(file, information):
  """----------------------------------\nThis function writes in to a file\nin the bytes format\n----------------------------------"""
  try:
    f = open(file, 'wb')
    f.write(information)
    f.close()
    return "Wrote [ " + inforamtion + " ] into the file named : " + file
  except:
    return "Error while writing [ " + information + " ] into the file named : " + file

def take_photo():
  """---------------------------------------------\nThis function takes an photo using your cam\n---------------------------------------------"""
  try:
    import cv2
  except:
    os.system('cmd /c "pip install opencv-python"')
  x = 0
  cam = cv2.VideoCapture(0)
  ret, frame = cam.read()
  if not ret:
      x = "fail"
      return "Error while grabbing a frame"
  cv2.imwrite("captured_face.jpg", frame)
  if x != "fail":
    return "Photo Sucessfully taken and saved as : " + "photo.png"

def play(file):
  """----------------------------------------\nThis function plays a sounds in a file\nwithout opening the certain file\n----------------------------------------"""
  try:
    from playsound import playsound
  except:
    os.system('cmd /c "pip install playsound"')
  playsound(file)

def random_number(how_many):
  """------------------------------\nThis function returns random\ncombinations of numbers\n------------------------------"""
  import random
  number = ""
  numbers = ['1','2','3','4','5','6','7','8','9']
  y = len(numbers) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    number += numbers[x]
  return number

def random_alpha_cs(how_many):
  """-----------------------------------------\nThis function gives you random alphabet\nIt returns the combination of:\n- c : Capital\n- s : Small\nAlphabtes\n-----------------------------------------"""
  import random
  alphabets = ""
  alpha = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']  
  y = len(alpha) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    alphabets += alpha[x]
  return alphabets

def random_alpha_s(how_many):
  """-----------------------------------------------------\nThis function gives a random lower case alphabets\n-----------------------------------------------------"""
  import random
  alphabets = ""
  alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P''Q','R','S','T','U','V','W','X','Y','Z']  
  y = len(alpha) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    alphabets += alpha[x]
  return alphabets

def random_alpha_c(how_many):
  """----------------------------------------------\nThis function gives a random Capital alphabets\n----------------------------------------------"""
  import random
  alphabets = ""
  alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P''Q','R','S','T','U','V','W','X','Y','Z']  
  y = len(alpha) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    alphabets += alpha[x]
  return alphabets.lower() 

def random_symbol(how_many):
  """-----------------------------------------\nThis function gives a random symbol\n-----------------------------------------"""
  import random
  symbol = ""
  symbols = ["¬","`","!","\"","$","£","%","^","&","*","(",")","_","{","}","[","]",";",":","'","@","#","~",",","<",".",">","/","?","|","\\","/","-","+"]
  y = len(symbols) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    symbol += symbols[x]
  return symbol

def random_code(how_many):
  """------------------------------------\nThis function returns a code\nwith combination of:\n- Random Alphabets [Capital\\Smaller]\n- Random Number\n- Random Symbols\n------------------------------------"""
  import random
  code = ""
  possible = ['A','a','B','b','C','c','D','d','1','2','3','4','5','6','7','8','9','E','e','F','f','G','g','H','h',"¬","`","!","\"","$","£","%","^","&","*","(",")","_","{","}","[","]",";",":","'","@","#","~",",","<",".",">","/","?","|","\\","/","-","+",'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
  y = len(possible) - 1
  for i in range(how_many):
    x = random.randint(0, y)
    code += possible[x]
  return code

def stop_watch(start_or_stop):
  """---------------------------------------------\nThis is a stop watch, the requirement are:\n- start_or_stop : This is rather ["start" or "stop"]\n---------------------------------------------"""
  import time
  global start

  if "start" in start_or_stop:
    start = time.perf_counter()
    return "Timer has beeen started"
  else:
    stop = time.perf_counter()
    return round(stop-start)

def cmd(what_to_type):
  """----------------------------------------\nThis funciton writes what you provide\ninto the Command Prompt [cmd]\n----------------------------------------"""
  os.system('cmd /c '+ what_to_type)

def extract_audio(file_name, start_time, stop_time):
  """--------------------------------------------\nThis function extracts audio from a video\nThe requirements are:\nfile_name : Name of the file\nstart_time : Time from when you want the audio\nstop_time : Time until you want the audio\n--------------------------------------------"""
  try:
    import moviepy.editor as mp
  except:
    os.system('cmd /c "pip install moviepy"')
  clip = mp.VideoFileClip(file_name).subclip(start_time,stop_time)
  clip.audio.write_audiofile("Extracted_audio.mp3")

def notify(title, message, time, icon):
  """----------------------------------------------\nThis notifies on a desktop\nThe Requirments are:\n- title : The title of the notification\n- message : The main message of the notification\ntime : For how long to display the image\nicon : The icon of the image\n       Type : [none] if you don't want an icon\n----------------------------------------------"""
  try:
    from plyer import notification
  except:
    os.system('cmd /c "pip install plyer"')
  if "none" in icon.lower():
    notification.notify(
      title = title,
      message = message,
      app_icon = None,
      timeout = int(time)
      )
  else:
    notification.notify(
      title = title,
      message = message,
      app_icon = icon,
      timeout = int(time)
      )

def module_setup(file_name):
  """------------------------------------\nThis function installes the module\nin it's place where it needs to be\nso that it can be used\n------------------------------------"""
  if ".py" not in file_name:
    file_name += ".py"
  f = open(file_name,'r')
  information = f.read()
  f.close()

  try:
    user = os.getlogin()
    normal_path = "C:/Users/"+user+"/AppData/Local/Programs/Python/Python38-32/Lib"
    os.chdir(normal_path)
    f = open(file_name, 'w')
    f.write(information)
    f.close()
  except:
    normal_path = "C:/Program Files/Python38/lib"
    os.chdir(normal_path)
    f = open(file_name, 'w')
    f.write(information)
    f.close()

def internet_speed():
  """-----------------------------------------\nThis function tests your internet speed\n-----------------------------------------"""
  os.system('cmd /k "speedtest-cli"')

def weather(city_name):
  """----------------------------------------------\nThis function gives the weather inforamtion\nof the city provided\nIt returns the following\n- Temperature in Celcius [°C]\n- Descrption on weather\n----------------------------------------------"""
  import requests, json 
  token = "" # Get the token form openwheather
  complete_url = f"http://api.openweathermap.org/data/2.5/weather?appid={token}&q={city_name}" 
  response = requests.get(complete_url) 
  x = response.json() 
  if x["cod"] != "404": 
    y = x["main"] 
    current_temperature = y["temp"] 
    z = x["weather"] 
    weather_description = z[0]["description"] 
    total = "Temperature : " + str(int(current_temperature - 273.15)) + "°C" + "\nDescription : " + str(weather_description)
    return total
  else: 
    return "City Not Found" 

def browse():
  """-------------------------------------------------\nThis function opens a file explorer\nUser can browser through and select a file\nThe the function returns the full path of the file\n-------------------------------------------------"""
  import tkinter as tk
  from tkinter import filedialog
  root = tk.Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename()

  return file_path


