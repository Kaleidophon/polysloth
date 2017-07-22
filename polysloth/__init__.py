"""
Main module defining the main class used to run the projects' contents.
"""

__version__ = "0.1.0"

# EXT
import todoist

# PROJECT
from polysloth.jobs import JobSpecification


class PolySloth:
    """
    Main PolySloth class. Initialize an object for this class and pass the necessary arguments,
    afterwords execute the `run()` function.
    """
    user = None
    todoist_projects = []

    def __init__(self, todoist_email, todoist_secret, job_specifications, **additional_arguments):
        assert isinstance(todoist_email, str)
        assert isinstance(todoist_secret, str)
        assert isinstance(job_specifications, dict)
        self._job_specifications = job_specifications

        # Initialise Todoist API
        self.todoist_api = todoist.TodoistAPI()
        self.login_todoist_user(todoist_email, todoist_secret)

        # Initialize jobs
        self.job_specifications = {}
        for project_name, job_specifications in self.todoist_projects.items():
            job_specification_dict = self._job_specifications[project_name]
            job_specification_dict.update({
                "todoist_project_name": project_name,
                "todoist_project_id": self.todoist_projects[project_name]["id"]
            })
            self.job_specifications[project_name] = JobSpecification(**job_specification_dict)

    def login_todoist_user(self, todoist_email, todoist_secret):
        # Login user and get token
        self.user = self.todoist_api.user.login(todoist_email, todoist_secret)
        response = self.todoist_api.sync()

        self.todoist_projects = {
            project["name"]: project
            for project in response["projects"] if project["name"] in self._job_specifications
        }
