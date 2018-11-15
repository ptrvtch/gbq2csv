# gbq2csv

This script does one simple task: sends SQL query to Google BigQuery and writes the results to csv file. 

## Prerequisites & Getting Started

You should have Python 3 installed, as well as packages `pandas` and `pandas-gbq`. 

To start using the script, copy this repo:
```
git clone https://github.com/ptrvtch/gbq2csv.git
cd gbq2csv
```
If you don't have packages `pandas` and `pandas-gbq` installed, run this command in your terminal:
```
$ cd gbq2csv
$ pip install -r requirements.txt
```
After that:
* Install dependencies with command `pip install -r requirements.txt`
* Paste the query in the `input.sql` file and save it
* Change the key.json to your service account key (get more info here: [Getting Started with Authentication](https://cloud.google.com/docs/authentication/getting-started))

Now you're ready to go!


## Run the script

The simplest way to run the script is:
```
$ python gbq2csv.py
```
After you run this command, the script will run the query from `input.sql` and write the results to `output.csv` file in the same directory. 

You can also run the script with following flags:
* `-v`, `--verbose`: prints more details in the command line window during script execution.
* `-i, --input <input file>`: specify the name of input file. It may be any file with text format which contains SQL query.
* `-o, --output <output file>`: specify the name of output file. The output will be stored in CSV format.
* `-k, --key <key file>`: specify the path to key.json (useful if you have multiple keys with different access levels).
* `-h, --help`: show help for the usage. 

## Built With

* [Pandas](https://pandas.pydata.org/)
* [Pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/)


## License

This project is licensed under the MIT License.