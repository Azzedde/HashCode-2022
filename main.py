def main():
    # arik()
    # ramon()
    # alicia()
    michael()
    pass


def nextProject(
    projects,
    currentDay,
    contributors,
):
    bestScore = 0
    bestProject = ""
    reservedContribs = []
    for name, project in projects.items():
        # check if we can do project at all, skip if not
        workingContribs = canBeDone(project, contributors)
        if len(workingContribs) == 0:
            # print(name, "can not be done")
            continue
        # calculate score
        score = project["score"] - max(
            0, ((currentDay + project["len"]) - project["best"])
        )
        if score > bestScore:
            bestProject = name
            bestScore = score
            reservedContribs = workingContribs

    return [bestProject, reservedContribs]


def canBeDone(project, contributors):
    reservedContributors = {}
    for skillName, level in project["roles"].items():
        found = False
        for contribName, conributerSkills in contributors.items():
            if (
                skillName in conributerSkills
                and conributerSkills[skillName] >= level
                and not contribName in reservedContributors
            ):
                reservedContributors[contribName] = {
                    "skills": conributerSkills,
                    "used": skillName,
                }
                found = True
                break

        if not found:
            return {}

    return reservedContributors


def parse(filename):
    contributers = {}
    projects = {}

    with open(filename) as file:
        lineIndex = 0
        lines = [line.rstrip() for line in file]

        header = lines[lineIndex]
        lineIndex = lineIndex + 1

        numContribs, numProjects = header.split()
        for n in range(0, int(numContribs)):
            (personName, skillCount) = lines[lineIndex].split()
            lineIndex = lineIndex + 1

            skills = {}

            for s in range(0, int(skillCount)):
                (skill, skillLevel) = lines[lineIndex].split()
                lineIndex = lineIndex + 1

                skills[skill] = int(skillLevel)

            contributers[personName] = skills

        for p in range(0, int(numProjects)):
            (projectName, length, score, best, roleCount) = lines[lineIndex].split()
            lineIndex = lineIndex + 1

            roles = {}

            for r in range(0, int(roleCount)):
                (role, roleLevel) = lines[lineIndex].split()
                lineIndex = lineIndex + 1

                roles[role] = int(roleLevel)

            projects[projectName] = {
                "len": int(length),
                "score": int(score),
                "best": int(best),
                "roles": roles,
            }

        return [contributers, projects]


def write_results(results):
    with open("results.txt", "w") as fil:
        fil.write(f"{str(len(results))}\n")
        for ele in results:
            proj = list(ele.keys())[0]
            members = list(ele.values())[0]
            fil.write(f"{proj}\n")
            fil.write(f'{" ".join(members)}\n')


def arik():
    print("lolchopf")
    pass


def ramon():
    print("ron weasley")
    pass


def alicia():
    print("Hermine")
    pass


def applyContributersToProject(contributes, project):

    pass


def michael():
    # {projectName: {contributes, endDay}}
    runningProjects = {}

    # ???
    openProjects = {}

    doneProjects = []

    (contributers, projects) = parse("./input_data/a_an_example.in.txt")
    # print(contributers, projects)

    openProjects = projects.copy()
    availableContributers = contributers.copy()

    currentDay = 0
    while len(openProjects) > 0 and currentDay < 100:
        # Is a project finished?
        for (runningProjectName, runningProjectValues) in runningProjects.items():
            if currentDay == runningProjectValues["endDay"]:
                # Level up
                cleanedContribs = {}
                for (contribName, something) in runningProjectValues[
                    "contributers"
                ].items():
                    skills = something["skills"]
                    skillToUpdate = something["used"]
                    skills[skillToUpdate] = skills[skillToUpdate] + 1
                    cleanedContribs[contribName] = skills

                # if yes, add contributers back to be available
                availableContributers = {
                    **availableContributers,
                    **cleanedContribs,
                }
                doneProjects.append(
                    {runningProjectName: runningProjectValues["contributers"]}
                )

        # Find Project
        (projectName, usedContributers) = nextProject(
            openProjects, currentDay, availableContributers
        )

        # No project to work on, we go to the next day
        if projectName is None or len(projectName) == 0:
            currentDay = currentDay + 1
            continue

        # We start working on the project
        runningProjects[projectName] = {
            "contributers": usedContributers,
            "endDay": openProjects[projectName]["len"],
        }
        openProjects.pop(projectName)
        for contribName in usedContributers.keys():
            availableContributers.pop(contribName)

        print("ALL")
        print(projects)

        print("OPEN")
        print(openProjects)

        print("RUNNING")
        print(runningProjects)

    write_results(doneProjects)

    # newContributes = applyContributersToProject(contributers, bestProject)

    # if newContributes is not empty:
    #     # TODO: Remove project from projcts

    #     nextBestProject = nextProject(projects, 0, newContributes)
    # else:
    #     # TODO: move days forword
    #     pass

    pass


if __name__ == "__main__":
    main()
