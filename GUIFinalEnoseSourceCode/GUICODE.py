import tkinter as tk
from tkinter import ttk
import csv

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create a Treeview widget with columns for date, time, label, MQ2, MQ7, MQ135, temperature, and humidity
        self.tree = ttk.Treeview(self, columns=("date", "time", "MQ2", "MQ7", "MQ135", "temperature", "humidity", "label"))
        self.tree.pack(side="left")

        # add headings for each column
        self.tree.heading("date", text="Date")
        self.tree.heading("time", text="Time")
        self.tree.heading("label", text="Label")
        self.tree.heading("MQ2", text="MQ2")
        self.tree.heading("MQ7", text="MQ7")
        self.tree.heading("MQ135", text="MQ135")
        self.tree.heading("temperature", text="Temperature")
        self.tree.heading("humidity", text="Humidity")

        # add vertical scrollbar to the right of the treeview widget
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=vsb.set)

        # add horizontal scrollbar to the bottom of the treeview widget
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        hsb.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=hsb.set)

        # read the CSV file and add the data to the treeview widget
        with open("/home/airquality/Desktop/Sensor_R_CSV/enosedataTestDATA.csv", "r") as f:
            reader = csv.reader(f)
            # skip the header row
            next(reader)
            for row in reader:
                self.tree.insert("", "end", values=row)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
