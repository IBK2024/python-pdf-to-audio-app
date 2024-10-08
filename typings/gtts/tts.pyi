"""
This type stub file was generated by pyright.
"""

from typing import Any, Generator
from typing import List as _list

__all__ = ["gTTS", "gTTSError"]
log = ...

class Speed:
    """Read Speed

    The Google TTS Translate API supports two speeds:
        Slow: True
        Normal: None
    """

    SLOW = ...
    NORMAL = ...

class gTTS:
    """gTTS -- Google Text-to-Speech.

    An interface to Google Translate's Text-to-Speech API.

    Args:
        text (string): The text to be read.
        tld (string): Top-level domain for the Google Translate host,
            i.e `https://translate.google.<tld>`. Different Google domains
            can produce different localized 'accents' for a given
            language. This is also useful when ``google.com`` might be blocked
            within a network but a local or different Google host
            (e.g. ``google.com.hk``) is not. Default is ``com``.
        lang (string, optional): The language (IETF language tag) to
            read the text in. Default is ``en``.
        slow (bool, optional): Reads text more slowly. Defaults to ``False``.
        lang_check (bool, optional): Strictly enforce an existing ``lang``,
            to catch a language error early. If set to ``True``,
            a ``ValueError`` is raised if ``lang`` doesn't exist.
            Setting ``lang_check`` to ``False`` skips Web requests
            (to validate language) and therefore speeds up instantiation.
            Default is ``True``.
        pre_processor_funcs (list): A list of zero or more functions that are
            called to transform (pre-process) text before tokenizing. Those
            functions must take a string and return a string. Defaults to::

                [
                    pre_processors.tone_marks,
                    pre_processors.end_of_line,
                    pre_processors.abbreviations,
                    pre_processors.word_sub
                ]

        tokenizer_func (callable): A function that takes in a string and
            returns a list of string (tokens). Defaults to::

                Tokenizer([
                    tokenizer_cases.tone_marks,
                    tokenizer_cases.period_comma,
                    tokenizer_cases.colon,
                    tokenizer_cases.other_punctuation
                ]).run

        timeout (float or tuple, optional): Seconds to wait for the server to
            send data before giving up, as a float, or a ``(connect timeout,
            read timeout)`` tuple. ``None`` will wait forever (default).

    See Also:
        :doc:`Pre-processing and tokenizing <tokenizer>`

    Raises:
        AssertionError: When ``text`` is ``None`` or empty; when there's nothing
            left to speak after pre-processing, tokenizing and cleaning.
        ValueError: When ``lang_check`` is ``True`` and ``lang`` is not supported.
        RuntimeError: When ``lang_check`` is ``True`` but there's an error loading
            the languages dictionary.

    """

    GOOGLE_TTS_MAX_CHARS = ...
    GOOGLE_TTS_HEADERS = ...
    GOOGLE_TTS_RPC = ...
    def __init__(
        self,
        text: str,
        tld: Any = ...,
        lang: Any = ...,
        slow: Any = ...,
        lang_check: Any = ...,
        pre_processor_funcs: Any = ...,
        tokenizer_func: Any = ...,
        timeout: Any = ...,
    ) -> None: ...
    def get_bodies(self) -> _list[Any]:
        """Get TTS API request bodies(s) that would be sent to the TTS API.

        Returns:
            list: A list of TTS API request bodies to make.
        """
        ...

    def stream(self) -> Generator[bytes, Any, None]:
        """Do the TTS API request(s) and stream bytes

        Raises:
            :class:`gTTSError`: When there's an error with the API request.

        """
        ...

    def write_to_fp(self, fp: Any) -> None:
        """Do the TTS API request(s) and write bytes to a file-like object.

        Args:
            fp (file object): Any file-like object to write the ``mp3`` to.

        Raises:
            :class:`gTTSError`: When there's an error with the API request.
            TypeError: When ``fp`` is not a file-like object that takes bytes.

        """
        ...

    def save(self, savefile: str) -> None:
        """Do the TTS API request and write result to file.

        Args:
            savefile (string): The path and file name to save the ``mp3`` to.

        Raises:
            :class:`gTTSError`: When there's an error with the API request.

        """
        ...

class gTTSError(Exception):
    """Exception that uses context to present a meaningful error message"""

    def __init__(self, msg: Any = ..., **kwargs: Any) -> None: ...
    def infer_msg(self, tts: Any, rsp: Any = ...) -> str:
        """Attempt to guess what went wrong by using known
        information (e.g. http response) and observed behaviour

        """
        ...
