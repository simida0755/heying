# _*_ coding: utf-8 _*_
from flask import render_template, url_for, redirect, flash
from flask_login import login_required, current_user
from sqlalchemy import or_

from app.libs.email import send_email
from app.libs.unums import Match_status, Group_status
from app.models.base import db
from app.models.group import Group
from app.models.movie import Movie
from app.view_model.group import GroupViewModel
from app.web import web

__author__ = 'john'



@web.route('/group/movie/<mid>')
@login_required
def group(mid):
    movie = Movie.query.filter_by(mid = mid).first()
    if not movie:
        flash('该电影已下架，无法合影')
        return redirect(url_for('web.index'))
    next_url = '/group/movie/{}'.format(mid)
    if not current_user.district:
        return redirect(url_for('web.modified_information', next=next_url))

    match = Group.find_group_matcher(current_user,movie)

    if match:
        with db.auto_commit():
            group = Group()
            group.mid = mid
            if current_user.gender == '男':
                group.man_match_id = current_user.id
                group.man_nickname = current_user.gender
                group.women_match_id = match.uid
                group.women_nickname = match.user.gender
            else:
                group.man_match_id = match.uid
                group.man_nickname = match.user.gender
                group.women_match_id = current_user.id
                group.women_nickname = current_user.gender

            group.movie_mainland_pubdate = match.matcher_district
            match.match_status = Match_status.match_success
            db.session.add(group)
        send_email(match.user.email, '{}合影成功'.format(movie.title),
                   'email/satisify_wish', matcher=match.user,user = current_user,
                   movie=movie)
        flash('合影成功，已通知：' + match.user.nickname)
        return redirect(url_for('web.movie_detail', mid=mid))
    return redirect(url_for('web.match',mid =mid))

@web.route('/my/group')
@login_required
def my_group():
    groups = Group.query.filter(Group.status == 1,
                or_(Group.women_match_id == current_user.id,
                    Group.man_match_id == current_user.id)).all()
    view_model = GroupViewModel.grouping(groups)
    return render_template('grouping.html',groups = view_model)


@web.route('/group/<int:gid>/redraw')
@login_required
def redraw_from_group(gid):
    group = Group.query.filter(
                    Group.id == gid,Group._group_status == Group_status.wait_watch.value,
                    or_(Group.women_match_id == current_user.id,
                    Group.man_match_id == current_user.id)).first()
    if not group:
        flash('该合影不存在，撤销失败')
    else:
        with db.auto_commit():
            group._group_status = Group_status.cancel_watch.value
    return redirect(url_for('web.my_group'))


@web.route('/group/<int:gid>/delete')
@login_required
def delete_from_group(gid):
    group = Group.query.filter(
                    Group.id == gid,
                    or_(Group.women_match_id == current_user.id,
                    Group.man_match_id == current_user.id)).first()
    if not group:
        flash('该合影不存在，删除失败')
    else:
        with db.auto_commit():
            group.status = 0
    return redirect(url_for('web.my_group'))