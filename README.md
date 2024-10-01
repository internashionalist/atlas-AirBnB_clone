![AirBnB](https://github.com/internashionalist/atlas-AirBnB_clone/blob/main/AIRBNB%20CLONE.png)

# AirBnB Console


>*"AirBnB happened because Brian Chesky couldn't pay his rent, but did have some space."*<br>
\-Sam Altman

[Synopsis](#synopsis)<br>
[Description](#description)<br>
[Use Instructions](#use-instructions)<br>
[Features](#features)<br>
[Authors](#authors)

## Synopsis

This is the first phase of the AirBnB Clone project - a custom command line interpreter to take in user input and execute commands.

## Description

The main objective of this console is to build a basic storage system that keeps track of all classes related to an AirBnB-type management service. The data for these classes is handled using JSON serialization, making it possible to store instances, update them, and retrieve them at any time.

This project is structured to handle different types of classes: User, Place, City, State, Amenity, and Review. Each class has its own set of attributes and relationships to other classes (e.g., Place is related to City and User). The console provides an environment where these classes can be created, modified, and destroyed.

## Use Instructions

### Installation
```
git clone https://github.com/internashionalist/atlas-AirBnB_clone.git
```

### Navigation
```
cd Atlas_AirBnB_clone
```

### Launch
```
./console.py
```
    Here, you'll see the command line prompt: (hbnb)
    From this point, the user can input different commands to operate the console.

    | Command | Description |
    |---------|-------------|
    | `help`  | Displays a list of available commands and their usage. |
    | `quit` or `EOF` | Exits the console. |
    | `create <ClassName>` | Creates a new instance of the specified class and prints its ID. |
    | `show <ClassName> <id>` | Displays the string representation of an instance based on class and ID. |
    | `destroy <ClassName> <id>` | Deletes an instance based on class and ID. |
    | `all [ClassName]` | Displays all instances of a given class, or all instances if no class is specified. |
    | `update <ClassName> <id> <attribute name> "<attribute value>"` | Updates an instance's attribute and saves the change. |


## Features





## Authors

[Stephen Newby](https://github.com/TheSnewby)

[Nash Thames](https://github.com/internashionalist/internashionalist/blob/main/README.md)
