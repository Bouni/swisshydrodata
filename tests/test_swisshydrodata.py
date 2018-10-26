from unittest import TestCase

import datetime
import swisshydrodata

class TestSwissHydroData(TestCase):

    def setUp(self):
        self.shd = swisshydrodata.SwissHydroData()

    def test_stations(self):
        stations = self.shd.get_stations()
        self.assertIsInstance(stations, list)
        for station in stations:
            self.assertIsInstance(station, int)

    def test_station(self):
        return
        stations = self.shd.get_stations()
        for id in stations:
            station = self.shd.get_station(id)
            self.assertIsInstance(station, dict)
            self.assertIn("name", station)
            self.assertIsInstance(station["name"], str)
            self.assertIn("water-body-name", station)
            self.assertIsInstance(station["water-body-name"], str)
            self.assertIn("water-body-type", station)
            self.assertIsInstance(station["water-body-type"], str)
            self.assertIn("coordinates", station)
            self.assertIsInstance(station["coordinates"], dict)
            self.assertIn("latitude", station["coordinates"])
            self.assertIsInstance(station["coordinates"]["latitude"], float)
            self.assertIn("longitude", station["coordinates"])
            self.assertIsInstance(station["coordinates"]["longitude"], float)
            self.assertIn("parameters", station)
            self.assertIsInstance(station["parameters"], dict)
            if "temperature" in station["parameters"]:
                self.assertIsInstance(station["parameters"]["temperature"], dict)
                self.assertIn("unit", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["unit"], str)
                self.assertIn("datetime", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["datetime"], str)
                self.assertIn("value", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["value"], float)
                self.assertIn("previous-24h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["previous-24h"], float)
                self.assertIn("delta-24h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["delta-24h"], float)
                self.assertIn("max-24h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["max-24h"], float)
                self.assertIn("mean-24h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["mean-24h"], float)
                self.assertIn("min-24h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["min-24h"], float)
                self.assertIn("max-1h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["max-1h"], float)
                self.assertIn("mean-1h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["mean-1h"], float)
                self.assertIn("min-1h", station["parameters"]["temperature"])
                self.assertIsInstance(station["parameters"]["temperature"]["min-1h"], float)
            if "level" in station["parameters"]:
                self.assertIsInstance(station["parameters"]["level"], dict)
                self.assertIn("unit", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["unit"], str)
                self.assertIn("datetime", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["datetime"], str)
                self.assertIn("value", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["value"], float)
                self.assertIn("previous-24h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["previous-24h"], float)
                self.assertIn("delta-24h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["delta-24h"], float)
                self.assertIn("max-24h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["max-24h"], float)
                self.assertIn("mean-24h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["mean-24h"], float)
                self.assertIn("min-24h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["min-24h"], float)
                self.assertIn("max-1h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["max-1h"], float)
                self.assertIn("mean-1h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["mean-1h"], float)
                self.assertIn("min-1h", station["parameters"]["level"])
                self.assertIsInstance(station["parameters"]["level"]["min-1h"], float)
                self.assertIsInstance(station["parameters"]["level"], dict)
            if "discharge" in station["parameters"]:
                self.assertIsInstance(station["parameters"]["discharge"], dict)
                self.assertIn("unit", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["unit"], str)
                self.assertIn("datetime", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["datetime"], str)
                self.assertIn("value", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["value"], float)
                self.assertIn("previous-24h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["previous-24h"], float)
                self.assertIn("delta-24h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["delta-24h"], float)
                self.assertIn("max-24h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["max-24h"], float)
                self.assertIn("mean-24h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["mean-24h"], float)
                self.assertIn("min-24h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["min-24h"], float)
                self.assertIn("max-1h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["max-1h"], float)
                self.assertIn("mean-1h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["mean-1h"], float)
                self.assertIn("min-1h", station["parameters"]["discharge"])
                self.assertIsInstance(station["parameters"]["discharge"]["min-1h"], float)
                self.assertIsInstance(station["parameters"]["discharge"], dict)

    def test_station_name(self):
        name = self.shd.get_station_name(2143)
        self.assertIsInstance(name, str)
    
    def test_station_water_body_name(self):
        name = self.shd.get_station_water_body_name(2143)
        self.assertIsInstance(name, str)
    
    def test_station_water_body_type(self):
        name = self.shd.get_station_water_body_type(2143)
        self.assertIsInstance(name, str)
    
    def test_station_coordinates(self):
        coordinates = self.shd.get_station_coordinates(2143)
        self.assertIsInstance(coordinates, dict)
        self.assertIn("latitude", coordinates)
        self.assertIsInstance(coordinates["latitude"], float)
        self.assertIn("longitude", coordinates)
        self.assertIsInstance(coordinates["longitude"], float)

    def test_station_parameters(self):
        parameters = self.shd.get_station_parameters(2143)
        self.assertIsInstance(parameters, dict)
        if "temperature" in parameters:
            self.assertIsInstance(parameters["temperature"], dict)
            self.assertIn("unit", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["unit"], str)
            self.assertIn("datetime", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["datetime"], str)
            self.assertIn("value", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["value"], float)
            self.assertIn("previous-24h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["previous-24h"], float)
            self.assertIn("delta-24h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["delta-24h"], float)
            self.assertIn("max-24h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["max-24h"], float)
            self.assertIn("mean-24h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["mean-24h"], float)
            self.assertIn("min-24h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["min-24h"], float)
            self.assertIn("max-1h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["max-1h"], float)
            self.assertIn("mean-1h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["mean-1h"], float)
            self.assertIn("min-1h", parameters["temperature"])
            self.assertIsInstance(parameters["temperature"]["min-1h"], float)
        if "level" in parameters:
            self.assertIsInstance(parameters["level"], dict)
            self.assertIn("unit", parameters["level"])
            self.assertIsInstance(parameters["level"]["unit"], str)
            self.assertIn("datetime", parameters["level"])
            self.assertIsInstance(parameters["level"]["datetime"], str)
            self.assertIn("value", parameters["level"])
            self.assertIsInstance(parameters["level"]["value"], float)
            self.assertIn("previous-24h", parameters["level"])
            self.assertIsInstance(parameters["level"]["previous-24h"], float)
            self.assertIn("delta-24h", parameters["level"])
            self.assertIsInstance(parameters["level"]["delta-24h"], float)
            self.assertIn("max-24h", parameters["level"])
            self.assertIsInstance(parameters["level"]["max-24h"], float)
            self.assertIn("mean-24h", parameters["level"])
            self.assertIsInstance(parameters["level"]["mean-24h"], float)
            self.assertIn("min-24h", parameters["level"])
            self.assertIsInstance(parameters["level"]["min-24h"], float)
            self.assertIn("max-1h", parameters["level"])
            self.assertIsInstance(parameters["level"]["max-1h"], float)
            self.assertIn("mean-1h", parameters["level"])
            self.assertIsInstance(parameters["level"]["mean-1h"], float)
            self.assertIn("min-1h", parameters["level"])
            self.assertIsInstance(parameters["level"]["min-1h"], float)
            self.assertIsInstance(parameters["level"], dict)
        if "discharge" in parameters:
            self.assertIsInstance(parameters["discharge"], dict)
            self.assertIn("unit", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["unit"], str)
            self.assertIn("datetime", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["datetime"], str)
            self.assertIn("value", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["value"], float)
            self.assertIn("previous-24h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["previous-24h"], float)
            self.assertIn("delta-24h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["delta-24h"], float)
            self.assertIn("max-24h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["max-24h"], float)
            self.assertIn("mean-24h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["mean-24h"], float)
            self.assertIn("min-24h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["min-24h"], float)
            self.assertIn("max-1h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["max-1h"], float)
            self.assertIn("mean-1h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["mean-1h"], float)
            self.assertIn("min-1h", parameters["discharge"])
            self.assertIsInstance(parameters["discharge"]["min-1h"], float)
            self.assertIsInstance(parameters["discharge"], dict)
            
    def test_station_temperature(self):
        temperature = self.shd.get_station_temperature(2143)
        self.assertIsInstance(temperature, dict)
        self.assertIn("unit", temperature)
        self.assertIsInstance(temperature["unit"], str)
        self.assertIn("datetime", temperature)
        self.assertIsInstance(temperature["datetime"], str)
        self.assertIn("value", temperature)
        self.assertIsInstance(temperature["value"], float)
        self.assertIn("previous-24h", temperature)
        self.assertIsInstance(temperature["previous-24h"], float)
        self.assertIn("delta-24h", temperature)
        self.assertIsInstance(temperature["delta-24h"], float)
        self.assertIn("max-24h", temperature)
        self.assertIsInstance(temperature["max-24h"], float)
        self.assertIn("mean-24h", temperature)
        self.assertIsInstance(temperature["mean-24h"], float)
        self.assertIn("min-24h", temperature)
        self.assertIsInstance(temperature["min-24h"], float)
        self.assertIn("max-1h", temperature)
        self.assertIsInstance(temperature["max-1h"], float)
        self.assertIn("mean-1h", temperature)
        self.assertIsInstance(temperature["mean-1h"], float)
        self.assertIn("min-1h", temperature)
        self.assertIsInstance(temperature["min-1h"], float)

    def test_station_temperature_unit(self):       
        unit = self.shd.get_station_temperature_unit(2143)
        self.assertIsInstance(unit, str)
    
    def test_station_temperature_datetime(self):       
        dt = self.shd.get_station_temperature_datetime(2143)
        self.assertIsInstance(dt, datetime.datetime)
    
    def test_station_temperature_value(self):       
        value = self.shd.get_station_temperature_value(2143)
        self.assertIsInstance(value, float)
    
    def test_station_temperature_previous24h(self):       
        previous24h = self.shd.get_station_temperature_previous24h(2143)
        self.assertIsInstance(previous24h, float)
    
    def test_station_temperature_delta24h(self):       
        delta24h = self.shd.get_station_temperature_delta24h(2143)
        self.assertIsInstance(delta24h, float)
    
    def test_station_temperature_max24h(self):       
        max24h = self.shd.get_station_temperature_max24h(2143)
        self.assertIsInstance(max24h, float)
    
    def test_station_temperature_mean24h(self):       
        mean24h = self.shd.get_station_temperature_mean24h(2143)
        self.assertIsInstance(mean24h, float)
    
    def test_station_temperature_min24h(self):       
        min24h = self.shd.get_station_temperature_min24h(2143)
        self.assertIsInstance(min24h, float)
    
    def test_station_temperature_max1h(self):       
        max1h = self.shd.get_station_temperature_max1h(2143)
        self.assertIsInstance(max1h, float)
    
    def test_station_temperature_mean1h(self):       
        mean1h = self.shd.get_station_temperature_mean1h(2143)
        self.assertIsInstance(mean1h, float)
    
    def test_station_temperature_min1h(self):       
        min1h = self.shd.get_station_temperature_min1h(2143)
        self.assertIsInstance(min1h, float)
            
    def test_station_level(self):
        level = self.shd.get_station_level(2143)
        self.assertIsInstance(level, dict)
        self.assertIn("unit", level)
        self.assertIsInstance(level["unit"], str)
        self.assertIn("datetime", level)
        self.assertIsInstance(level["datetime"], str)
        self.assertIn("value", level)
        self.assertIsInstance(level["value"], float)
        self.assertIn("previous-24h", level)
        self.assertIsInstance(level["previous-24h"], float)
        self.assertIn("delta-24h", level)
        self.assertIsInstance(level["delta-24h"], float)
        self.assertIn("max-24h", level)
        self.assertIsInstance(level["max-24h"], float)
        self.assertIn("mean-24h", level)
        self.assertIsInstance(level["mean-24h"], float)
        self.assertIn("min-24h", level)
        self.assertIsInstance(level["min-24h"], float)
        self.assertIn("max-1h", level)
        self.assertIsInstance(level["max-1h"], float)
        self.assertIn("mean-1h", level)
        self.assertIsInstance(level["mean-1h"], float)
        self.assertIn("min-1h", level)
        self.assertIsInstance(level["min-1h"], float)

    def test_station_level_unit(self):       
        unit = self.shd.get_station_level_unit(2143)
        self.assertIsInstance(unit, str)
    
    def test_station_level_datetime(self):       
        dt = self.shd.get_station_level_datetime(2143)
        self.assertIsInstance(dt, datetime.datetime)
    
    def test_station_level_value(self):       
        value = self.shd.get_station_level_value(2143)
        self.assertIsInstance(value, float)
    
    def test_station_level_previous24h(self):       
        previous24h = self.shd.get_station_level_previous24h(2143)
        self.assertIsInstance(previous24h, float)
    
    def test_station_level_delta24h(self):       
        delta24h = self.shd.get_station_level_delta24h(2143)
        self.assertIsInstance(delta24h, float)
    
    def test_station_level_max24h(self):       
        max24h = self.shd.get_station_level_max24h(2143)
        self.assertIsInstance(max24h, float)
    
    def test_station_level_mean24h(self):       
        mean24h = self.shd.get_station_level_mean24h(2143)
        self.assertIsInstance(mean24h, float)
    
    def test_station_level_min24h(self):       
        min24h = self.shd.get_station_level_min24h(2143)
        self.assertIsInstance(min24h, float)
    
    def test_station_level_max1h(self):       
        max1h = self.shd.get_station_level_max1h(2143)
        self.assertIsInstance(max1h, float)
    
    def test_station_level_mean1h(self):       
        mean1h = self.shd.get_station_level_mean1h(2143)
        self.assertIsInstance(mean1h, float)
    
    def test_station_level_min1h(self):       
        min1h = self.shd.get_station_level_min1h(2143)
        self.assertIsInstance(min1h, float)
    
    def test_station_discharge(self):
        discharge = self.shd.get_station_discharge(2143)
        self.assertIsInstance(discharge, dict)
        self.assertIn("unit", discharge)
        self.assertIsInstance(discharge["unit"], str)
        self.assertIn("datetime", discharge)
        self.assertIsInstance(discharge["datetime"], str)
        self.assertIn("value", discharge)
        self.assertIsInstance(discharge["value"], float)
        self.assertIn("previous-24h", discharge)
        self.assertIsInstance(discharge["previous-24h"], float)
        self.assertIn("delta-24h", discharge)
        self.assertIsInstance(discharge["delta-24h"], float)
        self.assertIn("max-24h", discharge)
        self.assertIsInstance(discharge["max-24h"], float)
        self.assertIn("mean-24h", discharge)
        self.assertIsInstance(discharge["mean-24h"], float)
        self.assertIn("min-24h", discharge)
        self.assertIsInstance(discharge["min-24h"], float)
        self.assertIn("max-1h", discharge)
        self.assertIsInstance(discharge["max-1h"], float)
        self.assertIn("mean-1h", discharge)
        self.assertIsInstance(discharge["mean-1h"], float)
        self.assertIn("min-1h", discharge)
        self.assertIsInstance(discharge["min-1h"], float)

    def test_station_discharge_unit(self):       
        unit = self.shd.get_station_discharge_unit(2143)
        self.assertIsInstance(unit, str)
    
    def test_station_discharge_datetime(self):       
        dt = self.shd.get_station_discharge_datetime(2143)
        self.assertIsInstance(dt, datetime.datetime)
    
    def test_station_discharge_value(self):       
        value = self.shd.get_station_discharge_value(2143)
        self.assertIsInstance(value, float)
    
    def test_station_discharge_previous24h(self):       
        previous24h = self.shd.get_station_discharge_previous24h(2143)
        self.assertIsInstance(previous24h, float)
    
    def test_station_discharge_delta24h(self):       
        delta24h = self.shd.get_station_discharge_delta24h(2143)
        self.assertIsInstance(delta24h, float)
    
    def test_station_discharge_max24h(self):       
        max24h = self.shd.get_station_discharge_max24h(2143)
        self.assertIsInstance(max24h, float)
    
    def test_station_discharge_mean24h(self):       
        mean24h = self.shd.get_station_discharge_mean24h(2143)
        self.assertIsInstance(mean24h, float)
    
    def test_station_discharge_min24h(self):       
        min24h = self.shd.get_station_discharge_min24h(2143)
        self.assertIsInstance(min24h, float)
    
    def test_station_discharge_max1h(self):       
        max1h = self.shd.get_station_discharge_max1h(2143)
        self.assertIsInstance(max1h, float)
    
    def test_station_discharge_mean1h(self):       
        mean1h = self.shd.get_station_discharge_mean1h(2143)
        self.assertIsInstance(mean1h, float)
    
    def test_station_discharge_min1h(self):       
        min1h = self.shd.get_station_discharge_min1h(2143)
        self.assertIsInstance(min1h, float)
