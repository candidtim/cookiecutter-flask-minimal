import unittest

import {{cookiecutter.package_name}}


class {{cookiecutter.package_name.capitalize()}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.package_name}}.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertTrue('Welcome to {{cookiecutter.application_name}}' in rv.data.decode())


if __name__ == '__main__':
    unittest.main()
