import os
import subprocess
import ctypes
import sys
from tkinter import * 
from tkinter import messagebox
import webbrowser

  

  
messagebox.showwarning("Critical", "This installer for Changed requires Git")

try:
  os_cmd = 'git'
  #print(subprocess.call(os_cmd, shell=True))
  if len(subprocess.call(os_cmd, shell=True)) <= 40:
      messagebox.showerror("Failed to init git.", "We are installing git automatically, Please make sure you have sufficient disk space.")
      raise Exception('Git does not exist on system. Installing now.')
      webbrowser.open("https://git-scm.com/")

      #webbrowser.open("https://git-scm.com/")
      #if os.system("winget install --id Git.Git -e --source winget") != 0:
      #    messagebox.showerror("Failed winget install.", "Please manually install Git here.")
      #    webbrowser.open("https://git-scm.com/")
  else :
      #print("Git found on system.")
      messagebox.showinfo("Confirmed!", "Git has been found on the system.")
except:
  pass

  
def requestUAC():
    ctypes.windll.shell32.IsUserAnAdmin() or (ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1) > 32, sys.exit())
requestUAC()

installDirectory = os.environ["ProgramFiles"]
os.system(f'git -C "{installDirectory}" clone https://github.com/Iurq/veria.git')