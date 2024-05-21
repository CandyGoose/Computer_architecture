import logging


class Logger:
    def __init__(self, name, type):
        self.code = name
        self.type = type

        with open(f"machine/logs/{type}.txt", "w") as log:
            log.truncate(0)

        self.log = logging.getLogger(type)
        self.log.setLevel(logging.DEBUG)
        handler = logging.FileHandler(f"machine/logs/{type}.txt", "w")
        formatter = logging.Formatter("%(levelname)s: %(message)s")

        handler.setFormatter(formatter)
        self.log.addHandler(handler)

    def skip_processor_information(self, tick):
        codes = {
            "hello_machine.txt": tick == 153 or tick == 390,
            "cat_machine.txt": tick == 154 or tick == 394,
            "hello_user_name_machine.txt": tick in [182, 423, 8782],
            "prob1_machine.txt": tick == 118
        }
        if codes[self.code]:
            self.log.warning("\n... Continue! ...\n")

    def can_log(self, tick):
        codes = {}
        if self.type == "processor":
            codes = {
                "hello_machine.txt": tick <= 100,
                "cat_machine.txt": tick <= 79 or 4268 <= tick <= 5000,
                "hello_user_name_machine.txt": tick <= 100,
                "prob1_machine.txt": tick <= 100 or 1250 <= tick
            }
        return codes[self.code]

    def info(self, msg, tick=0):
        if self.can_log(tick):
            self.log.info(msg)

    def debug(self, object, tick=0):
        if self.can_log(tick):
            self.log.debug(object)
            self.skip_processor_information(tick)

    def close(self):
        self.log.handlers.pop()
