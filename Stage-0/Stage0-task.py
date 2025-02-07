""" dictionary 
    with inforamtion 
    of each team member 
"""
info = {
    "Names": "Teodora, Alvin, Bilal, Tanson, Natt",
    "Slack usernames" : "Teodora, Alvin, bilal ashraf, K.Tanson, Natt",
    "Emails" : "teodoradespotovski@gmail.com, alvinobande123@gmail.com, eclecticbilalashraf@gmail.com, Kelvins.tanson@gmail.com, im.nathn@gmail.com",
    "Hobbies" : "Cooking, Music, Mixed Martial Arts, Graphic design, Read manga",
    "Countries" : "Serbia, Nigerian, Germany, Ghana, Australia",
    "Disciplines" : "Biochemistry, Medical Biotechnology, Bioinformatics, Medical Biochemistry and Molecular Biology, Biotechnology",
    "Preferred programming language" : "Python, Python, Python, R, Python"
} 

""" Creating variables for each value in dictionary. The .split  was used divide the string in diffine place (", ")
(important if we want to print one member of the group): """
Names = info["Names"].split(", ")
Usernames = info["Slack usernames"].split(", ")
Emails = info["Emails"].split(", ")
Hobbies = info["Hobbies"].split(", ")
Countries = info["Countries"].split(", ")
Disciplines = info["Disciplines"].split(", ")
Preffered_programming_language = info["Preferred programming language"].split(", ")

# Print all team members information, using .join to return the one string (beacuse .split was used above):
print(f"""Team members information: 
 Names: {(", ").join(Names)} 
 Usernames: {(", ").join(Usernames)} 
 Emails: {(", ").join(Emails)} 
 Hobbies: {(", ").join(Hobbies)} 
 Countries: {(", ").join(Countries)} 
 Disciplines: {(", ").join(Disciplines)} 
 Preffered programming langugae: {(", ").join(Preffered_programming_language)}""")

# Print information for only one team member, that is why the .split was used before:
print(f"""\nInformation for one team member: 
 Name: {Names[0]}
 Username: {Usernames[0]}
 Email: {Emails[0]} 
 Hobby: {Hobbies[0]}
 Country: {Countries[0]}
 Discipline: {Disciplines[0]} 
 Preffered_programming_language: {Preffered_programming_language[0]}""")
 # Note: If you want to print information for all other group memembrs you can just simply change [0] to [1]-[4]

# Find the code on: https://github.com/teodorades/hackbio-biocoding-internship/tree/main 