from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
from tracks.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    return render_template('blog/main.html')


@bp.route('/names/')
def names():
    db = get_db()
    nm = db.execute(
        'SELECT DISTINCT artist FROM tracks'
    ).fetchall()
    nm = len(nm)
    return render_template('blog/names.html', nm=nm)


@bp.route('/tracks/')
def tracks():
    db = get_db()
    tr = db.execute(
        'SELECT COUNT (id) as count FROM tracks'
    ).fetchall()
    return render_template('blog/tracks.html', tr=tr)


@bp.route('/tracks/<int:genre_id>')
def cnt_genre(genre_id):
    db = get_db()
    cg = db.execute(
        'SELECT COUNT (tracks.id) as count '
        'FROM tracks '
        'INNER JOIN genres on genres.id=tracks.genre_id '
        'WHERE genre_id = ?', (genre_id,)
    ).fetchall()
    return render_template('blog/cnt_genre.html', cg=cg)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    ts = db.execute(
        'SELECT * FROM tracks ORDER BY id'
    ).fetchall()
    return render_template('blog/tracks_sec.html', ts=ts)


@bp.route('/tracks-sec/statistics/')
def ts_statistics():
    db = get_db()
    tss = db.execute(
        'SELECT SUM (track_length) as sum, AVG (track_length) as avg FROM tracks'
    ).fetchall()

    return render_template('blog/ts_statistics.html', tss=tss)
