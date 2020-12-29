import os

from flask_sqlalchemy import SQLAlchemy

sqlalchemy = SQLAlchemy()


def init_sqlalchemy(server_app):
    sqlalchemy.init_app(server_app)

    @server_app.route("/config/db/init", methods=["GET"])
    def config_db_init():
        print("/config/db/init", os.getcwd())
        sqlalchemy.create_all()
        return "inited"

    @server_app.route("/config/db/drop", methods=['GET'])
    def config_db_drop():
        sqlalchemy.drop_all()
        return "dropped"

    return sqlalchemy
