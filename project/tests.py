# -*- coding: utf-8 -*-
import sys
import os.path
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from falcon.testing import TestBase


class HelloTest(TestBase):
    def test_hello(self):
        resp = self.simulate_request('/hello')
        self.assertEqual(resp.status, 200)
