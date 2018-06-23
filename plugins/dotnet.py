from plugin import Plugin

class Module(Plugin):
  def __init__(self, Installer):
    super().__init__("Setup dotnet", 0.1)
    self.Installer = Installer

  def run(self):
    #print the os
    print('Running os: ', self.Installer.OS)
    
    #setup the blah blahs based on ubutu
    # deb(fuckyou microsoft)