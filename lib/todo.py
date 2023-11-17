class TodoList:
    def __init__(self):
        self.todos = []


    def add(self, todo):
        """Adds a Todo object to the TodoList
        Params:
            A Todo instance
        Returns:
            None
        Side effects:
            updated self.todo list with Todo instance"""
        if type(todo) == Todo:
            self.todos.append(todo)


    def incomplete(self):
        """Returns:
            A list of Todo instances representing the todos that are not complete"""
        return [todo for todo in self.todos if not todo.completed]


    def complete(self):
        """Returns:
            A list of Todo instances representing the todos that are complete"""
        return [todo for todo in self.todos if todo.completed]


    def give_up(self):
        """Returns:
            None
        Side-effects:
            Marks all todos as complete"""
        for todo in self.todos:
            todo.mark_complete()



class Todo:
    def __init__(self, task):
        """Parameters:
            task: a string representing the task to be done
        Side-effects:
            Sets the task property
            Sets the complete property to False"""
        self.task = task
        self.completed = False


    def mark_complete(self):
        """Returns:
            Nothing
        Side-effects:
            Sets the complete property to True"""
        self.completed = True