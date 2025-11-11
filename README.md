# Personal Portfolio

My Python projects, with links to their GitHub repositories.

## Try it in your browser

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TSalim22/personal-portfolio?quickstart=1)

Sign in to GitHub, open a Codespace and wait for setup. Then run this in its terminal:

```sh
python app.py
```

Open port 5000 from the **Ports** tab if the app does not open automatically.

Codespaces uses your GitHub account’s allowance. Stop it when finished.

## Run it

Python 3.12 or later. Run these commands from the project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python app.py
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## How to use it

Open http://127.0.0.1:5000.

Edit `app.py` to change the projects, `templates/index.html` for the page text, and `static/style.css` for the design. Projects waiting to be uploaded are labelled on the page.

## Tests

```sh
python -m pytest -q
```

## Docker (optional)

```sh
docker build -t personal-portfolio .
docker run --rm -p 127.0.0.1:5000:5000 personal-portfolio
```

Docker hasn't been tested locally.
