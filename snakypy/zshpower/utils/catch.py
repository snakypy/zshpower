from functools import reduce
from os import listdir
from os.path import join, splitext
from re import M
from re import search as re_search
from typing import Any, Union

from docopt import docopt
from snakypy.helpers.ansi import FG, NONE
from snakypy.helpers.logging import Log

from snakypy.zshpower import __info__
from snakypy.zshpower.config import menu


def get_key(dictionary: dict, *args) -> Union[str, bool, dict]:
    """
    Function to get keys from a dictionary recursively without errors.
    If the key does not exist it returns an empty dictionary.

    Args:
        dictionary ([dict]): Receive a dictionary

    Returns:
        [str, bool]: Returning a str or a boolean if the object is True or False.
    """
    data = reduce(lambda c, k: c.get(k, {}), args, dictionary)
    if data == {}:
        return ""
    return data


def read_file_log(file: str, logfile: str) -> str:
    """
    Read a file with log creation option if it does not exist
    """
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as err:
        Log(filename=logfile).record(
            f"The {file} file was not found.", colorize=True, level="error"
        )
        raise FileNotFoundError(f"The {file} file was not found.", err)


def arguments(argv: Any = None) -> dict:
    formatted_version = (
        f"{__info__['name']} version: {FG().CYAN}{__info__['version']}{NONE}"
    )
    data = docopt(menu.options, argv=argv, version=formatted_version)
    return data


def get_zsh_theme(file: str, logfile: str) -> Union[tuple, bool]:
    """
    Get the current theme contained in the .zshrc file if using Oh My ZSH
    """
    current_file = read_file_log(file, logfile)
    m = re_search(r"ZSH_THEME=\".*", current_file)
    if m is not None:
        theme_var = m.group(0)
        lst = theme_var.split("=")
        theme_name = [s.strip('"') for s in lst][1]
        return theme_name, theme_var
    return False


def current_plugins(file: str, logfile: str) -> list:
    """
    Get current plugins from .zshrc file if using Oh My ZSH
    """
    current_file = read_file_log(file, logfile)
    m = re_search(r"^plugins=\(.*", current_file, flags=M)
    if m is not None:
        get = m.group(0)
        lst = get.split("=")
        current = [i.strip('"').replace("(", "").replace(")", "") for i in lst][1]
        return current.split()
    return []


def get_line(file: str, line: str, logfile: str) -> Union[str, bool]:
    """
    Get a given line from a given file
    """
    current_file = read_file_log(file, logfile)
    m = re_search(rf"{line}", current_file)
    if m is not None:
        return m.group(0)
    return False


def verify_objects(directory: str, /, data: dict) -> bool:
    """
    Checks whether there are objects from a particular directory.
    These can be folders, files and file extensions.
    """
    if type(data) is not dict:
        raise TypeError("Data parameter must be a dictionary.")

    if "files" not in data or "folders" not in data or "extensions" not in data:
        raise TypeError(
            "The dictionary does not contain one of the following keys: 'files', 'folders', 'extensions'."
        )

    objects_in_directory = listdir(directory)

    def files_folders(key):

        # The "strictly" key will check whether the dictionary keys (files and folders) are tuples or lists.
        # If you use tuples, it means that the search must be rigorous, that is, if there is no such object,
        # the return will always be False.

        # If you use list in "files" or "folders", the search is tolerant, that is, if it finds a single object,
        # the return will always be True.

        strictly = False

        if data[key]:
            if type(data[key]) is tuple:
                strictly = True
            for item in data[key]:
                if strictly is False:
                    if item in objects_in_directory:
                        return True
                    return False
                else:
                    if item not in objects_in_directory:
                        return False
                    return True
        return False

    def finder_extensions():
        if data["extensions"]:
            lst = []
            for ext in data["extensions"]:
                for file in objects_in_directory:
                    if file.endswith(ext):
                        lst.append(join(directory, file))

            e = [splitext(f)[-1] for f in lst]
            for ext in data["extensions"]:
                if ext in e:
                    return True
        return False

    files = files_folders("files")
    folders = files_folders("folders")
    extensions = finder_extensions()

    if (files is False and folders is False) and extensions is False:
        return False

    return True
