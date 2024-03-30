from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    """
    Класс, обрабатывающий запросы от клиента
    """
    def read_html(self):
        """
        Метод для открытия html файла.
        :return: Возвращает данные из html файла в строковом формате.
        """
        with open("src/index.html", "r", encoding="utf-8") as html_file:
            return html_file.read()

    def do_GET(self):
        """
        Метод для обработки входящих GET запросов
        """
        page_content = self.read_html()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, encoding="utf-8"))


if __name__ == "__main__":
    host_name = "localhost"
    server_port = 8080

    webServer = HTTPServer((host_name, server_port), MyServer)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
