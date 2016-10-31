from string import Template


def make_server_block(content):
    return Template("server {\n ${content} \n}").safe_substitute(content=content)


def make_location_block(content, pattern='/'):
    return Template("location ${pattern} {\n ${content} \n}").safe_substitute(pattern=pattern, content=content)
