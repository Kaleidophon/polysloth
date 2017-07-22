"""
Module defining everything regarding PolySloth jobs.
"""


class JobSpecification:
    """
    Specify all the relevant parameters for a PolySloth job, fall back to defaults if necessary.
    """
    def __init__(self, todoist_project_name, todoist_project_id, source_language, target_language, **additional_args):
        self.todoist_project_name = todoist_project_name
        self.todoist_project_id = todoist_project_id
        self.source_language = source_language
        self.target_language = target_language
        self.enable_lookups = additional_args.get("enable_lookups", True)
        self.allow_ignores = additional_args.get("allow_ignores", True)


class Job:
    """
    PolySloth job performing requests to Todoist and PONS API.
    """
    # TODO (Implement) [DU 23.07.17]
    pass
