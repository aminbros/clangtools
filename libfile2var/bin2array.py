
def writedata(infile, sout, options):
  b = infile.read(1)
  sout.write("{")
  while len(b) > 0:
    sout.write(str(ord(b[0])) + options.op_concat);
    b = infile.read(1)
  sout.write("}")
