# Ming 27/Feb/2019
import pandas as pd

# Read the holiday list into a DataFrame
df_wales_holidays = pd.read_csv('Raw Holiday List/Wales dim_holidays_uk.csv', sep=',',
                                names=['id', 'start_date', 'end_date'], parse_dates=['start_date', 'end_date'])
# Truncate the final .csv file
file = open('Exported Calendars/holiday_calendar_wales.csv', mode='w+')
file.close()
print('holiday_calendar_wales.csv is truncated! \n')

for i in range(df_wales_holidays.shape[0]):
    df_holiday = df_wales_holidays.iloc[i, ]
    # Retrieve values of start_ and end_date
    holiday_start = df_holiday[1]
    holiday_end = df_holiday[2]
    # Convert time series to strings for later use
    holiday_start = str(holiday_start)
    holiday_end = str(holiday_end)
    # Produce calendar
    holiday_range = pd.date_range(start=holiday_start, end=holiday_end, freq='D')
    # A new DF with all the data
    df_holiday_dates = pd.DataFrame(holiday_range, columns=['date'])
    # Add UIDs
    df_holiday_dates['id'] = str(df_holiday['id'])
    # Reordering the columns
    columns = ['id', 'date']
    df_holiday_dates = df_holiday_dates[columns]
    # Write to target .csv file
    df_holiday_dates.to_csv('Exported Calendars/holiday_calendar_wales.csv', mode='a', header=False)
    print(str(df_holiday[0]), ' exported.')
print('Job done for Wales')