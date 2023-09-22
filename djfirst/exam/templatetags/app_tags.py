from django import template
import datetime # import datetime module
#Template Tags
register=template.Library() #here i called the library function of template module.

@register.simple_tag(name="get_date")
def get_date():
    now=datetime.datetime.now() 
    return now
#Template Filters
@register.filter
def quote(value):
    s='"'+str(value)+'"'
    return s