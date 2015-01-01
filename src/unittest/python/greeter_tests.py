from StringIO import StringIO
import unittest

from mock import patch

from hellosphinx.greeter import Greeter


class TestHelloSphinx(unittest.TestCase):

    def setUp(self):
        self.sut = Greeter("Hello Sphinx!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_hello_sphinx(self, mock_stdout):
        self.sut.speak()
        self.assertEqual(mock_stdout.getvalue(), "Hello Sphinx!\n")