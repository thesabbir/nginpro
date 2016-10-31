"""
Utilities
"""

"""
format key value prefix
"""


def kv_format(pre, key, value):
    if pre == '':
        return '{} : {};'.format(key, value)
    return '{} : {} {};'.format(pre, key, value)


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
