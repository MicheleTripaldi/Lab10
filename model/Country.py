from dataclasses import dataclass


@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str
    def __hash__(self):
        return self.CCode

    def __eq__(self,other):
        return self.CCode == other.CCode

