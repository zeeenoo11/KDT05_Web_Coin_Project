import os

BASE_DIR = os.path.dirname(__file__)
DB_NAME_SQLITE = 'app.db'

DB_SQLITE_URL = f'sqlite:///{os.path.join(BASE_DIR, DB_NAME_SQLITE)}'
DB_MYSQL_URL = f'mysql+pymysql://root:kdt5@localhost:3306/Team2?charset=utf8mb4'

SQLALCHEMY_DATABASE_URI = DB_MYSQL_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

