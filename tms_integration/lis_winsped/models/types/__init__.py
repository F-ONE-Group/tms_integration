from typing import Union
from .adr import Adr
from .auftrag import Auftrag
from .ende import Ende
from .ggut import Ggut
from .ladeli import Ladeli
from .lademi import Lademi
from .posit import Posit
from .start import Start
from .text import Text


RecordTypes = Union[Auftrag, Ende, Ggut, Ladeli, Lademi, Posit, Start, Text, Adr]
