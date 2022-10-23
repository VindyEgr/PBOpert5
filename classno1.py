class Prod:
    
    def __init__(self, id, nama, hrg, jmlh):
        self.__id = id
        self.__nama = nama
        self.__hrg = hrg
        self.__jmlh = jmlh

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

    @property
    def hrg(self):
        return self.__hrg
    @hrg.setter
    def hrg(self, hrg):
        self.__hrg = hrg

    @property
    def jmlh(self):
        return self.__jmlh
    @jmlh.setter
    def jmlh(self, jmlh):
        self.__jmlh = jmlh

produk = Prod(0, 'Aqua', 5000, 3)
print (produk.id, produk.nama, produk.hrg, produk.jmlh)
        