import os


from app import config_app


config_type = os.getenv('APP_SETTINGS')
if None == config_type:
    config_type = 'development'

app = config_app(config_type)

from app.models import FibonacciNumbersRequest

if __name__ == '__main__':
    app.run()