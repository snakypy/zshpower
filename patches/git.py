#!/usr/bin/env python3

import git
import os


def git_branch(prefix=None):
    if os.path.isdir(os.path.join(os.getcwd(), ".git")):
        prefix = "git: " if prefix is None else prefix
        repo = git.Repo(os.getcwd())
        return f"{prefix}{repo.active_branch.name}"
    return ""


def git_status(icons=False):
    icons = {
        "A": ["\uf44d ", "+ "],
        "AM": ["\uf8ea ", "* "],
        "M": ["\uf8ea ", "* "],
        "D": ["\uf655 ", "x "],
        "??": ["\uf41e ", "?? "],
        "R": ["\uf101 ", ">> "],
        "OK": ["\uf62c ", "! "]
    }

    if os.path.isdir(os.path.join(os.getcwd(), ".git")):
        repo = git.Repo(os.getcwd())
        status_git = repo.git.status(porcelain=True).split()

        status_current = []
        status_icons = []
        if "D" in status_git:
            status_current.append("D")
        if "??" in status_git:
            status_current.append("??")
        if "R" in status_git:
            status_current.append("R")
        if "A" in status_git:
            status_current.append("A")
        if "AM" in status_git:
            status_current.append("AM")
        if "M" in status_git:
            status_current.append("M")
        if len(status_git) == 0:
            status_current.append("OK")

        for item in status_current:
            if icons:
                status_icons.append(f"{icons[item][0]}")
            else:
                status_icons.append(f"{icons[item][1]}")

        status = "".join(sorted(status_icons))
        return status
    return ""


if __name__ == "__main__":
    print(git_branch(), git_status(icons=True))
