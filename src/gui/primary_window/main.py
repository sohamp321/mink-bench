from src.gui.cpu_stats.cpu_stats import cpu_page
from src.gui.gpu_stats.gpu_stats import gpu_page
from src.gui.ram_stats.ram_stats import ram_page
from src.gui.disk_stats.disk_stats import disk_page
from src.gui.benchmark.benchmark_4 import benchmark_page
from src.gui.about.about import about_page
from src.gui.system_info.system_info import sys_info_page


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def hide_underline():
    # canvas.itemconfig(id, state='hidden'/'normal') 
    canvas.itemconfig(tagOrId=benchmarking_underline,state='hidden')
    canvas.itemconfig(tagOrId=about_underline,state='hidden')
    canvas.itemconfig(tagOrId=gpu_underline,state='hidden')
    canvas.itemconfig(tagOrId=disk_underline,state='hidden')
    canvas.itemconfig(tagOrId=ram_underline,state='hidden')
    canvas.itemconfig(tagOrId=cpu_underline,state='hidden')
    canvas.itemconfig(tagOrId=sys_info_underline,state='hidden')



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# def handle_button_press(btn_name):
#     hide_underline()
#     global current_window
#     if btn_name == "cpu":
#         cpu_btn_clicked()
#         canvas.itemconfig(cpu_underline,state='normal')
#         gpu_page(window,0)
#         ram_page(window,0)
#         disk_page(window,0)
#         sys_info_page(window,0)
#         current_window = cpu_page(window, 1)
#     elif btn_name == "gpu":
#         gpu_btn_clicked()
#         canvas.itemconfig(gpu_underline,state='normal')
#         cpu_page(window, 0)
#         ram_page(window,0)
#         disk_page(window,0)
#         sys_info_page(window,0)
#         current_window = gpu_page(window,1)
#     elif btn_name == "ram":
#         ram_btn_clicked()
#         canvas.itemconfig(ram_underline,state='normal')
#         cpu_page(window,0)
#         gpu_page(window,0)
#         disk_page(window,0)
#         sys_info_page(window,0)
#         current_window = ram_page(window,1)
#     elif btn_name == "disk":
#         disk_btn_clicked()
#         canvas.itemconfig(disk_underline,state='normal')
#         cpu_page(window,0)
#         gpu_page(window,0)
#         ram_page(window,0)
#         sys_info_page(window,0)
#         current_window = disk_page(window,1)
#     elif btn_name == "benchmarking":
#         benchmark_btn_clicked()
#         canvas.itemconfig(benchmarking_underline,state='normal')
#         cpu_page(window,0)
#         gpu_page(window,0)
#         ram_page(window,0)
#         disk_page(window,0)
#         sys_info_page(window,0)
#         current_window = benchmark_page(window)
#     elif btn_name == "about":
#         about_btn_clicked()
#         canvas.itemconfig(about_underline,state='normal')
#         cpu_page(window,0)
#         gpu_page(window,0)
#         ram_page(window,0)
#         disk_page(window,0)
#         sys_info_page(window,0)
#         current_window = about_page(window)
#     elif btn_name == "sys_info":
#         sys_info_btn_clicked()
#         canvas.itemconfig(sys_info_underline,state='normal')
#         cpu_page(window,0)
#         gpu_page(window,0)
#         ram_page(window,0)
#         disk_page(window,0)
#         current_window = sys_info_page(window,1)
    
    
        
def cpu_btn_clicked():
    print("cpu button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def gpu_btn_clicked():
    print("gpu button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def ram_btn_clicked():
    print("ram button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def disk_btn_clicked():
    print("disk button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def benchmark_btn_clicked():
    print("benchmark button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def about_btn_clicked():
    print("about button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)
def sys_info_btn_clicked():
    print("sys_info button clicked")
    # canvas.itemconfig(page_navigator, text="cpu")
    sidebar_navigator.place(x=0, y=133)

window = Tk()
window.title("Mink")
window.geometry("1280x720")
window.configure(bg = "#010101")

canvas = Canvas(
    window,
    bg = "#010101",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    152.0,
    360.0,
    image=image_image_1
)

# current_window = about_page(window)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
btn_about = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("about"),
    relief="flat"
)

btn_about.place(
    x=65.0,
    y=641.0,
    width=175.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
btn_benchmarking = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("benchmarking"),
    relief="flat"
)

btn_benchmarking.place(
    x=37.0,
    y=362.0,
    width=225.0,
    height=40.0
)

sys_info_underline = canvas.create_rectangle(
    38.0,
    356.0,
    264.0000305175781,
    357.4787292480469,
    fill="#3C3C45",
    outline="")

benchmarking_underline=canvas.create_rectangle(
    78.0,
    403.0,
    249.0,
    404.0,
    fill="#DFBAC7",
    outline="") ##Benchamrking Underline

about_underline=canvas.create_rectangle(
    125.0,
    689.0,
    205.99981689453125,
    690.1702117919922,
    fill="#DFBAC7",
    outline="") ##ABout Underline

gpu_underline=canvas.create_rectangle(
    102.0,
    300.0,
    157.9998779296875,
    301.1170196533203,
    fill="#DFBAC7",
    outline="")   ##GPU Underline

disk_underline=canvas.create_rectangle(
    101.99526977539062,
    343.5104217529297,
    158.00430297851562,
    346.4389419555664,
    fill="#DFBAC7",
    outline="")  ##DISK Underline

ram_underline=canvas.create_rectangle(
    102.00006103515625,
    251.87872314453125,
    160.00003051757812,
    253.12127685546875,
    fill="#DFBAC7",
    outline="") ##RAM Underline

cpu_underline=canvas.create_rectangle(
    101.995849609375,
    200.69244384765625,
    154.73220825195312,
    203.71759033203125,
    fill="#DFBAC7",
    outline="") ## CPU Underline

sys_info_underline =canvas.create_rectangle(
    78.0,
    157.0,
    219.0,
    158.0,
    fill="#DFBAC7",
    outline="") ##Underline

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
btn_disk = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("disk"),
    relief="flat"
)

btn_disk.place(
    x=39.0,
    y=307.0,
    width=225.0,
    height=36.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
btn_gpu = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("gpu"),
    relief="flat"
)
btn_gpu.place(
    x=37.0,
    y=255.0,
    width=225.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
btn_ram = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("ram"),
    relief="flat"
)
btn_ram.place(
    x=39.0,
    y=209.0,
    width=225.0,
    height=36.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
btn_cpu = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("cpu"),
    relief="flat"
)
btn_cpu.place(
    x=39.0,
    y=160.0,
    width=225.0,
    height=40.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
btn_sys_info = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: handle_button_press("sys_info"),
    relief="flat"
)
btn_sys_info.place(
    x=37.0,
    y=112.0,
    width=225.0,
    height=40.0
)

canvas.create_text(
    52.0,
    32.0,
    anchor="nw",
    text="MinkBench",
    fill="#DFBAC7",
    font=("Montserrat ExtraBold", 30 * -1)
)

canvas.create_rectangle(
    326.0,
    14.0,
    1263.0,
    707.0,
    fill="#010101",
    outline="")

# sidebar_navigator
sidebar_navigator = Frame(background="#FFFFFF")
sidebar_navigator.place(x=0, y=133, height=47, width=7)

# page_navigator
# page_navigator = canvas.create_text(
#     52.0, 80.0, anchor="nw", text="cpu", fill="#FFFFFF", font=("Inter Bold", 24 * -1)
# )
hide_underline()
canvas.itemconfig(sys_info_underline,state='normal')

window.resizable(False, False)
window.mainloop()
