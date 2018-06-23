from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("Setup VS Code", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")