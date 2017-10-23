def lang_genoeg(lengte):
    if lengte >= 120:

        return "Je bent lang genoeg"

    else:
        return "Je bent te kort"

lengte = eval(input("Vul je lengte in cm in:"))
print(lang_genoeg(lengte))




