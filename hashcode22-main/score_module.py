from io_manager import read_input


def get_score(solution, projects, contributors):
    day = 0
    score = 0

    days_to_complete = {p.name: p.length for p in projects.values()}
    assigned = {c.name: None for c in contributors.values()}

    while len(days_to_complete):
        to_be_unassigned = []

        for p in solution.list_of_projects:
            if p in days_to_complete:

                all_c_available = True
                for c in solution.proj_to_skill_to_contributor[p].values():
                    if assigned[c] is None: # required contributor is free
                        assigned[c] = p
                    elif assigned[c] != p: # required contributor is assigned on other project
                        all_c_available = False

                if all_c_available:
                    days_to_complete[p] -= 1
                    if days_to_complete[p] == 0: # project finished
                        p_penalty = max(0, day + 1 - projects[p].last_day)
                        p_score = max(0, projects[p].score - p_penalty)
                        score += p_score
                        del days_to_complete[p]
                        to_be_unassigned += [c for c in assigned if assigned[c] == p]

        for c in to_be_unassigned:
            assigned[c] = None
        day += 1

    return score


# if __name__ == "__main__":
#     solution = Solution(
#         list_of_projects=['WebServer', 'WebChat', 'Logging'],
#         proj_to_skill_to_contributor={
#             'WebServer': {'HTML': 'Bob', 'C++': 'Anna'},
#             'WebChat': {'Python': 'Maria', 'HTML': 'Bob'},
#             'Logging': {'C++': 'Anna'},
#         }
#     )
#     contributors, projects = read_input("a")
#     score = get_score(solution, projects, contributors)
#     print(score)
