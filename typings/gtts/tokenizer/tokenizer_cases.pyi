"""
This type stub file was generated by pyright.
"""

from typing import Pattern

def tone_marks() -> Pattern[str]:
    """Keep tone-modifying punctuation by matching following character.

    Assumes the `tone_marks` pre-processor was run for cases where there might
    not be any space after a tone-modifying punctuation mark.
    """
    ...

def period_comma() -> Pattern[str]:
    """Period and comma case.

    Match if not preceded by ".<letter>" and only if followed by space.
    Won't cut in the middle/after dotted abbreviations; won't cut numbers.

    Note:
        Won't match if a dotted abbreviation ends a sentence.

    Note:
        Won't match the end of a sentence if not followed by a space.

    """
    ...

def colon() -> Pattern[str]:
    """Colon case.

    Match a colon ":" only if not preceded by a digit.
    Mainly to prevent a cut in the middle of time notations e.g. 10:01

    """
    ...

def other_punctuation() -> Pattern[str]:
    """Match other punctuation.

    Match other punctuation to split on; punctuation that naturally
    inserts a break in speech.

    """
    ...

def legacy_all_punctuation() -> Pattern[str]:
    """Match all punctuation.

    Use as only tokenizer case to mimic gTTS 1.x tokenization.
    """
    ...
