from flask import Blueprint, render_template, request, redirect, url_for
from CoinWeb import db

bp = Blueprint('main_views', __name__, url_prefix='/noo')

@bp.route('/')
def home():
    return render_template('noo/jw_home.html')

@bp.route('/input')
def input():
    return render_template('jw_input.html')

@bp.route('/result', methods=['POST'])
def result():
    forms = request.form
    print(forms)
    return render_template('jw_result.html', forms=forms)