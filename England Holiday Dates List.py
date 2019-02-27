# Ming 27/Feb/2019
import pandas as pd

df_england_holidays = pd.read_csv('Raw Holiday List/England dim_holidays_uk.csv', sep=',',
                                  names=['id', 'start_date', 'end_date'], parse_dates=['start_date', 'end_date'])
file = open('Exported Calendars/holiday_calendar_england.csv', mode='w+')
file.close()
print('holiday_calendar_england.csv is truncated!')

for i in range(df_england_holidays.shape[0]):
    df_holiday = df_england_holidays.iloc[i, ]
    holiday_start = df_holiday[1]
    holiday_end = df_holiday[2]
    holiday_start = str(holiday_start)
    holiday_end = str(holiday_end)
    date_range = pd.date_range(start=holiday_start, end=holiday_end, freq='D')
    df_holiday_dates = pd.DataFrame(date_range, columns=['date'])
    df_holiday_dates['id'] = str(df_holiday['id'])
    columns = ['id', 'date']
    df_holiday_dates = df_holiday_dates[columns]
    df_holiday_dates.to_csv('Exported Calendars/holiday_calendar_england.csv', mode='a', header=False, index=False)
    print(str(df_holiday[0]), ' exported.')
print('Job done for England.')
