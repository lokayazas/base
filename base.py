import IPython
from IPython.utils import io
from IPython.display import display,HTML,clear_output
import subprocess

import os
from getpass import getpass
import urllib

from shutil import copy

def printh(t,dynamic=False):
  if(dynamic):
    time.sleep(1)
    clear_output(wait=True)
  display(IPython.display.HTML("<p>"+t+"</p>"))

def getapp():
  printh("User name: ")
  user = input('')
  printh("Password: ")
  password = getpass('')
  password = urllib.parse.quote(password) # your password is converted into url format
  printh("Repo name: ")
  repo_name = input('')

  cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(user, password, repo_name)

  os.system(cmd_string)
  cmd_string, password = "", "" # removing the password from the variable
  #os.chdir(repo_name)
  copyfile(repo_name+"/main.py", os.getcwd())

getapp()
