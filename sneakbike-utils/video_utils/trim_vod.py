import os
import subprocess
from datetime import datetime
from pathlib import Path
from tkinter import Tk, Label, Button, N, S, E, W, Frame, Entry
from tkinter.filedialog import askopenfilename


class TrimVOD(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.rowconfigure(10, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.grid(row=0, column=0, sticky=W + E + N + S)

        instructions = """
1. Click 'Select VOD' to select the vod.
2. Put the amount of time to cut from the
start in HH:MM:SS format.

(e.g., put 00:05:20 for five minutes twenty seconds.)

3. Click 'Clip VOD'.

If there is an error, read the included txt file.
"""

        self.master.title("Trimming Start and End of VODs")

        self.trim_intro_lbl = Label(self, text=instructions, justify="left")
        self.trim_intro_lbl.grid(row=1, column=0, columnspa=2, sticky=W)

        self.btn_select = Button(self, text="Select VOD", command=self.get_vod)
        self.btn_select.grid(row=2, column=0, columnspan=2, sticky=W)

        self.trim_start_lbl = Label(self, text="HH:MM:SS off start")
        self.trim_start_lbl.grid(row=3, column=0, sticky=W)
        self.trim_start_entry = Entry(self)
        self.trim_start_entry.grid(row=3, column=1)

        # self.trim_end_lbl = Label(self, text="M:S off end")
        # self.trim_end_lbl.grid(row=4, column=0, sticky=W)
        # self.trim_end_entry = Entry(self, width=20)
        # self.trim_end_entry.grid(row=4, column=1)

        self.btn_clip = Button(self, text="Clip VOD", command=self.clip_vod)
        self.btn_clip.grid(row=5, column=0, sticky=W)

        self.success_lbl = Label(self, text="")
        self.success_lbl.grid(row=6, column=0, columnspan=2, sticky=W)

    def get_vod(self):
        self.fname = Path(
            askopenfilename(
                title="Select file",
                filetypes=(
                    ("MP4 files", "*.mp4"),
                    ("AVI files", "*.avi"),
                    ("all files", "*.*"),
                ),
            )
        )

    def clip_vod(self):
        self.current_dir = Path(__file__).parent.absolute()

        self.ffmpeg_loc = self.current_dir.joinpath("ffmpeg.exe")
        if not self.ffmpeg_loc.is_file():
            raise FileNotFoundError("Cannot find ffmpeg.exe in the current directory.")

        self.dname = self.fname.parent
        self.new_fname = self.dname.joinpath(f"{self.fname.stem}_clipped.mp4")

        if self.new_fname.is_file():
            # If the file already exists, delete it and create a new one.
            os.remove(self.new_fname)

        self.cmd = [
            self.ffmpeg_loc,
            "-i",
            self.fname,
            "-ss",
            f"{self.trim_start_entry.get()}",
            self.new_fname,
        ]
        self.process = subprocess.run(self.cmd, capture_output=True)
        print(self.process)
        self.success_lbl["text"] = f"Clipped!"


TrimVOD().mainloop()
