# -*- coding: utf-8 -*-
import functools
import io
import json
import logging
import os
import sys

import kolibri_exercise_perseus_plugin


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
logging.StreamHandler(sys.stdout)


LOCALE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "kolibri", "locale")
)
SOURCE_PATH = os.path.join(LOCALE_PATH, "en", "LC_MESSAGES")
SUPPORTED_LANGS_PATH = os.path.join(LOCALE_PATH, "supported_languages.json")
PERSEUS_LOCALE_PATH = os.path.join(
    os.path.dirname(kolibri_exercise_perseus_plugin.__file__), "locale"
)
PERSEUS_SOURCE_PATH = os.path.join(PERSEUS_LOCALE_PATH, "en", "LC_MESSAGES")

PERSEUS_NOT_FOUND = """Cannot find Perseus locale directory.
Please ensure that you've installed the Perseus plugin in development mode using

    pip install -e [local_path_to_perseus_repo]

Also, please ensure that Perseus has been checked out the the correct commit.
"""


if not (os.path.exists(PERSEUS_LOCALE_PATH)):
    logging.error(PERSEUS_NOT_FOUND)
    sys.exit(1)


KEY_CROWDIN_CODE = "crowdin_code"
KEY_INTL_CODE = "intl_code"
KEY_LANG_NAME = "language_name"
KEY_ENG_NAME = "english_name"
KEY_DEFAULT_FONT = "default_font"

IN_CTXT_LANG = {
    KEY_CROWDIN_CODE: "ach",
    KEY_INTL_CODE: "ach-ug",
    KEY_LANG_NAME: "In context translation",
    KEY_ENG_NAME: "In context translation",
}


def to_locale(language):
    """
    Turns a language name (en-us) into a locale name (en_US).
    Logic is derived from Django so be careful about changing it.
    """
    p = language.find("-")
    if p >= 0:
        if len(language[p + 1 :]) > 2:
            return "{}_{}".format(
                language[:p].lower(),
                language[p + 1].upper() + language[p + 2 :].lower(),
            )
        return "{}_{}".format(language[:p].lower(), language[p + 1 :].upper())
    else:
        return language.lower()


def memoize(func):
    cache = func.cache = {}

    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoized_func


@memoize
def supported_languages(include_in_context=False, include_english=False):
    result = []
    with io.open(SUPPORTED_LANGS_PATH, mode="r", encoding="utf-8") as f:
        languages = json.load(f)
    for lang in languages:
        if include_english or lang[KEY_INTL_CODE] != "en":
            result.append(lang)
    if include_in_context:
        result.append(IN_CTXT_LANG)
    return result


@memoize
def local_locale_path(lang_object):
    return os.path.join(
        LOCALE_PATH, to_locale(lang_object[KEY_INTL_CODE]), "LC_MESSAGES"
    )


@memoize
def local_perseus_locale_path(lang_object):
    return os.path.join(
        PERSEUS_LOCALE_PATH, to_locale(lang_object[KEY_INTL_CODE]), "LC_MESSAGES"
    )
