import os

from PersonalBase import BaseApp

if __name__ == '__main__':
    # print("__main__", os.path.abspath("."))
    main_path = os.path.abspath(".")
    b = BaseApp("{}/PersonalBase/templates".format(main_path), "{}/PersonalBase/static".format(main_path))
    # b = BaseApp()
    b.run()
