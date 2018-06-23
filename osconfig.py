#!/usr/bin/env python3

import importlib, os, re, sys, time
import installer

# clears the screen
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# load the plugins
def load_plugins():
  pysearchre = re.compile('.py$', re.IGNORECASE)
  pluginfiles = filter(pysearchre.search, os.listdir(os.path.join(os.path.dirname(__file__), 'plugins')))

  form_module = lambda fp: '.' + os.path.splitext(fp)[0]
  
  plugins = map(form_module, pluginfiles)
  
  # import parent module / namespace
  importlib.import_module('plugins')
  
  modules = []
  
  for plugin in plugins:
    if not plugin.startswith('__'):
      modules.append(importlib.import_module(plugin, package="plugins"))

  return modules

# create the menu
def create_menu(plugins):
  print('\n')
  i = 1

  # iterate through the plugins and get the name and version for the menu
  for p in plugins:
    print("{}: {} ({})".format(i, p.get_menu_name(), p.get_version()))
    # print(p)
    i = i + 1
  
  # exit is always last
  print("{}: Exit".format(i))



############
# main
############

# load the plugins
plugs = load_plugins()

plugins = []

# get the installer
installer = installer.Installer()

# iterate through plugins and load the modules
for p in plugs:
  m = p.Module(installer)
  plugins.append(m)

exit = False
clear() #clear screen

# while we haven't exited!
while not exit:
  create_menu(plugins)  # generate the menu

  # wait for input
  option = input('> ')
  option = int(option)  # conver to integer

  if option == len(plugins) + 1: # exit
    exit = True
    break
  elif option <= 0 or option > len(plugins) + 1:  # out of bounds
    print('invalid selection')
    continue
  
  #clear the screen before we run the plugin
  clear()

  # run the selected plugin
  plugins[option - 1].run()
  
  # pause for 2 secs so the user can react
  time.sleep(2)
  
  # clear the screen before we redraw the menu
  clear()