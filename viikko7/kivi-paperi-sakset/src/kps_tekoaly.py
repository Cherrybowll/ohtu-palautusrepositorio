from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        self.tekoaly = tekoaly

    def _tokan_siirto(self, ekan_siirto):
        self.tekoaly.aseta_siirto(ekan_siirto)
        return self.tekoaly.anna_siirto()