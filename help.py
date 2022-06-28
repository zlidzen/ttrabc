def printHelp():
  print(
"""
There is app help!
  please use following commands:
    ttrabc -h   - for Help;
    ttrabc -bl  - for listing brands;
    ttrabc -blr {brand}  - for listng models of rubber in one brand;
    ttrabc -blb {brand}  - for listng models of blade in one brand;
    ttrabc -cr {brand:model} {brand:model}...  - for rubber compare;
    ttrabc -cb {brand:model} {brand:model}...  - for blade compare.

  GLHF.
  """)

def wrongParamsCount():
  print("Wrong params count. Try ttrabc -h.")

def unknownParam():
  print("Unknown param. Try ttrabc -h.")

def main():
  printHelp

if __name__ == "__main__":
  main()