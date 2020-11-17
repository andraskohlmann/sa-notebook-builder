import json


class Builder:
    @staticmethod
    def render(filename):
        with open(filename, "w+") as f:
            nb = {"cells": []}
            f.write(f'{json.dumps(nb)}')
