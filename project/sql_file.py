class sql_file:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.data = ''

    def set_data(self):
        sql = open(self.path + self.name, 'r')
        proc = ''
        for line in sql:
            proc = proc + line
            self.data = proc