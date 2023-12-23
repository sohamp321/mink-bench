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

from src.backend.cpu_stats.cpu_backend import battery

global x
x = []
global y
y = []



# def temp(data):
#     sensor1 = data['nvme']
#     sensor2 = data['nvme']
#     avg_temp = (sensor1[1][1] + sensor2[1][1])/2
#     return avg_temp

# data = psutil.sensors_temperatures()

# def cpu_usage():
#     print("cpu usage is", psutil.cpu_percent())
#     # return np.random.randint(0, 100)
#     return psutil.cpu_percent()


counter = count(0, 1)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

import os

# Set the current working directory to the project's root directory
project_root = os.path.dirname(os.path.abspath(__file__))  # Get the directory of your script
os.chdir(project_root)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("937x693")
# window.configure(bg="#010101")

import subprocess

def get_l2_capacity():
    result = subprocess.check_output("lscpu | grep -E 'L2|L3' | awk '{print $3}'", shell=True)
    cache_info = result.decode('utf-8').strip().split('\n')
    l2_cache_size = cache_info[0]
    l3_cache_size = cache_info[1] if len(cache_info) > 1 else "N/A"
    return l2_cache_size

def get_l3_capacity():
    result = subprocess.check_output("lscpu | grep -E 'L2|L3' | awk '{print $3}'", shell=True)
    cache_info = result.decode('utf-8').strip().split('\n')
    l2_cache_size = cache_info[0]
    l3_cache_size = cache_info[1] if len(cache_info) > 1 else "N/A"
    return l3_cache_size



