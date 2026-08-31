class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        Student_count = Counter(students)
        for s in sandwiches :
            if Student_count[s] > 0 :
                Student_count[s] -=1 
            else :
                break
        return sum(Student_count.values())
        