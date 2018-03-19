#!/bin/bash

set -x

browser_new_window() {
    chromium-browser --new-window "$1"
}

browser() {
    chromium-browser "$1"
}

SCRIPT_DIR="$( dirname "${BASH_SOURCE[0]}" )"

# ↓↓↓ Set project-specific variables here ↓↓↓

SESSION_NAME="latex"
WINDOW_NAME="latex"
REPO_URL="https://github.com/sleepymurph/project-templates"

# ↑↑↑ --- ↑↑↑

# Set start directory for whole session
cd "$SCRIPT_DIR"

# start tmux session
tmux new-session -d -s "$SESSION_NAME" -n "$WINDOW_NAME"
tmux select-window -t "$SESSION_NAME:0"

# Launch web pages and documents
browser_new_window "$REPO_URL"
xdg-open "doc.pdf"

# ↓↓↓ Customize here ↓↓↓

# In first window
tmux send-keys 'vim -O doc-content.tex sources.bib' C-m

# ↑↑↑ --- ↑↑↑

# back to the beginning
tmux select-window -t ':0'

# finally attach client
tmux attach-session
