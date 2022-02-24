import typing as t
from dataclasses import dataclass, field
from itertools import combinations, permutations

@dataclass
class Contributor:
    name: str
    skills: dict 

    def improve(self, skill, lvl):
        if lvl >= self.skills[skill]:
            self.skills[skill] += 1

    


@dataclass
class Project:
    name: str
    length: int
    score: int
    last_day: int
    num_contributors: int
    skills_required: dict

@dataclass
class Solution:
    list_of_projects: list = field(default_factory=list)
    proj_to_skill_to_contributor: dict = field(default_factory=dict)


def all_possible_assignments(project: Project, contributors: t.List[Contributor], max_tries:int=100):
    tries = 0
    for subset in combinations(contributors, project.num_contributors):
        for permutation in permutations(subset):
            possible_assignment = dict()
            for skill, contributor in zip(project.skills_required.keys(), permutation):
                possible_assignment[skill] = contributor
            if is_valid_assignment(project, possible_assignment):
                yield possible_assignment
            tries+=1
            if tries >= max_tries:
                break
        if tries >= max_tries:
            break
    


def is_valid_assignment(
    constraints: Project,
    assignments: t.Dict[str, Contributor]
) -> bool:

    if constraints.skills_required.keys() != assignments.keys():
        False
    
    mentoring = set()

    for skill_name, contributor in assignments.items():
        # Get the level from the constraints
        required_level = constraints.skills_required[skill_name]
        contributor_level = contributor.skills[skill_name]
        if contributor_level == required_level - 1:
            mentoring.add(skill_name)
        elif contributor_level < required_level:
            return False
    
    for skill_name in mentoring:
        required_level = constraints.skills_required[skill_name]
        found = False
        for contributor in assignments.values():
            contributor_level = contributor.skills[skill_name]
            if contributor_level >= required_level:
                found = True
                continue
        if not found:
            return False 

    return True

if __name__ == "__main__":
    example_solution = [
        {
            "Logging": {
                "C++": "Anna",
            },
        },
        {
            "WebServer": {
                "HTML": "Anna",
                "C++": "Bob",
            }
        }, # project 2
        {
            "WebChat": {
                "Python": "Anna",
                "HTML": "Bob",
            }
        }, # project 3
    ]
    example_mapping = dict()
    example_projects = []
    for proj in example_solution:
        example_mapping.update(proj)
        example_projects.append(list(proj.keys())[0])

    example_sol = Solution(example_projects, example_mapping)
    
    