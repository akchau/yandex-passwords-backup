import os
import unittest

from src.settings import BASE_DIR

TEST_FOLDER = os.path.join(BASE_DIR, 'tests')


if __name__ == '__main__':
    tests = unittest.TestLoader().discover(TEST_FOLDER)
    unittest.TextTestRunner(verbosity=2).run(tests)