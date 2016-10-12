import codage64
import sys

def usage():
    '''
    prints how to use the program
    '''
    print("Usage : %s [-e|-d] <fichier>\n" % sys.argv[0], file=sys.stderr)
    print("\t -e pour encoder\n\t -d pour decoder\n", file = sys.stderr)
    exit(1)

def main():
  if len(sys.argv) != 3:
      usage()
  else:
      option = sys.argv[1]
      file = sys.argv[2]
      if option == "-e":
          codage64.base64_encode(file)
      elif option == "-d":
          codage64.base64_decode(file)
      else:
          usage()

if __name__ == '__main__':
    main() 
