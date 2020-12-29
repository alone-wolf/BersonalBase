import os

from PersonalBase import BaseApp

if __name__ == '__main__':
    main_path = os.path.abspath(".")
    BaseApp("{}/PersonalBase/templates".format(main_path),
            "{}/PersonalBase/static".format(main_path),
            host="0.0.0.0",
            port=5000,
            debug=False).run()
