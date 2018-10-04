# swisshydrodata

swisshydrodata is a library that allow you to request data from the Swiss Federal Office for the Environment FOEN.

## Example
```
from swisshydrodata import SwissHydroData 

sh = SwissHydroData()
# load data for station
s.load_station_data(2143)

# get the latest values
s.get_latest_level()
s.get_latest_temperature()
s.get_latest_discharge()

# get the min values within the last 24h
s.get_min_level()
s.get_min_temperature()
s.get_min_discharge()

# get the max values within the last 24h
s.get_max_level()
s.get_max_temperature()
s.get_max_discharge()

# get the mean values within the last 24h
s.get_mean_level()
s.get_mean_temperature()
s.get_mean_discharge()
```

