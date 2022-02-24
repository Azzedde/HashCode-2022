
from operator import attrgetter


f = open('input/b_better_start_small.in.txt',"rt")
c, p = f.readline().strip().split()
class Contirbutor:
    def __init__(self,name,skills,available):
        self.name = name
        self.skills = skills
        self.available = available

class Project:
    def __init__(self,name, time, score, ddl, nb_contrib, skills):
        self.name = name
        self.time = time
        self.score = score
        self.ddl = ddl
        self.nb_contrib = nb_contrib
        self.skills = skills

class Skill:
    def __init__(self, name, level, contributor):
        self.name = name
        self.level = level
        self.contributor = contributor

contributors=[]
for i in range(int(c)):
    name, nb_skill=f.readline().strip().split()
    skills=[]
    for j in range(int(nb_skill)):
        skill, level = f.readline().strip().split()

        skills.append(Skill(skill,int(level),None))
    contributors.append(Contirbutor(name,skills,True))

projects=[]
for i in range(int(p)):
    name, time, score, ddl, nb_contrib = f.readline().strip().split()
    skills=[]
    for j in range(int(nb_contrib)):
        skill, level = f.readline().strip().split()
        skills.append(Skill(skill,int(level),None))
    projects.append(Project(name, int(time), int(score), int(ddl), int(nb_contrib),skills))

#ShortestJobFirst:
projects.sort(key=attrgetter('ddl')) #Sorting the projects by their deadlines
days=0
for p in projects:
    days += p.time

cpt = 0

affected=[]

for p in projects:
    for c in contributors:
        for p_skill in p.skills:
            for c_skill in c.skills:
                if( p_skill.name == c_skill.name and c_skill.level >= p_skill.level):
                    affected.append(c)

completed=[]

for p in projects:
    if(p.nb_contrib == len(affected)):
        completed.append(p)

f1 = open("output.txt", "w")

f1.write(str(len(projects)-8)+"\n")
for p in projects:
    f1.write(p.name+"\n")
    for c in affected:
        f1.write(c.name+" ")
    f1.write("\n")








        


