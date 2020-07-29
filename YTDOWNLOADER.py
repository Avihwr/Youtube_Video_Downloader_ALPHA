from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def progressCheck(stream=None, chunk=None,remaining=None):
    file_downloaded=(file_size-remaining)
    per=(file_downloaded/file_size)*100
    dBtn.config(text="{:00.0f} % downloaded".format(per))


def start_download():
    global file_size
    try:
        url = urlField.get()
        # CHANGING BUTTON TEXT AFTER CLICK AND DISABLE IT
        dBtn.config(text="Your File Is Now Downloading.....")
        dBtn.config(state=DISABLED)
        path_video = askdirectory()
        if path_video is None:
            return

        ob = YouTube(url, on_progress_callback=progressCheck)

        strm = ob.streams.filter(adaptive=True).first()

        file_size = strm.filesize
        vTitle.config(text=strm.title)
        vTitle.pack(side=TOP)
        sTitle.config(text="Video Size: "+str(round(file_size/1048576))+" MB")
        sTitle.pack(side=BOTTOM)

        strm.download(path_video)
        print('done...')
        dBtn.config(text='Click To Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Donate Me :3", "Congrats!! Video Downloaded Successfully")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print('download failed')
        showinfo("Error :((", "Download Failed")
        dBtn.config(text='Click To Start Download')
        dBtn.config(state=NORMAL)


def startDownloadThread():
    thread = Thread(target=start_download)
    thread.start()


# Starting GUI building
main = Tk()
main.title("Youtube Downloader By AVi-test")

# setting icon

main.iconbitmap('youtube1.ico')
main.geometry("500x600")

# setting head image
file = PhotoImage(file="youtube.png")
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=40)

dBtn = Button(main, text="Click To Start Download", font=('verdana', 18), relief='ridge', command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

vTitle = Label(main, text=" Video Title ")
sTitle = Label(main, text="File Size: ")

main.mainloop()
