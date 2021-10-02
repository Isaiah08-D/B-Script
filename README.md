# B-Script
A language to replace your command prompt.

# Usage
Note that most of these things may not currently work. All things that may not be working will be in italics. If something else is not working, please add an issue.

## Functions
### The show command
Basic show command:
```
show > text
```
The text that you use the show command on does not need to be in
quotation marks. You can also show variables, though we will get to
that later.

### Creating variables
```
var > name > value
```
### Showing variables
```
show > get > varname
```

### Type declaration
B-Script type declaration is very simple. Simply put a letter before the variable value.
To initiate a string, put an s at the beginning of it.  
`var > mystring > sMy String`  
To initiate an integer, use an i.
`var > myint > i123`

### Cd command
Use `cd` to change the current path. For example:
```
C:\Users\james: cd > programing
C:\Users\james\programing:  
```
*One can use `cd > -` to go down a directory.*

### Running python files
Use `python` to run python files.
```
C:\Users\james: python > sayhi.py
Hi!
```
**Make sure not to use the entire path.**