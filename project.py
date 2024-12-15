from tkinter import Tk, Label, Entry, Button
from pytube import YouTube

def download_high():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    status_label.config(text="Downloaded in High Resolution!")

def download_low():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.get_lowest_resolution()
    stream.download()
    status_label.config(text="Downloaded in Low Resolution!")

def download_audio():
    url = link_entry.get()
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    status_label.config(text="Audio Downloaded!")

root = Tk()
root.title("YouTube Downloader")

title_label = Label(root, text="YouTube Downloader", font=("Arial", 16))
title_label.pack(pady=10)

link_label = Label(root, text="Enter YouTube Link:")
link_label.pack()
link_entry = Entry(root, width=40)
link_entry.pack(pady=5)

high_button = Button(root, text="Download High Quality", command=download_high)
high_button.pack(pady=5)

low_button = Button(root, text="Download Low Quality", command=download_low)
low_button.pack(pady=5)

audio_button = Button(root, text="Download Audio", command=download_audio)
audio_button.pack(pady=5)

status_label = Label(root, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()
