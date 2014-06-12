class Core():
    def __init__(self):
        self._inputs = []
        self._outputs = []
        self._processors = []
    def add_input(self, inputs):
        inputs.core = self
        self._inputs.append(inputs)
    def remove_input(self, input_name):
        i = self.get_input(input_name)
        if i:
            self._inputs.remove(i)
        else:
            return None
    def get_input(self, input_name):
        for i in self._inputs:
            if i.name = input_name:
                return i
        return None
    def received(self, text):
        