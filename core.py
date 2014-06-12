class Core():
    def __init__(self):
        self._inputs = []
        self._outputs = []
        self._processors = []
    ######################################
    # Input Functions
    ######################################
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
    
    ######################################
    # Output Functions
    ######################################
    def add_output(self, output):
        output.core = self
        self._outputs.append(output)
    def remove_output(self, output_name):
        o = self.get_output(input_name)
        if o:
            self._outputs.remove(o)
        else:
            return None
    def get_output(self, output_name):
        for o in self._outputs:
            if o.name = output_name:
                return o
        return None

    ######################################
    # Processor Functions
    ######################################
    def add_processor(self, processor):
        processor.core = self
        self._processors.append(processor)
    def remove_processor(self, processor_name):
        p = self.get_processor(processor_name)
        if p:
            self._processors.remove(p)
        else:
            return None
    def get_processor(self, processor_name):
        for p in self._processors:
            if p.name = processor_name:
                return p
        return None

    ######################################
    # Core Hooks
    ######################################
    def received(self, text):
        for p in self.processors:
            p.received()
    def response(self, text):
        for o in self.outputs:
            o.response()
    
    ######################################
    # Update Loop
    ######################################
    def update(self):
        for i in self.inputs:
            i.update()