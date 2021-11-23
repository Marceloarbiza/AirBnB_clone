##  0x00. AirBnB clone - The console
<img src="https://github.com/Diego-Guarise/Icons-and-logos/blob/master/airbnb.png">

##

# Index
1. [General Info](#general-info)
2. [Evironment](#evironment)
3. [Installation](#installation)
4. [Guide](#guide)
5. [Directories](#directories)
6. [Collaboration](#collaboration)


## General Info


In this project we will build the airBnB Clone base and then use this in our future projects: HTML / CSS templating, database storage, API, front-end integration.

## Evironment

|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height="30px" src="https://raw.githubusercontent.com/Diego-Guarise/Icons-and-logos/master/ubuntu.svg"> Basic Ubuntu 20.04  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height="30px" src="https://raw.githubusercontent.com/Diego-Guarise/Icons-and-logos/master/python.svg"> Python 3.8.10 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <img height="30px" src="https://raw.githubusercontent.com/Diego-Guarise/Icons-and-logos/master/neovim.svg"> NeoVim 0.4.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img height="30px" src="https://raw.githubusercontent.com/Diego-Guarise/Icons-and-logos/master/vim.svg"> Vim 8.1.2269&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
## Style guidelines
 * [Pycodestyle](https://www.python.org/dev/peps/pep-0008/) - version 2.7.*
 * [PEP8](https://pep8.org/)
## Installation

A little intro about the installation. 
```bash
$ git clone https://github.com/Diego-Guarise/AirBnB_clone.git
```
## Guide
 ```bash
$ cd ./AirBnB_clone
$ ./console.py
  ```
Now the console will look like this
 ```bash
(hbnb) 
```
 This is the props.
 When type help all available commands appear. if you type help <command> you will see the information individually
 ```bash
 (hbnb) help


Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
 ```
 Now we will add a command to help
 ```bash
 (hbnb) help create
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id

(hbnb) 

```
### Below an example of how to create an instance:
```bash
(hbnb) create State
dc4dd825-d14d-4118-8c37-84c76a2eec38
```
or
```bash
(hbnb) State.create()
f21992ef-fb5a-49ea-bc55-a85abbba1d8f
```

 <br>

 If you type wrong or missing an argument, the console will tell you ;)
<br>

 ```bash
 (hbnb) create
** class name missing **
 ```
 or
  ```bash
(hbnb) create()
** class name missing **
   ```
 <br>
 If you will go out, use the command 

````bash
(hbnb) quit
$
````

## Directories

| Directory | Descripción |
| --- | --- |
| [/tests](https://github.com/Diego-Guarise/AirBnB_clone/tree/main/tests) | Unittest files |
| [/models](https://github.com/Diego-Guarise/AirBnB_clone/tree/main/models) | BaseModel class and Inherited class instances |
| [/models/engine](https://github.com/Diego-Guarise/AirBnB_clone/tree/main/models/engine) | Serializes instances to a JSON file and deserializes JSON file to instances |


## Collaboration
| Marcelo Arbiza  | Diego Guarise |
|--|--|
| [GitHub](https://github.com/Marceloarbiza) |[GitHub](https://github.com/Diego-Guarise)|
|[Linkedin](https://www.linkedin.com/in/marcelo-arbiza-7b9b9b15a/)|[Linkedin](https://www.linkedin.com/in/diego-guarise/)|
