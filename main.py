from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = 'localhost'
server_port = 8080


class MyWeb(BaseHTTPRequestHandler):
    """
        Класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def MyIndex(self) -> str:
        """
        Метод для чтения файла index.html
        :return: index.html
        """
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()

    def do_GET(self):
        """
        Метод обрабатывает GET-запросы браузера к серверу.
        """
        page_content = self.MyIndex()
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(page_content.encode('utf-8'))


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), MyWeb)
    print('Server started http://%s:%s' % (host_name, server_port))
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
