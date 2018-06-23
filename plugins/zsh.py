from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("ZSH setup", 0.1)

  def run(self):
    print("FUCK YOU BITCHES")

    #setup zsh and oh-my-zsh