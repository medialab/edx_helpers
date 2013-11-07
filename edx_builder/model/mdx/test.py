import markdown
import re
from scribd import ScribdExtension

ext = ScribdExtension()

print markdown.markdown(u'[[pdf:igegefe]]', [ext])

sample = open('test.md', 'r').read()

core = re.compile('\* \* \*(.*?)\* \* \*', re.DOTALL)

m = re.findall(core, sample)
