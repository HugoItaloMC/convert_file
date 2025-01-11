from src.factory.rules.abs import *
__all__ = ["ConcretDataFrame"]

############# CONCRETS CLASS  #################
# Attr `run` apontado na meta-class          ##
# refrênciando descritor da classe Handler   ##
###############################################
                                           
class ConcretDataFrame(AbstractDataFrame): run = ...

                                             