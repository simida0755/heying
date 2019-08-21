# _*_ coding: utf-8 _*_
from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy import or_

from app.forms.movie import SearchForm
from app.libs.unums import Match_status, Group_status
from app.models.group import Group
from app.models.match import Match
from app.models.movie import Movie
from app.models.user import User
from app.web import web

__author__ = 'john'


@web.route('/test')
def test():
    return 'test'


@web.route('/movie/search')
def search():
    form = SearchForm(request.args)
    q = form.q.data.strip()
    movie = Movie.query.filter(Movie.title.like('%{}%'.format(q))|Movie.casts.like('%{}%'.format(q))).all()
    return render_template('index.html',recent=movie)

@web.route('/movie/<mid>/detail')
def movie_detail(mid):

    movie = Movie.query.filter_by(mid=mid).first_or_404()
    if current_user.is_authenticated:
        has_in_match = Match.query.filter_by(
            uid=current_user.id, mid=mid,
            _match_status=Match_status.wait_match.value).first()

        group = Group.query.filter(
                    or_(Group.man_match_id == current_user.id,
                        Group.women_match_id == current_user.id),
            or_(Group._group_status == Group_status.wait_watch.value,
                Group._group_status == Group_status.has_been_watch.value),
                    Group.mid == mid,Group.status == 1).first()
        matchers = Match.query.filter_by(
            mid = mid,_match_status = Match_status.wait_match.value,
            matcher_gender = current_user.group_sex).all()
        return render_template('movie_detail.html',movie=movie,wishes=[],gifts=[],
                           has_in_match = has_in_match,group = group,matchers = matchers)
    else:

        matchers = Match.query.filter_by(
            mid=mid, _match_status = Match_status.wait_match.value).all()
        return render_template('movie_detail.html', movie=movie, wishes=[], gifts=[],
                               has_in_match=False, group=False,matchers = matchers)

@web.route('/movie/<int:mid>/detail_more')
def movie_detail_more(mid):
    flash('此功能待开发,敬请期待')
    return redirect(url_for('web.index'))

@web.route('/save_to_wish')
def save_to_wish():
    pass


@web.route('/satisfy_wish')
def satisfy_wish():
    pass

@web.route('/send_drift')
def send_drift():
    pass