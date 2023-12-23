import psutil
from pathlib import Path

# from tkinter import *

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

global x
x = []
global y
y = []


def ram_usage():
    print("ram usage is", psutil.virtual_memory().percent)
    # return np.random.randint(0, 100)
    return psutil.virtual_memory().percent


counter = count(0, 1)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("937x693")
# window.configure(bg="#010101")


def ram_page(parent, page):
    usage = 0
    global update

    def update():
        if(not page):
            print("halt ram")
            return
        print("ram update called")
        
        global usage
        new_usage = psutil.virtual_memory().percent
        x.append(next(counter))
        y.append(new_usage)

        usage = new_usage
        canvas.itemconfig(tagOrId=usage_entry, text=str(new_usage) + "%")
        canvas.itemconfig(tagOrId=ram_size, text=str(int(psutil.virtual_memory().total / (1024**2))) + "MB")
        canvas.itemconfig(tagOrId=free_ram, text=str(int(psutil.virtual_memory().available / (1024**2))) + "MB")
        canvas.itemconfig(tagOrId=usage_entry, text=str(int(psutil.virtual_memory().used / (1024**2))) + "MB")
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
        ax.fill_between(x, y, alpha=0.5, color="#DB6E8E")
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
    ax.fill_between(x, y, alpha=0.5)
    ax.tick_params(axis="both", colors="white")
    ax.grid(color="#DEBDBF", linestyle="dashed", linewidth=0.5)
    mgraph = FigureCanvasTkAgg(fig, master=canvas)
    mgraph.get_tk_widget().place(x=40, y=75)

    canvas.place(x=300, y=14)
    
    global image_image_1
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(469.0, 249.0, image=image_image_1)

    global image_image_2
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(469.0, 550.0, image=image_image_2)

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
        30.0,
        580.0,
        anchor="nw",
        text="Ram Size",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="RAM Statistics",
        fill="#DFBAC7",
        font=("Inter Bold", 24 * -1),
    )

    ram_size=canvas.create_text(
        30 + 169.0,
        580.0,
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
        30.0+169.0,
        540.0,
        anchor="nw",
        text="3.5GHz",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        30.0,
        540.0,
        anchor="nw",
        text="Free Ram",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # global image_image_6
    # image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    # image_6 = canvas.create_image(124.0, 478.0, image=image_image_6)

    usage_entry=canvas.create_text(
        30 + 169.0,
        500.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        30.0,
        500.0,
        anchor="nw",
        text="Ram Usage",
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
