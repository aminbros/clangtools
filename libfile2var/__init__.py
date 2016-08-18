from . import txt2str
from . import bin2array
from collections import namedtuple
import os


ProgramDef = namedtuple("ProgramDef", ["name","writedata"])
InputType = namedtuple("InputType", ["name", "path"])
Options = type("Options", (object,),
               dict((name,None) for name in
                    ["declare", "pretty", "defprefix", "op_eq",
                     "op_concat", "endstatement", "varcomment",
                     "headerext", "sourceext", "noheader",
                     "headerstart", "headerend",
                     "sourcestart", "sourceend", "forcenoheader"]))

programs = [
  ProgramDef("txt2str", txt2str.writedata),
  ProgramDef("bin2array", bin2array.writedata),
]

def name2var(name):
  return name.replace(".", "_")

def execute_program(program, outputdir, outputname, inputs, options):
  if options.forcenoheader:
    options.noheader = True
  if options.noheader:
    hout = None
    sout = open("{}/{}".format(outputdir, outputname), "w")
  else:
    hout = open("{}/{}".format(outputdir, outputname) + options.headerext, "w")
    sout = open("{}/{}".format(outputdir, outputname) + options.sourceext, "w")
  output_varname = name2var(outputname)
  odict = { "uppername": output_varname.upper(), "varname": output_varname,
            "name": outputname }
  if not options.noheader:
    hout.write(options.headerend.format(**odict))
  sout.write(options.sourceend.format(**odict))

  for inp in inputs:
    name = inp.name
    path = inp.path
    varname= name2var(name)
    pnewline = "\n" if options.pretty else ""
    fsize = os.stat(path).st_size
    fdict = {"path":path, "varname":varname, "filesize": fsize, "name": name,
             "filesize_p1":fsize + 1 }
    infile = open(path, "r")
    if hout != None:
      hout.write(options.declare.format(**fdict) + pnewline)
    sout.write(options.defprefix.format(**fdict) + options.op_eq + pnewline)
    program.writedata(infile, sout, options)
    sout.write(options.endstatement + \
               options.varcomment.format(**fdict) + pnewline)

  if not options.noheader:
    hout.write(options.headerend.format(**odict))
    hout.close()

  sout.write(options.sourceend.format(**odict))  
  sout.close()
