data = {
    "1": {
        "Total": 340, "Obtained": 245.14, "GPA": 3.48, "Percentage": 72.10,
        "Subjects": [
            ["ENG-321", "FUNCTIONAL ENGLISH", 43.26, 60, "B"],
            ["ISL-321", "ISLAMIC STUDIES", 28.84, 40, "B"],
            ["MTH-301", "CALCULUS-I", 43.26, 60, "B"],
            ["MTH-303", "DISCRETE MATHEMATICS", 43.26, 60, "B"],
            ["PHY-325", "FUNDAMENTALS OF ELEC & MAG", 43.26, 60, "B"],
            ["STA-322", "INTRO TO STAT THEORY-I", 43.26, 60, "B"]
        ]
    },
    "2": {
        "Total": 340, "Obtained": 238.56, "GPA": 3.29, "Percentage": 70.16,
        "Subjects": [
            ["ENG-322", "ENGLISH COMPREHENSION", 36.00, 60, "C"],
            ["MTH-302", "CALCULUS-II", 48.48, 60, "A"],
            ["MTH-304", "LINEAR ALGEBRA", 50.40, 60, "A"],
            ["PHY-425", "HEAT AND THERMODYNAMICS", 47.52, 60, "B"],
            ["PST-321", "PAKISTAN STUDIES", 21.12, 40, "C"],
            ["STA-323", "INTRO TO STAT THEORY-II", 35.04, 60, "C"]
        ]
    },
    "3": {
        "Total": 360, "Obtained": 240.00, "GPA": 3.05, "Percentage": 66.67,
        "Subjects": [
            ["CSI-321", "INTRO TO COMPUTING", 51.20, 60, "A"],
            ["ENG-421", "COMMUNICATION SKILLS", 40.00, 60, "B"],
            ["MTH-401", "CALCULUS-III", 33.60, 60, "C"],
            ["MTH-403", "MECHANICS-I", 38.40, 60, "C"],
            ["MTH-405", "DIFFERENTIAL EQUATIONS-I", 40.80, 60, "B"],
            ["MTH-407", "NUMBER THEORY", 36.00, 60, "C"]
        ]
    },
    "4": {
        "Total": 360, "Obtained": 245.28, "GPA": 3.08, "Percentage": 66.67,
        "Subjects": [
            ["MTH-402", "AFFINE & EUCLIDEAN GEOM", 34.40, 60, "C"],
            ["MTH-404", "MECHANICS-II", 43.20, 60, "B"],
            ["MTH-406", "DIFFERENTIAL EQUATIONS-II", 35.20, 60, "C"],
            ["MTH-408", "COMBINATORICS", 38.40, 60, "C"],
            ["MTH-410", "C++", 39.20, 60, "B"],
            ["PSY-422", "INTRO TO PSYCHOLOGY", 49.60, 60, "A"]
        ]
    },
    "5": {
        "Total": 360, "Obtained": 245.28, "GPA": 3.21, "Percentage": 68.13,
        "Subjects": [
            ["MTH-501", "REAL ANALYSIS-I", 44.16, 60, "B"],
            ["MTH-503", "COMPLEX ANALYSIS-I", 41.28, 60, "B"],
            ["MTH-505", "ALGEBRA-I", 45.60, 60, "B"],
            ["MTH-507", "VECTOR & TENSOR ANALYSIS", 32.16, 60, "C"],
            ["MTH-509", "POINT SET TOPOLOGY", 44.64, 60, "B"],
            ["MTH-511", "DIFFERENTIAL GEOMETRY", 37.44, 60, "C"]
        ]
    },
    "6": {
        "Total": 360, "Obtained": 305.68, "GPA": 3.96, "Percentage": 84.91,
        "Subjects": [
            ["MTH-502", "REAL ANALYSIS-II", 48.48, 60, "A"],
            ["MTH-504", "COMPLEX ANALYSIS-II", 48.48, 60, "A"],
            ["MTH-506", "ALGEBRA-II", 46.08, 60, "B"],
            ["MTH-508", "MECHANICS", 55.68, 60, "A"],
            ["MTH-510", "FUNCTIONAL ANALYSIS", 51.84, 60, "A"],
            ["MTH-512", "MATHEMATICAL METHODS", 55.20, 60, "A"]
        ]
    }
}

print("--- TRANSCRIPT SYSTEM LOADED ---")
print("Options: 1, 2, 3, 4, 5, 6, ALL, SUB")
choice = input("Enter your choice: ").strip().upper()
if choice == "ALL":
    grand_obt = 0
    grand_tot = 0
    for i in range(1, 7):
        sid = str(i)
        s = data[sid]
        print("\n=== SEMESTER " + sid + " ===")
        for sub in s["Subjects"]:
            print(sub[0] + " | " + sub[1] + " | " + str(sub[2]) + "/" + str(sub[3]) + " | Grade: " + sub[4])
        print("Obtained: " + str(s["Obtained"]) + " | GPA: " + str(s["GPA"]))
        grand_obt += s["Obtained"]
        grand_tot += s["Total"]
    print("\n" + "*"*30)
    print("GRAND TOTAL: " + str(round(grand_obt, 2)) + "/" + str(grand_tot))
    print("PERCENTAGE: " + str(round((grand_obt/grand_tot)*100, 2)) + "%")
    print("*"*30)
elif choice in data:
    s = data[choice]
    print("\n--- SEMESTER " + choice + " DETAILS ---")
    for sub in s["Subjects"]:
        print(sub[0] + " | " + sub[1] + " | " + str(sub[2]) + "/" + str(sub[3]) + " | Grade: " + sub[4])
    print("-" * 30)
    print("Obtained: " + str(s["Obtained"]))
    print("Total: " + str(s["Total"]))
    print("GPA: " + str(s["GPA"]))
    print("Percentage: " + str(s["Percentage"]) + "%")
elif choice == "SUB":
    code = input("Enter Subject Code: ").strip().upper()
    found = False
    
    for sem in data:
        for sub in data[sem]["Subjects"]:
            if sub[0] == code:
                print("\n--- SUBJECT RESULT FOUND ---")
                print("Semester: " + sem)
                print("Code: " + sub[0])
                print("Title: " + sub[1])
                print("Marks: " + str(sub[2]) + "/" + str(sub[3]))
                print("Grade: " + sub[4])
                found = True
                break
        if found:
            break
    
    if not found:
        print("Subject code not found.")

else:
    print("Error: Please enter 1-6, ALL or SUB.")
