![logo](https://github.com/Glozano26/holbertonschool-AirBnB_clone/blob/main/images/console.png)
# AirBnB Clone Command Interpreter :department_store:
Welcome to the README for the AirBnB Clone Command Interpreter, which is an integral part of the AirBnB Clone project. This command interpreter allows you to manage AirBnB objects efficiently. In this document, we'll provide you with an overview of the project, its purpose, and the steps you need to follow to get started.

## Table of Contents
- Introduction
- Project Overview
- Getting Started
- Usage
- How to use
- Unittesting

## Introduction
The AirBnB Clone Command Interpreter is the first step toward building a full web application, the AirBnB clone. This step is crucial because it lays the foundation for the subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development. Here's what this project aims to achieve:

1. Create a parent class named BaseModel to handle the initialization, serialization, and deserialization of instances.
2. Establish a simple flow of serialization and deserialization: Instance <-> Dictionary <-> JSON string <-> file.
3. Define all classes required for the AirBnB project (e.g., User, State, City, Place) that inherit from BaseModel.
4. Develop the first abstracted storage engine for the project, which is the File storage.
5. Implement unit tests to validate all classes and the storage engine.

## Project Overview
### What's a Command Interpreter?
Think of the Command Interpreter as similar to the shell, but it's tailored for a specific purpose. In this case, we want to manage objects in our AirBnB project, allowing us to perform the following actions:

- Create a new object (e.g., a new User or a new Place).
- Retrieve an object from various data sources (e.g., a file or a database).
- Perform operations on objects (e.g., count, compute statistics, etc.).
- Update attributes of an object.
- Delete an object.

## Getting Started
Before you begin working with the AirBnB Clone Command Interpreter, make sure you have the following resources installed or familiarized:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- Understanding of args and kwargs in Python
- [Python Test Cheatsheet](https://realpython.com/python-testing/)
  
## Usage
To use the AirBnB Clone Command Interpreter, follow these general step:
> $ git clone git@github.com:glozano26/holbertonschool-AirBnB_clone.git

### Running the Command Interpreter
To start the command interpreter, run the following command:

> python console.py

You'll enter an interactive command-line interface where you can execute commands for managing AirBnB objects.

```
./console.py

(hbnb) help

Documented commands (type help <topic>):
======================================== 
EOF  help  quit

(hbnb)

(hbnb)

(hbnb) quit

$
```
They should pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## How to use:

| File   | Description                         | Attributes                               |
|--------|-------------------------------------|------------------------------------------|
| help   | Display all commands available      | help                                     |
| create | Creates a new object                | create (class here)                     |
| update | Updates attribute of an object     | update class id name_attribute var_attribute |
| all    | Display all objects in class        | all (class here) or only (all)          |
| show   | Retrieve an object from a file      | show class id                           |
| destroy | Destroy specified object            | destroy class id                        |
| quit   | Close the console                   | quit                                     |

## Unittesting:keyboard:
All the test files can be executed by this command -
```python3 -m unittest discover tests```
Or run tests file by file using this command -
```python3 -m unittest tests/test_models/test_base_model.py```

## Authors:
- [Gilberto Lozano Gutiérrez](AUTHORS#nombre-del-autor-1)
- [David Vasquez Mahecha](AUTHORS#nombre-del-autor-2)
