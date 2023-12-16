#!/usr/bin/python3
# testapp_label_array.py
# Ian Stewart - 2023-12-16
import pathlib
import tkinter.ttk as ttk
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "test.ui"


class TestApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("toplevel2", master)
        builder.connect_callbacks(self)

        #  === End of most of the pygubu generated code ===

        #  === Manually add code for array of labels and button call-backs ===
        self.labelframe_0 = builder.get_object("labelframe1", master)
        self.labelframe_1 = builder.get_object("labelframe2", master)

        #  Instantiate ttk.Style as its used later for styling the labels
        self.style = ttk.Style()

        #  See what text the top label frame has from Design mode.
        print(self.labelframe_0.cget("text"))
        #  See if the text of the top label frame can be changed to something else
        self.labelframe_0.config(text="Register bits")
        print(self.labelframe_0.cget("text"))

        # Set text on bottom label frame.
        self.labelframe_1.config(text="Select Register Contents")


        # Call method to setup the label array in the bit register labelframe.
        self.setup_register_bits()

    def button_cb(self, widget_id):  # <-- Method heading provided by pygubu designer
        #pass
        """
        Manually added...
        Callback for buttons was set in pygubu design mode with Type:"Set Widgit ID".
        Set all register bits to either zeros or ones or a mix of zero and ones.
        Simple loop to update label_list. More complex to update if this was a
        series of individual label objects.
        """
        #print(widget_id)  #  button1, button2,...

        #  zeros
        if  widget_id == "button1":
            for i in range(len(self.label_list)):
                self.label_list[i].config(text = "0")
        #  ones
        if widget_id == "button2":
            for i in range(len(self.label_list)):
                self.label_list[i].config(text = "1")

        #  mix of ones and zeros
        if widget_id == "button3":
            for i in range(0, len(self.label_list), 2):
                self.label_list[i].config(text = "0")
                self.label_list[i+1].config(text = "1")

        if widget_id == "buttonx":
            """
            Alternative for button3.
            Manually edit 'if widget_id == "button3":' to "buttonx" and vica versa
            Fill label array with a random number between 0 and 65535 / hex FFFF
            """
            import random
            dec_integer = random.randint(0, 65535)
            print(dec_integer)
            bin_integer_list = list(bin(dec_integer)[2:].zfill(16))
            for i in range(0, len(self.label_list)):
                self.label_list[i].config(text = bin_integer_list[i])

    def setup_register_bits(self):
        """
        Create an array of labels in the Register Bits Labelframe, self.labelframe_0.
        Fill labels with spaces.
        """
        self.style.configure("Bits.TLabel", borderwidth=1, font=('Helvetica', 11),
                                relief="solid", width = 2, anchor="center")
        self.label_list = []
        for i in range(16):
            self.label_list.append(ttk.Label(self.labelframe_0, text=str(" "),
                                    style="Bits.TLabel",))
            self.label_list[i].grid(row=0, column=i,)

    #  === End of manually written code ===

    #  This method was created by pygubu designer.
    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = TestApp()
    app.run()

