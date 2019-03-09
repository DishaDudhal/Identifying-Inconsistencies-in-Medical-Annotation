from django.template.defaulttags import register
from django import template
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def getName(dictionary):
    return(list(dictionary)[0])

@register.filter
def Append(X,x):
	return(X+"<p>"+x+"</p>")
@register.filter
def myTerm(X,x):
	return(X+x)

@register.filter
def toString(X):
	return(str(X))
@register.simple_tag
def sixAppend(a, b, c ,d ,e,f):
	return(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))

@register.simple_tag
def fiveAppend(a,b,c,d,e):
	return(str(a)+str(b)+str(c)+str(d)+str(e))

class IncrementVarNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self,context):
        value = context[self.var_name]
        context[self.var_name] = value + 1
        return u""

def increment_var(parser, token):

    parts = token.split_contents()
    return IncrementVarNode(parts[1])

register.tag('increment', increment_var)

class Increment1VarNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self,context):
        value = context[self.var_name]
        context[self.var_name] = value + 1
        return u""

def increment1_var(parser, token):

    parts = token.split_contents()
    return Increment1VarNode(parts[1])

register.tag('increment1', increment1_var)

class AppendvarNode(template.Node):

	def __init__(self,var_name):
		self.var_name = var_name

	def render(self,context):
		print(context[self.var_name])
		value = context[self.var_name]
		context[self.var_name] = value + "<p>" + "cd" + "</p>"
		return u""
def append_var(parser, token):
	parts = token.split_contents()
	print("hullu",parts)
	return AppendvarNode(parts[1])

register.tag('append', append_var)