from machine.isa import Opcode

SCLK = 0
MISO = 1
MOSI = 2
CS = 3

class Ports:

    def __init__(self, input_tokens, code_file):
        self.tick = 0
        self.data = {SCLK: 0, MISO: 0, MOSI: 0, CS: 0}
        self.data_reg = 0
        self.output_buffer = []
        self.input_tokens = input_tokens
        self.first_cs = True
        self.can_remove_from_input = False
        self.data_path = None

    def io_buffer_manager(self, opcode, port_id):
        acc = bin(self.data_path.acc)[2:].zfill(32)
        if opcode == Opcode.IN:
            acc = acc[:-1] + str(self.data[port_id])
            self.data_path.acc = int(acc, 2)
        else:
            self.data[port_id] = int(acc[0])

    def inverse_signal(self, port_id):
        self.data[port_id] = int(not self.data[port_id])

        if port_id == SCLK and self.data[port_id] == 1:
            self.shift()
        elif port_id == CS and self.data[CS] == 1:
            self.add_to_output_buffer()

    def shift(self):
        self.data_path.acc = (self.data_path.acc & (2**31 - 1)) << 1
        self.get_impulse()

    def add_input(self, tick):
        if len(self.input_tokens) > 0 and self.data[CS] == 1 and tick >= self.input_tokens[0][0]:
            self.data_reg = ord(self.input_tokens[0][1])
            self.can_remove_from_input = True

    def get_impulse(self):
        binary = bin(self.data_reg)[2:].zfill(8)
        self.data[MISO] = int(binary[0])
        binary = binary[1:] + str(self.data[MOSI])
        self.data_reg = int(binary, 2)

    def add_to_output_buffer(self):
        if self.data[CS] == 1:
            if self.first_cs:
                self.first_cs = False
            else:
                if self.data_reg != 1:
                    self.output_buffer.append(chr(self.data_reg))
                if len(self.input_tokens) > 0 and self.can_remove_from_input:
                    self.input_tokens.pop(0)
                    self.can_remove_from_input = False
                self.data_reg = 0

