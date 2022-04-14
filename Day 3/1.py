import numpy
def date_yesterday_today_tomorrow():
    yesterday = numpy.datetime64('today', 'D') - numpy.timedelta64(1, 'D')
    today = numpy.datetime64('today', 'D')
    tomorrow = numpy.datetime64('today', 'D') + numpy.timedelta64(1, 'D')
    return yesterday, today, tomorrow

print(date_yesterday_today_tomorrow())