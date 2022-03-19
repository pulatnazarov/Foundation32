from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton
from PyQt5.QtGui import QFont
import sys
class Btn(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setGeometry(x,y,70,70)
        self.setFont(QFont("Times",30))
    def click(self,func):
        self.clicked.connect(func)

class Window(QWidget):
    ls=[]; lst=[]
    text=str()
    def __init__(self):
        super().__init__()
        self.control()
    def font(self,ob):
        ob.setFont(QFont("Times",15))
    def control(self):
        self.setGeometry(100,300,330,530)
        self.setWindowTitle("Calculator")
        self.one=Btn("1", self, 10, 210)
        self.two=Btn("2", self, 90, 210)
        self.three=Btn("3", self, 170, 210)
        self.four=Btn("4", self, 10, 290)
        self.five=Btn("5", self, 90, 290)
        self.six=Btn("6", self, 170, 290)
        self.seven=Btn("7", self, 10, 370)
        self.eight=Btn("8", self, 90, 370)
        self.nine=Btn("9", self, 170, 370)
        self.zero=Btn("0", self, 90, 450)
        self.C=Btn("C", self, 10, 450)
        self.equal=Btn("=", self, 170, 450)
        self.plus=Btn("+", self, 250, 450)
        self.minus=Btn("-", self, 250, 370)
        self.mult=Btn("*", self, 250, 290)
        self.devide=Btn("/", self, 250, 210)
        self.result=QLabel("",self)
        self.font(self.result)
        self.result.move(10,170)

        self.C.click(self.clear)
        self.one.click(self.adin)
        self.two.click(self.dva)
        self.three.click(self.tri)
        self.four.click(self.chetiri)
        self.five.click(self.pyat)
        self.six.click(self.shest)
        self.seven.click(self.sem)
        self.eight.click(self.vosem)
        self.nine.click(self.devat)
        self.zero.click(self.nol)
        self.plus.click(self.pribavit)
        self.minus.click(self.mnus)
        self.mult.click(self.umnojenie)
        self.devide.click(self.delenie)
        
        self.equal.click(self.ravno)
        
    def clear(self):
        self.result.setText("")
        self.ls=[]
    def adin(self):
        self.ls.append("1")
        self.result.setText(self.result.text()+"1")
        self.result.adjustSize()
    def dva(self):
        self.ls.append("2")
        self.result.setText(self.result.text()+"2")
        self.result.adjustSize()
    def tri(self):
        self.ls.append("3")
        self.result.setText(self.result.text()+"3")
        self.result.adjustSize()
    def chetiri(self):
        self.ls.append("4")
        self.result.setText(self.result.text()+"4")
        self.result.adjustSize()
    def pyat(self):
        self.ls.append("5")
        self.result.setText(self.result.text()+"5")
        self.result.adjustSize()
    def shest(self):
        self.ls.append("6")
        self.result.setText(self.result.text()+"6")
        self.result.adjustSize()
    def sem(self):
        self.ls.append("7")
        self.result.setText(self.result.text()+"7")
        self.result.adjustSize()
    def vosem(self):
        self.ls.append("8")
        self.result.setText(self.result.text()+"8")
        self.result.adjustSize()
    def devat(self):
        self.ls.append("9")
        self.result.setText(self.result.text()+"9")
        self.result.adjustSize()
    def nol(self):
        self.ls.append("0")
        self.result.setText(self.result.text()+"0")
        self.result.adjustSize()
    
    def pribavit(self):
        self.ls.append("+")
        self.result.setText(self.result.text()+"+")
        self.result.adjustSize()
    def mnus(self):
        self.ls.append("-")
        self.result.setText(self.result.text()+"-")
        self.result.adjustSize()
    def umnojenie(self):
        self.ls.append("*")
        self.result.setText(self.result.text()+"*")
        self.result.adjustSize()
    def delenie(self):
        self.ls.append("/")
        self.result.setText(self.result.text()+"/")
        self.result.adjustSize()
    def ravno(self):
        for item in self.ls:
            if item not in "+-*/":
                self.text+=item
            else:
                self.lst.append(self.text)
                self.lst.append(item)
                self.text=str()
        self.lst.append(self.text)
        k=1
        while k!=0:
            for item in range(1,len(self.lst)):
                if '/' not in self.lst and '*' not in self.lst:
                    k=0
                if self.lst[item]=='*':
                    self.lst[item-1]=int(self.lst[item-1])*int(self.lst[item+1])
                    self.lst[item]=int(self.lst[item-1])*int(self.lst[item+1])
                    self.lst[item+1]=int(self.lst[item-1])*int(self.lst[item+1])
                    self.lst.pop(item)
                    self.lst.pop(item)
                
                    break
                elif self.lst[item]=='/':
                    self.lst[item-1]=int(self.lst[item-1])/int(self.lst[item+1])
                    self.lst[item]=int(self.lst[item-1])/int(self.lst[item+1])
                    self.lst[item+1]=int(self.lst[item-1])/int(self.lst[item+1])
                    self.lst.pop(item)
                    self.lst.pop(item)
                    
                    break
        q=1
        while q!=0:
            for item in range(1,len(self.lst)):
                if '+' not in self.lst and '-' not in self.lst:
                    q=0
                if self.lst[item]=='+':
                    self.lst[item-1]=int(self.lst[item-1])+int(self.lst[item+1])
                    self.lst[item]=int(self.lst[item-1])+int(self.lst[item+1])
                    self.lst[item+1]=int(self.lst[item-1])+int(self.lst[item+1])
                    self.lst.pop(item)
                    self.lst.pop(item)
                    
                    break
                elif self.lst[item]=='-':
                    self.lst[item-1]=int(self.lst[item-1])-int(self.lst[item+1])
                    self.lst[item]=int(self.lst[item-1])-int(self.lst[item+1])
                    self.lst[item+1]=int(self.lst[item-1])-int(self.lst[item+1])
                    self.lst.pop(item)
                    self.lst.pop(item)
                    
                    break
        print(self.lst)
        a=str(self.lst[0])
        self.result.setText(self.result.text()+a)
        self.result.adjustSize()

app=QApplication(sys.argv)
wind=Window()
wind.show()
app.exec_()
