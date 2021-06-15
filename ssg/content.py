import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = Content.__regex.split(string, 2)

    def __init__(self, metadata, content):
        self.data = metadata
        self.dat = {'content': content}

    @property
    def body(self):
        return self.data['content']

    @property
    def type(self):
        if 'type' in self.data:
            return self.data['type']
        else:
            return None

    @type.setter
    def type(self, value):
        self.data['type'] = value

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        iter.self.data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        return str(data)





