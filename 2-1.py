# a list of 12 months
months = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]

# a list of endings of 31 days
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
+ ['st', 'nd', 'rd'] + 7 * ['th'] \
+ ['st']

year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

month_number = int(month) - 1
day_number = int(day) - 1

month_name = months[month_number]
ordinal = day + endings[day_number]

print(month_name + ' ' + ordinal + ', ' + year)