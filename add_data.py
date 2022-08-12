from csv import DictReader
from datetime import datetime
from clickhouse_driver import Client
client = Client(host='localhost',port=9000,user='user_ch',password='secret_ch')
print(client.execute('show databases'))


# date,meantemp,humidity,wind_speed,meanpressure
def iter_csv(filename):
    converters = {
        'date': lambda x: datetime.strptime(x, '%Y-%m-%d'),
        'meantemp': float,
        'humidity': float,
        'wind_speed': float,
        'meanpressure': float,
    }
    with open(filename, 'r') as f:
        reader = DictReader(f)
        for line in reader:
            res = {k: (converters[k](v) if k in converters else v) for k, v in line.items()}
            yield res

client.execute('''
CREATE TABLE IF NOT EXISTS test.DailyDelhiClimateTest
(
    date DateTime,
    meantemp Float32,
    humidity Float32,
    wind_speed Float32,
    meanpressure Float32
) Engine = Memory;
'''
)
client.execute('INSERT INTO test.DailyDelhiClimateTrain VALUES', iter_csv('./data/DailyDelhiClimateTrain.csv'))
client.execute('INSERT INTO test.DailyDelhiClimateTest VALUES', iter_csv('./data/DailyDelhiClimateTest.csv'))
