create table dim_holidays_uk
(
  country         varchar(50)                      not null,
  local_authority varchar(50) default 'National'   not null,
  holiday_name    varchar(50)                      not null,
  start_date      date                             not null,
  end_date        date        default '9999-12-31' null,
  id              varchar(100)                     not null
)
  ENGINE = InnoDB;

update dim_holidays_uk dhu
set dhu.end_date = '2020-12-31'
where dhu.end_date = '9999-12-31';

update dim_holidays_uk dhu1, dim_holidays_uk dhu2
set dhu2.duration = datediff(dhu1.end_date, dhu1.start_date)
where dhu1.id = dhu2.id;

# The following code should be run every time the table is updated.
update dim_holidays_uk dhu1, dim_holidays_uk dhu2
set dhu2.id = concat(year(dhu1.start_date), '_', left(dhu1.country, 3), '_', dhu1.local_authority, '_',
                     dhu1.holiday_name)
where dhu1.country = dhu2.country
  and dhu1.local_authority = dhu2.local_authority
  and dhu1.holiday_name = dhu2.holiday_name
  and dhu1.start_date = dhu2.start_date;

/* Further DDL:
alter table dim_holidays_uk add duration int(3) default 1;
*/

