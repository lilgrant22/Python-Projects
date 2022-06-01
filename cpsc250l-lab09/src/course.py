
class Course:

    def __init__(self, crn_name, std_dev, test_avg, quiz_avg, project_avg, course_avg):
        self.crn_name = crn_name
        self.std_dev = std_dev
        self.test_avg = test_avg
        self.quiz_avg = quiz_avg
        self.project_avg = project_avg
        self.course_avg = course_avg

    def __str__(self):
        return "CRN: {}, Standard Deviation: {}, Test Average: {}, Quiz Average: {}, Project Average: {}, Course Average: {}".format(self.crn_name, self.std_dev, self.test_avg, self.quiz_avg, self.project_avg, self.course_avg)