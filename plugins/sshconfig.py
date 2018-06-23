from plugin import Plugin

#Configures file(~/.ssh/config) and sets up ssh
class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("SSH Config", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")
    # print ssh config if exists (change y/N?)
    # configure ssh (y/N)?