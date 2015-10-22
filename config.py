import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('BUCKETLIST_SECRET_KEY') or 'dsbjgnkslmtdjtsdklnrjsjfesn94apw83'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('BUCKETLIST_DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bucketlist-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('BUCKETLIST_TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bucketlist-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('BUCKETLIST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bucketlist.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
