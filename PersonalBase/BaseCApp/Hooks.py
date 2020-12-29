def init_hooks_main(server_app,db):
    @server_app.before_first_request
    def auto_init():
        db.create_all()
