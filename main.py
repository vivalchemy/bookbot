PATH_TO_FILE = "./books/frankenstein.txt"


def read_file():
    with open(PATH_TO_FILE) as f:
        return f.read()


def count_words(str):
    return len(str.split())


def sort_characters_by_count(array_of_maps):
    array_of_maps.sort(key=lambda x: x["count"], reverse=True)


def count_characters(str):
    str = str.lower()
    char_map = [{"char": None, "count": 0} for _ in range(26)]
    for char in str:
        if char.isalpha():
            index = ord(char) - 97
            if char_map[index]["char"] is None:
                char_map[index]["char"] = char
            char_map[index]["count"] += 1
    return char_map


def print_report(word_count, character_count_map):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for map in character_count_map:
        print(f"The '{map["char"]}' character was found {map["count"]} times")
    print("--- End report ---")


def main():
    file_contents = read_file()
    word_count = count_words(file_contents)
    character_count_map = count_characters(file_contents)
    sort_characters_by_count(character_count_map)
    print_report(word_count, character_count_map)


if __name__ == "__main__":
    main()
