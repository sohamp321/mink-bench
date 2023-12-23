import psutil
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import numpy as np
from itertools import count
import pandas as pd
from matplotlib import style
from data import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

from itertools import count

import subprocess

# Run the 'glxinfo -B' command and capture the output
output = subprocess.check_output(['glxinfo', '-B'], universal_newlines=True)

# Initialize variables to store GPU information
vendor = None
device = None
video_memory = None
total_available_memory = None

# Split the output into lines and search for relevant information
lines = output.split('\n')
for line in lines:
    if "Vendor:" in line:
        vendor = line.split("Vendor:")[1].strip()
    if "Device:" in line:
        device = line.split("Device:")[1].strip()
    if "Video memory:" in line:
        video_memory = line.split("Video memory:")[1].strip().split()[0]
    if "Currently available dedicated video memory:" in line:
        total_available_memory = line.split("Currently available dedicated video memory:")[1].strip().split()[0]


video_memory=video_memory[0:len(video_memory)-2]
video_memory = int(video_memory)
total_available_memory = int(total_available_memory)
print(video_memory)
print(total_available_memory)
global x
x = []
global y
y = []

# print(((video_memory-total_available_memory)/video_memory)*100)

# print(type(total_available_memory))
def gpu_usage():
    yy=((video_memory-total_available_memory)/video_memory)*100
    # return np.random.randint(0, 100)
    gpu_per=yy
    return gpu_per
print(gpu_usage())
counter = count(0, 1)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("937x693")
# window.configure(bg="#010101")


def gpu_page(parent, page):
    usage = 0
    global update

    def update():
        
        if(not page):
            print("halt gpu")
            return
        print("gpu update called")
        
        global usage
        gpu_usage()
        new_usage = gpu_usage()
        # print(new_usage)
        x.append(next(counter))
        y.append(new_usage)

        usage = new_usage
        canvas.itemconfig(tagOrId=usage_entry, text=str(new_usage) + "%")
        canvas.itemconfig(tagOrId=ram_size, text=str(video_memory )+ "MB")
        # print(video_memory)
        canvas.itemconfig(tagOrId=free_ram, text=str(total_available_memory) + "MB")
        # print(total_available_memory)
        canvas.itemconfig(tagOrId=usage_entry, text=str(video_memory-total_available_memory) + "MB")
        # only plot last 60 points  

        plot()

        canvas.itemconfig(tagOrId=mgraph, figure=fig)

        canvas.after(500, update)
    def plot():
        if len(x) > 30:
            x.pop(0)
            y.pop(0)
        ax.cla()
        ax.set_facecolor("#1A1A25")
        ax.fill_between(x, y, alpha=0.4, color="#AEF359")
        ax.set_title("RAM Usage chart", color="white", fontweight="bold")
        ax.set_xlabel("Time", color="white")
        ax.set_ylabel("Usage %", color="white")   
        ax.set_ylim(0, 100)
        ax.tick_params(axis="both", colors="white")
        ax.grid(color="#A8A4C3", linestyle="dashed", linewidth=0.5)
        mgraph.draw()
    
    canvas = Canvas(
        parent,
        bg="#010101",
        height=693,
        width=937,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )

    # adding figure badi mehnat se
    global fig
    fig = Figure(figsize=(8.5, 3.5), facecolor="#1A1A25")
    ax = fig.add_subplot()
    ax.set_facecolor("#1A1A25")
    ax.fill_between(x, y, alpha=0.4)
    ax.tick_params(axis="both", colors="white")
    ax.grid(color="#DEBDBF", linestyle="dashed", linewidth=0.5)
    mgraph = FigureCanvasTkAgg(fig, master=canvas)
    mgraph.get_tk_widget().place(x=40, y=75)

    canvas.place(x=300, y=14)
    
    global image_image_1
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(469.0, 249.0, image=image_image_1)

    # global image_image_2
    # image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    # image_2 = canvas.create_image(469.0, 578.0, image=image_image_2)

    # canvas.create_text(
    #     29.0,
    #     529.0,
    #     anchor="nw",
    #     text="Base Speed",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     731.0,
    #     524.0,
    #     anchor="nw",
    #     text="Logical\nProcessors",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     29.0,
    #     568.0,
    #     anchor="nw",
    #     text="Sockets",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     29.0,
    #     607.0,
    #     anchor="nw",
    #     text="Cores",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # global image_image_3
    # image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    # image_3 = canvas.create_image(584.0, 478.0, image=image_image_3)

    canvas.create_text(
        23.0,
        600.0,
        anchor="nw",
        text="Gpu Size",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="Gpu Statistics",
        fill="#DFBAC7",
        font=("Inter Bold", 24 * -1),
    )

    ram_size=canvas.create_text(
        169.0,
        600.0,
        anchor="nw",
        text="25W",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # global image_image_4
    # image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    # image_4 = canvas.create_image(814.0, 478.0, image=image_image_4)

    # global image_image_5
    # image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    # image_5 = canvas.create_image(354.0, 478.0, image=image_image_5)

    free_ram=canvas.create_text(
        169.0,
        550.0,
        anchor="nw",
        text="3.5GHz",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        23.0,
        550.0,
        anchor="nw",
        text="Free Gpu",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # global image_image_6
    # image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    # image_6 = canvas.create_image(124.0, 478.0, image=image_image_6)

    usage_entry=canvas.create_text(
        169.0,
        490.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        23.0,
        490.0,
        anchor="nw",
        text="Gpu Usage",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # canvas.create_text(
    #     724.0,
    #     466.0,
    #     anchor="nw",
    #     text="Ram Size",
    #     fill="#DFBAC7",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     859.0,
    #     466.0,
    #     anchor="nw",
    #     text="50°C",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     161.0,
    #     529.0,
    #     anchor="nw",
    #     text="3.2GHz",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     192.0,
    #     568.0,
    #     anchor="nw",
    #     text="1",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     190.0,
    #     607.0,
    #     anchor="nw",
    #     text="8",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     274.0,
    #     529.0,
    #     anchor="nw",
    #     text="L1 Cache",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     274.0,
    #     568.0,
    #     anchor="nw",
    #     text="L2 Cache",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     274.0,
    #     607.0,
    #     anchor="nw",
    #     text="L3 Cache",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     400.0,
    #     529.0,
    #     anchor="nw",
    #     text="512KB",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     397.0,
    #     568.0,
    #     anchor="nw",
    #     text="4.0MB",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     394.0,
    #     607.0,
    #     anchor="nw",
    #     text="16.0MB",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     491.0,
    #     529.0,
    #     anchor="nw",
    #     text="Processes",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     501.0,
    #     568.0,
    #     anchor="nw",
    #     text="Threads",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     499.0,
    #     607.0,
    #     anchor="nw",
    #     text="Handles ",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )










    # canvas.create_text(
    #     635.0,
    #     529.0,
    #     anchor="nw",
    #     text="369",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     627.0,
    #     568.0,
    #     anchor="nw",
    #     text="6040",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     619.0,
    #     607.0,
    #     anchor="nw",
    #     text="158479",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    # canvas.create_text(
    #     888.0,
    #     536.0,
    #     anchor="nw",
    #     text="16",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )
    update()
