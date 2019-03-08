import sys
import data
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QListWidgetItem, QTreeWidgetItem, QInputDialog, QMessageBox
from PyQt5.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow
from ui_questions import Ui_Questions
from ui_edit import Ui_Edit
 
class MainWindow(QMainWindow,Ui_MainWindow):
 
    def __init__(self):
        super(MainWindow,self).__init__()
        self.title = 'Aki'
        self.initUI()
 
    def initUI(self):
        global qw
        self.setupUi(self)
        self.updateQuestions()
        _buildTree(self.treeWidget)
        self.treeWidget.currentItemChanged.connect(self.selectAgent)
        self.setWindowTitle(self.title)
        
        self.guessButton.clicked.connect(qw)
        self.editButton.clicked.connect(ew)

        self.addQButton.clicked.connect(self.addQuestion)
        self.delQButton.clicked.connect(self.delQuestion)
        
        self.addAButton.clicked.connect(self.addAnswer)
        self.delAButton.clicked.connect(self.delAnswer)

        
        
        self.show()
        
    def addQuestion(self):
        t=QInputDialog.getText(self,"Question","Question à poser :")
        if len(t[0]) and t[1]:
            data.addQuestion(t[0])
            self.updateQuestions()

    def updateQuestions(self):
        self.qListWidget.disconnect()
        self.qListWidget.clear()
        for q in data.questions:
            i=QListWidgetItem(data.questions[q],self.qListWidget)
            i.setFlags(i.flags()|2)
            i.qId=q
        self.selectAgent(0,0)
        self.qListWidget.itemChanged.connect(self.updateQuestion)

    def updateQuestion(self,i):
        data.updateQuestion(i.qId,i.text())
        self.selectAgent(0,0)
        
    def delQuestion(self):
        i=self.qListWidget.currentItem()
        if i:
            mb=QMessageBox(self)
            mb.setWindowTitle("Supprimer ?")
            mb.setText("Supprimer la question et les réponses associées ?")
            mb.setInformativeText(self.qListWidget.currentItem().text())
            mb.setStandardButtons(mb.Yes|mb.No)
            if mb.exec()==mb.Yes:
                data.delQuestion(i.qId)
                self.updateQuestions()

    def addAnswer(self):
        i=self.treeWidget.currentItem()
        q=self.qListWidget.currentItem()
        if i and q:
            if i.aId:
                data.addAnswer(i.aId,q.qId)
                self.selectAgent(0,0)

    def updateAnswer(self,i):
        data.updateAnswer(i.aId,i.qId,i.checkState()-1)

    def delAnswer(self):
        i=self.ansListWidget.currentItem()
        if i:
            data.delAnswer(i.aId,i.qId)
            self.selectAgent(0,0)

    
    def selectAgent(self,i,previousItem):
        i=self.treeWidget.currentItem()
        if i:
            self.ansListWidget.clear()
            if i.aId:
                self.ansListWidget.disconnect()
                ans=data.agents[i.aId].all_answers()
                for a in ans:
                    li=QListWidgetItem(data.questions[a]+" ("+data.agents[data.agents[i.aId].answer_owner(a)].name+")",self.ansListWidget)
                    li.setCheckState(1+ans[a])
                    li.setFlags(li.flags()|256) # tristate
                    li.qId=a
                    li.aId=data.agents[i.aId].answer_owner(a)
                    #if a not in data.agents[i.aId].answers.keys():
                    #    li.setFlags(li.flags()^16) # Si la réponse concerne un agent aïeul, on empêche les modifs
                self.ansListWidget.itemChanged.connect(self.updateAnswer)

def _buildTree(tw):
    s=set(data.agents.keys())
    tw.clear()

    def addChildren(i,s):
        i.setExpanded(True)
        s.discard(i.aId)
        for c in data.agents[i.aId].children:
            child=QTreeWidgetItem(i)
            child.setText(0,c.name)
            child.aId=c.aId
            addChildren(child,s)
    
    for a in data.agents:
        if not data.agents[a].parent:
            i=QTreeWidgetItem(tw)
            i.setText(0,data.agents[a].name)
            i.aId=a
            addChildren(i,s)
    if len(s):
        i=QTreeWidgetItem(tw)
        i.setText(0,"Items perdus")
        i.setExpanded(True)
        i.aId=0
        for a in s:
            c=QTreeWidgetItem(i)
            c.setText(0,data.agents[a].name)
            c.aId=a
            


