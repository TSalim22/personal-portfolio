import os
from flask import Flask, render_template, Response

PROJECTS = [
    ('CLI Habit Tracker','cli-habit-tracker','Python · JSON','Daily habits, completion history and streaks.'),
    ('To-Do List','todo-list','Python · Flask · SQL','Accounts, priorities, due dates and task editing.'),
    ('Personal Finance','personal-finance-tracker','Python · PostgreSQL · Chart.js','Income, expenses, category charts and CSV export.'),
    ('Multiplayer Game','realtime-multiplayer-game','Python · WebSockets','A shared coin collecting game with live player positions.'),
    ('Level Editor','game-level-editor','Python · Tkinter','Build tile maps and save them as readable JSON.'),
    ('Secure File Vault','secure-file-vault','Python · Cryptography','Password-based authenticated file encryption.'),
    ('Sensor Dashboard','realtime-sensor-dashboard','Python · SSE · Chart.js','Stream simulated readings and export a CSV.'),
    ('OBJ Model Viewer','obj-model-viewer','Python · Tkinter · Geometry','Rotate and zoom wireframe models.'),
    ('Productivity Extension','dev-productivity-extension','Python · Browser APIs','A focus timer with local statistics.'),
]

# Repositories waiting to be uploaded.
PENDING_REPOS = {'game-level-editor','secure-file-vault','realtime-sensor-dashboard','obj-model-viewer'}


def create_app():
    app = Flask(__name__)
    app.config.update(APP_TITLE='TSalim22 / Portfolio', APP_DESCRIPTION='My Python projects.')

    @app.get('/')
    def index():
        return render_template('index.html', title='Python project portfolio', projects=PROJECTS, pending=PENDING_REPOS)

    @app.get('/robots.txt')
    def robots():
        return Response('User-agent: *\nAllow: /\n', mimetype='text/plain')

    return app


if __name__ == '__main__':
    create_app().run(host=os.getenv('HOST','127.0.0.1'),port=5000)
