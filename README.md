

### Q:  what does `if __name__ == "__main__"` signifiy?

`__name__` is a variable Python automatically sets for every file/module.

- **Run directly** (e.g. `python ft_garden_intro.py`)
  → `__name__` is set to the fixed string `"__main__"` (filename is irrelevant here)
- **Imported** (e.g. `import ft_garden_intro`)
  → `__name__` is set to the filename itself: `"ft_garden_intro"`

`__main__` is a literal string with a fixed, constant value.



### Q:  What is an _import_ in Python?
In Python, as with other OOP languages, programmer can `import` another script/module to resuse its functions, classes, and variables.


## Standard practice:  Utilize guard clause: `if __name__ == "__main__"`
We add this clause

```
if __name__ == "__main__":
    program_function_name() 
```

e.g.
```
if __name__ == "__main__":
    ft_garden_intro() 
```


## Adding this clause enables us to 
- Run the current file (e.g. `ft_garden_intro.py` as a standalone file to be interpreted and executed)
- Be called (imported) by another program without auto-running
