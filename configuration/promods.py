from configuration.vanilla import VanillaConfiguration


class ProModsConfiguration(VanillaConfiguration):
    def __init__(self):
        super().__init__()
        self.rhs_driver_countries = rhs_driver_countries


rhs_driver_countries = [
    "gb", "cy", "gbg", "gbm", "irl", "m", "gbj"
]

# New countries

# aland (ax)
# andorra (and)
# armenia (am)
# belarus (by)
# cyprus (cy)
# faroe (fo)
# georgia (ge)
# greece (gr)
# greenland (gl)
# guernsey (gbg)
# iceland (is)
# ireland (irl)
# isleofman (gbm)
# jersey (gbj)
# liecht (fl)
# malta (m)
# moldova (md)
# monaco (mc)
# nireland (gb)
# sanmarino (rsm)
# svalbard (sj)
# ukraine (ua)
