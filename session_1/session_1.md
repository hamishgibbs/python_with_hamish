👄 👶 🎡 🚝 📑 ↘️ 👨 🗄 ☂ 🖍 🛢 🛃 ♣️ 🍵 😺 🍕 🐝 ◼️ 👜 📘 👙 🔌 🏝 🍇 🈯️ 🔳 🍊 🔎 🚊 🙄 🔛 🙀
# Session 1

## Setup

On Mac: Use Terminal.  
On Linux: Use Bash.  
On Windows: Use [`git bash`](https://gitforwindows.org/), [Anaconda Prompt](https://docs.anaconda.com/anaconda/user-guide/getting-started/), or another emulator.  

Check that python is installed:

`python --version`

Play around with the terminal:

`cd ~`: go home.  
`cd /somewhere`: go somewhere.  
`cd ..`: go one level up from where you are.  
`cat`: Print a file to the terminal.  
`cp`: Copy a file to another place.  
`mv`: Move a file to another place.  
`mkdir`: Create a directory.  
`touch`: Create a blank file.  
`rm`: Delete a file.  
`rm -r`: Delete a directory and its contents.  

Create a new directory somewhere:

```{shell}
mkdir /path/to/this/directory/session_1
cd /path/to/this/directory/session_1
```

Create a python file:

```{shell}
touch whatever.py
```

Run your python file:
```{shell}
python whatever.py
```

## Exercises

1. Print something to the terminal from your python file.

```{python}
print("Howdy!")
```

2. Define a function that does something.

```{python}
def add_three(x):
    return x + 3
```

3. Call your function and print the result.

4. Write a function that calls a function.

5. Write a function that calls a function that calls a function.

6. Call your function, assign the result to a variable, pass this variable to another function.

6. Separate functions into multiple files.

7. Import these functions into the original file.

```{python}
from mynewfile import add_three
```

8. Define a function called `main` and write an ["import guard"](https://stackoverflow.com/questions/419163/what-does-if-name-main-do).

```{python}
if __name__ == '__main__':
  main()
```

## Extras

1. For some mind-bending - play around with a recursive function:

```{python}
def factorial(x):
  if x == 1:
    return 1
  else:
    return (x * factorial(x-1))
```

2. Compare the code in `update_mobiliy.py` and `refactored_update_mobiliy.py`.
  * Is `refactored_update_mobiliy.py` easier to follow?
  * Is `refactored_update_mobiliy.py` harder to follow?
  * Are there two many small functions?
  * How easy would it be to update each file in case the inputs change?
  * What is the best way to divide responsibility between functions?
  * How are functions [coupled](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) together?
  * How will `refactored_update_mobiliy.py` be impacted if we change the implementation of one function?

3. Consider how you could refactor one of your own workflows to make it more clear.

## Tips

Think of the command line as a file explorer.

The goal of modular code is to remember what a section of code does 6 months from now.

There are no right answers, just better and worse. You will have to find coding practices that work for you.

There are very many programming languages, tools, frameworks, packages, helpers, package managers, editors, containers, automators, bits & bobs. Don't worry too much - the basics of programming are always the same.
