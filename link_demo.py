from pymapd import connect
import pygdf
user_str = 'C7EF7A5119BF54624B02'
password_str = 'XBWXbs70mrll3nLBalIVymHl9ghjF2E4jpCVbRh9'
host_str = 'use2-api.mapd.cloud'
dbname_str = 'mapd'
cursor = None
def get_cursor():
    global cursor
    if not cursor:
        connection = connect(user=user_str, password=password_str, host=host_str, dbname=dbname_str, port=443, protocol='https')
        cursor = connection.cursor()
        print('new conn created')
    return cursor