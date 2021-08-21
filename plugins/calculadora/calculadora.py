from errbot import BotPlugin, botcmd
from pyfiglet import Figlet
# https://www.w3schools.com/python/ref_math_pi.asp
from math import pi


class Calculadora(BotPlugin):
    """
    Calculadora de operações matemáticas.
    """
    @botcmd
    def comandos(self, msg, args):
        """
        Comandos do Bot.
        """
        yield "Para calcular a área de uma circunferência, utilize o comando !raio <valor em metros>"

    @botcmd(split_args_with=' ')
    def raio(self, msg, args):

        try:
            texto = args[0].replace (",", ".")
            numero = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero * numero * pi, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def lado(self, msg, args):

        try:
            texto = args[0].replace (",", ".")
            numero1 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero1 * numero1, 2))) + "\n```"