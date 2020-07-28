from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def progressCheck(stream=None, chunk=None, file_handle=None, remaining=None):
    percentage = [(file_size - remaining) / file_size] * 100
    dBtn.config("{:00.0f} downloaded.format(percentage)")


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

        strm = ob.streams.first()
        file_size = strm.filesize

        strm.download(path_video)
        print('done...')
        dBtn.config(text='Click To Start Download')
        dBtn.config(state=NORMAL)
        showinfo("Donate Me :3", "Congrats!! Video Downloaded Successfully")
        urlField.delete(0, END)

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
main.title("Youtube Downloader By AVi")

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

main.mainloop()
