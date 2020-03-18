from flask import Blueprint
import wmi,win32com
import pythoncom
#申明一个蓝图对象
windowsInfo_page = Blueprint('windowsInfo_page',__name__)

@windowsInfo_page.route('/get_windowsInfo')
def get_windowsInfo():
    pythoncom.CoInitialize()
    winIfo = wmi.WMI()
    result = winIfo.Win32_Processor()
    for cpu in result:
        print(cpu)
        print('cpu个数：',len(result))
        print("cpu核心数",cpu.NumberOfCores)
        print("cpu型号", cpu.Name)
    import json
    obj = winIfo.Win32_ComputerSystem()[0]
    print("机器型号", obj.model)
    print("制造商", obj.Manufacturer)
    print(obj)
    pythoncom.CoUninitialize()
    print(result)
    return str(result)