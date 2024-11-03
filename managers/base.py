from gevent.pool import pass_value
from werkzeug.exceptions import NotFound

from db import db
from models import RoleType


class BaseManager(object):

    def get_item(user, db_model, item_id, error_msg):

        query = db.select(db_model)
        item = db.session.execute(
            query.filter_by(id=item_id)
        ).scalar()

        if not item:
            raise NotFound(f"{error_msg} with id {item_id} does not exist")

        if user.role.user == RoleType.user:
            query = query.filter_by(id=item_id, user_id=user.id)
        return db.session.execute(query).scalar()

    def update_item(self, item_id, data):
        pass

    def delete_item(self, item_id):
        pass


