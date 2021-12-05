import wmi

system = wmi.WMI().Win32_ComputerSystem()[0]
print(system)