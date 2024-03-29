import sys

import LarvaLibs.Utility as Utility

class Log:
    def __init__(self, contents: str, use_timestamp=True):
        self.contents = str(contents)
        self.name = sys.argv[0].split("\\")[-1].split(".")[0]
        self.use_timestamp = use_timestamp

    def build(self) -> str:
        log = f"{Utility.timestamp()} " * self.use_timestamp
        log += f"{self.name}: {self.contents}"
        return log

    def to_larva(self, pipeline=True) -> None:
        """Display the log.
        
        Use the pipeline if `pipeline`, else print out the log."""
        if pipeline:
            Utility.file_write(Utility.pipe_path("larva"), self.build(), "a")
        else:
            print(self.build())
