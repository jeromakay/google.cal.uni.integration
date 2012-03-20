import os
from google.appengine.ext.webapp import template

def make(self, pageTitle, bodyTemplate ):
	template_values = {
		'page_title': pageTitle,
	}
	headerPath = os.path.join(os.path.dirname(__file__), 'root/header.html')
	bodyPath = os.path.join(os.path.dirname(__file__), bodyTemplate+'.html')
	footerPath = os.path.join(os.path.dirname(__file__), 'root/footer.html')
	self.response.out.write(template.render(headerPath, template_values) + template.render(bodyPath, template_values) + template.render(footerPath, template_values))