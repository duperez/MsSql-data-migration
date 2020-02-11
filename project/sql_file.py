class sql_file:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.data = ''

    def set_data(self):
        sql = open(self.path + self.name, 'r')
        for line in sql:
            self.data = self.data + line