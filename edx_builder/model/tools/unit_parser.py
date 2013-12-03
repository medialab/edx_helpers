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
import yaml

def parse_unit(file_string):
    components = []

    for component in file_string.split('* * *'):
        if component.strip() == '':
            raise Exception('UnitParser::EmptyComponent')

        index, ctype = parse_header(component)

        remaining_lines = component.splitlines()[index:]

        if ctype == 'html':
            metas = parse_markdown(remaining_lines)
        else:
            metas = parse_yaml(remaining_lines)

        components.append({
            'type': ctype,
            'metas': metas
        })

    return components


def parse_header(component):

    # Getting the first yaml line
    index = 0
    for line in (i for i in component.splitlines()):
        if ':' in line:
            return index + 1, yaml.load(line)['component']
        index += 1
    raise Exception('UnitParser::HeaderNotFound')

def parse_yaml(lines):
    return yaml.load('\n'.join(lines))

def parse_markdown(lines):
    return {
        'name': yaml.load(lines[0])['name'],
        'text': '\n'.join(lines[1:]).strip('\n')
    }