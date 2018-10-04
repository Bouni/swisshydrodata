from unittest import TestCase

from datetime import datetime
import swisshydrodata

class TestSwissHydroData(TestCase):

    def setUp(self):
        self.shd = swisshydrodata.SwissHydroData()
        self.shd.load_station_data(2143)

    def test_latest_level(self):
        level = self.shd.get_latest_level()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m ü.M")

    def test_latest_temperature(self):
        level = self.shd.get_latest_temperature()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "°C")

    def test_latest_discharge(self):
        level = self.shd.get_latest_discharge()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m3/s")

    def test_min_level(self):
        level = self.shd.get_min_level()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m ü.M")

    def test_min_temperature(self):
        level = self.shd.get_min_temperature()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "°C")

    def test_min_discharge(self):
        level = self.shd.get_min_discharge()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m3/s")

    def test_max_level(self):
        level = self.shd.get_max_level()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m ü.M")

    def test_max_temperature(self):
        level = self.shd.get_max_temperature()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "°C")

    def test_max_discharge(self):
        level = self.shd.get_max_discharge()
        self.assertIsInstance(level["timestamp"], datetime)
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m3/s")

    def test_mean_level(self):
        level = self.shd.get_mean_level()
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m ü.M")

    def test_mean_temperature(self):
        level = self.shd.get_mean_temperature()
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "°C")

    def test_mean_discharge(self):
        level = self.shd.get_mean_discharge()
        self.assertIsInstance(level["value"], float)
        self.assertIsInstance(level["unit"], str)
        self.assertEqual(level["unit"], "m3/s")

    def test_missing_values(self):
        self.shd.load_station_data(2392)
        self.assertIsNone(self.shd.get_mean_discharge())

