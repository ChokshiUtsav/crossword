import jinja2

TEMPLATE_FILE = "template.jinja"

class HtmlTemplate(object):
    def __init__(self, search_path, output_file):
        template_loader = jinja2.FileSystemLoader(searchpath=search_path)
        template_env = jinja2.Environment(loader=template_loader)
        self.template = template_env.get_template(TEMPLATE_FILE)
        self.template_vars = {}
        self.output_file = output_file

    def add_template_variable(self, key, value):
        self.template_vars[key] = value

    def render_html(self):
        html_text = self.template.render(self.template_vars)
        fo = open(self.output_file, 'w')
        fo.write(html_text)
        fo.close()