from pathlib import Path


class Site:

    def __init__(self, source, dest, parsers):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = None

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(self, extension):
        for parser in self.parsers:


    def run_parser(self, path):
        