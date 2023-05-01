import pymysql
from config import Config
from simsearch import SimSearch

config = {
  'host': Config.server,
  'port': Config.port,
  'user': Config.username,
  'passwd':Config.password,
  'db': Config.dbname,
  'charset': 'utf8',
  'cursorclass': pymysql.cursors.DictCursor
}

def main():
  simsearch = SimSearch()
  connect = pymysql.connect(**config)
  cursor = connect.cursor()
  cursor.execute('select id, description from showcase')
  results = cursor.fetchall()
  simsearch.sentence_embedding(results)
  cursor.close()
  connect.close()
  print ('create embedding')

if __name__ == '__main__':
  main()



