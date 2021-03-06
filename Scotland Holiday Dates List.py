# Ming 26/Feb/2019
import pandas as pd

# Read the holiday list into a DataFrame
df_scotland_holidays = pd.read_csv('Raw Holiday List/Scotland dim_holidays_uk.csv', sep=',',
                                   names=['id', 'start_date', 'end_date', 'duration'],
                                   parse_dates=['start_date', 'end_date'])
# Truncate the final .csv file
file = open('Exported Calendars/holiday_calendar_scotland.csv', mode='w+')
file.close()
print('holiday_calendar_scotland.csv is truncated!')

for i in range(0, df_scotland_holidays.shape[0]):
    df_sample_holiday = df_scotland_holidays.iloc[i,]
    # Access that row with iloc/loc and specify the column index/column to get int64 or float data.
    # Retrieve the value from series.
    holiday_start = df_sample_holiday[1]
    holiday_end = df_sample_holiday[2]
    # Convert TimeSeries to strings
    holiday_start = str(holiday_start)
    holiday_end = str(holiday_end)
    # print('\n', type(holiday_end), '\n')
    # Produce calendar
    date_range = pd.date_range(start=holiday_start, end=holiday_end, freq='D')
    # Now generate a new DataFrame containing the data wanted.
    df_holiday_dates = pd.DataFrame(date_range, columns=['date'])
    # With uids for holidays
    df_holiday_dates['id'] = str(df_sample_holiday['id'])
    # Reorder the columns
    columns = ['id', 'date']
    df_holiday_dates = df_holiday_dates[columns]
    # Write to a .csv file
    df_holiday_dates.to_csv('Exported Calendars/holiday_calendar_scotland.csv', mode='a', header=False, index=False)
    print(str(df_sample_holiday[0]), ' exported.')
print('Job done for Scotland')
