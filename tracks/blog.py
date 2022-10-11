from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    ind = db.execute(
        'SELECT * FROM tracks'
    ).fetchall()
    return render_template('blog/main.html', ind=ind)


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
        'SELECT COUNT (*) FROM tracks'
    )
    return render_template('blog/tracks.html', tr=tr)


@bp.route('/tracks/rock')
def cnt_genre():
    db = get_db()
    cg = db.execute(
        'SELECT COUNT (id) FROM tracks WHERE genre = rock'
    )
    return render_template('blog/names.html', cg=cg)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    ts = db.execute(
        'SELECT * FROM tracks'
    ).fetchall()
    return render_template('blog/tracks_sec.html', ts=ts)


@bp.route('/tracks-sec/statistics/')
def ts_statistics():
    db = get_db()
    tss = db.execute(
        'SELECT * FROM tracks'
    ).fetchall()
    return render_template('blog/ts_statistics.html', tss=tss)
