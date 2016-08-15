import re
import os

def name2var(name):
  return name.replace(".", "_")

def bin2carray(varname, binfn, hout, sout):
  infile = open(binfn, "rb")
  fsize = os.stat(binfn).st_size
  if hout != None:
    hout.write("extern const unsigned char " + varname + "[" + str(fsize) + "];\n")
  sout.write("const unsigned char " + varname + "[" + str(fsize) + "] = \n{")
  b = infile.read(1)
  while len(b) > 0:
    sout.write(str(b[0]) + ",");
    b = infile.read(1)
  sout.write("};\n // var " + varname + "\n\n")

def bin2carray_cli(outputdir, outputname, inputs, codeonly=False):
  if codeonly:
    hout = None
    sout = open("{}/{}".format(outputdir, outputname), "w")
  else:
    hout = open("{}/{}.h".format(outputdir, outputname), "w")
    sout = open("{}/{}.c".format(outputdir, outputname), "w")
  output_varname = name2var(outputname)
  if not codeonly:
    hout.write(
      "#ifndef _{name}__H_\n"
      "#define _{name}__H_\n\n".format(name=output_varname.upper()))

  if not codeonly:
    sout.write("\n\n")

  for inp in inputs:
    varname = name2var(inp.name)
    bin2carray(varname, inp.path, hout, sout)

  if not codeonly:
    sout.write("\n\n")
    hout.write("\n\n#endif\n")
    hout.close()
  
  sout.close()
