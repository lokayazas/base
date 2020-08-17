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

import importlib

from google.colab import files
import ipywidgets as widgets



def printh(t,dynamic=False):
  if(dynamic):
    time.sleep(1)
    clear_output(wait=True)
  display(IPython.display.HTML("<p>"+t+"</p>"))

'''
def getapp():
  printh("User name: ")
  user = input('')
  printh("Password: ",True)
  password = getpass('')
  password = urllib.parse.quote(password) # your password is converted into url format
  repo_name = ""
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
    shutil.copy(repo_name+"/main.py", os.getcwd())
    shutil.rmtree(repo_name, ignore_errors=True)
    printh("Repo confirmed. Start building app...", True)
  except(e):
    printh("Cannot access to repo. Please try again.",True)
'''

def getlib(py_names,repo_name="tasks",isgetapp=False):
  if rpn.user == None:
    printh("User name: ")
    rpn.user = input('')
  if rpn.password == None:
    printh("Password: ",True)
    rpn.password = getpass('')
  password = urllib.parse.quote(rpn.password) # your password is converted into url format
  if repo_name=="":
    if rpn.name==None:
      printh("Repo name: ",True)
      repo_name = input('')
    else:
      repo_name = rpn.name

  cmd_string = 'git clone https://{0}:{1}@github.com/{0}/{2}.git'.format(rpn.user, rpn.password, repo_name)
  try:
    os.system(cmd_string)
    if not isgetapp:
      cmd_string, password = "", "", "" # removing the password from the variable
      rpn.user = None
      rpn.password = None
    else:
      cmd_string = ""
    #os.chdir(repo_name)
    for pyn in py_names:
      shutil.copy(repo_name+"/"+pyn+".py", os.getcwd())
    shutil.rmtree(repo_name, ignore_errors=True)
    printh("Repo confirmed. Start building app...", True)
  except:
    printh("Cannot access to repo. Please try again.",True)
    
def getapp():
  getlib(["main"],repo_name="",isgetapp=True)

'''
def getandimportlib(py_names):
  getlib(py_names)
  tasks = {}
  for pyn in py_names:
    tasks[pyn] = importlib.import_module(pyn)
  return tasks
'''

try:
  if rpn.getlib == False:
    getapp()
except:
  getapp()

  
