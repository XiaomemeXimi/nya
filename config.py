from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 7211512
    API_HASH = "c3e90518b21f8c4ad5d022f4bac5f330"
    # the name to display in your alive message
    ALIVE_NAME = "Your value"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://clttqdrkbynjmk:68db43d52fef7d73c8914734be1900a32a2e51f1f7782e2f1dfb3bbf74a2755c@ec2-3-208-45-228.compute-1.amazonaws.com:5432/d5j950j94sep77"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1900136253:AAEzIK-pREiecKVslRAexoZtzXNAdH64OXg"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001367203087
    # command handler
    COMMAND_HAND_LER = "/"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = ",,"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
