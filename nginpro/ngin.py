import argparse
from nginx_conf import server, reverse_proxy
from nginx_blocks import make_location_block, make_server_block
from utils import to_nginx_template, make_indent

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
Usage Example: ngin.py -r -n example.com -p http://localhost:9000
"""
if args.revproxy:
    if args.name is None or args.proxypass is None:
        raise SystemExit('Name and Pass is required!')
    server['server_name'] = args.name
    reverse_proxy['proxy_pass'] = args.proxypass
    location = make_location_block(to_nginx_template(reverse_proxy), '/')
    server = to_nginx_template(server)
    conf = make_server_block('{} {}'.format(server, location))
    print make_indent(conf)
