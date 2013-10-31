import markdown
import re
from mdx_scribd import ScribdExtension

ext = ScribdExtension()

print markdown.markdown(u'[[pdf:igegefe]]', [ext])

sample = open('test.md', 'r').read()

core = re.compile('\* \* \*(.*?)\* \* \*', re.DOTALL)

m = re.findall(core, sample)
