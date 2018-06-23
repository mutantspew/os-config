from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("Copy dotfiles", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")

    #copys or downloads dotfiles and sets up symlinks where necessary