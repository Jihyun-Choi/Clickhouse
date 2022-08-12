from clickhouse_driver import Client
client = Client(host='localhost',port=9000,user='user_ch',password='secret_ch')
print(client.execute('show databases'))
