from score_module import get_score
from io_manager import read_input, write_output
from strategy import method_3 as method


for char in "abcdef":
    contributors, projects = read_input(char)
    print(f"Num contributors: {len(contributors)}")
    print(f"Num projects: {len(projects)}")

    result = method(contributors, projects)
    # score = get_score(result, projects, contributors)
    # print(f"Case {char}: {score} score \n")
    print(char)

    write_output(result, char)
