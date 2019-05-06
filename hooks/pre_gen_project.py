#!/usr/bin/env python3
import re
import sys
import subprocess


class bsc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


if __name__ == "__main__":

    if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9]+$',
                    '{{ cookiecutter.project_slug }}'):
        print(
            bsc.FAIL +
            'ERROR: The project slug ({{cookiecutter.project_slug}})'
            'is not a valid Python module name. Please do not use a'
            '- and use _ instead' + bsc.END)
        sys.exit(1)

    if "{{ cookiecutter.git_remote }}"[:4] in ["[Y1]", "[Y2]"]:
        try:
            subprocess.run(["git", "ls-remote", "-h",
                            "{{ cookiecutter.git_remote_url }}"],
                           check=True,
                           stderr=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(
                bsc.FAIL +
                "Remote Github repository does not exist.\n" +
                "If using Github, create an empty repository first." +
                bsc.END)
            sys.exit(1)

    if "{{ cookiecutter.r_packrat }}"[:3] == "[Y]":
        try:
            subprocess.run(
                ["Rscript", "-e",
                 'if (!"packrat" %in% rownames(installed.packages())) { stop() }'],
                check=True,
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL)
        except OSError:
            print(bsc.FAIL + "Rscript executable not found." + bsc.END)
            sys.exit(1)
        except subprocess.CalledProcessError:
            print(bsc.FAIL +
                  "Please install the Packrat R library first." + bsc.END)
            sys.exit(1)
