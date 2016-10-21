class BaseClient:
    # URL vk api
    BASE_URL = None
    # метод vk api
    method = None
    # GET, POST, ...

    #  Получение GET параметров запроса
    def get_params(self):
        pass

    # Получение данных POST запроса
    def get_json(self):
        pass

    # Получение HTTP заголовков
    def get_headers(self):
        pass

    # Склейка url
    def generate_url(self, method):
        return '{0}/{1}'.format(self.BASE_URL, method)

    # Отправка запроса к VK API
    def _get_data(self, method):
        response = None
        return self.response_handler(response)

    # Обработка ответа от VK API
    def response_handler(self, response):
        return response

    # Запуск клиента
    def execute(self):
        return self._get_data(
            self.method
        )
