import re

def name2var(name):
  return name.replace(".", "_")

toinq_escpttrn = re.compile("[\"\\\\]")

def toinquote(txt):
  ret = toinq_escpttrn.sub(r'\\\g<0>', txt)
  ret = ret.replace("\n", "\\n")
  return ret

def txt2cstring(varname, txtfn, hout, sout):
  infile = open(txtfn, "r")
  if hout != None:
    hout.write("extern const char *" + varname + ";\n")
  sout.write("const char *" + varname + " = \n")
  for line in infile:
    sout.write("\"" + toinquote(line) + "\"\n")
  sout.write("; // var " + varname + "\n\n")


def txt2cstr_cli(outputdir, outputname, inputs, codeonly=False):
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
    txt2cstring(varname, inp.path, hout, sout)

  if not codeonly:
    sout.write("\n\n")
    hout.write("\n\n#endif\n")
    hout.close()
  
  sout.close()
