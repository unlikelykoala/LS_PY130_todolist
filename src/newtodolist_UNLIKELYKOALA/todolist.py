from todo import Todo


class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only append Todo instances to TodoList")
        self._todos.append(todo)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)
    
    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
    
    def todo_at(self, idx):
        return self._todos[idx]
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)
    
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        todo = self.find_by_title(title)
        todo.done = True
    
    def mark_done_at(self, idx):
        self._todos[idx].done = True

    def mark_all_done(self):
        def done(todo):
            todo.done = True
        
        self.select(done)

    def mark_undone_at(self, idx):
        self._todos[idx].done = False

    def mark_all_undone(self):
        def undone(todo):
            todo.done = False
        
        self.select(undone)
    
    def remove_at(self, idx):
        self._todos.pop(idx)

    def select(self, callback):
        new = TodoList(self.title)
        # new._todos = [todo for todo in self._todos if callback(todo)]
        new._todos = list(filter(callback, self._todos))

        return new
    
    def to_list(self):
        return self._todos.copy()
    
    def __len__(self):
        return len(self._todos)
    
    def __str__(self):
        # strings = f'----- {self.title} -----\n'
        # for todo in self._todos:
        #     strings += f'{todo}\n'
        
        # return strings

        strings = [f'----- {self.title} -----']
        
        for todo in self._todos:
            strings.append(str(todo))
        
        return '\n'.join(strings)
