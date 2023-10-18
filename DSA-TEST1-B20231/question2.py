catholic_martyrs = ["Achileo Kiwanuka", "Adolphus Ludigo-Mukasa", "Ambrosius Kibuuka",
                    "Anatoli Kiriggwajjo", "Andrew Kaggwa", "Antanansio Bazzekuketta",
                    "Bruno Sserunkuuma", "Charles Lwanga", "Denis Ssebuggwawo Wasswa", "Gonzaga Gonza",
                    "Gyavira Musoke", "James Buuzaabalyaawo", "John Maria Muzeeyi", "Joseph Mukasa",
                    "Kizito", "Lukka Baanabakintu", "Matiya Mulumba", "Mbaga Tuzinde", "Mugagga Lubowa",
                    "Mukasa Kiriwawanvu", "Nowa Mawaggali", "Ponsiano Ngondwe"]

anglican_martyrs = ["Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza", "George Kizza", "James Hannington", "Janani Luwum",
                    "Joseph Balikuddembe", "Kizito", "Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu",
                    "Robert Munyagayirwa", "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa",
                    "Yosefu Lugalama", "Yowana Kitaka", "Yowana Maria Mukasa"]


catholic_martyrs = list(set(catholic_martyrs))
anglican_martyrs = list(set(anglican_martyrs))


def martyr_group(name):
    if name in catholic_martyrs:
        return name + " belongs to the Catholic Martyrs"
    elif name in anglican_martyrs:
        return name + " belongs to the Anglican Martyrs"
    else:
        return name + " is not present in any of the lists"


kizito_group = martyr_group("Kizito")
print("Group of Kizito:", kizito_group) 


def is_martyr_present(name):
    return name in catholic_martyrs and name in anglican_martyrs
