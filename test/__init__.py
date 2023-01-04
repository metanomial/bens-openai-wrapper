import unittest


def run():
    # Load all tests
    loader = unittest.TestLoader()
    suite = loader.discover("test")

    # Run the tests
    runner = unittest.TextTestRunner()
    runner.run(suite)
