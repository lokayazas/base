import rpn

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

def getlib(py_name,user=None,password=None,repo_name="tasks"):
  if user == None:
    printh("User name: ")
    user = input('')
  if password == None:
    printh("Password: ",True)
    password = getpass('')
  password = urllib.parse.quote(password) # your password is converted into url format
  if rpn.name==None:
    printh("Repo name: ",True)
    repo_name = input('')
  else:
    repo_name = rpn.name

  cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(user, password, repo_name)
  try:
    os.system(cmd_string)
    cmd_string, password = "", "" # removing the password from the variable
    #os.chdir(repo_name)
    shutil.copy(repo_name+"/"+py_name, os.getcwd())
    shutil.rmtree(repo_name, ignore_errors=True)
    printh("Repo confirmed. Start building app...", True)
  except(e):
    printh("Cannot access to repo. Please try again.",True)
