from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("ssh-keygen", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")