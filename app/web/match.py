# _*_ coding: utf-8 _*_
from flask import request, flash, redirect, url_for, render_template
from flask_login import current_user, login_required

from app.libs.unums import Match_status
from app.models.base import db
from app.models.group import Group
from app.models.match import Match
from app.models.movie import Movie
from app.web import web

__author__ = 'john'

@web.route('/match/movie/<mid>')
@login_required
def match(mid):
    # 找到当前用户
    user = current_user
    # 找到添加到待观影中的电影
    movie =  Movie.query.filter_by(mid = mid).first()
    if not movie:
        flash('该电影不存在或已下架，无法合影')
        return redirect(url_for('web.index'))
    if not user.can_save_macth_or_group:
        flash('你需要更新资料才能合影')
        return redirect(url_for('web.modified_information'))

    if not Match.has_in_match(user,movie):
        with db.auto_commit():
            match = Match()
            match.mid = movie.mid
            match.movie_mainland_pubdate = movie.mainland_pubdate
            match.uid = user.id
            match.matcher_gender = user.gender
            match.matcher_district = user.district
            match.matcher_subway_site = user.subway_site
            db.session.add(match)
    else:
        flash('该电影已添加到合影队列，等待匹配')
        return redirect(url_for('web.movie_detail',mid = mid))
    return redirect(url_for('web.movie_detail',mid = mid))

@web.route('/my/matches')
@login_required
def my_match():
    matches = Match.query.filter_by(uid=current_user.id,status=1).all()
    return render_template('my_match.html',matches = matches)

@web.route('/match/movie/<int:match_id>/redraw')
@login_required
def redraw_from_Match(match_id):
    match = Match.query.filter_by(id=match_id,uid = current_user.id).first()
    if not match:
        flash('该心愿不存在，无法取消')
    else:
        with db.auto_commit():
            match._match_status = Match_status.cancel_match.value
    return redirect(url_for('web.my_match'))






@web.route('/match/movie/<int:match_id>/delete')
@login_required
def delete_from_Match(match_id):
    match = Match.query.filter_by(id=match_id,uid = current_user.id).first()
    if not match:
        flash('该心愿不存在，删除失败')
    else:
        with db.auto_commit():
            match.status = 0
    return redirect(url_for('web.my_match'))
