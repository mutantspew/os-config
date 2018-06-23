from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("Backup Dotfiles", 0.1)
  
  def run(self):
    print('runnin\' bitches')