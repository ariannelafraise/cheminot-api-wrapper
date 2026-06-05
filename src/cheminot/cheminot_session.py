import requests

class CheminotSession():
    """
    Wrapper for interacting with Cheminot's API

    Parameters
    ----------
    auth_token : str
        Bearer authentication token used for API requests.
    user_agent : str
        User-Agent header sent with each request.
    student_id : str
    program_id : str | int
    semester_id : str
    base_url : str
        Base URL of the API
    """
        
    def __init__(self, auth_token, user_agent, student_id, program_id, semester_id, base_url):
        self.AUTH_TOKEN = auth_token
        self.USER_AGENT = user_agent
        self.STUDENT_ID = student_id
        self.PROGRAM_ID = program_id
        self.SEMESTER_ID = semester_id
        self.BASE_URL = base_url

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.AUTH_TOKEN}",
            "User-Agent": self.USER_AGENT
        })

    def get_path_courses(self):
        """
        Retrieve the program's path's courses.
        """
        return self.session.get(
            f"{self.BASE_URL}/api" +
            f"/Etudiant/{self.STUDENT_ID}" +
            f"/programme/{self.PROGRAM_ID}" +
            f"/cheminement?session={self.SEMESTER_ID}"
        )

    def get_course_available_groups(self, course_id):
        """
        Get available groups for a specific course.

        Parameters
        ----------
        course_id : str
        """
        return self.session.get(
            f"{self.BASE_URL}/api" +
            f"/CoursOfferts/{self.STUDENT_ID}" +
            f"/programme/{self.PROGRAM_ID}" +
            f"/cours/{course_id}" +
            f"?sessionInscr={self.SEMESTER_ID}"
        )
        
    def register_to_course(self, course_id, group_number, concentration):
        """
        Register to a course's group.

        Parameters
        ----------
        course_id : str
        group_number : str
        concentration : str
        """
        return self.session.post(
            f"{self.BASE_URL}/api/horaire" +
            f"/etudiant/{self.STUDENT_ID}" +
            f"/programme/{self.PROGRAM_ID}" +
            f"/horaire/add?session={self.SEMESTER_ID}&concentration={concentration}",
            json = {
                "Sigle": course_id,
                "Groupe": group_number
            },
            headers = {
                "Content-Type": "application/json"
            }
        )

    def unregister_from_course(self, course_id):
        """
        Unregister from a course.

        Parameters
        ----------
        course_id : str
        """
        return self.session.delete(
            f"{self.BASE_URL}/api/horaire" +
            f"/etudiant/{self.STUDENT_ID}" +
            f"/programme/{self.PROGRAM_ID}" +
            f"/session/{self.SEMESTER_ID}" +
            f"/cours/{course_id}"
        )

    def get_schedule(self):
        """
        Retrieve the current schedule.
        """
        return self.session.get(
            f"{self.BASE_URL}/api/horaire" +
            f"/etudiant/{self.STUDENT_ID}" +
            f"/programme/{self.PROGRAM_ID}" +
            f"/horaire?session={self.SEMESTER_ID}"
        )

    def confirm_schedule(self):
        """
        Confirm/save the current schedule.
        """
        return self.session.put(
            f"{self.BASE_URL}/api/horaire" +
            f"/etudiant/{self.STUDENT_ID}" +
            "/confirmation-horaire",
            json = {
                "SessionInscr": self.SEMESTER_ID,
                "ProgrammeId": str(self.PROGRAM_ID)
            },
            headers = {
                "Content-Type": "application/json"
            }
        )
