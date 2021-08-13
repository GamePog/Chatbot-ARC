from errbot import BotPlugin, botcmd

class Raio(BotPlugin):
    @botcmd(split_args_with=' ')
    def settings():
        return: Opções