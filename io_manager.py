from collections import Counter
from base_class import Contributor, Project, Solution


def read_input(character):
    baseclasses = []
    with open(f"data/{character}.in.txt") as f:
        for i, line in enumerate(f):
            continue
            BaseClass()
    return


def write_output(solution: Solution, character:str):
    with open(f"output/{character}.out.txt", "w") as f:
        f.write(f"{len(solution.list_of_projects)}\n")
        for project, assignment in zip(solution.list_of_projects, solution.proj_to_skill_to_contributor.values()):
            f.writelines(project+"\n")
            f.writelines(" ".join(list(assignment.values()))+"\n")


def read_input(file):
    contributors = dict()
    projects = dict()
    
    with open(f"data/{file}.in.txt") as f:
        num_contributors, num_projects = list(map(int, f.readline().split(' ')))

        # parse contributor skills
        for _ in range(num_contributors):
            name, num_skills = f.readline().split(' ')
            num_skills = int(num_skills)
            skills = Counter()

            for _ in range(num_skills):
                skill_name, level = f.readline().split(' ')
                skills[skill_name] = int(level)

            contributors[name] = Contributor(name, skills)
        
        # parse projects
        for p in range(num_projects):
            proj_name, duration, score, last_day, num_contributors = f.readline().split(' ')
            duration = int(duration)
            score = int(score)
            last_day = int(last_day)
            num_contributors = int(num_contributors)

            skills_required = dict()
            for _ in range(num_contributors):
                skill_name, level = f.readline().split(' ')
                level = int(level)
                skills_required[skill_name] = level

            projects[proj_name] = Project(proj_name, duration, score, last_day, num_contributors, skills_required)

    return contributors, projects




        


        

