from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("Setup NPM/Node.JS/NVM", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")

    #sets up npm and node