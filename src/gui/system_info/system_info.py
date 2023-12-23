
from pathlib import Path
import psutil
import time
import platform
import subprocess
# from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def cpu_name1():
    result = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2", shell=True)
    cpu_model = result.decode('utf-8').strip()
    return cpu_model


def sys_info_page(parent,page):
    global update
    def update():
        if(not page):
            print("halt system")
            return
        print("system update called")
        
        canvas.itemconfig(battery, text=str(round(psutil.sensors_battery().percent,2))+"%")
        canvas.itemconfig(mac_name, text=str(platform.machine()))
        canvas.itemconfig(os_name, text=str(platform.system()))
        canvas.itemconfig(os_release, text=str(platform.release()))
        canvas.itemconfig(os_version, text=str(platform.version()))
        canvas.itemconfig(platform_name, text=str(platform.platform()))
        canvas.itemconfig(cpu_name, text=cpu_name1())
        canvas.itemconfig(network, text=str(platform.node()))
        canvas.itemconfig(connect, text=str(len(psutil.net_connections())))
        canvas.after(500, update)
    
    canvas = Canvas(
        parent,
        bg = "#010101",
        height = 693,
        width = 937,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 300, y = 14)
    
    global image_image_1
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        469.0,
        105.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        469.0,
        212.0,
        image=image_image_2
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        469.0,
        341.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        469.0,
        470.0,
        image=image_image_4
    )

    global image_image_5
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        468.0,
        577.0,
        image=image_image_5
    )

    canvas.create_text(
        54.0,
        363.0,
        anchor="nw",
        text="OS Version ",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 20 * -1)
    )

    canvas.create_text(
        53.0,
        577.0,
        anchor="nw",
        text="Networks Connected",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 20 * -1)
    )

    canvas.create_text(
        54.0,
        82.0,
        anchor="nw",
        text="Machine Name",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 36 * -1)
    )

    mac_name=canvas.create_text(
        424.0,
        82.0,
        anchor="nw",
        text="Asus Zephyrus G15",
        fill="#FFFFFF",
        font=("MontserratRoman SemiBold", 36 * -1)
    )

    battery=canvas.create_text(
        424.0,
        198.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 24 * -1)
    )

    os_name=canvas.create_text(
        290.0,
        288.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 20 * -1)
    )

    os_release=canvas.create_text(
        290.0,
        326.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 20 * -1)
    )

    os_version=canvas.create_text(
        290.0,
        370.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 12 * -1)
    )

    platform_name=canvas.create_text(
        290.0,
        439.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 18 * -1)
    )

    cpu_name=canvas.create_text(
        290.0,
        474.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 18 * -1)
    )

    network=canvas.create_text(
        290.0,
        544.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 20 * -1)
    )

    connect=canvas.create_text(
        425.0,
        577.0,
        anchor="nw",
        text="76%",
        fill="#99999B",
        font=("MontserratRoman Medium", 20 * -1)
    )

    canvas.create_text(
        54.0,
        439.0,
        anchor="nw",
        text="Platform Name",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 22 * -1)
    )

    canvas.create_text(
        57.0,
        288.0,
        anchor="nw",
        text="OS Name",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 24 * -1)
    )

    canvas.create_text(
        57.0,
        326.0,
        anchor="nw",
        text="OS Release",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 24 * -1)
    )

    canvas.create_text(
        54.0,
        198.0,
        anchor="nw",
        text="Battery Percentage",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 24 * -1)
    )

    canvas.create_text(
        54.0,
        474.0,
        anchor="nw",
        text="CPU Name",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 22 * -1)
    )

    canvas.create_text(
        363.0,
        16.0,
        anchor="nw",
        text="System Info",
        fill="#DFBAC7",
        font=("Inter Bold", 24 * -1)
    )

    canvas.create_text(
        54.0,
        543.0,
        anchor="nw",
        text="Network Name",
        fill="#DFBAC7",
        font=("MontserratRoman Bold", 20 * -1)
    )

    update()