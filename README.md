# Personal Portfolio

A responsive portfolio served by Python Flask.

This is a small, independent Python portfolio project. The code favours ordinary functions and clear modules over complex architecture.

## Setup

Requires Python 3.12+ (desktop tools also require Tkinter, included with the standard Windows Python installer).

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux instead: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python app.py
```

Run commands from this repository's root. Web apps bind to localhost by default. Each app is independent, so stop one before starting another on the same port.

## Check it

```sh
python -m pytest -q
```

## Dates

The commit author dates have been deliberately arranged between October 2025 and October 2026 at the portfolio owner's request. They are presentation metadata, not a record of the actual development timeline. Repository creation and upload timestamps remain the real dates.

## Use and customise

Open http://127.0.0.1:5000. Edit the project list in `app.py`, the content in `templates/index.html`, and colours in `static/style.css`. The layout adapts to phones and has semantic headings, labels and a description meta tag. It lists public repository links only; private API projects are intentionally omitted.

This is a Flask implementation of the portfolio idea. No React build, account, external API or deployment service is required.

## Optional local container

```sh
docker build -t personal-portfolio .
docker run --rm -p 127.0.0.1:5000:5000 personal-portfolio
```

This runs a local demonstration server. Container storage is temporary unless you mount a volume for `instance/`. Docker commands were supplied but Docker is not installed in the development environment, so container execution was not verified here.
