def gemiddelde_per_student(studentencijfers):
    antw = []
    for lijst_van_een_student in studentencijfers:
        gemiddelde = sum(lijst_van_een_student) / len(lijst_van_een_student)
        antw.append(gemiddelde)

    return antw

def gemiddelde_van_alle_studenten(studentencijfers):

    antw =[]
    for lijst_van_een_student in studentencijfers:
        gemiddelde = sum(lijst_van_een_student) / len(lijst_van_een_student)
        antw.append(gemiddelde)

    return sum(antw) / len(antw)

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
