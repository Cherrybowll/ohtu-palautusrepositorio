from kivipaperisakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _tokan_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")

