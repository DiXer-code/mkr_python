import re


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def count_sentences(text):
    sentence_endings = re.findall(r"\.\.\.|[.!?]", text)
    return len(sentence_endings)


def count_words(text):
    cleaned_text = re.sub(r"\.\.\.|[.!?]", " ", text)
    words = re.split(r"[,\s:;]+", cleaned_text)
    words = [word for word in words if word]
    return len(words)


def analyze_text_file(file_path):
    text = read_text_file(file_path)
    return {
        "words": count_words(text),
        "sentences": count_sentences(text)
    }


if __name__ == "__main__":
    file_path = input("Enter path to .txt file: ")
    result = analyze_text_file(file_path)
    print(f"Words: {result['words']}")
    print(f"Sentences: {result['sentences']}")