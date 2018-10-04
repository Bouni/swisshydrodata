# swisshydrodata

swisshydrodata is a library that allow you to request data from the [Swiss Federal Office for the Environment FOEN](https://www.hydrodaten.admin.ch/en/stations-and-data.html).

To find a station near to you, use the [list of stations](https://www.hydrodaten.admin.ch/en/stations-and-data.html) on the FEON website.

## Example
```
from swisshydrodata import SwissHydroData 

s = SwissHydroData()
# load data for station
s.load_station_data(2143)

# get the latest values
print(s.get_latest_level())
print(s.get_latest_temperature())
print(s.get_latest_discharge())

# get the min values within the last 24h
print(s.get_min_level())
print(s.get_min_temperature())
print(s.get_min_discharge())

# get the max values within the last 24h
print(s.get_max_level())
print(s.get_max_temperature())
print(s.get_max_discharge())

# get the mean values within the last 24h
print(s.get_mean_level())
print(s.get_mean_temperature())
print(s.get_mean_discharge())
```

The result of the above example would look like this:
```
{'timestamp': datetime.datetime(2018, 10, 4, 11, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 322.186, 'unit': 'm ü.M'}
{'timestamp': datetime.datetime(2018, 10, 4, 11, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 16.29, 'unit': '°C'}
{'timestamp': datetime.datetime(2018, 10, 4, 11, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 230.09, 'unit': 'm3/s'}
{'timestamp': datetime.datetime(2018, 10, 4, 3, 20, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 322.15, 'unit': 'm ü.M'}
{'timestamp': datetime.datetime(2018, 10, 3, 22, 30, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 16.01, 'unit': '°C'}
{'timestamp': datetime.datetime(2018, 10, 4, 3, 20, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 218.999, 'unit': 'm3/s'}
{'timestamp': datetime.datetime(2018, 10, 4, 0, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 322.235, 'unit': 'm ü.M'}
{'timestamp': datetime.datetime(2018, 10, 4, 11, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 16.29, 'unit': '°C'}
{'timestamp': datetime.datetime(2018, 10, 4, 0, 50, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600))), 'value': 245.521, 'unit': 'm3/s'}
{'value': 322.1848551724139, 'unit': 'm ü.M'}
{'value': 16.097862068965497, 'unit': '°C'}
{'value': 229.77437241379295, 'unit': 'm3/s'}
```
