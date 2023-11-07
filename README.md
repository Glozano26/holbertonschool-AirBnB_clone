# AirBnB Clone Command Interpreter README
Welcome to the README for the AirBnB Clone Command Interpreter, which is an integral part of the AirBnB Clone project. This command interpreter allows you to manage AirBnB objects efficiently. In this document, we'll provide you with an overview of the project, its purpose, and the steps you need to follow to get started.

## Table of Contents
Introduction
Project Overview
Getting Started
Usage
Supported Commands
Resources

## Introduction
The AirBnB Clone Command Interpreter is the first step toward building a full web application, the AirBnB clone. This step is crucial because it lays the foundation for the subsequent projects, including HTML/CSS templating, database storage, API integration, and front-end development. Here's what this project aims to achieve:

1. **Create a parent class named BaseModel to handle the initialization, serialization, and deserialization of instances.
2. **Establish a simple flow of serialization and deserialization: Instance <-> Dictionary <-> JSON string <-> file.
3. **Define all classes required for the AirBnB project (e.g., User, State, City, Place) that inherit from BaseModel.
4. **Develop the first abstracted storage engine for the project, which is the File storage.
5. **Implement unit tests to validate all classes and the storage engine.

## Project Overview
What's a Command Interpreter?
Think of the Command Interpreter as similar to the shell, but it's tailored for a specific purpose. In this case, we want to manage objects in our AirBnB project, allowing us to perform the following actions:

1. **Create a new object (e.g., a new User or a new Place).
2. **Retrieve an object from various data sources (e.g., a file or a database).
3. **Perform operations on objects (e.g., count, compute statistics, etc.).
4. **Update attributes of an object.
5. **Delete an object.

## Getting Started
Before you begin working with the AirBnB Clone Command Interpreter, make sure you have the following resources installed or familiarized:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime module](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- Understanding of args and kwargs in Python
- [Python Test Cheatsheet](https://realpython.com/python-testing/)
  
##Usage
To use the AirBnB Clone Command Interpreter, follow these general steps:

1. **Clone the project repository to your local machine.
2. **Navigate to the project directory.

### Running the Command Interpreter
To start the command interpreter, run the following command:

> python console.py




[Gilberto Lozano Gutiérrez](AUTHORS#nombre-del-autor-1)
[David Vasquez Mahecha](AUTHORS#nombre-del-autor-2)
