__author__ = 'aric'

import random
from  . import models
class Recommen(object):

    def GetRandomProduct(self, range):
        if range == 0:
            range = 1

        rdm = random.randint(1, range)
        product = models.ProductDetail
        res_product = product.objects.get(id=rdm)

        return res_product

    pass
