import os
import subprocess
from datetime import datetime
from pathlib import Path
from tkinter import Tk, Label, Button, N, S, E, W, Frame
from tkinter.filedialog import askopenfilename


class RawAVItoQTRLE(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W + E + N + S)

        self.master.title("Raw AVI with Alpha to QTRLE")
        self.btn = Button(
            self, text="Select Raw AVI w/ Alpha", command=self.convert, width=80
        )
        self.btn.grid(row=1, column=0, sticky=W)

        self.success_lbl = Label("", width=80)
        self.success_lbl.grid(row=2, column=0, sticky=W)

    def convert(self):
        self.fname = Path(
            askopenfilename(
                title="Select file",
                filetypes=(("AVI files", "*.avi"), ("all files", "*.*")),
            )
        )

        self.success_lbl["text"] = "Converting file..."
        self.current_dir = Path(__file__).parent.absolute()
        self.ffmpeg_loc = self.current_dir.joinpath("ffmpeg.exe")
        if not self.ffmpeg_loc.is_file():
            raise FileNotFoundError("Cannot find ffmpeg.exe in the current directory.")

        self.dname = self.fname.parent
        self.new_fname = self.dname.joinpath(f"{self.fname.stem}.mov")

        if self.new_fname.is_file():
            # If the file already exists, delete it and create a new one.
            os.remove(self.new_fname)

        self.cmd = [self.ffmpeg_loc, "-i", self.fname, "-c:v", "qtrle", self.new_fname]
        self.process = subprocess.run(self.cmd, capture_output=True)
        print(self.process)
        self.success_lbl["text"] = f"{self.new_fname} created at {datetime.now()}."


RawAVItoQTRLE().mainloop()
