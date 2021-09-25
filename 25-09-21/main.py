import unittest
from tasks import *

class TasksTest(unittest.TestCase):

  def test_one_taks_done(self):
    input = "1 1\n1\n"

    self.assertEqual(divideTasks(input), "\n\n")

  def test_one_task_not_done(self):
    input = "1 0\n\n"

    self.assertEqual(divideTasks(input), "1\n\n")

  def test_two_tasks_one_not_done(self):
    input = "2 1\n1\n"

    self.assertEqual(divideTasks(input), "2\n\n")

  def test_three_tasks_one_done(self):
    input = "3 1\n2\n"

    self.assertEqual(divideTasks(input),"1\n3\n")

  def test_three_tasks_another_one_done(self):
    input = "3 1\n1\n"

    self.assertEqual(divideTasks(input),"2\n3\n")

  def test_example_one(self):
    input = "6 3\n2 4 1\n"

    self.assertEqual(divideTasks(input),"3 6\n5\n")

  def test_example_two(self):
    input = "3 2\n3 2\n"

    self.assertEqual(divideTasks(input),"1\n\n")

  def test_example_three(self):
    input = "8 2\n3 8\n"

    self.assertEqual(divideTasks(input),"1 4 6\n2 5 7\n")

  def test_breaks_limits(self):
    input = "1 2\n1 2\n"

    self.assertEqual(divideTasks(input), "\n\n")

unittest.main()
