from typing import List
from pathlib import Path
import shutil


class Parser:

    def __init__(self):
        self.extensions=List[str]

    def valid_extension(self, extension):
        if extension in self.extensions:
            return True

    @staticmethod
    def parse(self, path, source, dest):
        Path(path)
        Path(source)
        Path(dest)

    def read(self, path):
        with open(Path(path), mode="rf", encoding="utf-8") as f:
            return f.read()

    def write(self, path, dest, content, ext='.html'):
        full_path = self.dest / path.with_suffix(ext)
        with open(Path(path), mode="wf", encoding="utf-8") as f:
            f.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path)


class ResourceParsed(Parser):

    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    Parser.parse()


