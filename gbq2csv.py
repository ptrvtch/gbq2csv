import getopt
import sys
import os
import json
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:k:v', [
            'help', 'input=', 'output=', 'key=', 'verbose'])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    verbose = False
    inputfile = 'input.sql'
    outputfile = 'output.csv'
    key = 'key.json'
    project_id = ''
    for o, a in opts:
        if o in ('-h', '--help'):
            print("usage: gbq-csv-cli.py -i <inputfile> -o <outputfile>. By default takes 'input.sql' as input and 'output.csv' as output, 'key.json' as credentials key")
            sys.exit()
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-i', '--input'):
            inputfile = a
        elif o in ('-o', '--output'):
            outputfile = a
        elif o in ('-k', '--key'):
            key = a
    print("input is {}, output is {}, key is {}\n".format(
        inputfile, outputfile, key)) if verbose else None
    try:
        query = open(inputfile, 'r').read()
        print("query: {}".format(query)) if verbose else None
        project_id = json.load(open(key))['project_id']
        print("project_id is {}".format(project_id)) if verbose else None
    except Exception as e:
        print("exception: {}".format(str(e)))
        sys.exit(2)
    try:
        df = pd.read_gbq(query, project_id=project_id,
                         dialect="standard", private_key=key)
        print(df.head()) if verbose else None
        df.to_csv(outputfile, index=False)
        print("Done! {} rows saved to {}".format(len(df), outputfile))
    except Exception as e:
        print("Error running query: {}".format(str(e)))
        sys.exit(2)


if __name__ == "__main__":
    main()
