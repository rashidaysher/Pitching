from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch, Comment
from .. import db, photos
from .forms import UpdateProfile, PitchForm, CommentForm
from flask_login import login_required, current_user




