from mongodb_migrations.base import BaseMigration
from mongodb_migrations.cli import MigrationManager

class Migration(BaseMigration):
    def __init__(self, host='localhost', port='5000', database='test', user=None, password=None, url=None):
        super().__init__(host, port, database, user, password, url)

    def upgrade(self):
        self.db['mpk-cities'].save()
    
    def downgrade(self):
        self.db['mpk-cities'].drop()

manager = MigrationManager()
manager.config.config_file = '/app/migrations/config.ini'
manager.config._from_ini()
manager.run()