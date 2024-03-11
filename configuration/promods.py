from configuration.vanilla import VanillaConfiguration


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
# iom (gbm)
# jersey (gbj)
# liecht (fl)
# malta (m)
# moldova (md)
# nireland (gb)
# sanmarino (rsm)
# svalbard (sj)
# ukraine (ua)

class ProModsConfiguration(VanillaConfiguration):
    def __init__(self):
        super().__init__()
        self.car_spawn_config = car_spawn_config
        self.truck_spawn_config = truck_spawn_config
        self.rhs_driver_countries = rhs_driver_countries


car_spawn_config = {
    "netherlands": {
        "national": 0.79,
        "international": [("germany", 0.07), ("belgium", 0.05), ("poland", 0.04), ("france", 0.02), ("uk", 0.02)],
        "random": 0.01,
    },
    "germany": {
        "national": 0.79,
        "international": [("netherlands", 0.035), ("switzerland", 0.02), ("austria", 0.02), ("czech", 0.035),
                          ("poland", 0.04), ("france", 0.02), ("denmark", 0.02), ("ukraine", 0.01)],
        "random": 0.01,
    },
    "austria": {
        "national": 0.69,
        "international": [("germany", 0.08), ("netherlands", 0.06), ("switzerland", 0.02), ("czech", 0.03),
                          ("slovenia", 0.02), ("slovakia", 0.03), ("hungary", 0.025), ("italy", 0.025),
                          ("liecht", 0.01)],
        "random": 0.01,
    },
    "belgium": {
        "national": 0.79,
        "international": [("luxembourg", 0.05), ("netherlands", 0.05), ("germany", 0.03), ("france", 0.05),
                          ("uk", 0.02)],
        "random": 0.01,
    },
    "france": {
        "national": 0.79,
        "international": [("netherlands", 0.04), ("spain", 0.04), ("belgium", 0.02), ("switzerland", 0.01),
                          ("italy", 0.01), ("germany", 0.04), ("uk", 0.02), ("luxembourg", 0.01), ("jersey", 0.005),
                          ("guernsey", 0.005)],
        "random": 0.01,
    },
    "luxembourg": {
        "national": 0.70,
        "international": [("belgium", 0.08), ("germany", 0.07), ("netherlands", 0.06), ("france", 0.08)],
        "random": 0.01,
    },
    "norway": {
        "national": 0.79,
        "international": [("germany", 0.05), ("netherlands", 0.04), ("denmark", 0.04), ("sweden", 0.06),
                          ("iceland", 0.01)],
        "random": 0.01,
    },
    "uk": {
        "national": 0.79,
        "international": [("germany", 0.045), ("netherlands", 0.045), ("france", 0.04), ("belgium", 0.03),
                          ("lithuania", 0.01), ("poland", 0.02), ("jersey", 0.005), ("guernsey", 0.005)],
        "random": 0.01,
    },
    "turkey": {
        "national": 0.79,
        "international": [("germany", 0.04), ("netherlands", 0.005), ("bulgaria", 0.03), ("romania", 0.025),
                          ("greece", 0.025), ("sweden", 0.005), ("russia", 0.025), ("macedonia", 0.005),
                          ("bosnia", 0.005), ("georgia", 0.01), ("armenia", 0.01), ("cyprus", 0.005),
                          ("ukraine", 0.01)],
        "random": 0.01,
    },
    "lithuania": {
        "national": 0.79,
        "international": [("latvia", 0.06), ("poland", 0.05), ("estonia", 0.04), ("uk", 0.03), ("russia", 0.01),
                          ("belarus", 0.01)],
        "random": 0.01,
    },
    "bulgaria": {
        "national": 0.78,
        "international": [("romania", 0.06), ("hungary", 0.03), ("germany", 0.03), ("turkey", 0.02),
                          ("macedonia", 0.02), ("serbia", 0.025), ("greece", 0.025)],
        "random": 0.01,
    },
    "poland": {
        "national": 0.79,
        "international": [("czech", 0.035), ("slovakia", 0.035), ("germany", 0.025), ("lithuania", 0.025),
                          ("latvia", 0.03),
                          ("estonia", 0.02), ("belarus", 0.01), ("ukraine", 0.02)],
        "random": 0.01,
    },
    "portugal": {
        "national": 0.79,
        "international": [("spain", 0.05), ("france", 0.05), ("uk", 0.02), ("luxembourg", 0.01), ("netherlands", 0.03),
                          ("germany", 0.03), ("andorra", 0.01)],
        "random": 0.01,
    },
    "spain": {
        "national": 0.79,
        "international": [("portugal", 0.05), ("france", 0.05), ("uk", 0.02), ("luxembourg", 0.01), ("andorra", 0.01),
                          ("netherlands", 0.03), ("germany", 0.03)],
        "random": 0.01,
    },
    "romania": {
        "national": 0.79,
        "international": [("germany", 0.04), ("italy", 0.01), ("france", 0.01), ("turkey", 0.02), ("hungary", 0.035),
                          ("serbia", 0.025), ("poland", 0.02), ("bulgaria", 0.02), ("moldova", 0.02)],
        "random": 0.01,
    },
    "russia": {
        "national": 0.85,
        "international": [("finland", 0.03), ("estonia", 0.03), ("latvia", 0.02), ("lithuania", 0.01),
                          ("belarus", 0.03), ("georgia", 0.01), ("armenia", 0.01)],
        "random": 0.01,
    },
    "estonia": {
        "national": 0.79,
        "international": [("latvia", 0.05), ("lithuania", 0.03), ("finland", 0.05), ("germany", 0.03), ("poland", 0.01),
                          ("russia", 0.03)],
        "random": 0.01,
    },
    "finland": {
        "national": 0.79,
        "international": [("estonia", 0.045), ("latvia", 0.045), ("lithuania", 0.02), ("sweden", 0.02),
                          ("norway", 0.03),
                          ("poland", 0.02), ("russia", 0.01), ("aland", 0.01)],
        "random": 0.01,
    },
    "hungary": {
        "national": 0.79,
        "international": [("romania", 0.05), ("slovakia", 0.04), ("austria", 0.02), ("serbia", 0.02),
                          ("slovenia", 0.02), ("croatia", 0.02), ("italy", 0.01), ("germany", 0.01), ("turkey", 0.01)],
        "random": 0.01,

    },
    "switzerland": {
        "national": 0.74,
        "international": [("germany", 0.045), ("france", 0.045), ("austria", 0.045), ("italy", 0.045), ("uk", 0.03),
                          ("netherlands", 0.02), ("liecht", 0.02)],
        "random": 0.01,
    },
    "latvia": {
        "national": 0.78,
        "international": [("lithuania", 0.06), ("estonia", 0.05), ("finland", 0.02), ("germany", 0.02),
                          ("poland", 0.02), ("russia", 0.02), ("belarus", 0.02)],
        "random": 0.01,
    },
    "sweden": {
        "national": 0.79,
        "international": [("norway", 0.05), ("finland", 0.04), ("denmark", 0.04), ("germany", 0.03),
                          ("netherlands", 0.03), ("aland", 0.01)],
        "random": 0.01,
    },
    "denmark": {
        "national": 0.79,
        "international": [("germany", 0.06), ("sweden", 0.05), ("norway", 0.05), ("netherlands", 0.04)],
        "random": 0.01,
    },
    "czech": {
        "national": 0.79,
        "international": [("germany", 0.04), ("poland", 0.045), ("austria", 0.035), ("slovakia", 0.04),
                          ("hungary", 0.03), ("ukraine", 0.01)],
        "random": 0.01,
    },
    "italy": {
        "national": 0.79,
        "international": [("germany", 0.055), ("netherlands", 0.035), ("switzerland", 0.02), ("france", 0.02),
                          ("slovenia", 0.02), ("austria", 0.015), ("greece", 0.015), ("malta", 0.01),
                          ("sanmarino", 0.01)],
        "random": 0.01,
    },
    "slovakia": {
        "national": 0.79,
        "international": [("czech", 0.04), ("poland", 0.05), ("austria", 0.04), ("germany", 0.03), ("hungary", 0.04)],
        "random": 0.01,
    },
    "albania": {
        "national": 0.79,
        "international": [("montenegro", 0.04), ("kosovo", 0.03), ("macedonia", 0.05), ("germany", 0.02),
                          ("serbia", 0.03), ("greece", 0.03)],
        "random": 0.01,
    },
    "bosnia": {
        "national": 0.79,
        "international": [("montenegro", 0.06), ("croatia", 0.06), ("serbia", 0.06), ("hungary", 0.02)],
        "random": 0.01,
    },
    "croatia": {
        "national": 0.79,
        "international": [("montenegro", 0.02), ("slovenia", 0.05), ("hungary", 0.03), ("bosnia", 0.04),
                          ("serbia", 0.03), ("germany", 0.02), ("netherlands", 0.01)],
        "random": 0.01,
    },
    "kosovo": {
        "national": 0.79,
        "international": [("montenegro", 0.03), ("serbia", 0.08), ("macedonia", 0.05), ("albania", 0.04)],
        "random": 0.01,
    },
    "macedonia": {
        "national": 0.79,
        "international": [("kosovo", 0.03), ("turkey", 0.02), ("bulgaria", 0.04), ("serbia", 0.04), ("albania", 0.04),
                          ("greece", 0.03)],
        "random": 0.01,
    },
    "montenegro": {
        "national": 0.79,
        "international": [("bosnia", 0.05), ("croatia", 0.02), ("serbia", 0.05), ("kosovo", 0.04), ("albania", 0.04)],
        "random": 0.01,
    },
    "serbia": {
        "national": 0.79,
        "international": [("montenegro", 0.02), ("bosnia", 0.03), ("hungary", 0.03), ("bulgaria", 0.03),
                          ("kosovo", 0.03), ("turkey", 0.02), ("macedonia", 0.02), ("croatia", 0.02)],
        "random": 0.01,
    },
    "slovenia": {
        "national": 0.79,
        "international": [("croatia", 0.05), ("austria", 0.05), ("italy", 0.04), ("hungary", 0.03),
                          ("bosnia", 0.02), ("germany", 0.01)],
        "random": 0.01,
    },

    # PM countries

    "aland": {
        "national": 0.88,
        "international": [("sweden", 0.05), ("finland", 0.05)],
        "random": 0.02,
    },
    "andorra": {
        "national": 0.69,
        "international": [("spain", 0.10), ("france", 0.10), ("uk", 0.02), ("portugal", 0.02),
                          ("netherlands", 0.03), ("germany", 0.03)],
        "random": 0.01,
    },
    "armenia": {
        "national": 0.79,
        "international": [("georgia", 0.10), ("turkey", 0.05), ("russia", 0.05)],
        "random": 0.01,
    },
    "belarus": {
        "national": 0.79,
        "international": [("russia", 0.06), ("latvia", 0.04), ("poland", 0.04), ("lithuania", 0.04), ("ukraine", 0.02)],
        "random": 0.01,
    },
    "cyprus": {
        "national": 0.80,
        "international": [("greece", 0.10), ("turkey", 0.08)],
        "random": 0.02
    },
    "faroe": {
        "national": 0.80,
        "international": [("denmark", 0.05), ("iceland", 0.05), ("uk", 0.05), ("norway", 0.04)],
        "random": 0.01
    },
    "georgia": {
        "national": 0.80,
        "international": [("turkey", 0.08), ("armenia", 0.06), ("russia", 0.05)],
        "random": 0.01
    },
    "greece": {
        "national": 0.79,
        "international": [("turkey", 0.04), ("cyprus", 0.02), ("bulgaria", 0.03), ("italy", 0.03), ("albania", 0.04),
                          ("macedonia", 0.04)],
        "random": 0.01
    },
    "greenland": {
        "national": 0.79,
        "international": [("denmark", 0.05), ("iceland", 0.05), ("uk", 0.05), ("norway", 0.05)],
        "random": 0.01
    },
    "guernsey": {
        "national": 0.80,
        "international": [("uk", 0.08), ("france", 0.08), ("ireland", 0.03)],
        "random": 0.01,
    },
    "iceland": {
        "national": 0.85,
        "international": [("uk", 0.08), ("norway", 0.03), ("faroe", 0.03)],
        "random": 0.01
    },
    "ireland": {
        "national": 0.79,
        "international": [("uk", 0.12), ("germany", 0.02), ("france", 0.02), ("iom", 0.01), ("nireland", 0.02)],
        "random": 0.02
    },
    "iom": {
        "national": 0.80,
        "international": [("uk", 0.12), ("ireland", 0.07)],
        "random": 0.01
    },
    "jersey": {
        "national": 0.80,
        "international": [("uk", 0.09), ("france", 0.08), ("ireland", 0.02)],
        "random": 0.01,
    },
    "liecht": {
        "national": 0.79,
        "international": [("switzerland", 0.05), ("germany", 0.05), ("austria", 0.05), ("france", 0.015),
                          ("italy", 0.015)],
        "random": 0.03,
    },
    "malta": {
        "national": 0.89,
        "international": [("italy", 0.09)],
        "random": 0.02,
    },
    "moldova": {
        "national": 0.79,
        "international": [("romania", 0.10), ("ukraine", 0.08), ("russia", 0.02)],
        "random": 0.01
    },
    "nireland": {
        "national": 0.80,
        "international": [("uk", 0.08), ("ireland", 0.08), ("iom", 0.02)],
        "random": 0.02
    },
    "sanmarino": {
        "national": 0.74,
        "international": [("italy", 0.12), ("germany", 0.04), ("netherlands", 0.03), ("switzerland", 0.02),
                          ("france", 0.02), ("slovenia", 0.01), ("austria", 0.01)],
        "random": 0.01
    },
    "svalbard": {
        "national": 0.80,
        "international": [("norway", 0.10), ("russia", 0.09)],
        "random": 0.01
    },
    "ukraine": {
        "national": 0.80,
        "international": [("poland", 0.04), ("belarus", 0.04), ("moldova", 0.02), ("russia", 0.04), ("slovakia", 0.02),
                          ("hungary", 0.02), ("romania", 0.01)],
        "random": 0.01
    },
}

