import numpy
# def weekday_number(month, year):
#     date = 0

# #     if month == 12:
# #         end = str(year) + '-' + str(month) + '-31'
# #         begin = str(year) + '-' + str(month) + '-01'
# #     else:
# #         if month < 10:
# #             endM = '-0'+str(month+1)
# #             beginM = '-0'+str(month)
# #         else:
# #             endM = '-'+str(month+1)
# #             beginM = '-'+str(month)

# #         end = str(year)+endM+'-01'
# #         begin = str(year)+beginM+'-01'
# #         return (numpy.datetime64(end) - numpy.datetime64(begin)+date)

# # print(weekday_number(9, 2022))

import numpy as np
print("Number of weekdays in March 2017:")
print(np.busday_count('2017-03', '2017-04'))
