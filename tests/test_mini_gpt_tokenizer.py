
from research_radar.mini_gpt.tokenizer import CharTokenizer

def test_char_tokenizer_roundtrip() -> None:
    text = "hello world"
    tokenizer = CharTokenizer(text=text)
    assert tokenizer.decode(tokenizer.encode(text)) == text


def test_char_tokenizer_vocab_size_is_unique_character_count() -> None:
    text = "banana"
    tokenizer = CharTokenizer(text=text)
    assert tokenizer.vocab_size == len(set(text))


def test_char_tokenizer_encode_returns_integers() -> None:
    tokenizer = CharTokenizer(text="abc")
    ids = tokenizer.encode("cab")
    assert all(isinstance(token_id, int) for token_id in ids)
