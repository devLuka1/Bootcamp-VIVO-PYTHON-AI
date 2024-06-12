# 🐍 **Understanding the Python Programming Language**

---

## 📊 **Data Types**

### 🎯 **What are Types?**

Types are used to define the characteristics and behaviors of a value (object) to the interpreter, for example:
- With this type, I can perform mathematical operations.
- This type, when stored in memory, will consume 24 bytes.

### 🛠️ **Types in Python**

The built-in types are:

### 🧮 **Numeric Types**

#### 🔢 **Integers**

Integers are represented by the `int` class and have unlimited precision. Valid examples of integers are:
1, 10, 100, -1, -10, -100... 99001823

#### 🔣 **Floating Point Numbers**

Floating point numbers are used to represent rational numbers and are implemented by the `float` class. Valid examples of floating point numbers are:
1.5, -10.543, 0.76... 999278.002

### 🔵 **Boolean and String Types**

#### ✔️ **Boolean**

It is used to represent true or false and is implemented by the `bool` class. In Python, the boolean type is a subclass of int, since any number other than 0 represents true and 0 represents false. Valid examples of booleans are:
True and False

#### 🔤 **Strings**

Strings or character strings are used to represent alphanumeric values. In Python, strings are defined using the `str` class. Valid examples of strings are:
"Python", 'Python', """Python""", ""Python"", "p"

---

## 🔄 **Interactive Mode**

The Python interpreter can run in a mode that allows the developer to write code and see the result immediately.

### 🚀 **Starting Interactive Mode**

There are two ways to start interactive mode, by simply calling the interpreter (`python`) or by executing the script with the `-i` flag (`python -i app.py` where `app.py` is the name of the file).

### 📜 **`dir` Function**

Without arguments, it returns the list of names in the current local scope. With an argument, it returns a list of valid attributes for the object. Example:
`dir()`
`dir(100)`

### 💡 **`help` Function**

Invokes the built-in help system. It is possible to search in interactive mode or inform by parameter the name of the module, function, class, method, or variable. Example:
`help()`
`help(100)`

---

## 📊 **Variables and Constants**

### 💼 **Variables**

In programming languages, we can define values that can change during program execution. These values are called variables because they are born with a value and do not necessarily have to remain with it during program execution.

### 📝 **Changing Values**

Notice that we do not need to define the data type of the variable; Python does this automatically for us. Therefore, we cannot simply create a variable without assigning a value to it. To change the value of the variable, simply assign a new value.

### 🛑 **Constants**

Like variables, constants are used to store values, however, a constant is born with a value and remains with it until the end of the program execution, that is, the value is immutable.

#### ❌ **Python does not have constants**

There is no reserved word to inform the interpreter that the value is constant. In some languages, for example: Java and C, we use `final` and `const`, respectively, to declare a constant. In Python, we use the convention (combined) that tells the programmer that the variable is a constant. To do this, you must create the variable with the name all in uppercase.

---

## 🚦 **Best Practices**

- The naming convention should be snake case (replace all whitespace with "_").
- Choose suggestive names.
- Constant names all in uppercase.

### 🔄 **Converting Types**

Sometimes it is necessary to convert the type of a variable to manipulate it differently. For example:
- String variables, which store numbers and we need to perform a mathematical operation with this value.

#### 🔢🔄 **Integer to Float**

```python
integer = 10
floating_point = float(integer)
print(floating_point)  # Output: 10.0
```
#### 🔢🔄 **Float to Integer**

```python
floating_point = 10.5
integer = int(floating_point)
print(integer)  # Output: 10
```


#### ➗ **Division Conversion**

```python
num1 = 10
num2 = 3
result = num1 / num2
print(result)  # Output: 3.3333333333333335
```

#### 🔢🔤 **Numeric to String**

```python
number = 10
string = str(number)
print(string)  # Output: '10'
```

#### 🔤🔢 **String to Number**

```python
string = '10'
number = int(string)
print(number)  # Output: 10
```

#### ⚠️ **Conversion Error**

```python
string = 'abc'
try:
    number = int(string)
except ValueError as e:
    print("Conversion error:", e)  # Output: Conversion error: invalid literal for int() with base 10: 'abc'
```

## ⌨️ Input and Output Functions

#### 📥 input Function
The built-in input function is used when we want to read data from the standard input (keyboard). It takes an argument of type string, which is displayed to the user on the standard output (screen). The function reads the input, converts it to a string, and returns the value. Example:

```python
input_data = input("Enter something: ")
print("You entered:", input_data)
```

#### 📤 print Function
The built-in print function is used when we want to display data on the standard output (screen). It takes a mandatory argument of type varargs of objects and 4 optional arguments (sep, end, file, and flush). All objects are converted to strings, separated by sep, and terminated by end. The final string is displayed to the user. Example:

```python
name = "John"
age = 30
print("Name:", name, "Age:", age)  # Output: Name: John Age: 30
```






