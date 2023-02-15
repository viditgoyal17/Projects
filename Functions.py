import mysql.connector as mc
import random as r

mydb=mc.connect(user='root', passwd='2403ujjwal', host='localhost', database='python_project_xii')


cur=mydb.cursor()

#MEMBERS

def insert(srno, name, age, dobd, dobm, doby, email, paswd, course,):
      cur.execute('select SR_NO from members')
      while srno in cur.fetchall():
            srno=r.randint(10000)
      d=doby,'-',dobm,'-',dobd
      dob=''
      for i in d:
            dob+=i

      cur.execute('insert into members values ({0},"{1}",{2},"{3}","{4}","{5}","{6}","{7}")'.format(srno,name,age,dob,email,paswd,course,'y'))
      mydb.commit()

def pascheck(srno):
      cur.execute('select PASSWD from members where SR_NO={0}'.format(srno))
      pasc=cur.fetchall()
      return pasc

def fndsr(em):
      sr=0
      cur.execute('select SR_NO from members where EMAIL_ID="{0}"'.format(em))
      d=cur.fetchall()
      for i in d:
            for j in i:
                  sr+=j
      return sr


def fndnam(srno):
      cur.execute('select NAME from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def fndag(srno):
      cur.execute('select AGE from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def fndem(srno):
      cur.execute('select EMAIL_ID from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def fndcou(srno):
      cur.execute('select COURSE from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def fndpay(srno):
      cur.execute('select PAYMENT_STAT from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      if j in ('y','Y'):
            return 'PAID'
      else:
            return 'DUE'

def fnddob(srno):
      cur.execute('select DATE_OF_BIRTH from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def fndpa(srno):
      cur.execute('select PASSWD from members where SR_NO={0}'.format(srno))
      nam=cur.fetchall()
      name1=''
      for i in nam:
            for j in i:
                  name1=j
      name=''
      for i in name1:
            name+='*'
            
      return name

def updnam(nn,srno):
      cur.execute('update members set NAME="{0}" where SR_NO={1}'.format(nn,srno))
      mydb.commit()

def upddob(dobd,dobm,doby,srno):
      d=doby,'-',dobm,'-',dobd
      dob=''
      for i in d:
            dob+=i

      y=2020-int(doby)

      cur.execute('update members set DATE_OF_BIRTH="{0}" where SR_NO={1}'.format(dob,srno))
      cur.execute('update members set AGE={0} where SR_NO={1}'.format(y,srno))
      mydb.commit()

def updem(em,srno):
      cur.execute('update members set EMAIL_ID="{0}" where SR_NO={1}'.format(em,srno))
      mydb.commit()

def updcou(cou,srno):
      cur.execute('update members set COURSE="{0}" where SR_NO={1}'.format(cou,srno))
      mydb.commit()

def updpas(pa,srno):
      cur.execute('update members set PASSWD="{0}" where SR_NO={1}'.format(pa,srno))
      mydb.commit()

def updpay(pay,srno):
      cur.execute('update members set PAYMENT_STAT="{0}" where SR_NO={1}'.format(pay,srno))
      mydb.commit()

def delrec(srno):
      cur.execute('update members set STATUS="{0}" where SR_NO={1}'.format('n',srno))
      mydb.commit()

def actrec(srno):
      cur.execute('update members set STATUS="{0}" where SR_NO={1}'.format('y',srno))
      mydb.commit()


#TRAINERS

def tinsert(tr_no, name, age, dobd, dobm, doby, email, paswd, qual, sal, cou):
      cur.execute('select trainee_id from trainers')
      while tr_no in cur.fetchall():
            tr_no=r.randint(10000)
      d=doby,'-',dobm,'-',dobd
      dob=''
      for i in d:
            dob+=i

      cur.execute('insert into trainers values ({0},"{1}",{2},"{3}","{4}","{5}","{6}",{7},"{8}")'.format(tr_no,name,age,dob,email,paswd,qual,sal,cou))
      mydb.commit()

def tpascheck(srno):
      cur.execute('select PASSWD from trainers where trainee_id={0}'.format(srno))
      pasc=cur.fetchall()
      return pasc

def tfndsr(em):
      sr=0
      cur.execute('select trainee_id from trainers where EMAIL_ID="{0}"'.format(em))
      d=cur.fetchall()
      for i in d:
            for j in i:
                  sr+=j
      return sr


def tfndnam(srno):
      cur.execute('select name from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def tfndag(srno):
      cur.execute('select age from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def tfndem(srno):
      cur.execute('select EMAIL_ID from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def tfndqual(srno):
      cur.execute('select QUALIFICATIONS from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def tfndsal(srno):
      cur.execute("select SALARY from trainers where trainee_id={0}".format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name      
      
def tfndpro(srno):
      cur.execute('select PROFILE_STATUS from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      if j in ('y','Y'):
            return 'ACTIVE'
      else:
            return 'INACTIVE'

def tfnddob(srno):
      cur.execute('select DATE_OF_BIRTH from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name=''
      for i in nam:
            for j in i:
                  name=j
      return name

def tfndpa(srno):
      cur.execute('select PASSWD from trainers where trainee_id={0}'.format(srno))
      nam=cur.fetchall()
      name1=''
      for i in nam:
            for j in i:
                  name1=j
      name=''
      for i in name1:
            name+='*'
            
      return name

def tupdnam(nn,srno):
      cur.execute('update trainers set name="{0}" where trainee_id={1}'.format(nn,srno))
      mydb.commit()

def tupddob(dobd,dobm,doby,srno):
      d=doby,'-',dobm,'-',dobd
      dob=''
      for i in d:
            dob+=i

      y=2020-int(doby)

      cur.execute('update trainers set DATE_OF_BIRTH="{0}" where trainee_id={1}'.format(dob,srno))
      cur.execute('update trainers set age={0} where trainee_id={1}'.format(y,srno))
      mydb.commit()

def tupdem(em,srno):
      cur.execute('update trainers set EMAIL_ID="{0}" where trainee_id={1}'.format(em,srno))
      mydb.commit()

def tupdqual(cou,srno):
      cur.execute('update trainers set QUALIFICATIONS="{0}" where trainee_id={1}'.format(cou,srno))
      mydb.commit()

def tupdpas(pa,srno):
      cur.execute('update trainers set PASSWD="{0}" where trainee_id={1}'.format(pa,srno))
      mydb.commit()

def tupdcou(pay,srno):
      cur.execute('update trainers set COURSE="{0}" where trainee_id={1}'.format(pay,srno))
      mydb.commit()

def tdelrec(srno):
      cur.execute('delete from trainers where trainee_id={0}'.format(srno))
      mydb.commit()


"""
#################   NOT NEEDED ANYMORE   #################

def tupdsal(pay,srno):
      cur.execute('update trainers set SALARY="{0}" where trainee_id={1}'.format(pay,srno))
      mydb.commit()
"""


"""
def tactrec(srno):
      cur.execute('update trainers set PROFILE_STATUS="{0}" where trainee_id={1}'.format('y',srno))
      mydb.commit()
"""

            
      
      
