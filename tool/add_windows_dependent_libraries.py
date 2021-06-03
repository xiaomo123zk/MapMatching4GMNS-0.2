# @author       Kai (Frank) Zhang (zhangk2019@seu.edu.cn)
# @time         2021/5/8 9:11
# @desc         [script description]

import os.path
from sys import platform
import shutil


def add_libraries():
    if platform.startswith('win32'):
        filePath = os.path.join(os.path.dirname(
            __file__), 'Dependent_libraries_missing_in_windows_system/')

    systemPath = 'C:/Windows/System32/'
    if(os.path.isfile(systemPath+'kernel32.dll') == False):
        shutil.copy(filePath+'kernel32.dll', systemPath)
    if(os.path.isfile(systemPath+'msvcp140d.dll') == False):
        shutil.copy(filePath+'msvcp140d.dll', systemPath)
    if(os.path.isfile(systemPath+'ucrtbased.dll') == False):
        shutil.copy(filePath+'ucrtbased.dll', systemPath)
    if(os.path.isfile(systemPath+'vcomp140d.dll') == False):
        shutil.copy(filePath+'vcomp140d.dll', systemPath)
    if(os.path.isfile(systemPath+'vcruntime140d.dll') == False):
        shutil.copy(filePath+'vcruntime140d.dll', systemPath)
    if(os.path.isfile(systemPath+'vcruntime140_1d.dll') == False):
        shutil.copy(filePath+'vcruntime140_1d.dll', systemPath)


if __name__ == "__main__":
    add_libraries()

    '''
    #If an error occurs: [Errno 13] Permission denied: 'C:/Windows/System32/*.dll',
    # you need to manually copy the dependency library 
    # from folder Dependent_libraries_missing_in_windows_system to Windows System Folder C:/Windows/System32/.

    Note: If your windows system has existed some dependencies in the C:\Windows\System32, 
    you only need to copy the dependency libraries that are not.
    '''
