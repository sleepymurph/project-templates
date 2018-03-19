#!/bin/bash

set -x

# cd to directory of script, which should be parent dir for whole project
cd "$( dirname "${BASH_SOURCE[0]}" )"

SESSION_NAME="latex"

browser_new_window() {
    chromium-browser --new-window "$1"
}

browser() {
    chromium-browser "$1"
}

tmux new-session -d -s "$SESSION_NAME"
tmux select-window -t "$SESSION_NAME:0"

# Lauch web pages and documents
browser_new_window "https://github.com/sleepymurph/project-templates"
xdg-open "latex_report.pdf"

tmux rename-window -t ':0' 'latex'
tmux send-keys "cd '$PWD/latex_report/'" C-m
tmux send-keys 'vim -O doc-content.tex macros-general.tex' C-m

# back to the beginning
tmux select-window -t ':0'

# finally attach client
tmux attach-session
