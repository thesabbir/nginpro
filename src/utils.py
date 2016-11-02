"""
Utilities
"""

"""
Takes a python dictionary and converts it to nginx compatible configuration block
"""


def to_nginx_template(config):
    template = ''
    for key, value in config.iteritems():
        if isinstance(value, dict):
            for key2, value2 in value.items():
                template += "{} {} {};\n".format(key, key2, value)
        else:
            template += "{} {};\n".format(key, value)
    return template


"""
nginx configuration indentation
"""


def make_indent(contents):
    indents = '    '
    lines = map(str.strip, contents.splitlines())
    current_indent = 0
    for index, line in enumerate(lines):
        if line.endswith('}'):
            current_indent -= 1
        lines[index] = current_indent * indents + line

        if line.endswith('{'):
            current_indent += 1

    return '\n'.join(lines)
