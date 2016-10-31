"""
Utilities
"""

"""
format key value prefix
"""


def kv_format(pre, key, value):
    if pre == '':
        return "{} {};\n".format(key, value)
    return "{} {} {};\n".format(pre, key, value)


"""
Takes a python dictionary and converts it to nginx compatible configuration block
"""


def to_nginx_template(d):
    template = ''
    for key, value in d.items():
        if isinstance(value, dict):
            for key2, value2 in value.items():
                template += kv_format(key, key2, value2)
        else:
            template += kv_format('', key, value)
    return template


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