class QuestionsWindow(QWidget,Ui_Questions):

    def __init__(self):
        super(QuestionsWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Deviner")

        self.qList=data.random_questions()
        self.aList=[]
        self.currentQ=0
        if len(self.qList):
            self.label_question.setText(self.qList[0][1])

        self.yesButton.clicked.connect(self.yes)
        self.mayButton.clicked.connect(self.ign)
        self.noButton.clicked.connect(self.no)

        self.listWidget.itemChanged.connect(self.updateAnswer)
        
        self.setAttribute(55) # 55 : delete on close
        self.show()

    def updateAnswer(self,i):
        self.aList[i.qN].a=i.checkState()-1
        self.updateAgents()
    
    def updateAgents(self):
        l=data.sortedAgents(self.aList)
        self.treeWidget.clear()
        for s in l:
            i=QTreeWidgetItem(self.treeWidget)
            i.setText(0,"Score : "+str(s))
            i.setExpanded(True)
            for a in l[s]:
                li=QTreeWidgetItem(i)
                li.setText(0,a.name)

    def nextQuestion(self):
        self.listWidget.disconnect()
        try:
            a=self.aList[self.currentQ]
            i=QListWidgetItem(self.listWidget)
            i.qId=self.qList[self.currentQ][0]
            i.qN=self.currentQ
            i.setText(self.qList[self.currentQ][1])
            i.setCheckState(1+a.a)
            i.setFlags(i.flags()|256) # tristate
        except:
            pass
        self.currentQ+=1
        try:
            self.label_question.setText(self.qList[self.currentQ][1])
        except:
            self.label_question.setText("Plus aucune question")
        self.listWidget.itemChanged.connect(self.updateAnswer)
        self.updateAgents()

    def ign(self):
        try:
            self.aList.append(data.Answer(q=self.qList[self.currentQ][0],a=0))
        except:
            pass
        self.nextQuestion()

    def yes(self):
        try:
            self.aList.append(data.Answer(q=self.qList[self.currentQ][0],a=1))
        except:
            pass
        self.nextQuestion()
        
    def no(self):
        try:
            self.aList.append(data.Answer(q=self.qList[self.currentQ][0],a=-1))
        except:
            pass
        self.nextQuestion()
        
class EditWindow(QWidget,Ui_Edit):

    def __init__(self):
        super(EditWindow,self).__init__()
        self.setupUi(self)
        _buildTree(self.selectTreeWidget)

        self.selectTreeWidget.currentItemChanged.connect(self.selectAgent)

        self.addButton.clicked.connect(self.addAgent)
        self.delButton.clicked.connect(self.delAgent)
        self.saveButton.clicked.connect(self.saveAgent)
        
        self.a=0
        
        self.setWindowTitle("Édition de l'arbre")
        self.setAttribute(55)
        self.show()

    def selectAgent(self,i,previousItem):
        if i.aId:
            try:
                self.a.setParent(self.a.oldParent)
            except:
                pass
            
            self.a=data.agents[i.aId]
            self.nameEdit.setText(self.a.name)
            self.parentLabel.setText("Aucun")
            self.a.newParent=self.a.parentId

            try:
                self.parentTreeWidget.disconnect()
            except:
                pass
            
            self.parentTreeWidget.clear()

            def _addChildren(i):
                i.setExpanded(True)
                if i.aId==self.a.parentId:
                    self.parentLabel.setText(self.a.parent.name)
                    self.parentTreeWidget.setCurrentItem(i)
                for c in data.agents[i.aId].children:
                    child=QTreeWidgetItem(i)
                    child.setText(0,c.name)
                    child.aId=c.aId
                    _addChildren(child)
            
            i=QTreeWidgetItem(self.parentTreeWidget)
            i.setText(0,"Aucun")
            i.aId=0
            
            for a in data.agents:
                if not data.agents[a].parent:
                    i=QTreeWidgetItem(self.parentTreeWidget)
                    i.setText(0,data.agents[a].name)
                    i.aId=a
                    _addChildren(i)
                    
            self.parentTreeWidget.currentItemChanged.connect(self.selectParent)

    def selectParent(self,i,previousItem):
        try:
            if i.aId:
                self.a.newParent=i.aId
                self.parentLabel.setText(data.agents[i.aId].name)
            else:
                self.a.newParent=0
                self.parentLabel.setText("Aucun")
        except:
            pass
        
    def addAgent(self):
        t=QInputDialog.getText(self,"Nom","Nom de l'élément à ajouter :")
        if len(t[0]) and t[1]:
            i=QTreeWidgetItem(self.selectTreeWidget)
            i.setText(0,t[0])
            i.aId=data.addAgent(t[0])
            self.selectTreeWidget.setCurrentItem(i)
            try:
                _buildTree(mwh.treeWidget)
            except:
                pass

    def delAgent(self):
        if self.a and self.a.aId:
            self.selectTreeWidget.disconnect()
            mb=QMessageBox(self)
            mb.setWindowTitle("Supprimer ?")
            mb.setText("Supprimer l'élément et les réponses associées ?")
            mb.setInformativeText(self.a.name)
            mb.setStandardButtons(mb.Yes|mb.No)
            if mb.exec()==mb.Yes:
                data.delAgent(self.a.aId)
                self.parentLabel.setText("")
                self.nameEdit.setText("")
                self.parentTreeWidget.disconnect()
                self.parentTreeWidget.clear()
                self.a=lambda:None # Objet vide
                self.a.aId=0
                _buildTree(self.selectTreeWidget)
            self.selectTreeWidget.currentItemChanged.connect(self.selectAgent)
            try:
                _buildTree(mwh.treeWidget)
            except:
                pass

    def saveAgent(self):
        if self.a and self.a.aId:
            self.selectTreeWidget.disconnect()
            self.a.setParent(self.a.newParent)
            self.a.name=self.nameEdit.text()
            data.updateAgent(self.a)
            _buildTree(self.selectTreeWidget)
            self.selectTreeWidget.currentItemChanged.connect(self.selectAgent)
            try:
                _buildTree(mwh.treeWidget)
            except:
                pass

qwh=0
def qw():
    global qwh
    qwh=QuestionsWindow() # Ce zarba occasionne des fuites mémoires, pas grave vu l'empreinte du programme mais à revoir quand même

ewh=0
def ew():
    global ewh
    ewh=EditWindow()

mwh=0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mwh = MainWindow()
    sys.exit(app.exec_())
