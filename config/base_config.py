import os


class BaseConfig:
    SHORT_WAIT = 5
    DEFAULT_WAIT = 10
    LONG_WAIT = 20

    HEADLESS = False
    BROWSER = 'chrome'
    """
        BROWSER parameter can take the options below:
              * chrome
              * firefox
        """
    if os.environ.get('BROWSER') is not None:
        print('BROWSER is read from ENV: {}'.format(os.environ.get('BROWSER')))
        BROWSER = os.environ['BROWSER']

    ENVS = 'insider'
    """
    ENVS parameter can take the options below:
          * insider
    """

    if os.environ.get('ENVS') is not None:
        print('ENVS is read from ENV: {}'.format(os.environ.get('ENVS')))
        ENVS = os.environ['ENVS']

    if ENVS == 'insider':
        APP_BASE_URL = 'https://useinsider.com/'
        BACKEND_URL = 'https://petstore.swagger.io'
