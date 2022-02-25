# HashCode-2022
Our solution for the 2022 [Google Hashcode](https://codingcompetitions.withgoogle.com/hashcode) qualification round problem with libraries and books.

<p align="center">
<img src="/images/hashcode.jpg" alt="Hashcode Logo" width="500"/>
</p>


## The problem
You are given a list of contributors, who have already mastered various skills, and a list of projects with different skill requirements. Contributors can improve their skills by completing projects and can mentor each other to work is roles in which they couldn't succeed on their own. Your task is to assign contributors to project roles that fit their qualifications and maximize the score for completed projects.

## Our first Intuition
We thinked about an OOP approach. We created classes: Project, Contributor, Skill:
```
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
```
We generated a list of contributor objects:
``` 
contributors=[]
for i in range(int(c)):
    name, nb_skill=f.readline().strip().split()
    skills=[]
    for j in range(int(nb_skill)):
        skill, level = f.readline().strip().split()

        skills.append(Skill(skill,int(level),None))
    contributors.append(Contirbutor(name,skills,True))
``` 
We generated a list of project objects:
```
projects=[]
for i in range(int(p)):
    name, time, score, ddl, nb_contrib = f.readline().strip().split()
    skills=[]
    for j in range(int(nb_contrib)):
        skill, level = f.readline().strip().split()
        skills.append(Skill(skill,int(level),None))
    projects.append(Project(name, int(time), int(score), int(ddl), int(nb_contrib),skills))
```
We ordered then the list of projects by deadlines: `projects.sort(key=attrgetter('ddl'))`
It was the first step to our ShortJobFirst Approach, after that we created a list of completed projects, then wrote the output file which contains each one of them with its contributors affected within the roles. 
```
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
```
This is what we thaught about.
It was a great experience.
Thanks to:
Hattabi Ilyes
Touami Mohamed
Mahdid Lilia
Aitsaid Azzedine Idir
