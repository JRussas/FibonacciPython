import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, config_app, models


config = config_type=os.getenv('APP_SETTINGS')
if None == config:
    config = 'development'
app = config_app(config)
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()