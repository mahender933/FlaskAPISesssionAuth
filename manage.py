import unittest

from app import app
from auth import db, ma, auth_blueprint
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


# Order matters: Initialize SQLAlchemy before Marshmallow
db.init_app(app)
ma.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

app.url_map.strict_slashes = False
app.register_blueprint(auth_blueprint)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover(start_dir='', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
