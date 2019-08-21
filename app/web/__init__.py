# _*_ coding: utf-8 _*_
from flask import Blueprint

__author__ = 'john'


web = Blueprint('web',__name__)

from app.web import movie
from app.web import main
from app.web import auth
from app.web import group
from app.web import match