import unittest
from website_check import check


class WebsiteChecks(unittest.TestCase):
    def test_valid_structure(self):
        result = check('<title>Example</title><main><h1>Hi</h1><img alt="x"></main>')
        self.assertTrue(all(result.values()))

    def test_missing_elements_are_failures(self):
        result = check('<title> </title><p>Hello</p><img src="x">')
        self.assertTrue(all(not value for value in result.values()))

    def test_decorative_image_and_main_role(self):
        result = check('<title>T</title><div role="main"><h1>A</h1><img alt=""></div>')
        self.assertTrue(all(result.values()))


if __name__ == '__main__':
    unittest.main()
