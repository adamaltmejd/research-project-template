#!/usr/bin/env python3
import os
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


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.license }}" == "None":
        remove_file('LICENSE')

    # Initialize Renv (R)
    if "{{ cookiecutter.r_renv }}"[:3] == "[Y]":
        r_command = ('renv::init()')
        try:
            subprocess.run(["Rscript", "-e", r_command], check=True,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except OSError:
            print(bsc.FAIL + "Rscript executable not found." + bsc.END)
            sys.exit(1)
        except subprocess.CalledProcessError:
            print(bsc.FAIL + "Error initializing Renv." + bsc.END)
            sys.exit(1)

    # Write sourcing of global Rprofile to local one.
    if "{{ cookiecutter.r_append_rprofile }}"[:3] == "[Y]":
        with open(os.path.join(PROJECT_DIRECTORY, ".Rprofile"), "a") as f:
            f.write('source("~/.Rprofile")')

    if "{{ cookiecutter.git_init }}" == "Yes":

        # Initialize git repo
        subprocess.run(["git", "init"],
                       stdout=subprocess.DEVNULL, check=True)

        # Add all files in project folder
        subprocess.run(["git", "add", "."],
                       stdout=subprocess.DEVNULL, check=True)

        # Commit initial scaffold
        subprocess.run(["git", "commit", "-m",
                        "Initial autocommit"],
                       stdout=subprocess.DEVNULL, check=True)

        # If remote configured, push initial commit to remote
        if "{{ cookiecutter.git_remote }}"[:4] in ["[Y1]", "[Y2]"]:
            try:
                subprocess.run(["git", "remote", "add", "origin",
                                "{{ cookiecutter.git_remote_url }}"],
                               stdout=subprocess.DEVNULL, check=True)
            except:
                print(bsc.FAIL + "Failed to add Git Remote: "
                      "\n{{ cookiecutter.git_remote_url }}\n"
                      "You will have to add it yourself." + bsc.END)
            try:
                subprocess.run(["git", "push", "-u",
                                "origin", "master"],
                               stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL, check=True)
            except:
                print(bsc.FAIL + "Failed to push repo to Remote. "
                      "You will have to do that yourself." + bsc.END)

    print(bsc.OKGREEN +
          "Finished creating project: {{ cookiecutter.project_name }}" +
          bsc.END)
