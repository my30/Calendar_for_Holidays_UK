# Calendar_for_Holidays_UK
This project builds calendars of holidays for England, Scotland, NI and Wales 

The previous project ('School_Holidays_in_the_UK') scrapes holiday start and end dates from web. 
Data were then cleaned to meet our standards and imported into our data warehouse (dim_holidays_uk). 
  DDL for table creation is in Raw Holiday List/create_table_dim_holidays_uk.sql
School holidays and public holidays are firstly extracted from database using the script at Raw Holiday List/Retrieve Raw Holiday Lists.sql
Individual .py files were executed, to generate output files under Exported Calendars/
