import argparse
from nginx_conf import server, reverse_proxy
from utils import to_nginx_template, make_indent, make_block

"""
Initiate argparse
"""
parser = argparse.ArgumentParser()

"""
Add arguments
"""
parser.add_argument("-r", "--revproxy", help="reverse proxy", action="store_true")
parser.add_argument("-n", "--name", help="server name or domain name", action="store")
parser.add_argument("-p", "--proxypass", help="proxy pass server", action="store")

"""
Parsing arguments
"""
args = parser.parse_args()

"""
Reverse proxy config generator
"""
if args.revproxy:
    if args.name is None or args.proxypass is None:
        raise SystemExit('Name and Pass is required!')
    server['server_name'] = args.name
    reverse_proxy['proxy_pass'] = args.proxypass
    to_nginx_template(reverse_proxy)
    location = make_block(name="location", content=to_nginx_template(reverse_proxy), pattern='/')
    server = to_nginx_template(server)
    block = '{} {}'.format(server, location)
    conf = make_block(name="server", content=block, pattern="")
    print make_indent(conf)
