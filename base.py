import IPython
from IPython.utils import io
from IPython.display import display,HTML,clear_output
import subprocess

import os
from getpass import getpass
import urllib

import shutil

import time

from google.colab import files
import ipywidgets as widgets

def printh(t,dynamic=False):
  if(dynamic):
    time.sleep(1)
    clear_output(wait=True)
  display(IPython.display.HTML("<p>"+t+"</p>"))

def getapp():
  printh("User name: ")
  user = input('')
  printh("Password: ",True)
  password = getpass('')
  password = urllib.parse.quote(password) # your password is converted into url format
  printh("Repo name: ",True)
  if repo_name==None:
    repo_name = input('')

  cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(user, password, repo_name)
  try:
    os.system(cmd_string)
    cmd_string, password = "", "" # removing the password from the variable
    #os.chdir(repo_name)
    shutil.copy(repo_name+"/main.py", os.getcwd())
    shutil.rmtree(repo_name, ignore_errors=True)
    printh("Repo confirmed. Start building app...", True)
  except(e):
    printh("Cannot access to repo. Please try again.",True)
getapp()
