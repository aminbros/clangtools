txt2str = {
  "declare": "extern const char {varname}[{filesize_p1}];",
  "pretty": True,
  "defprefix": "const char {varname}[{filesize_p1}] ",
  "op_eq": "=",
  "op_concat": "",
  "endstatement": ";",
  "varcomment": " // {varname}\n",
  "headerext": ".h",
  "sourceext": ".c",
  "headerstart": "#ifndef _{uppername}__H_\n"
                 "#define _{uppername}__H_\n\n",
  "headerend": "\n\n#endif\n",
  "sourcestart": "",
  "sourceend": "\n",
  "noheader": False
}
bin2array = {
  "declare": "extern const char {varname}[{filesize}];",
  "pretty": True,
  "defprefix": "const char {varname}[{filesize}] ",
  "op_eq": "=",
  "op_concat": ",",
  "endstatement": ";",
  "varcomment": " // {varname}\n",
  "headerext": ".h",
  "sourceext": ".c",
  "headerstart": "#ifndef _{uppername}__H_\n"
                 "#define _{uppername}__H_\n\n",
  "headerend": "\n\n#endif\n",
  "sourcestart": "",
  "sourceend": "\n",
  "noheader": False
}
