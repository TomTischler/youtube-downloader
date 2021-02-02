from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #python -m pip install git+https://github.com/nficano/pytube

#------------- Programm funktionen ------------

Folder_Name = ""

#Verzeichnis standort
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    
    else:
        locationError.config(text="Ordner auswählen",fg="red")

#Video Download
def DownloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choices == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        
        else:
            ytdError.config(text="Link Ungültig!",fg="red")

    #Download funktion
    select.download(Folder_Name)
    ytdError.config(text="Download abgeschlossen!")

#------------- Programmfenster ---------------

root = Tk()
root.title("YouTube Downloader") #Programmfenster titel
root.geometry("350x400") #Programmfenster größe
root.columnconfigure(0,weight=1) #Inhalt ausrichten

#------------- Programmfenster Elemente ---------------

#Link Download Textüberschrift
ytdLabel = Label(root,text="Video URL eingeben",font=("jost",15))
ytdLabel.grid()

#Eingabe Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="Error!",fg="red",font=("jost",10))
ytdError.grid()

#Datei Speichern Textüberschrift
saveLabel = Label(root,text="Datei Speichern",font=("jost",15,"bold"))
saveLabel.grid()

#Datei Speichern Button
saveEntry = Button(root,width=15,bg="red",fg="white",text="Pfad auswählen",command=openLocation)
saveEntry.grid()

#Location Error
locationError = Label(root,text="Verzeichnisfehler",fg="red",font=("jost",10))
locationError.grid()

#Download Qualität
ytdQuality = Label(root,text="Download-Qualität auswählen",font=("jost",15))
ytdQuality.grid()

#Auswahlbox
choices = ["720p","144p","MP3"]
ytdChoices = ttk.Combobox(root,values=choices)
ytdChoices.grid()

#Download Button
downloadbtn = Button(root,text="Download",width=15,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

root.mainloop()