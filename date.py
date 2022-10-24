import datetime

def right(s, amount):
    return s[-amount:]


def formatAsCustomString(date, number):
    date_time_obj = datetime.strptime(date, '%Y-%m-%d')
    
    return (number.zfill(5) + "-" + right(date_time_obj.strftime('%Y%m%d'), 8))

obj = formatAsCustomString('1990-10-22', '12345')
print (obj)

'''

# ****************** BODY *********************
def formatAsCustomString(date, number):
    num = str(number)
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    return (num.zfill(5) + "-" + right(date_time_obj.strftime('%y%m%d'),8))

'''