![AirBnB](https://github.com/internashionalist/atlas-AirBnB_clone/blob/main/AIRBNB%20CLONE.png)

# AirBnB Console


>*"AirBnB happened because Brian Chesky couldn't pay his rent, but did have some space."*<br>
\-Sam Altman

[Synopsis](#synopsis)<br>
[Description](#description)<br>
[Use Instructions](#use-instructions)<br>
[Features](#features)<br>
[Examples](#examples)<br>
[Authors](#authors)

## Synopsis

This is the first phase of the AirBnB Clone project - The AirBnB Console is a command-line interface application that allows users to interact with the backend of a simplified AirBnB-like system.

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

| Command                                                    | Description                                                        |
|-----------------------------------------------------------|--------------------------------------------------------------------|
| `help`                                                    | Displays a list of available commands and their usage.             |
| `quit` or `EOF`                                           | Exits the console.                                                 |
| `create <ClassName>`                                      | Creates a new instance of the specified class and prints its ID.   |
| `show <ClassName> <id>`                                   | Displays the string representation of an instance based on class and ID. |
| `destroy <ClassName> <id>`                                | Deletes an instance based on class and ID.                         |
| `all [ClassName]`                                         | Displays all instances of a given class, or all instances if no class is specified. |
| `update <ClassName> <id> <attribute name> "<attribute value>"` | Updates an instance's attribute and saves the change.             |


## Features

The AirBnB Console uses an object-oriented approach to manage different classes:

	•	BaseModel Class: This acts as the parent class for all other models, providing common attributes such as id, created_at, and updated_at. Every new model class inherits from BaseModel.
	•	JSON Serialization: All instances are stored in a file called file.json using JSON format. This allows for data "persistence," so you can exit the console and later retrieve all previously created instances.
	•	Interactive Command Handling: The console supports commands that allow users to:
	    +   Create new instances of models.
	    +   Display specific instances or lists of instances.
	    +   Update attributes of instances.
	    +   Delete instances.

## Examples

    Create a new user:

    ```
    (hbnb) create User
    ```

    Output: (new User ID)

    ```
    23a5041c-8fe9-422f-83e2-22be9f0f0aa2
    ```

    Update new User's First Name:

    ```
    update User 23a5041c-8fe9-422f-83e2-22be9f0f0aa2 first_name "John"
    ```

    Verify Change:

    ```
    show User 23a5041c-8fe9-422f-83e2-22be9f0f0aa2
    ```

    Output (User attributes)
    
    ```
    [User] (23a5041c-8fe9-422f-83e2-22be9f0f0aa2) {'id': '23a5041c-8fe9-422f-83e2-22be9f0f0aa2', 'created_at': datetime.datetime(2024, 10, 1, 19, 6, 27, 738194), 'updated_at': datetime.datetime(2024, 10, 1, 19, 7, 20, 460239), 'first_name': 'John'}
    ```

## Authors

[Stephen Newby](https://github.com/TheSnewby)

[Nash Thames](https://github.com/internashionalist/internashionalist/blob/main/README.md)
