def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff", 
                    "Slytherin", 
                    "Ravenclaw", 
                    "Gryffindor", 
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])
    
    """

    houses = set()

    # Code goes here
    datafile = open(filename)
    for line in datafile:
        cohort_data = line.split('|')
        if cohort_data[2] != '':
            houses.add(cohort_data[2]) 


    return houses

#print unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]
    
    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    # Code goes here
    datafile = open(filename)
    for line in datafile:
        line = line.rstrip('\n')
        cohort_data = line.split('|')
        student_name = cohort_data[0] + " " + cohort_data[1]
        if cohort_data[4] == "Spring 2015":
            spring_15.append(student_name)
        elif cohort_data[4] == "Summer 2015":
            summer_15.append(student_name)
        elif cohort_data[4] == "Winter 2015":
            winter_15.append(student_name)
        elif cohort_data[1] in ["Bryant", "Karl", "Lefevre", "Mahnken", "McClure", "Wiedl"]:
            tas.append(student_name)
    all_students.append(winter_15)
    all_students.append(spring_15)
    all_students.append(summer_15)
    all_students.append(tas)

    return all_students
#print sort_by_cohort("cohort_data.txt")

def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff, 
                        gryffindor, 
                        ravenclaw, 
                        slytherin, 
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas 
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []

    # Code goes here
    datafile = open(filename)
    for line in datafile:
        line = line.rstrip('\n')
        cohort_data = line.split('|')
        student_name = cohort_data[0] + " " + cohort_data[1]
        if cohort_data[1] in ["Bryant", "Karl", "Lefevre", "Mahnken", "McClure", "Wiedl"]:
            tas.append(student_name)
        elif cohort_data[2] == "Gryffindor":
            gryffindor.append(student_name)
        elif cohort_data[2] == "Hufflepuff":
            hufflepuff.append(student_name)
        elif cohort_data[2] == "Slytherin":
            slytherin.append(student_name)
        elif cohort_data[2] == "Dumbledore's Army":
            dumbledores_army.append(student_name)
        elif cohort_data[2] == "Order of the Phoenix":
            order_of_the_phoenix.append(student_name)
        elif cohort_data[2] == "Ravenclaw":
            ravenclaw.append(student_name)

    
    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(dumbledores_army)
    all_students.append(order_of_the_phoenix)
    all_students.append(ravenclaw)
    all_students.append(tas)

    return all_students

   
#print students_by_house("cohort_data.txt")



def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """
    tuple_list = []
    datafile = open(filename)
    for line in datafile:
        line = line.rstrip('\n')
        student_info = line.split('|')
        student_name = student_info[0] + " " + student_info[1]
        student_info[:2] = [student_name]
        student_info = tuple(student_info)
        tuple_list.append(student_info)

    

    # Code goes here

    return tuple_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here
    all_student_info = all_students_tuple_list("cohort_data.txt")
    for student in all_student_info:
        if student[0] == student_list:
            return student[3]
    
    return "Student not found."

#print find_cohort_by_student_name("Lauren Orencio")
##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts. 
    Uses set operations (set math) to create a set of these names. 
    NOTE: Do not include staff -- or do, if you want a greater challenge. 

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here
    group_students_by_cohort = sort_by_cohort(filename)
    print group_students_by_cohort
    for cohort in group_students_by_cohort:
        cohort_data = set(cohort)
        print cohort_data
        for student in cohort_data:
            cohort_data.add(student[0].split(' ')[0])
        #print cohort_data
     

    return duplicate_names

find_name_duplicates("cohort_data.txt")
def find_house_members_by_student_name(student_list):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here
    student_info = all_students_tuple_list("cohort.txt")
    cohort, house = student_info[3], student_info[1]
    winter = student_info[0]
    return

