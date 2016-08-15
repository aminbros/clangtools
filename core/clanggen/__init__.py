
from .txt2cstr import txt2cstr_cli
from .bin2carray import bin2carray_cli
from core import ProgramDef

programs = [
  ProgramDef("txt2cstr", txt2cstr_cli),
  ProgramDef("bin2carray", bin2carray_cli),
]
