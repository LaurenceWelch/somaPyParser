# somaPyParser
The purpose of this WIP script is to parse log files.

# current functionality
As of now, the script can detect and count events based on a regular expression, more functionality is planned.

# basic usage
Install python 3, open a terminal and perform these commands.
```bash
python3
```
```python
import somaPyParser
somaPyParser.countIP('logfile.log')
```
Much more functionality can be derived by calling the helper functions directly.
The file2List function takes a filename, a re string, optionally a slice and optionally invert=True|False and converts it to a list, filtering lines through a whitelist or a blacklist depending on `invert`.
The getCount function takes a list, a regular expression and a lambda, and uses that re to pull specific data points from each line which can be processed by the lambda function. It uses a dictionary to count occurences of this re and returns said dictionary.
Finally, the printD function takes a dictionary and prints it.
