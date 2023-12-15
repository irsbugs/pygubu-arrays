#!/usr/bin/python3
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

    def run(self):
        self.mainwindow.mainloop()

    def button_cb(self, widget_id):
        pass


if __name__ == "__main__":
    app = TestApp()
    app.run()
