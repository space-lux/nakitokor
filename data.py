import sqlite3
from random import sample


conn=sqlite3.connect('data.db')
cur=conn.cursor()

agents=dict()
questions=dict()

class Answer():

    def __init__(self,q=None,a=0):
        self.q=q
        self.a=a
        # a étant le niveau de réponse : 1=oui, 0=na, -1=non
        # q étant l'id de la question
        
class Agent():

    def __init__(self,parent=0,name="",aId=None):
        self.name=name
        self.children=set()
        self.answers=dict()
        self.aId=aId
        self.setParent(parent)

    def __str__(self):
        if len(self.name):
            return self.name
        return "no name agent"
    
    def all_answers(self):
        ans=dict(self.answers)
        try:
            pa=self.parent.all_answers()
            for k in pa:
                if k not in ans.keys():
                    ans[k]=pa[k]
        except:
            pass
        return ans
    
    def answer_owner(self,a):
        try:
            if a in self.answers.keys():
                return self.aId
            return self.parent.answer_owner(a)
        except:
            return -1
    def setParent(self,parent):
        self.parentId=parent
        try:
            self.parent.children.discard(self)
        except:
            pass

        try:
            self.parent=agents[parent]
            self.parent.children.add(self)
        except:
            self.parent=parent
            
    def score(self,answers):
        sa=self.all_answers()
        return sum(sa[a.q]*a.a for a in answers if a.q in sa.keys())



cur.execute("PRAGMA foreign_keys = ON")
cur.execute('CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,txt TEXT)')
cur.execute('CREATE TABLE IF NOT EXISTS agents (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,name TEXT,parent INTEGER)')
cur.execute('''CREATE TABLE IF NOT EXISTS answers
                (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                ans INTEGER,
                question INTEGER,
                agent INTEGER,
                FOREIGN KEY(question) REFERENCES questions(id) ON DELETE CASCADE,
                FOREIGN KEY(agent) REFERENCES agents(id) ON DELETE CASCADE)''')

conn.commit()

def updateQuestions():
    global questions
    cur.execute('SELECT * FROM questions')
    questions={q[0]:q[1] for q in cur.fetchall()}

def addQuestion(q):
    cur.execute("INSERT INTO questions (txt) VALUES(?)",(q,))
    i=cur.lastrowid
    questions[i]=q
    conn.commit()
    return i

def delQuestion(i):
    cur.execute("DELETE FROM questions WHERE id=?",(i,))
    del(questions[i])
    conn.commit()
    for a in agents:
        if i in agents[a].answers.keys():
            del agents[a].answers[i]

def updateQuestion(i,q):
    cur.execute("UPDATE questions SET txt=? WHERE id=?",(q,i))
    conn.commit()
    questions[i]=q

def addAnswer(a,q):
    if q not in agents[a].all_answers().keys():
        agents[a].answers[q]=0
        cur.execute("INSERT INTO answers (ans,question,agent) VALUES (0,?,?)",(q,a))
        conn.commit()

def updateAnswer(aId,qId,a):
    if aId in agents.keys():
        agents[aId].answers[qId]=a
        cur.execute("UPDATE answers SET ans=? WHERE question=? AND agent=?",(a,qId,aId))
        conn.commit()

def delAnswer(aId,qId):
    if aId in agents.keys():
        cur.execute("DELETE FROM answers WHERE question=? AND agent=?",(qId,aId))
        del(agents[aId].answers[qId])
        conn.commit()

def updateAgents():
    global agents
    cur.execute('SELECT * FROM agents')
    agents={a[0]:Agent(name=a[1],parent=a[2],aId=a[0]) for a in cur.fetchall()}
    for a in agents:
        try:
            agents[a].setParent(agents[a].parentId)
        except:
            pass

    cur.execute('SELECT * FROM answers')
    for a in cur.fetchall():
        agents[a[3]].answers[a[2]]=a[1]


def updateAgent(a):
    cur.execute("UPDATE agents SET parent=?, name=? WHERE id=?",(a.parentId,a.name,a.aId))
    conn.commit()
    updateAgents()

def addAgent(name="Aucun"):
    cur.execute("INSERT INTO agents (name,parent) VALUEs(?,0)",(name,))
    i=cur.lastrowid
    agents[i]=Agent(name=name,parent=0,aId=i)
    conn.commit()
    return i

def delAgent(aId):
    if aId in agents.keys():
        agents[aId].setParent(0)
        del(agents[aId])
        cur.execute("DELETE FROM agents WHERE id=?",(aId,))
        conn.commit()

def random_questions(l=-1):
    if l<0:
        l=len(questions)
    return sample(list(questions.items()),min(l,len(questions)))

def sortedAgents(ansList):
    l=[(agents[a].score(ansList),agents[a]) for a in agents]
    l=sorted(l,key=lambda a:-a[0])
    r={}
    for a in l:
        try:
            r[a[0]].append(a[1])
        except:
            r[a[0]]=[a[1]]
    return r

updateQuestions()
updateAgents()
