import psutil

def battery():
    temp = psutil.sensors_battery()
    return round(temp.percent,2)

print(battery())