#!/bin/bash

PROJECT=arpy

compile_n_run() {
    # Checking if python 3 is installed
    if command -v python3 &>/dev/null; then
        # Removing previous python converted file
        if [ -f "$1.py" ];then
            rm "$1.py"
        fi
        if [ "$#" -gt 2 ]; then
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1.$2"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py" ${@:3}
                rm "$1.py"
            fi
        elif [ "$#" -gt 1 ]; then
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1.$2"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py"
                rm "$1.py"
            fi
        else
            # Converting script to python
            python3 $HOME/$PROJECT/start.py "$1"
            # Running python converted file
            if [ -f "$1.py" ];then
                python3 "$1.py"
                rm "$1.py"
            fi
        fi
    else
        echo "Python3 not installed"
    fi
}

if [ "$#" -gt 1 ]; then
    IFS='.' read -ra names <<< "$1"
    echo "${@:2}"
    if [ "${#names[@]}" -gt 1 ]; then
        compile_n_run "${names[0]}" "${names[1]}" ${@:2}
    else
        # Checking file extensions and running code
        if [ -f "$1.بايثون" ];then
            compile_n_run "$1" "بايثون" ${@:2}
        elif [ -f "$1.arpy" ];then
            compile_n_run "$1" "arpy" ${@:2}
        else
            echo "extension $1" ${@:2}
        fi
    fi

elif [ "$#" -gt 0 ]; then
    IFS='.' read -ra names <<< "$1"

    if [ "${#names[@]}" -gt 1 ]; then
        compile_n_run "${names[0]}" "${names[1]}"
    else
        # Checking file extensions and running code
        if [ -f "$1.بايثون" ];then
            compile_n_run "$1" "بايثون"
        elif [ -f "$1.arpy" ];then
            compile_n_run "$1" "arpy"
        else
            echo "extension $1"
        fi
    fi
else
    echo "No file found"
fi
