import sys
import help

def main(arg1 = "-h", arg2=""):
  if arg1 == "-h" or arg1 == "":
    help.printHelp()
  else:
    help.unknownParam()

if __name__ == "__main__":
  paramsCount = len(sys.argv)

  if paramsCount == 2:
     main(sys.argv[1])

  elif paramsCount == 3:
    main(sys.argv[1], sys.argv[2])
  
  else:
    help.wrongParamsCount()