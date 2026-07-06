from typing import TypedDict

class WorkflowState(TypedDict):

    url: str

    brd_path: str

    brd_text: str

    website: dict

    requirements: dict

    mapping: dict

    generated_tests: list

    execution_results: list

    failures: list

    report_path: str