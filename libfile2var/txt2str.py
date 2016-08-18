import re

toinq_escpttrn = re.compile("[\"\\\\]")

def toinquote(txt):
  ret = toinq_escpttrn.sub(r'\\\g<0>', txt)
  ret = ret.replace("\n", "\\n")
  return ret

def writedata(infile, sout, options):
  if options.pretty:
    line = infile.readline()
    while line != "":
      sout.write("\"" + toinquote(line) + "\"")
      line = infile.readline()
      if line != "":
        sout.write(options.op_concat)
      sout.write("\n")
  else:
    sout.write("\"")
    for line in infile:
      toinquote(line)
    sout.write("\"")
