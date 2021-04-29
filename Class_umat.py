class Umat:
    def __init__(self, *args, **kwargs):
        self.nama = kwargs.get('nama')
        self.tanggal = kwargs.get('tanggal')
        self.bulan = kwargs.get('bulan')
        self.tahun = kwargs.get('tahun')
        self.lingkungan = kwargs.get('lingkungan')
        self.wilayah = kwargs.get('wilayah')
        self.alamat = kwargs.get('alamat')
    def __repr__(self):
        return '''
Nama            : {}
Tanggal Lahir   : {}-{}-{}
Lingkungan      : St. {}
Wilayah         : {}
Alamat Rumah    : {}
        '''.format(self.nama, str(self.tanggal), str(self.bulan), str(self.tahun), self.lingkungan, self.wilayah, self.alamat)