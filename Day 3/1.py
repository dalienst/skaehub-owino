import numpy
def date_yesterday_today_tomorrow():
    yesterday = numpy.datetime64('2022-04-14', 'D') - numpy.timedelta64(1, 'D')
    tod = numpy.datetime64('2022-04-14', 'D')
    tomorrow = numpy.datetime64('2022-04-14', 'D') + numpy.timedelta64(1, 'D')
    #return yesterday, today, tomorrow
    print("Today is date: ", tod)
    print("Tomorrow is date: ", tomorrow)
    print("Yesterday was date: ", yesterday)

print(date_yesterday_today_tomorrow())