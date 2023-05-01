class Config():
    SECRET_KEY = 'you-will-never-guess'
    username = 'aichain'
    password = 'ai!chain135'
    server = '156.232.9.199'
    port = 3306
    dbname = 'marketplace'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + username + ':' + password + '@' + server + '/' + dbname
    SQLALCHEMY_TRACK_MODIFICATIONS = True
