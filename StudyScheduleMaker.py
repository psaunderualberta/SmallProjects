class Course():
    def __init__(self, name):
        self.name = name
        self.topics = []
        self.examDate = ''
        self.topicOccurrence = 0
    
    def addTopics(self, topicsList):
        for topic in topicsList:
            self.topics.append(topic)
        
    def setExamDate(self, date):
        self.examDate = date

def main():
    
    print("Welcome to the Study Schedule Maker!")
    print("You just need to enter your classes, exam dates,\n" + 
        "and current date, and the program will then"
        "generate a study schedule just for you!\n" +
        "Note: Please separeate your inputs with spaces unless instructed otherwise.")
    print("-" * 50)
    courseList = input("What are you classes? (separate each class by a space)\n").split(' ')
    print("\n")
    for i, course in enumerate(courseList):
        print("COURSE: " + course)
        courseList[i] = Course(course)
        topics = input("What topics would you like to study in " + str(course) + "?\n")
        courseList[i].addTopics(topics)
        examDate = input("When is your exam for " + str(course) + "? (YYYY/MM/DD)\n")
        courseList[i].setExamDate(examDate)
        print("\n")
    date = input("Finally, what is today's date? (YYYY/MM/DD)\n")
    print("Thanks so much!")



main()