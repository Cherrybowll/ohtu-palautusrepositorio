OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=OLETUSKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._validoi_positiivinen_kokonaisluku(kapasiteetti)
        self._validoi_positiivinen_kokonaisluku(kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0
        self.ljono = self._luo_lista(self.kapasiteetti)

    def kuuluu(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
        if self.alkioiden_lkm == len(self.ljono):
            uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(self.ljono, uusi_lista)
            self.ljono = uusi_lista

        return True

    def poista(self, n):
        apu_indeksi = 0
        n_indeksi = self._etsi_indeksi(n)

        if n_indeksi == None:
            return False

        self.ljono[n_indeksi] = 0
        for i in range(n_indeksi, self.alkioiden_lkm - 1):
            apu_indeksi = self.ljono[i]
            self.ljono[i] = self.ljono[i + 1]
            self.ljono[i + 1] = apu_indeksi

        self.alkioiden_lkm -= 1
        return True

    def _etsi_indeksi(self, n):
        for i in range(self.alkioiden_lkm):
            if n == self.ljono[i]:
                return i
        return None
    
    def _validoi_positiivinen_kokonaisluku(self, n):
        if not isinstance(n, int):
            raise TypeError("Arvo ei ole kokonaisluku")
        if n < 0:
            raise ValueError("Arvon pitää olla epänegatiivinen")

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        if self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        tuotos = "{"
        for i in range(self.alkioiden_lkm - 1):
            tuotos += f"{self.ljono[i]}, "
        tuotos += str(self.ljono[self.alkioiden_lkm - 1])
        tuotos += "}"
        return tuotos
