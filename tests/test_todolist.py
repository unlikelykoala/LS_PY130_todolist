import unittest
from todolist import TodoList, Todo


class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        lst = self.todos.to_list()
        self.assertIsInstance(lst, list)
        self.assertIn(self.todo1, lst)
        self.assertIn(self.todo2, lst)
        self.assertIn(self.todo3, lst)

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(1)
    
        with self.assertRaises(TypeError):
            self.todos.add('hey')

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)

    def test_mark_done_at(self):
        self.assertFalse(self.todos.todo_at(0).done)
        self.todos.mark_done_at(0)
        self.assertTrue(self.todos.todo_at(0).done)
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)

    def test_mark_unone_at(self):
        self.todos.mark_done_at(0)
        self.assertTrue(self.todos.todo_at(0).done)

        self.todos.mark_undone_at(0)        
        self.assertFalse(self.todos.todo_at(0).done)

        with self.assertRaises(IndexError):
            self.todos.todo_at(3)

    def mark_all_done(self):
        def is_done(todo):
            return todo.done == True

        self.assertFalse(all(self.todos.each(is_done)))

        self.todos.mark_all_done()
        self.assertTrue(all(self.todos.each(is_done)))

    def test_remove_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(3, len(self.todos))
        
        self.todos.remove_at(0)
        self.assertNotEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(2, len(self.todos))

        with self.assertRaises(IndexError):
            self.todos.remove_at(3)

    def test_str(self):
        string = [f'----- {self.todos.title} -----']

        for todo in self.todos.to_list():
            string.append(str(todo))

        self.assertEqual('\n'.join(string), str(self.todos))

    def test_str_done_todo(self):
        self.todos.mark_done_at(1)

        string = [f'----- {self.todos.title} -----']

        for todo in self.todos.to_list():
            string.append(str(todo))

        self.assertEqual('\n'.join(string), str(self.todos))

    def test_str_all_done_todo(self):
        self.todos.mark_all_done()

        string = [f'----- {self.todos.title} -----']

        for todo in self.todos.to_list():
            string.append(str(todo))

        self.assertEqual('\n'.join(string), str(self.todos))

    def test_each(self):
        lst = []

        def add_to_lst(todo):
            lst.append(todo)

        self.todos.each(add_to_lst)

        self.assertEqual(lst, self.todos.to_list())

    def test_select(self):
        self.todos.mark_done_at(2)

        new = self.todos.select(lambda todo: todo.done)

        self.assertEqual([self.todo3], new.to_list())




if __name__ == "__main__":
    unittest.main()
