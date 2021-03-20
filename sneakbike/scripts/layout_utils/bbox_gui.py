import os
from tkinter import Tk, Label, Button, filedialog, colorchooser, W

from bounding_box_creator import BoundingBox


class BBox:
    def __init__(self, master):
        self.master = master
        self.master.title("Bounding Box Creator")
        self.master.geometry("400x150")
        self.save_folder = os.path.expanduser("~")
        self.inner_color = "#62b0ff"
        self.outer_color = "#004080"

        self.btn_save_folder = Button(
            self.master, text="Save to...", command=self.select_folder
        )
        self.btn_save_folder.grid(row=0, column=0)
        self.lbl_save_folder_val = Label(self.master, text=self.save_folder)
        self.lbl_save_folder_val.grid(row=0, column=1)

        self.lbl_color_outer = Label(self.master, text="Outer Color").grid(
            row=1, column=0
        )
        self.lbl_color_inner = Label(self.master, text="Inner Color").grid(
            row=2, column=0
        )

        self.btn_color_outer = Button(
            self.master,
            text="           ",
            command=self.select_color_outer,
            bg=self.outer_color,
        )
        self.btn_color_outer.grid(
            row=1, column=1, sticky=W,
        )

        self.btn_color_inner = Button(
            self.master,
            text="           ",
            command=self.select_color_inner,
            bg=self.inner_color,
        )
        self.btn_color_inner.grid(
            row=2, column=1, sticky=W,
        )

        self.btn_generate = Button(self.master, text="Generate", command=self.generate,)
        self.btn_generate.grid(
            row=3, sticky=W,
        )

    def select_folder(self):
        self.save_folder = filedialog.askdirectory()
        self.lbl_save_folder_val["text"] = self.save_folder

    def select_color_outer(self):
        """ Color is given as (rgb, hx). """
        (_, self.outer_color) = colorchooser.askcolor()
        print(self.outer_color)
        self.btn_color_outer["bg"] = self.outer_color

    def select_color_inner(self):
        """ Color is given as (rgb, hx). """
        (_, self.inner_color) = colorchooser.askcolor()
        self.btn_color_inner["bg"] = self.inner_color

    def generate(self):
        save_folder_with_img_folder = os.path.join(
            self.save_folder, f"bbox_{self.inner_color[1:]}_{self.outer_color[1:]}"
        )
        os.mkdir(save_folder_with_img_folder)

        BoundingBox(
            file_prefix="NES",
            interior_width=512,
            interior_height=480,
            outer_color=self.outer_color,
            inner_color=self.inner_color,
            save_folder=save_folder_with_img_folder,
        )

        BoundingBox(
            file_prefix="SNES",
            interior_width=544,
            interior_height=476,
            outer_color=self.outer_color,
            inner_color=self.inner_color,
            save_folder=save_folder_with_img_folder,
        )

        BoundingBox(
            file_prefix="GENESIS",
            interior_width=640,
            interior_height=448,
            outer_color=self.outer_color,
            inner_color=self.inner_color,
            save_folder=save_folder_with_img_folder,
        )

        BoundingBox(
            file_prefix="NAMEPLATE",
            interior_width=375,
            interior_height=90,
            outer_color=self.outer_color,
            inner_color=self.inner_color,
            save_folder=save_folder_with_img_folder,
        )


root = Tk()
bbox = BBox(root)
root.mainloop()