truck_spawn_config = {
    "netherlands": {
        "national": 0.60,
        "international": [("poland", 0.10), ("romania", 0.04), ("germany", 0.05), ("belgium", 0.04),
                          ("lithuania", 0.02), ("france", 0.01), ("uk", 0.01), ("spain", 0.01), ("hungary", 0.01),
                          ("luxembourg", 0.01)],
        "random": 0.10,
    },
    "germany": {
        "national": 0.59,
        "international": [("poland", 0.125), ("netherlands", 0.03), ("lithuania", 0.03), ("romania", 0.02),
                          ("austria", 0.01), ("czech", 0.01), ("bulgaria", 0.01), ("slovenia", 0.01),
                          ("hungary", 0.01), ("luxembourg", 0.01), ("denmark", 0.01), ("france", 0.01),
                          ("switzerland", 0.01), ("portugal", 0.01), ("ireland", 0.005)],
        "random": 0.10,
    },
    "austria": {
        "national": 0.60,
        "international": [("germany", 0.08), ("poland", 0.04), ("hungary", 0.03), ("slovenia", 0.03),
                          ("slovakia", 0.03), ("romania", 0.02), ("czech", 0.02), ("croatia", 0.02),
                          ("lithuania", 0.01), ("switzerland", 0.01), ("italy", 0.01)],
        "random": 0.10,
    },
    "belgium": {
        "national": 0.60,
        "international": [("netherlands", 0.06), ("luxembourg", 0.05), ("poland", 0.05), ("france", 0.04),
                          ("romania", 0.02), ("uk", 0.02), ("lithuania", 0.01), ("germany", 0.01), ("italy", 0.01),
                          ("hungary", 0.01), ("portugal", 0.01), ("ireland", 0.01)],
        "random": 0.10,
    },
    "france": {
        "national": 0.60,
        "international": [("poland", 0.06), ("belgium", 0.04), ("spain", 0.04), ("lithuania", 0.03),
                          ("portugal", 0.03), ("uk", 0.02), ("romania", 0.02), ("germany", 0.02), ("italy", 0.01),
                          ("luxembourg", 0.01), ("netherlands", 0.01), ("switzerland", 0.01), ("ireland", 0.01)],
        "random": 0.09,
    },
    "luxembourg": {
        "national": 0.60,
        "international": [("belgium", 0.06), ("france", 0.05), ("poland", 0.05), ("germany", 0.03),
                          ("netherlands", 0.05), ("lithuania", 0.03), ("romania", 0.02), ("switzerland", 0.01)],
        "random": 0.10,
    },
    "norway": {
        "national": 0.60,
        "international": [("sweden", 0.08), ("lithuania", 0.07), ("poland", 0.04), ("latvia", 0.03), ("germany", 0.03),
                          ("denmark", 0.02), ("estonia", 0.02), ("netherlands", 0.01)],
        "random": 0.10,
    },
    "uk": {
        "national": 0.60,
        "international": [("poland", 0.07), ("ireland", 0.04), ("germany", 0.04), ("netherlands", 0.03),
                          ("france", 0.03), ("belgium", 0.03), ("lithuania", 0.02), ("romania", 0.02), ("hungary", 0.02)],
        "random": 0.10,
    },
    "turkey": {
        "national": 0.79,
        "international": [("bulgaria", 0.04), ("romania", 0.025), ("poland", 0.025), ("greece", 0.02),
                          ("georgia", 0.02), ("ukraine", 0.02), ("russia", 0.02), ("serbia", 0.01),  ("armenia", 0.01)],
        "random": 0.02,
    },
    "lithuania": {
        "national": 0.62,
        "international": [("latvia", 0.08), ("poland", 0.06), ("estonia", 0.06), ("finland", 0.02), ("sweden", 0.02),
                          ("russia", 0.01), ("belarus", 0.03)],
        "random": 0.10,
    },
    "bulgaria": {
        "national": 0.60,
        "international": [("turkey", 0.10), ("romania", 0.08), ("hungary", 0.04), ("serbia", 0.03), ("poland", 0.03),
                          ("macedonia", 0.02)],
        "random": 0.10,
    },
    "poland": {
        "national": 0.60,
        "international": [("germany", 0.07), ("lithuania", 0.06), ("romania", 0.05),  ("belarus", 0.03),
                          ("slovakia", 0.02), ("latvia", 0.02), ("czech", 0.01), ("austria", 0.01), ("slovenia", 0.01),
                          ("hungary", 0.01), ("croatia", 0.01)],
        "random": 0.10,
    },
    "portugal": {
        "national": 0.60,
        "international": [("spain", 0.07), ("romania", 0.04), ("poland", 0.04), ("france", 0.03), ("bulgaria", 0.02),
                          ("lithuania", 0.02), ("uk", 0.02), ("czech", 0.02), ("germany", 0.02), ("hungary", 0.01),
                          ("slovenia", 0.01)],
        "random": 0.10,
    },
    "spain": {
        "national": 0.60,
        "international": [("portugal", 0.06), ("romania", 0.04), ("poland", 0.04), ("france", 0.03), ("bulgaria", 0.02),
                          ("lithuania", 0.02), ("uk", 0.02), ("netherlands", 0.02), ("germany", 0.02),
                          ("hungary", 0.01), ("andorra", 0.02), ("slovenia", 0.01)],
        "random": 0.09,
    },
    "romania": {
        "national": 0.60,
        "international": [("turkey", 0.08), ("hungary", 0.08), ("poland", 0.07), ("serbia", 0.03), ("bulgaria", 0.04)],
        "random": 0.10,
    },
    "russia": {
        "national": 0.80,
        "international": [("lithuania", 0.03), ("latvia", 0.02), ("poland", 0.02), ("finland", 0.02), ("turkey", 0.015),
                          ("estonia", 0.01), ("belarus", 0.03), ("georgia", 0.015), ("armenia", 0.01), ("ukraine", 0.02)],
        "random": 0.01,
    },
    "estonia": {
        "national": 0.60,
        "international": [("latvia", 0.07), ("lithuania", 0.06), ("poland", 0.06), ("finland", 0.05), ("russia", 0.02),
                          ("romania", 0.02), ("germany", 0.02)],
        "random": 0.10,
    },
    "finland": {
        "national": 0.60,
        "international": [("poland", 0.09), ("estonia", 0.06), ("germany", 0.03), ("sweden", 0.03), ("norway", 0.03),
                          ("latvia", 0.02), ("lithuania", 0.02), ("russia", 0.02)],
        "random": 0.10,
    },
    "hungary": {
        "national": 0.60,
        "international": [("poland", 0.075), ("romania", 0.055), ("slovakia", 0.05), ("turkey", 0.04),
                          ("czech", 0.02), ("germany", 0.02), ("austria", 0.02), ("croatia", 0.01), ("serbia", 0.01)],
        "random": 0.10,
    },
    "switzerland": {
        "national": 0.60,
        "international": [("germany", 0.11), ("poland", 0.07), ("italy", 0.06), ("austria", 0.01), ("slovakia", 0.01),
                          ("france", 0.01), ("netherlands", 0.01), ("hungary", 0.01), ("lithuania", 0.01)],
        "random": 0.10,
    },
    "latvia": {
        "national": 0.60,
        "international": [("lithuania", 0.07), ("poland", 0.07), ("estonia", 0.07), ("finland", 0.02), ("sweden", 0.02),
                          ("russia", 0.02), ("belarus", 0.03)],
        "random": 0.10,
    },
    "sweden": {
        "national": 0.60,
        "international": [("poland", 0.08), ("norway", 0.04), ("denmark", 0.04), ("lithuania", 0.03), ("latvia", 0.02),
                          ("germany", 0.02), ("estonia", 0.02), ("netherlands", 0.02), ("finland", 0.02),
                          ("romania", 0.01)],
        "random": 0.10,
    },
    "denmark": {
        "national": 0.60,
        "international": [("poland", 0.08), ("norway", 0.05), ("sweden", 0.05), ("germany", 0.04), ("lithuania", 0.03),
                          ("romania", 0.02), ("netherlands", 0.02), ("czech", 0.01)],
        "random": 0.10,
    },
    "czech": {
        "national": 0.60,
        "international": [("poland", 0.09), ("slovakia", 0.09), ("germany", 0.04), ("lithuania", 0.02),
                          ("hungary", 0.02), ("romania", 0.01), ("austria", 0.02), ("netherlands", 0.01)],
        "random": 0.10,
    },
    "italy": {
        "national": 0.60,
        "international": [("poland", 0.06), ("romania", 0.035), ("france", 0.035), ("lithuania", 0.03),
                          ("germany", 0.03),
                          ("slovenia", 0.025), ("austria", 0.025), ("bulgaria", 0.03), ("slovakia", 0.02),
                          ("switzerland", 0.01), ("sanmarino", 0.01)],
        "random": 0.09,
    },
    "slovakia": {
        "national": 0.60,
        "international": [("czech", 0.09), ("poland", 0.06), ("hungary", 0.05), ("austria", 0.01), ("germany", 0.1)],
        "random": 0.09,
    },
    "albania": {
        "national": 0.79,
        "international": [("montenegro", 0.04), ("kosovo", 0.04), ("macedonia", 0.05), ("italy", 0.03),
                          ("serbia", 0.03), ("germany", 0.01)],
        "random": 0.01,
    },
    "bosnia": {
        "national": 0.89,
        "international": [("germany", 0.03), ("austria", 0.02), ("montenegro", 0.01), ("croatia", 0.01),
                          ("serbia", 0.02), ("hungary", 0.01)],
        "random": 0.01,
    },
    "croatia": {
        "national": 0.79,
        "international": [("slovenia", 0.03), ("poland", 0.03), ("hungary", 0.03), ("germany", 0.03),
                          ("slovakia", 0.02), ("turkey", 0.01), ("italy", 0.01), ("lithuania", 0.01),
                          ("montenegro", 0.01), ("bosnia", 0.01), ("serbia", 0.01)],
        "random": 0.01,
    },
    "kosovo": {
        "national": 0.79,
        "international": [("montenegro", 0.03), ("serbia", 0.07), ("macedonia", 0.03), ("albania", 0.07)],
        "random": 0.01,
    },
    "macedonia": {
        "national": 0.79,
        "international": [("turkey", 0.06), ("kosovo", 0.03), ("bulgaria", 0.03), ("serbia", 0.04), ("albania", 0.04)],
        "random": 0.01,
    },
    "montenegro": {
        "national": 0.79,
        "international": [("germany", 0.04), ("bosnia", 0.03), ("croatia", 0.02), ("serbia", 0.03), ("kosovo", 0.04),
                          ("albania", 0.04)],
        "random": 0.01,
    },
    "serbia": {
        "national": 0.69,
        "international": [("turkey", 0.08), ("romania", 0.06), ("hungary", 0.05), ("bulgaria", 0.03),
                          ("montenegro", 0.02), ("bosnia", 0.02), ("kosovo", 0.01), ("macedonia", 0.02),
                          ("croatia", 0.01)],
        "random": 0.01,
    },
    "slovenia": {
        "national": 0.65,
        "international": [("romania", 0.06), ("poland", 0.04), ("slovakia", 0.04), ("hungary", 0.03), ("turkey", 0.03),
                          ("italy", 0.02), ("austria", 0.02), ("slovenia", 0.01), ("croatia", 0.01), ("serbia", 0.01),
                          ("bulgaria", 0.01), ("macedonia", 0.01), ("bosnia", 0.01)],
        "random": 0.05,
    },

    # PM countries

    "aland": {
        "national": 0.80,
        "international": [("sweden", 0.09), ("finland", 0.09)],
        "random": 0.02,
    },
    "andorra": {
        "national": 0.60,
        "international": [("spain", 0.10), ("france", 0.09), ("poland", 0.05), ("uk", 0.02), ("portugal", 0.02),
                          ("germany", 0.02)],
        "random": 0.10,
    },
    "armenia": {
        "national": 0.70,
        "international": [("turkey", 0.17), ("georgia", 0.07), ("russia", 0.05)],
        "random": 0.01,
    },
    "belarus": {
        "national": 0.70,
        "international": [("russia", 0.09), ("latvia", 0.06), ("poland", 0.07), ("lithuania", 0.04), ("ukraine", 0.03)],
        "random": 0.01,
    },
    "cyprus": {
        "national": 0.80,
        "international": [("greece", 0.10), ("turkey", 0.08)],
        "random": 0.02
    },
    "faroe": {
        "national": 0.75,
        "international": [("denmark", 0.15), ("iceland", 0.04), ("uk", 0.03), ("norway", 0.02)],
        "random": 0.01
    },
    "georgia": {
        "national": 0.70,
        "international": [("turkey", 0.15), ("armenia", 0.08), ("russia", 0.06)],
        "random": 0.01
    },
    "greece": {
        "national": 0.60,
        "international": [("turkey", 0.08), ("cyprus", 0.02), ("bulgaria", 0.09), ("italy", 0.03), ("albania", 0.04),
                          ("macedonia", 0.04)],
        "random": 0.10
    },
    "greenland": {
        "national": 0.79,
        "international": [("denmark", 0.05), ("iceland", 0.05), ("uk", 0.05), ("norway", 0.05)],
        "random": 0.01
    },
    "guernsey": {
        "national": 0.75,
        "international": [("uk", 0.12), ("france", 0.08), ("ireland", 0.04)],
        "random": 0.01,
    },
    "iceland": {
        "national": 0.85,
        "international": [("uk", 0.08), ("norway", 0.03), ("faroe", 0.03)],
        "random": 0.01
    },
    "ireland": {
        "national": 0.60,
        "international": [("uk", 0.07), ("poland", 0.05), ("germany", 0.03), ("netherlands", 0.03), ("france", 0.03),
                          ("belgium", 0.03), ("lithuania", 0.02), ("romania", 0.02), ("hungary", 0.02)],
        "random": 0.10,
    },
    "iom": {
        "national": 0.75,
        "international": [("uk", 0.15), ("ireland", 0.09)],
        "random": 0.01
    },
    "jersey": {
        "national": 0.75,
        "international": [("uk", 0.12), ("france", 0.08), ("ireland", 0.04)],
        "random": 0.01,
    },
    "liecht": {
        "national": 0.60,
        "international": [("switzerland", 0.06), ("germany", 0.065), ("poland", 0.065), ("italy", 0.05),
                          ("austria", 0.01), ("slovakia", 0.01),
                          ("france", 0.01), ("netherlands", 0.01), ("hungary", 0.01), ("lithuania", 0.01)],
        "random": 0.10,
    },
    "malta": {
        "national": 0.80,
        "international": [("italy", 0.18)],
        "random": 0.02,
    },
    "moldova": {
        "national": 0.60,
        "international": [("romania", 0.08), ("ukraine", 0.08), ("turkey", 0.06), ("poland", 0.05), ("hungary", 0.04),
                          ("serbia", 0.03), ("bulgaria", 0.025), ("russia", 0.025)],
        "random": 0.01

    },
    "nireland": {
        "national": 0.70,
        "international": [("uk", 0.05), ("ireland", 0.04), ("poland", 0.04), ("germany", 0.03), ("iom", 0.02),
                          ("netherlands", 0.02), ("france", 0.02), ("belgium", 0.02), ("lithuania", 0.02),
                          ("romania", 0.015), ("hungary", 0.015)],
        "random": 0.01
    },
    "sanmarino": {
        "national": 0.60,
        "international": [("italy", 0.06), ("poland", 0.05), ("romania", 0.035), ("france", 0.035), ("lithuania", 0.025),
                          ("germany", 0.025), ("slovenia", 0.025), ("austria", 0.025), ("bulgaria", 0.02),
                          ("slovakia", 0.02), ("switzerland", 0.01)],
        "random": 0.07
    },
    "svalbard": {
        "national": 0.80,
        "international": [("norway", 0.10), ("russia", 0.09)],
        "random": 0.01
    },
    "ukraine": {
        "national": 0.80,
        "international": [("poland", 0.03), ("belarus", 0.025), ("moldova", 0.02), ("russia", 0.025), ("slovakia", 0.02),
                          ("hungary", 0.02), ("romania", 0.03), ("turkey", 0.02)],
        "random": 0.01
    },

}

rhs_driver_countries = [
    "gb", "cy", "gbg", "gbm", "irl", "m", "gbj", "gb_"
]
