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
        yield "Para calcular a área de uma circulo, utilize o comando !ac <valor do raio>"
        yield "Para calcular a área de um quadrado, utilize o comando !aq <valor do lado>"
        yield "Para calcular a área do triângulo, utilize o comando !at <valor da base> <valor da altura>"
        yield "Para calcular a área do retângulo, utilize o comando !ar <valor da base> <valor da altura>"
        yield "Para calcular a circunferência do circulo, utilize o comando !cc <valor do raio>"
        yield "Para calcular o perímetro do quadrado, utilize o comando !pq <valor do lado>"
        yield "Para calcular o volume do cubo, utilize o comando !vc <valor do lado>"
        yield "Para calcular o volume da esfera, utilize o comando !ve <valor do raio>"

    @botcmd(split_args_with=' ')
    def ac(self, msg, args):
        """
        Área Circulo
        """

        try:
            texto = args[0].replace (",", ".")
            numero = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero * numero * pi, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def aq(self, msg, args):
        """
        Área Quadrado
        """

        try:
            texto = args[0].replace (",", ".")
            numero1 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero1 * numero1, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def cc(self, msg, args):
        """
        Circunferência Circulo
        """
        
        try:
            texto = args[0].replace (",", ".")
            numero2 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(2 * pi * numero2, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def pq(self, msg, args):
        """
        Perímetro quadrado
        """
        
        try:
            texto = args[0].replace (",", ".")
            numero3 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(4 * numero3, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def vc(self, msg, args):
        """
        Volume Cubo
        """
        
        try:
            texto = args[0].replace (",", ".")
            numero4 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero4 * numero4 * numero4, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def ve(self, msg, args):
        """
        Volume Esfera
        """
        
        try:
            texto = args[0].replace (",", ".")
            numero5 = float(texto)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero5 * numero5 * numero5 * pi * 4 / 3, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def at(self, msg, args):
        """
        Área Triangulo
        """
        
        try:
            texto = args[0].replace (",", ".")
            texto2 = args[1].replace (",", ".")
            numero6 = float(texto)
            numero7 = float(texto2)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero6 * numero7 / 2, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def ar(self, msg, args):
        """
        Área Retângulo
        """
        
        try:
            texto = args[0].replace (",", ".")
            texto2 = args[1].replace (",", ".")
            numero8 = float(texto)
            numero9 = float(texto2)
        except:
            return "Não é um número real"
        else:
            return "```\n" + Figlet(font='slant').renderText(str(round(numero8 * numero9, 2))) + "\n```"

    @botcmd(split_args_with=' ')
    def adele(self, msg, args):
        """
        Adele
        """
        return "Never mind, I'll find someone like you | I wish nothing but the best for you, too | Don't forget me,  I begged | I remember you said | Sometimes it lasts in love, but sometimes it hurts instead"

