import argparse
from string import Template

"""
Subclassing template class
"""
class NginTemplate(Template):
    delimiter = '#'


"""
Reverse Proxy Template
"""
reverse_proxy_template = """
server {
    listen 80;
    server_name #{server_name};
    access_log /var/log/nginx/#{server_name}.access.log;
    error_log /var/log/nginx/#{server_name}.error.log;

    location  / {
        proxy_pass #{proxy_pass};
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}"""

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
    params = {'server_name': args.name, 'proxy_pass': args.proxypass}
    conf = NginTemplate(reverse_proxy_template).safe_substitute(params)
    print conf