class Todo:
    DONE_MARKER = 'x'
    NOT_DONE_MARKER = ' '
    
    def __init__(self, title):
        self._title = title
        self.done = False

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, status):
        self._done = status

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return self.title == other.title and self.done == other.done

    def __ne__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return self.title != other.title or self.done != other.done

    def __str__(self):
        marker = Todo.DONE_MARKER if self.done else Todo.NOT_DONE_MARKER
        return f'[{marker}] {self.title}'
