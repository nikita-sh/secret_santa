# Secret Santa

A command line application to generate a secret santa matching made using Python. It uses Ford-Fulkerson to find a matching which is probably over-engineered, but I hadn't played with graphs in a while so I thought it'd be fun.

### Running the application
1. Make sure you have `python3` and `pip3` installed.
2. Clone the repository.
3. Run `install.sh` to download any dependencies.
4. Run `python3 secret_santa -s source_file.txt -e exceptions_file.txt`

Usage information:
```
usage: Secret Santa [-h] -s SOURCE [-e EXCEPTIONS]

Assigns Secret Santa pairs given a list of emails

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Path to file containing emails to match.
  -e EXCEPTIONS, --exceptions EXCEPTIONS
                        Path to file containing forbidden pairings.
```

The output will be printed to the console. The exceptions file is an optionYou can also use the `-h` flag for help with command line options.

### File Format

The application expects the following formats for input files. For the source file, use a `.txt` file with a name and email delimited by a comma on each line. For example:
```
input.txt
---
Nikita Shumeiko,email@gmail.com
John Doe,jdoe@gmail.com
Jane Doe,jadoe@gmail.com
Dane Joe,dajoe@gmail.com
```

For the exceptions file, use a `.txt` file with a pair of emails delimited by a comma on each line. For example:
```
except.txt
---
email@gmail.com,jdoe@gmail.com
dajoe@gmail.com,jadoe@gmail.com
```

### Further Reading
For more info on Ford-Fulkerson, or flow networks in general I've added some links:
- https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
- https://en.wikipedia.org/wiki/Flow_network
- https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
