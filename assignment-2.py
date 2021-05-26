"""
Day 3
Turkish Ai Hub - Assignment 2
@author: Mehmet Baran Munar
"""



cv_1 = {
    "Name":"David",
    "Surname":"Gibbons",
    "Age":"25",
    "Education":"Aston University, BSc Computer Science",
    "Skills":["Python Expert","C Expert","Javascript Expert"],
    "Hobbies":["Reading sci-fi books.","Solving puzzles."],
    "Mobile": 17933168158
    }

cv_2 =  {
    "Name":"Emma",
    "Surname":"Red",
    "Age":24,
    "Education":"Yale University, BSc Computer Science",
    "Skills":["C++ Expert","C# Expert","Python Expert"],
    "Hobbies":["Listening jazz music.","Meet with friends."],
    "Mobile": 48645424135
    }

cv_3 =  {
    "Name":"Robert",
    "Surname":"Ne DirO",
    "Age":22,
    "Education":"Georgia University, BSc Computer Science",
    "Skills":["PHP Expert","Ruby Expert","Javascript Expert"],
    "Hobbies":["Playing guitar.","Playing chess."],
    "Mobile": 85484534545
    }

cv_4 =  {
    "Name":"Dun",
    "Surname":"Kirk",
    "Age":28,
    "Education":"Harvard University, BSc Computer Science",
    "Skills":["Python Expert","C Expert",],
    "Hobbies":["Swimming","Trekking"],
    "Mobile": 65465448745
    }

cv_5 =  {
    "Name":"Leonardo",
    "Surname":"Cidaprio",
    "Age":27,
    "Education":"Harran University, BSc Computer Science",
    "Skills":["GO Expert","Ruby Expert","R Expert"],
    "Hobbies":["Riding horse.","Playing video games."],
    "Mobile": 68771687453
    }

cv = [cv_1, cv_2, cv_3, cv_4, cv_5]

for c in cv:
    print(" ")
    for k, v in c.items():
        print(k,"-",v)