from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trainer_file_path : str
    test_file_path : str
    