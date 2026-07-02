

class CharTokenizer:
    """Simple tokenizer for character-level language models."""

    def __init__(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not text:
            raise ValueError("text cannot be empty")

        self.text = text
        self.chars = sorted(set(text))
        self._char_to_id = {char: i for i, char in enumerate(self.chars)}
        self._id_to_char = {i: char for char, i in self._char_to_id.items()}

    @property
    def vocab_size(self) -> int:
        """Returns the size of the vocabulary."""
        return len(self.chars)

    def encode(self, text: str) -> list[int]:
        """Converts a string to a list of ids."""
        return [self._char_to_id[char] for char in text]

    def decode(self, ids: list[int]) -> str:
        """Converts a list of ids to a string."""
        return "".join(self._id_to_char[token_id] for token_id in ids)
