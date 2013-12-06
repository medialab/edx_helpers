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

TITLE_RE = re.compile('#{1,6}(.+)$', re.MULTILINE)
FIRST_TEXT_RE = re.compile('(.+$)', re.MULTILINE)

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
    raise Exception('parse_unit::HeaderNotFound')

def parse_yaml(lines):
    return yaml.load('\n'.join(lines))

def parse_markdown(lines):
    metas = {}

    try:
        metas['name'] = yaml.load(lines[0])['name']
    except:
        text = '\n'.join(lines)
        metas['text'] = text
        metas['name'] = get_default_name(text)
    else:
        metas['text'] = '\n'.join(lines[1:]).strip('\n')
    return metas

def get_default_name(text):

    # Matching a markdown title
    title_match = re.search(TITLE_RE, text)
    if title_match is not None:
        title = title_match.group(1)
    else:
        first_text_match = re.search(FIRST_TEXT_RE, text)
        if first_text_match is not None:
            title = first_text_match.group(1)
    return smart_truncate(title)


def smart_truncate(content, length=60, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix