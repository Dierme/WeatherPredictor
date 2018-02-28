import requests
from HttpException import HttpException


class HttpClient:
    base_url = 'http://httpbin.org/post'

    @staticmethod
    def print_request(req):
        print('HTTP/1.1 {method} {url}\n{headers}\n\n{body}'.format(
            method=req.method,
            url=req.url,
            headers='\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            body=req.body,
        ))

    @staticmethod
    def print_response(res):
        print('HTTP/1.1 {status_code}\n{headers}\n\n{body}'.format(
            status_code=res.status_code,
            headers='\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            body=res.content,
        ))


class ApiClient(HttpClient):
    base_url = 'http://api.openweathermap.org/data/2.5'
    mode = {'weather': 'weather', 'forecast': 'forecast'}

    def __init__(self, key, city_id):
        self.key = key
        self.city_id = city_id

    def _construct_params(self):
        return {
            'appid':    self.key,
            'id':       self.city_id,
            'units':    'metric'
        }

    def weather(self):
        url = self.base_url + '/'+self.mode['weather']
        response = requests.get(url=url, params=self._construct_params())
        if response.status_code != 200:
            self.print_response(response)
            raise HttpException("{} responded with status code {}".format(response.url, response.status_code))
        return response

