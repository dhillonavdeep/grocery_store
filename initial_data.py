from main import app
from application.models import db,Role


with app.app_context():
    admin_role = Role(name='Admin', description='Admin Description')
    manager_role = Role(name='Manager', description='Manager Description')
    user_role = Role(name='User', description='User Description')

    db.session.add_all([admin_role, manager_role, user_role])
    
    try:
        db.session.commit()
    except:
        pass
