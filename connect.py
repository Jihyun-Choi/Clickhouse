from clickhouse_driver import connect

#Account number: password @ host name: port number / database
#conn = connect(f'clickhouse://{user}:{pw}@{host}:9000/{database}')
conn = connect(host='localhost',port=9000,user='user_ch',password='secret_ch')
cursor = conn.cursor()
cursor.execute('SHOW TABLES')
print(cursor.execute('SHOW Databases'))
