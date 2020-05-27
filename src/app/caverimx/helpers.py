from jinja2 import Template
class TemplateLoader:
    def __init__(self, path_dir):
        self.path_dir = path_dir
    def get(self, name):
        with open('%s/%s'%(self.path_dir,name)) as file:
            template = file.read()
            file.close()
            return Template(template) 
    