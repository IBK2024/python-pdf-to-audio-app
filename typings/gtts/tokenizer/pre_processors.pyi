"""
This type stub file was generated by pyright.
"""

def tone_marks(text: str) -> None:
    """Add a space after tone-modifying punctuation.

    Because the `tone_marks` tokenizer case will split after a tone-modifying
    punctuation mark, make sure there's whitespace after.

    """
    ...

def end_of_line(text: str) -> None:
    """Re-form words cut by end-of-line hyphens.

    Remove "<hyphen><newline>".

    """
    ...

def abbreviations(text: str) -> None:
    """Remove periods after an abbreviation from a list of known
    abbreviations that can be spoken the same without that period. This
    prevents having to handle tokenization of that period.

    Note:
        Could potentially remove the ending period of a sentence.

    Note:
        Abbreviations that Google Translate can't pronounce without
        (or even with) a period should be added as a word substitution with a
        :class:`PreProcessorSub` pre-processor. Ex.: 'Esq.', 'Esquire'.

    """
    ...

def word_sub(text: str) -> None:
    """Word-for-word substitutions."""
    ...
