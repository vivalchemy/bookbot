# Bookbot

BookBot is a python program that counts the number of words and the total
number of time a character occurs in a book

![Book bot demo](./assets/demo.gif)

## Installation

1. Clone the repository locally:

```sh
git clone https://github.com/vivalchemy/bookbot.git
```

2. Go into cloned directory:

```sh
cd bookbot
```

3. Create a directory name books:

```sh
mkdir -p books
```

4. Put a book in .txt format in the books directory:

```sh
curl -sS https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt > books/frankenstein.txt
```

5. Run the program:

```sh
make run
```

> if you don't have make installed you can use `python3 main.py`

## Development

### Dependencies

- python3
- make(*optional*) *required if using make commands*
- bat(*optional*) *required if using make commands*
