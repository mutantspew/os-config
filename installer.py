# use this to install based on os
# apt/pacman

# also use this to run shell code

import os, platform, subprocess
from enum import Enum

class OS(Enum):
  DEBIAN9 = 1
  DEBIAN8 = 2
  RHEL = 3
  UBUNTU1804 = 4
  UBUNTU1710 = 5
  FEDORA28 = 6
  CENTOSORACLE = 7
  OPENSUSE = 8
  SLES = 9

class Installer:
  def __init__(self):
    self.get_os()
  
  def get_os(self):
    # osname = os.name()
    platform_ = platform.system()

    if platform_ == 'Linux':
      distro = platform.linux_distribution()
      self.distro = distro
      self.distro_name = distro[0]

      if distro[0] == 'Ubuntu':
        if distro[1] == '18.04':
          self.OS = OS.UBUNTU1804
        elif distro[1] == '17.10':
          self.OS = OS.UBUNTU1710
      elif distro[0] == 'RHEL':
        self.OS == OS.RHEL
      elif distro[0] == 'Debian':
        pass
      elif distro[0] == 'Fedora':
        pass
      elif distro[0] == 'Centos/Oracle':
        pass
      elif distro[0] == 'OpenSuse':
        pass
      elif distro[0] == 'Sles':
        pass
    elif platform_ == 'Windows':
      pass
    elif platform_ == 'macosx':
      pass

  def get_sudo(self):
    return "sudo"

  def get_installer(self):
    inst = ""

    if self.OS == OS.UBUNTU1710 or self.OS == OS.UBUNTU1804:
      inst = "apt install -y"
    else:
      return "FAILED"
    
    return inst

  def get_install(self, package):
    return "{} {} {}".format(self.get_sudo, self.get_installer(), package)
  
  def run(self, command):
    return subprocess.run("{}".format(command), shell = True)
  
  def run_sudo(self, command):
    return self.run("{} {}".format(self.get_sudo(), command))