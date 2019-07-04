# Gradient Descent

*    Title: Gradient Descent    
*    Author: Guillem Alomar
*    Initial release: June 4th, 2019                     
*    Code version: 0.1                         
*    Availability: Public     

**Index**
* [Requirements](#requirements)
* [Documentation](#documentation)
* [Using the application](#using-the-application)
    * [First of all](#first-of-all)
    * [Executing](#executing)
    * [Additional Parameters](#additional-parameters)
* [Understanding the output](#the-output)

## Requirements

- Python +3.5
- matplotlib +3.1.1

## Documentation

### Explanation

This project consists in a Gradient Descent implementation in python3.

## Using the application

### First of all

#### Execution parameters

You can modify the execution parameters in _src/settings.py_

You should also add your training set csv to the _input_ folder.

### Executing

This is done by typing the following command:
```
$ python3 GradientDescent.py
```

### Additional Parameters

```
usage: GradientDescent.py [-h] [-f FILE] [-i INPUT]

Gradient Descent

optional arguments:
  -h, --help               show this help message and exit
  -f FILE, --file FILE     CSV input file. If not specified it will use a default one.
  -i INPUT, --input INPUT  Input values to process. Between 's. Example: '2.2 3.3'
 ```
 
 ## The output
 
Once the execution has finished, the resulting images will be stored in _output/_. These images should look similar to this:
 
![alt text][logo2]

[logo2]: output/example_3Db_output.png "Application Architecture"

The names of the images follow the next syntax:

```
$inputname_output.png
```

Logs can be found in _src/execution.log_ 
