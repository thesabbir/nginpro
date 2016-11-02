"""
Utilities
"""
from string import Template

"""
Generate configuration blocks
"""


def make_block(name, content, pattern=""):
    return Template("""
        ${name} ${pattern} {
            ${content}
        }
    """).safe_substitute(name=name, content=content, pattern=pattern)


"""
Takes a python dictionary and converts it to nginx compatible configuration block
"""


def to_nginx_template(config):
    template = ""
    for key, value in config.iteritems():
        if isinstance(value, dict):
            for key2, value2 in value.iteritems():
                template += "{} {} {};\n".format(key, key2, value2)
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


"""
Get nginx config args
"""


def get_nginx_config_args():
    # TODO: make this more pythonic
    import subprocess
    import re
    options = {}
    try:
        process = subprocess.Popen(['nginx', '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err, out = process.communicate()
        matches = re.findall('--([^\s]+)', out)
        for option in matches:
            if '=' in option:
                v = option.split('=')
                options[v[0]] = v[1]
            else:
                options[option] = True
    except OSError:
        print 'Nginx is not installed or not in $PATH'
    return options
