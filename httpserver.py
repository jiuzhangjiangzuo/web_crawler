#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Source: https://blog.fundebug.com/2019/02/22/compare-http-method-get-and-post/

import socket
import argparse

HOST, PORT = '', 23333

DEMO_URL_LENGTH = "url_length"
DEMO_LXML = "lxml"

def server_run(args):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
    print('Serving HTTP on port %s ...' % PORT)
    while True:
        # 接受连接
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection, args)


def handle_request(client_connection, args):
    # 获取请求报文
    request = ''
    while True:
        recv_data = client_connection.recv(2400)
        recv_data = recv_data.decode()
        request += recv_data
        if len(recv_data) < 2400:
            break

    # 解析首行
    first_line_array = request.split('\r\n')[0].split(' ')
    url_length = len(first_line_array[1])
    # 分离 header 和 body
    space_line_index = request.index('\r\n\r\n')
    header = request[0: space_line_index]
    body = request[space_line_index + 4:]

    # 打印请求报文
    print(request)

    # 返回报文
    http_response_for_url_length = """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
</head>
<body>
<p style="color: green">Hello, World!</p>
<p style="color: green">URL Length:{}</p>
</body>
</html>
"""

    http_response_for_url_length = http_response_for_url_length.format(url_length).encode('utf-8')

    # 演示lxml
    http_response_for_lxml_demo = b"""\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
    <title>lxml demo!</title>
</head>
<body>
<div>
    <a href="link.html">Item List</a>
    <ul>
        <li class="item-0"><a href="link1.html">item 0</a></li>
        <li class="item-1"><a href="link2.html", id='limited'>item 1</a></li>
        <li class="item-2"><a href="link2.html">item 2</a></li>
        <li class="item-3"><a href="link2.html">item 3</a></li>
        <li class="item-4"><a href="link2.html", id='limited'>item 4</a></li>
    </ul>
</div>
</body>
</html>
"""
    if args.demo == DEMO_URL_LENGTH:
        client_connection.sendall(http_response_for_url_length)
    else:
        client_connection.sendall(http_response_for_lxml_demo)
    client_connection.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP Server')
    parser.add_argument('--demo', type=str, default=DEMO_URL_LENGTH, help='which demo')
    args = parser.parse_args()
    server_run(args)
