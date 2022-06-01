
class GradeBook:

    def __init__(self, id, quiz_avg, test_avg, project_avg, course_avg):
        self.id = id
        self.quiz_avg = quiz_avg
        self.test_avg = test_avg
        self.project_avg = project_avg
        self.course_avg = course_avg

    def __str__(self):
        return "id: {}, Quiz Average: {}, Test Average: {}, Project Average: {}, Course Average {}".format(self.id, self.quiz_avg, self.test_avg, self.project_avg, self.course_avg)
