import pytest

from src.main import analyze_text_file, count_sentences, count_words


@pytest.fixture
def sample_text():
    return "Hello, world! Python is great. Testing is important..."


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world.", 2),
        ("One,two:three;four", 4),
        ("Python   testing", 2),
        ("", 0),
    ]
)
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world.", 1),
        ("Hello! How are you?", 2),
        ("Testing is important...", 1),
        ("", 0),
    ]
)
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


def test_count_words_with_fixture(sample_text):
    assert count_words(sample_text) == 8


def test_count_sentences_with_fixture(sample_text):
    assert count_sentences(sample_text) == 3


def test_analyze_text_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello, world! Python is great...", encoding="utf-8")

    result = analyze_text_file(test_file)

    assert result == {
        "words": 5,
        "sentences": 2
    }
