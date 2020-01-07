import sys
import csv

def ft_prediction(b, a, feature):
    print("\nWith input "+ str(feature) + " the predicted output is " + str(int(b + (feature * a))) + "$\n")

def ft_load():
    b = 0
    a = 0
    f = open("data/temp","r")
    content_reader = csv.reader(f, delimiter=" ")
    for row in content_reader:
        b = row[0]
        a = row[1]
    f.close()
    return (float(b), float(a))

def main():
    if (len(sys.argv) != 2):
        print("error: you need to provide one argument")
    else:
        b, a = ft_load()
        ft_prediction(b, a, int(sys.argv[1]))

if __name__ == "__main__":
    main()
