#!/usr/bin/python3
""" Unittest for base class
"""
import unittest
from os import path, remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_id(unittest.TestCase):
    """ Class for unittest of __init__ and id """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """ Id no argument """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_none(self):
        """ Id None """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_ints(self):
        """ Id int """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        b2 = Base(-5)
        self.assertEqual(b2.id, -5)
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_extra_args(self):
        """ More than 1 argument """
        with self.assertRaises(TypeError):
            b1 = Base(5, 1)

    def test_private(self):
        """ Check priv attribute in instance """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects


class Test_instance(unittest.TestCase):
    """ Clas for unittest of  instance """

    def test_base_self(self):
        """ Check if is instance """
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))

    def test_Rectangle(self):
        """ Check if is instance """
        r1 = Rectangle(1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_Square(self):
        """ Check if is instance """
        s1 = Square(1)
        self.assertTrue(isinstance(s1, Base))


class Test_to_json_string(unittest.TestCase):
    """ Class for unittest of to_json_string method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_conversion(self):
        """ Conversion with None, empty list, and dicts"""

        l0 = None
        j0 = Base.to_json_string(l0)
        self.assertEqual(j0, "[]")
        self.assertEqual(type(j0), str)

        l1 = []
        j1 = Base.to_json_string(l1)
        self.assertEqual(j1, "[]")
        self.assertEqual(type(j1), str)

        l2 = [{}]
        j2 = Base.to_json_string(l2)
        self.assertEqual(j2, "[{}]")
        self.assertEqual(type(j2), str)

        l3 = [{'x': 1, 'y': 2}]
        j3 = Base.to_json_string(l3)
        st = str(l3)
        self.assertEqual(j3, st.replace("'", "\""))
        self.assertEqual(type(j3), str)

        l4 = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        j4 = Base.to_json_string(l4)
        st = str(l4)
        self.assertEqual(j4, st.replace("'", "\""))
        self.assertEqual(type(j4), str)

    def test_Rectangle(self):
        """ Test with Rectangle instance """
        r1 = Rectangle(10, 7, 2, 

