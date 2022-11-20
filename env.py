import platform


def getFilePath(name):
    plat = platform.system().lower()
    if plat == 'windows':
        return 'C:/Temp/' + name
    elif plat == 'linux':
        return './' + name
    else:
        return './' + name
