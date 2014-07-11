import unittest
import main

class test_imagejudge(unittest.TestCase):
    def setUp(self):
        self.judge = main.JudgeGoal()

    def testfile1(self):
        self.judge.loadimage(filename='./torero.png')
        self.judge.objectselect()
        self.assertEqual(self.judge.objectdirection(), "left")

unittest.main()
