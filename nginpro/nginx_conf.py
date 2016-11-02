"""
Nginx configuration as python data
Templates will be generated from this
"""

reverse_proxy = {
    'proxy_pass': 'http://localhost:2369',
    'proxy_redirect': 'off',
    'proxy_set_header': {
        'Host': '$host',
        'X-Real-IP': ' $remote_addr',
        'X-Forwarded-For': '$proxy_add_x_forwarded_for'
    },
    'client_max_body_size': '10m',
    'client_body_buffer_siz': '128k',
    'proxy_connect_timeout': '90',
    'proxy_send_timeout': '90',
    'proxy_read_timeout': '90',
    'proxy_buffers': '32 4k',
}

mime_types = {
    'text/html': 'html htm shtml',
    'text/css': 'css',
    'text/xml': 'xml rss',
    'image/gif': 'gif',
    'image/jpeg': 'jpeg jpg',
    'application/x-javascript': 'js',
    'text/plain': 'txt',
    'text/x-component': 'htc',
    'text/mathml': 'mml',
    'image/png': 'png',
    'image/x-icon': 'ico',
    'image/x-jng': 'jng',
    'image/vnd.wap.wbmp': 'wbmp',
    'application/java-archive': 'jar war ear',
    'application/mac-binhex40': 'hqx',
    'application/pdf': 'pdf',
    'application/x-cocoa': 'cco',
    'application/x-java-archive-diff': 'jardiff',
    'application/x-java-jnlp-file': 'jnlp',
    'application/x-makeself': 'run',
    'application/x-perl': 'pl pm',
    'application/x-pilot': 'prc pdb',
    'application/x-rar-compressed': 'rar',
    'application/x-redhat-package-': 'managerrpm',
    'application/x-sea': 'sea',
    'application/x-shockwave-flash': 'swf',
    'application/x-stuffit': 'sit',
    'application/x-tcl': 'tcl tk',
    'application/x-x509-ca-cert': 'der pem crt',
    'application/x-xpinstall': 'xpi',
    'application/zip': 'zip',
    'application/octet-stream': 'deb',
    'application/octet-stream': 'bin exe dll',
    'application/octet-stream': 'dmg',
    'application/octet-stream': 'eot',
    'application/octet-stream': 'iso img',
    'application/octet-stream': 'msi msp msm',
    'audio/mpeg': 'mp3',
    'audio/x-realaudio': ' ra',
    'video/mpeg': 'mpeg mpg',
    'video/quicktime': 'mov',
    'video/x-flv': 'flv',
    'video/x-msvideo': 'avi',
    'video/x-ms-wmv': 'wmv',
    'video/x-ms-asf': 'asx asf',
    'video/x-mng': 'mng',
}

fastcgi_conf = {
    'fastcgi_index': 'index.php',
    'fastcgi_pass': 'http://localhost:2790',
    'fastcgi_param': {
        'SCRIPT_FILENAME': ' $document_root$fastcgi_script_name',
        'QUERY_STRING': '$query_string',
        'REQUEST_METHOD': '$request_method',
        'CONTENT_TYPE': '$content_type',
        'CONTENT_LENGTH': '$content_length',
        'SCRIPT_NAME ': '$fastcgi_script_name',
        'REQUEST_URI ': '$request_uri',
        'DOCUMENT_URI': '$document_uri',
        'DOCUMENT_ROOT': '$document_root',
        'SERVER_PROTOCOL': '$server_protocol',
        'GATEWAY_INTERFACE': 'CGI/1.1',
        'SERVER_SOFTWARE': 'nginx/$nginx_version',
        'REMOTE_ADDR': '$remote_addr',
        'REMOTE_PORT': '$remote_port',
        'SERVER_ADDR': '$server_addr',
        'SERVER_PORT': '$server_port',
        'SERVER_NAME': '$server_name',
        'REDIRECT_STATUS': 200,
    }
}

uwsgi_conf = {
    'uwsgi_pass': '127.0.0.1:5000'
}

server = {
    'listen': '80',
    'server_name': 'localhost',
    'root': 'html',
}

http = {
    'sendfile': ' on',
    'keepalive_timeout': 65
}

events = {
    'worker_connections': 1024
}

log = {
    'access_log': 'access_log',
    'error_log': 'error_log',
}

restrict = {
    'deny': 'all'
}

gzip_conf = {
    'gzip': 'on',
    'gzip_disable': 'msie6',
    'gzip_vary ': 'on',
    'gzip_proxied': ' any',
    'gzip_comp_level': ' 6',
    'gzip_buffers': ' 16 8k',
    'gzip_http_version': ' 1.1',
    'gzip_types': 'text/plain text/css application/json application/x-javascript '
                  'text/xml application/xml application/xml+rss text/javascript'
}

ssl_conf = {
    'ssl_ciphers': 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256'
                   ':ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:'
                   'DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:'
                   'ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:'
                   'ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:'
                   'ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:'
                   'DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:'
                   'DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:'
                   'AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:'
                   'CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:'
                   '!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA',
    'ssl_prefer_server_ciphers': 'on',
    'ssl_protocols': 'TLSv1.2 TLSv1.1',
    'ssl_certificate': '/etc/pki/tls/certs/cert.crt',
    'ssl_certificate_key': '/etc/pki/tls/private/example_com_no_pass.key',
    'ssl_dhparam': '/etc/pki/tls/certs/dhparams.pem',
    'ssl_stapling': 'on',
    'ssl_stapling_verify': 'on'
}
