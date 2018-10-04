from unittest import TestCase

from datetime import datetime
import swisshydrodata

class TestSwissHydroData(TestCase):

    def setUp(self):
        self.shd = swisshydrodata.SwissHydroData()

    def test_get_data(self):
        self.assertEqual(self.shd.data,
                         {"level": [], "temperature": [], "discharge": []})
        self.shd.load_station_data(2143)
        self.assertNotEqual(self.shd.data,
                            {"level": [], "temperature": [], "discharge": []})

    def test_latest_level(self):
        self.shd.load_station_data(2143)
        level = self.shd.get_latest_level()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m ü.M.")

    def test_latest_temperature(self):
        self.shd.load_station_data(2143)
        level = self.shd.get_latest_temperature()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "°C")

    def test_latest_discharge(self):
        self.shd.load_station_data(2143)
        level = self.shd.get_latest_discharge()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m3/s")

    def test_not_measured_values(self):
        self.shd.load_station_data(2392)
        level = self.shd.get_latest_discharge()
        self.assertIsNone(level)
