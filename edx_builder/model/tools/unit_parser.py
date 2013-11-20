# -------------------------------------------------------------------
# EdxBuilder Unit Parser
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import re
import yaml

UNIT_RE = re.compile('\* \* \*(.*?)\* \* \*', re.DOTALL)

def parse_unit(file_string):
    matches = re.findall(UNIT_RE, file_string)

    components = []
    for m in matches:
        lines = m.splitlines()
        ctype = yaml.load(lines[1])['component'].strip()
        components.append({
            'type': ctype,
            'data': '\n'.join(lines[2:])
        })

    return components