def cpu_page(parent,page):
    
    usage = 0
    global update
    global usage_entry

    def update():
        
        if(not page):
            print("halt cpu")
            return
        print("cpu update called")
    
        
        
        global usage
        new_usage = psutil.cpu_percent()
        x.append(next(counter))
        y.append(new_usage)

        usage = new_usage
        canvas.itemconfig(tagOrId=usage_entry, text=str(new_usage) + "%")
        
        # take average of sensor1 and sensor2 temperature
        # avg_temp = (psutil.sensors_temperatures()['coretemp'][0].current + psutil.sensors_temperatures()['coretemp'][1].current)/2
        # only plot last 60 points
        # canvas.itemconfig(clock_speed, text=str(psutil.cpu_freq().current/1000)+"GHz")
        canvas.itemconfig(battery_percent, text=str(round(psutil.sensors_battery().percent,2))+"%")
        canvas.itemconfig(Curr_speed, text=str(round(psutil.cpu_freq().current/1000,2))+"GHz")
        canvas.itemconfig(curr_temp, text=str((psutil.sensors_temperatures()['nvme'][1][1]+psutil.sensors_temperatures()['nvme'][2][1])/2)+"°C")
        canvas.itemconfig(phy_cores, text=str(psutil.cpu_count(logical=False)))
        canvas.itemconfig(log_cores, text=str(psutil.cpu_count(logical=True)))
        canvas.itemconfig(max_speed, text=str(round(psutil.cpu_freq().max/1000,2))+"GHz")
        # canvas.itemconfig(ram, text=str(round(psutil.virtual_memory().total/(1024**3),2))+"GB")
        canvas.itemconfig(L3_mem, text=str(get_l3_capacity())+"KB")
        canvas.itemconfig(L2_mem, text=str(get_l2_capacity())+"KB")
        canvas.itemconfig(cpu_int, text=str(psutil.cpu_stats().interrupts))
        canvas.itemconfig(calls, text=str(psutil.cpu_stats().syscalls))
        canvas.itemconfig(con_swi, text=str(psutil.cpu_stats().ctx_switches))
        plot()

        canvas.itemconfig(tagOrId=mgraph, figure=fig)

        canvas.after(500, update)
    def plot():
        if len(x) > 30:
            x.pop(0)
            y.pop(0)
        ax.cla()
        ax.set_facecolor("#1A1A25")
        ax.fill_between(x, y, alpha=0.5, color="#2b8da3")
        # label = "CPU Usage: " + str(usage) + "%"
        ax.set_title("CPU Usage chart", color="white", fontweight="bold")
        ax.set_xlabel("Time", color="white")
        ax.set_ylabel("Usage %", color="white")
        # ax.set_ylim(0, 100)
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
    image_2 = canvas.create_image(469.0, 578.0, image=image_image_2)

    canvas.create_text(
        29.0,
        529.0,
        anchor="nw",
        text="Max Speed",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        491.0,
        568.0,
        anchor="nw",
        text="Logical Processors",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # canvas.create_text(
    #     29.0,
    #     568.0,
    #     anchor="nw",
    #     text="Ram",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    canvas.create_text(
        29.0,
        607.0,
        anchor="nw",
        text="Physical Cores",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    global image_image_3
    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(584.0, 478.0, image=image_image_3)

    canvas.create_text(
        487.0,
        466.0,
        anchor="nw",
        text="Battery",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="CPU Statistics",
        fill="#DFBAC7",
        font=("Inter Bold", 24 * -1),
    )

    battery_percent = canvas.create_text(
        609.0,
        466.0,
        anchor="nw",
        text="25W",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    global image_image_4
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(814.0, 478.0, image=image_image_4)

    global image_image_5
    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(354.0, 478.0, image=image_image_5)

    Curr_speed=canvas.create_text(
        370.0,
        466.0,
        anchor="nw",
        text="3.5GHz",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        261.0,
        466.0,
        anchor="nw",
        text="Speed",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    global image_image_6
    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(124.0, 478.0, image=image_image_6)

    usage_entry=canvas.create_text(
        169.0,
        466.0,
        anchor="nw",
        text="5",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        23.0,
        466.0,
        anchor="nw",
        text="CPU Usage",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        714.0,
        466.0,
        anchor="nw",
        text="Temperature",
        fill="#DFBAC7",
        font=("MontserratRoman Medium", 14 * -1),
    )

    curr_temp = canvas.create_text(
        849.0,
        469.0,
        anchor="nw",
        text="50°C",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 12 * -1),
    )

    max_speed=canvas.create_text(
        161.0,
        529.0,
        anchor="nw",
        text="3.2GHz",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # ram=canvas.create_text(
    #     160.0,
    #     568.0,
    #     anchor="nw",
    #     text="1",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    phy_cores=canvas.create_text(
        190.0,
        607.0,
        anchor="nw",
        text="8",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        274.0,
        529.0,
        anchor="nw",
        text="L3 cache",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        274.0,
        568.0,
        anchor="nw",
        text="L2 cache",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        274.0,
        607.0,
        anchor="nw",
        text="Cpu Interupts",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    L3_mem=canvas.create_text(
        400.0,
        529.0,
        anchor="nw",
        text="512KB",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    L2_mem=canvas.create_text(
        397.0,
        568.0,
        anchor="nw",
        text="4.0MB",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    cpu_int=canvas.create_text(
        424.0,
        607.0,
        anchor="nw",
        text="16.0MB",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        491.0,
        529.0,
        anchor="nw",
        text="Context Switches",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    canvas.create_text(
        29.0,
        568.0,
        anchor="nw",
        text="Sys Calls",
        fill="#99999B",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # canvas.create_text(
    #     499.0,
    #     607.0,
    #     anchor="nw",
    #     text="Context Switches",
    #     fill="#99999B",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    con_swi=canvas.create_text(
        695.0,
        529.0,
        anchor="nw",
        text="369",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    calls=canvas.create_text(
        127.0,
        568.0,
        anchor="nw",
        text="6040",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )

    # con_swt=canvas.create_text(
    #     720.0,
    #     607.0,
    #     anchor="nw",
    #     text="158479",
    #     fill="#FFFFFF",
    #     font=("MontserratRoman Medium", 16 * -1),
    # )

    log_cores=canvas.create_text(
        693.0,
        568.0,
        anchor="nw",
        text="16",
        fill="#FFFFFF",
        font=("MontserratRoman Medium", 16 * -1),
    )
    update()
