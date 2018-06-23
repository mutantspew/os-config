# plugin class to derive from
class Plugin(object):
  def __init__(self, name, version):
    self.name = name # plugin name
    self.version = version # plugin version
    
  def get_menu_name(self):
    return self.name
  
  def get_version(self):
    return "v{}".format(self.version)
  
  def run(self):
    raise NotImplementedError