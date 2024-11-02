from db import db
from models import HomeModel, RoleType


class HomeManager:

    def get_homes(user):
        query = db.session.query(HomeModel)
        if user.role.user == RoleType.user:
            query = query.filter_by(user_id=user.id)
        return db.session.execute(query).scalar().all()

    def create_home(user, data):
        data["user_id"] = user.id
        new_home = HomeModel(**data)
        db.session.add(new_home)
        db.session.flush()
        db.session.commit()

    def get_home(user, home_id):
        query = db.session.query(HomeModel)
        if user.role.user == RoleType.user:
            query = query.filter_by(id=home_id, user_id=user.id).first_or_404()
        return db.session.execute(query).scalar()
