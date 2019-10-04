class Course():
    def __init__(self, name):
        self.name = name
        self.topics = []
        self.examDate = ''
    
    def self.addTopics(self, topicsList):
        for topic in topicsList:
            self.topics.appemd(topic)
        
    def self.setExamDate(self, date):
        self.examDate = date

def main():
    
    print("Welcome to the Study Schedule Maker!")
    print("You just need to enter your classes, exam dates\n" + 
        "and current date, and the program will then generate a study\n" + 
        "schedule just for you!\n" +
        "Note: Please separeate your inputs with spaces unless instructed otherwise.")
    print("-" * 50)
    courseList = input("What are you classes? (separate each class by a space)\n").split(' ')
    for course, i in enumerate(courseList):
        courseList[i] = Course(course)
        topics = input("What topics would you like to study in",str(course)),"?")
        courseList[i].addTopics(topics)
        examDate = input("When is your exam? (YYYY/MM/DD)")
        courseList[i].setExamDate(examDate)

main()