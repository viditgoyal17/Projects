''' THIS IS A PYTHON PROJECT BASED ON PYTHON AND SQL CONNECTIVITY.
    IT IS A 'FITNESS CENTRE DATABASE MANAGEMENT' SOFTWARE.
'''

import mysql.connector as mc
import random as r
import Functions as p2

mydb=mc.connect(user='root', passwd='2403ujjwal', host='localhost', database='python_project_xii')

cur=mydb.cursor()  

print('------------------------------------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------------------------------------')    
print('-------------------------------------         WELCOME TO THE "FEELn THE BURNs" FITNESS CENTRE      ---------------------------------')
print('------------------------------------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------------------------------------')

print()
print()


while True:
      
      print('-----CHOOSE FROM ONE OF THE FOLLOWING:-----')
      print()
      print('1.> MEMBER ? LOGIN HERE')
      print('2.> TRAINER ? LOGIN HERE')
      print('3.> NEW TRAINEE HERE ? JOIN')
      print('4.> NEW TRAINER HERE ? JOIN')
      print('5.> OUR FITNESS PLANS')
      print('6.> ABOUT US')
      print('7.> EXIT')
      print()
      c1=input('ENTER YOUR CHOICE>> ')
      print()
      print()
      
      if c1=='1':
            
            em=input('Enter your EMAIL ID>>')
            p=input('Enter your password>> ')
            print()
            print()
            sr=p2.fndsr(em)
            a=p2.pascheck(sr)
            if [(p,)]==a:
                  print('WELCOME BACK',p2.fndnam(sr))
                  print()
                  print('------YOUR PROFILE------')
                  print()
                  print('1.> YOUR NAME:',p2.fndnam(sr))
                  print('2.> YOUR AGE:',p2.fndag(sr))
                  print('3.> YOUR EMAIL ID:',p2.fndem(sr))
                  print('4.> YOUR DOB:',p2.fnddob(sr))
                  print('5.> YOUR COURSE:',p2.fndcou(sr))
                  print('6.> YOUR PAYMENT STATUS:',p2.fndpay(sr))
                  print('7.> YOUR PASSWORD:',p2.fndpa(sr))
                  print()
                  e=input('PRESS ENTER TO CONTINUE')
                  print()
                  c11=input('DO YOU WANT TO UPDATE SOMETHING?? Y/N>> ')
                  if c11=='y' or c11=='Y':
                        print('WHAT DO YOU WISH TO DO??')
                        print()
                        print('1.> DO YOU WANT TO UPDATE SOME THING??')
                        print('2.> DO YOU WANT TO CANCEL YOUR MEMBERSHIP')
                        print()
                        c5=int(input('ENTER YOUR CHOICE>> '))
                        if c5==1:
                              print('WHAT DO YOU WANT TO UPDATE??')
                              print()
                              print('1.> NAME')
                              print('2.> DATE OF BIRTH')
                              print('3.> EMAIL ID')
                              print('4.> COURSE')
                              print('5.> PASSWORD')
                              print()
                              c6=int(input('ENTER YOUR CHOICE>> '))
                              print()
                              if c6==1:
                                    pwd=input('ENTER YOUR PASSWORD')
                                    if [(pwd,)]==p2.pascheck(sr):
                                          nn=input('ENTER YOUR NEW NAME>> ')
                                          p2.updnam(nn,sr)
                                          print()
                                          print('YOUR NEW NAME IS',nn)

                              elif c6==2:
                                    pwd=input('ENTER YOUR PASSWORD>> ')
                                    if [(pwd,)]==p2.pascheck(sr):
                                          mdobd=input('ENTER YOUR NEW DAY OF BIRTH>> ')
                                          mdobm=input('ENTER YOUR NEW MONTH OF BIRTH>> ')
                                          mdoby=input('ENTER YOUR NEW YEAR OF BIRTH>> ')
                                          
                                          p2.upddob(mdobd,mdobm,mdoby,sr)
                                          print()
                                          d=mdoby,'-',mdobm,'-',mdobd
                                          dob=''
                                          for i in d:
                                                dob+=i

                                          print('YOUR NEW DOB IS',dob)

                              elif c6==3:
                                    pwd=input('ENTER YOUR PASSWORD>> ')
                                    if [(pwd,)]==p2.pascheck(sr):
                                          EI=input('ENTER YOUR NEW EMAIL ID>> ')
                                          p2.updem(EI,sr)
                                          print()
                                          print('YOUR NEW EMAIL ID IS',EI)

                              elif c6==4:
                                    pwd=input('ENTER YOUR PASSWORD>> ')
                                    if [(pwd,)]==p2.pascheck(sr):
                                          print('WHICH COURSE DO YOU WANT ENROLLMENT IN??')
                                          print()
                                          print('1.> AEROBICS (2 sessions per week)   :- ₹350/session')
                                          print('2.> YOGA (2 sessions per week)       :- ₹400/session')
                                          print('3.> BODY BUILDING                    :- ₹1000/month')               
                                          print('4.> WEIGHT LOSS                      :- ₹1200/month')               
                                          print('5.> FITNESS MAINTAINANCE             :- ₹900/week')     
                                          print('6.> ZUMBA (2 sessions per week)      :- ₹250/session')       
                                          print()
                                          print('*****************   WITH ₹400 PER MONTH FOR MEMBERSHIP CHARGES   *****************')
                                          print()
                                          c7=int(input('Enter your Choice>> '))
                                          print()
                                          if c7==1:
                                                print('PLEASE PAY ₹700 + ₹400 = ₹1100 FOR THE WEEKS SESSIONS')
                                                print()
                                                print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                p2.updcou('AEROBICS',sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==2:
                                                print('PLEASE PAY ₹800 + ₹400 = ₹1200 FOR THE WEEKS SESSIONS')
                                                print()
                                                print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                c='YOGA'
                                                p2.updcou(c,sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==3:
                                                print('PLEASE PAY ₹1000 + ₹400 = ₹1400 FOR THE MONTH SESSIONS')
                                                print()
                                                print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                p2.updcou('BODY BUILDING',sr)
                                                print()
                                                print('OK DONE!!')
                                          elif c7==4:
                                                print('PLEASE PAY ₹1200 + ₹400 = ₹1700 FOR THE MONTH SESSIONS')
                                                print()
                                                print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                p2.updcou('WEIGHT LOSS',sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==5:
                                                c8=input('DO YOU NEED A TRAINER?? Y/N>> ')
                                                if c8 in ('Y','y'):
                                                      print('PLEASE PAY ₹900 + ₹400 + ₹400 = ₹1700 FOR THE WEEKS SESSIONS')
                                                      print()
                                                      print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                      p2.updcou('FIT_MANAGE WITH TRAINER',sr)
                                                      print()
                                                      print('OK DONE!!')
                                    
                                                elif c8 in ('n','N'):
                                                      print('PLEASE PAY ₹900 + ₹400 = ₹1300 FOR THE WEEKS SESSIONS')
                                                      print()
                                                      print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                      p2.updcou('FIT_MANAGE W/O TRAINER',sr)
                                                      print()
                                                      print('OK DONE!!')
                                    
                                                else:
                                                      print('Choose either Y or N')
                                                      print()
                                    
                                    
                                          elif c7==6:                                                               
                                                print('PLEASE PAY ₹500 + ₹400 = ₹900 FOR THE WEEKS SESSIONS')
                                                print()
                                                print('YOU CANNOT ENROLL WITHOUT PAYMENT')
                                                p2.updcou('ZUMBA',sr)
                                                print()
                                                print('OK DONE!!')

                              elif c6==5:
                                    op=input('ENTER YOUR OLD PASSWORD>> ')
                                    if [(op,)]==p2.pascheck(sr):
                                          np=input('ENTER YOUR NEW PASSWORD>> ')
                                          cp=input('CONFIRM YOUR NEW PASSWORD>> ')
                                          if cp==np:
                                                p2.updpas(np, sr)
                                                print('Password changed successfully!!!')
                                          else:
                                                print('Passwords donot match')
                                    else:
                                          print('Incorrect password')
                                          

                        elif c5==2:
                              em=input('Enter the EMAIL ID of the record you want to delete>> ')
                              cur.execute('select EMAIL_ID from members')
                              rec=cur.fetchall()
                              while (email,) in rec:
                                    print('Email already taken')
                                    email=input('Enter another E-mail ID>> ')
                              print()
                              passwo=input('Enter your password>> ')
                              sro=p2.fndsr(em)
                              if [(passwo,)]==p2.pascheck(sro):
                                    p2.delrec(sro)
                                    print('OK DONE!! SHALL HOPE THAT YOU RESUME OUR SERVICES AGAIN SOON')
                        else:
                              print('INCORRECT PASSWORD')
                              

                              
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()

                  elif c11=='n' or c11=='N':
                        print('OK BYE')
                        print()
                        print()
                        break
            
                  else:
                        print('TYPE "Y" OR "N"')
                        print()
                        print()
            else:
                  print('Password is incorrect. Retry')
                  print()
                  print()

      elif c1=="2":
            em=input('Enter your EMAIL ID>>')
            p=input('Enter your password>> ')
            print()
            print()
            sr=p2.tfndsr(em)
            a=p2.tpascheck(sr)
            if [(p,)]==a:
                  print('WELCOME BACK',p2.tfndnam(sr))
                  print()
                  print('------YOUR PROFILE------')
                  print()
                  print('1.> YOUR NAME:',p2.tfndnam(sr))
                  print('2.> YOUR AGE:',p2.tfndag(sr))
                  print('3.> YOUR EMAIL ID:',p2.tfndem(sr))
                  print('4.> YOUR DOB:',p2.tfnddob(sr))
                  print('5.> YOUR QUALIFICATONS:',p2.tfndqual(sr))
                  print('6.> YOUR SALARY:',p2.tfndsal(sr))
                  print('7.> YOUR PASSWORD:',p2.tfndpa(sr))
                  print()
                  e=input('PRESS ENTER TO CONTINUE')
                  print()
                  c11=input('OPEN PROFILE ?? Y/N >> ')
                  if c11=='y' or c11=='Y':
                        print('WHAT DO YOU WISH TO DO??')
                        print()
                        print('1.> DO YOU WANT TO UPDATE YOUR PROFILE ??')
                        print('2.> DO YOU WANT TO CANCEL YOUR MEMBERSHIP ??')
                        print()
                        c5=int(input('ENTER YOUR CHOICE>> '))
                        if c5==1:
                              print('WHAT DO YOU WANT TO UPDATE??')
                              print()
                              print('1.> NAME')
                              print('2.> DATE OF BIRTH')
                              print('3.> EMAIL ID')
                              print('4.> QUALIFICATIONS')
                              print('5.> PASSWORD')
                              print('6.> COURSE') 
                              print()
                              c6=int(input('ENTER YOUR CHOICE>> '))
                              print()
                              if c6==1:
                                    pwd=input('ENTER YOUR PASSWORD >> ')
                                    if [(pwd,)]==p2.tpascheck(sr):
                                          nn=input('ENTER YOUR NEW NAME >> ')
                                          p2.tupdnam(nn,sr)
                                          print()
                                          print('YOUR NEW NAME IS',nn)

                              elif c6==2:
                                    pwd=input('ENTER YOUR PASSWORD>> ')
                                    if [(pwd,)]==p2.tpascheck(sr):
                                          mdobd=input('ENTER YOUR NEW DAY OF BIRTH >> ')
                                          mdobm=input('ENTER YOUR NEW MONTH OF BIRTH >> ')
                                          mdoby=input('ENTER YOUR NEW YEAR OF BIRTH >> ')
                                          p2.tupddob(mdobd,mdobm,mdoby,sr)
                                          print()
                                          d=mdoby,'-',mdobm,'-',mdobd
                                          dob=''
                                          for i in d:
                                                dob+=i

                                          print('YOUR NEW DOB IS ',dob)

                              elif c6==3:
                                    pwd=input('ENTER YOUR PASSWORD >> ')
                                    if [(pwd,)]==p2.tpascheck(sr):
                                          EI=input('ENTER YOUR NEW EMAIL ID >> ')
                                          p2.tupdem(EI,sr)
                                          print()
                                          print('YOUR NEW EMAIL ID IS ',EI)

                              elif c6==6:
                                    pwd=input('ENTER YOUR PASSWORD >> ')
                                    if [(pwd,)]==p2.tpascheck(sr):
                                          print('WHICH COURSE ARE YOU SPECIALIZED IN ??')
                                          print()
                                          print('1.> AEROBICS')
                                          print('2.> YOGA')
                                          print('3.> BODY BUILDING')               
                                          print('4.> WEIGHT LOSS')               
                                          print('5.> FITNESS MAINTAINANCE')     
                                          print('6.> ZUMBA')
                                          print()
                                          c7=int(input('Enter your Choice >> '))
                                          print()
                                          if c7==1:
                                                p2.tupdcou('AEROBICS',sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==2:
                                                c='YOGA'
                                                p2.tupdcou(c,sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==3:
                                                p2.tupdcou('BODY BUILDING',sr)
                                                print()
                                                print('OK DONE!!')
                                          elif c7==4:
                                                p2.tupdcou('WEIGHT LOSS',sr)
                                                print()
                                                print('OK DONE!!')
                              
                                          elif c7==5:
                                               p2.tupdcou('FIT_MANAGE',sr)
                                               print()
                                               print('OK DONE!!')
                                                                        
                                    
                                          elif c7==6:                                                               
                                                p2.tupdcou('ZUMBA',sr)
                                                print()
                                                print('OK DONE!!')

                              elif c6==5:
                                    op=input('ENTER YOUR OLD PASSWORD>> ')
                                    if [(op,)]==p2.tpascheck(sr):
                                          np=input('ENTER YOUR NEW PASSWORD >> ')
                                          cp=input('CONFIRM YOUR NEW PASSWORD >> ')
                                          if cp==np:
                                                p2.tupdpas(np, sr)
                                                print('Password changed successfully!!!')
                                          else:
                                                print('Passwords does not match')
                                    else:
                                          print('Incorrect password')
                                          


                              elif c6==4:
                                    pwd=input('ENTER YOUR PASSWORD>> ')
                                    if [(pwd,)]==p2.tpascheck(sr):
                                          PAY=input('ENTER YOUR QUALIFICATIONS>> ')
                                          p2.tupdqual(PAY,sr)
                                          print()             
                                          print('OK DONE!!')

                                    else:
                                          print('INCORRECT PASSWORD')

                        elif c5==2:
                              em=input('Enter your EMAIL ID >> ')
                              passwo=input('Enter your password >> ')
                              sro=p2.tfndsr(em)
                              if [(passwo,)]==p2.tpascheck(sro):
                                    p2.tdelrec(sro)
                                    print('OK DONE!! SHALL HOPE THAT YOU RESUME OUR SERVICES AGAIN')
                        else:
                              print('INCORRECT PASSWORD')
                              

                              
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()

                  elif c11=='n' or c11=='N':
                        print('OK BYE')
                        print()
                        print()
                        break
            
                  else:
                        print('TYPE "Y" OR "N"')
                        print()
                        print()
            else:
                  print('Password is incorrect. Retry')
                  print()
                  print()
                  

      elif c1=='3':
            
            c0=input('WHERE YOU ALREADY A MEMBER HERE BEFORE?? Y/N>> ')
            if c0 in ('y','Y'):
                  ema=input('Enter the email id with which you had loggged in >>')
                  sr=p2.fndsr(ema)
                  pa=input('Enter a password >> ')
                  conpa=input('Repeat the password >> ')
                  if pa==conpa:
                        p2.updpas(pa, sr)
                        p2.actrec(sr)
                        print('Please pay your membership of Rs. 400')
                        e=input('Please press enter to continue ')
                        print('WELCOME BACK!!')
                  else:
                        print('Password donot match')
            elif c0 in ('n','N'):
                  print('WELCOME NEW COMER!!')
                  print()
                  name=input('Enter your full name >> ')
                  age=int(input('Enter your age >> '))
                  dobd=input('Enter your DAY of birth >> ')
                  dobm=input('Enter your MONTH of birth (number )>> ')
                  doby=input('Enter your YEAR of birth >> ')
                  email=input('Enter your E-mail ID >> ')
                  cur.execute('select EMAIL_ID from members')
                  rec=cur.fetchall()
                  while (email,) in rec:
                        print('Email already taken')
                        email=input('Enter another E-mail ID >> ')
                        print()
                  pa=input('Enter a password >> ')
                  conpa=input('Repeat the password >> ')
                  if pa==conpa:
                        print()
                        print('WHICH COURSE DO YOU WANT ENROLLMENT IN??')
                        print()
                        print('1.> AEROBICS (2 sessions per week)   :- ₹350/session')
                        print('2.> YOGA (2 sessions per week)       :- ₹400/session')
                        print('3.> BODY BUILDING                    :- ₹1000/month')               
                        print('4.> WEIGHT LOSS                      :- ₹1200/month')               
                        print('5.> FITNESS MAINTAINANCE             :- ₹900/week')     
                        print('6.> ZUMBA (2 sessions per week)      :- ₹250/session')       
                        print()
                        print('*****************   WITH ₹400 PER MONTH FOR MEMBERSHIP CHARGES   *****************')
                        print()
                        c2=int(input('Enter your Choice >> '))
                        print()
                        if c2==1:
                              print('PLEASE PAY ₹700 + ₹400 = ₹1100 FOR THE WEEKS SESSIONS')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa, 'AEROBICS')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')                        
                              print()
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                              
                        if c2==2:
                              print('PLEASE PAY ₹800 + ₹400 = ₹1200 FOR THE WEEKS SESSIONS')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa, 'YOGA')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                              print()
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                              
                        if c2==3:
                              print('PLEASE PAY ₹1000 + ₹400 = ₹1400 FOR THE MONTH SESSIONS')
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa,'BODY BUILDING')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                              print()
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                        if c2==4:
                              print('PLEASE PAY ₹1200 + ₹400 = ₹1700 FOR THE MONTH SESSIONS')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa, 'WEIGHT LOSS')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                              print()
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                              
                        if c2==5:
                              print('PLEASE PAY ₹900 + ₹400 + ₹400 = ₹1700 FOR THE WEEKS SESSIONS')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa, 'FIT_MANAGE')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                              print()
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                                    
                                    
                        if c2==6:                                                               
                              print('PLEASE PAY ₹500 + ₹400 = ₹900 FOR THE WEEKS SESSIONS')
                              print()
                              srno=r.randint(1,10000)
                              p2.insert(srno, name, age, dobd, dobm, doby, email, conpa, 'ZUMBA')
                              print('CONGRATULATIONS!!!! YOU ARE NOW OFFICIAL !!!')
                              e=input('PRESS ENTER TO CONTINUE')
                              print()
                              print()
                     

                        
                  else:
                        print('ERROR: Passwords do not match. Try again!!!!')
                        print()
                        print()
            else:
                  print('WRONG CHOICE')
            
      elif c1=='4':
            
            print('WELCOME NEW COMER!!')
            print()
            name=input('Enter your full name >> ')
            age=int(input('Enter your age >> '))
            dobd=input('Enter your DAY of birth>> ')
            dobm=input('Enter your MONTH of birth (number)>> ')
            doby=input('Enter your YEAR of birth>> ')
            email=input('Enter your E-mail ID >> ')
            qual=input("Enter name of INSTITUE from where you are qualified >> ")
            cur.execute('select EMAIL_ID from trainers')
            while (email,) in cur.fetchall():
                  print('Email already taken')
                  email=input('Enter another E-mail ID >> ')
                  print()
            pa=input('Enter a password>> ')
            conpa=input('Repeat the password>> ')
            if pa==conpa:
                  print()
                  print('WHICH COURSE ARE YOU SPECIALIZED IN ??')
                  print()
                  print('1.> AEROBICS')
                  print('2.> YOGA')
                  print('3.> BODY BUILDING')               
                  print('4.> WEIGHT LOSS')               
                  print('5.> FITNESS MAINTAINANCE')     
                  print('6.> ZUMBA')
                  print()
                  c2=int(input('Enter your Choice>> '))
                  print()
                  if c2==1:
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 6000, "AEROBICS")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')                        
                        print()
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  elif c2==2:
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 4000, "YOGA")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                        print()
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  elif c2==3:
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 8000, "BODY BUILDING")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                        print()
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  elif c2==4:
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 5000, "WEIGHT LOSS")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                        print()
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  elif c2==5:
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 5500, "FIT_MANAGE")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICAL!!!!')
                        print()
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  elif c2==6:                                                               
                        srno=r.randint(1,10000)
                        p2.tinsert(srno, name, age, dobd, dobm, doby, email, conpa, qual, 3500, "ZUMBA")
                        print('CONGRATULATIONS!!!! YOU ARE NOW OFFICIAL!!!')
                        e=input('PRESS ENTER TO CONTINUE')
                        print()
                        print()
                  else:
                        print("WRONG CHOICE! GETTING YOU BACK TO THE LOGIN PAGE...")

                        
            else:
                  print('ERROR: Passwords donot match. Try again!!!!')
                  print()
          
            

      elif c1=='5':
          
            print('HERE ARE THE COURSES WE OFFER (ALL COURSES HAVE HIGHLY QUALIFIED TRAINERS)')
            print()
            print('1.> AEROBICS              :- ₹350/session')
            print('2.> YOGA                  :- ₹400/session')
            print('3.> BODY BUILDING         :- ₹1000/month')               
            print('4.> WEIGHT LOSS           :- ₹1200/month')               
            print('5.> FITNESS MAINTAINANCE  :- ₹900/week')     
            print('6.> ZUMBA                 :- ₹250/session')                                             
            print()
            print('*****************   WITH ₹400 PER MONTH FOR MEMBERSHIP CHARGES   *****************')
            print()
            e=input('PRESS ENTER TO CONTINUE')
            print()
            print()

            
      elif c1=='6':
            
            
            print('                    ----------------    "FEELn THE BURNs"    ----------------                        ')
            print()
            print('A Gym for the Classy People. Stay Fit and Stay Healthy.')
            print('Contact today itself - "FEELn THE BURNs" , Sector XX, ABC STREET, UTTAR PRADESH, INDIA.')

            print('A fully-equipped fitness center at the heart of ABC STREET serving with highly professional trainers')
            print('and a huge range of group activities.')

            print('One membership to workout:-')
            print('  1.) Across 4,000+ gyms and fitness studios pan-India')
            print('  2.) Anywhere, anytime - near your home, office or friend’s house')
            print('  3.) Yoga, Aerobics, Weight Loss, Gym workout and many more')
            print()
            print('CONTACT US TODAY:')
            print('PhNo.    :- 9999XXXXXX')
            print('Email    :- feelntheburnsatABC@gmail.com')
            print('Address  :- B-98, Sector XX, ABC STREET, UTTAR PRADESH, INDIA')
            print()
            e=input('PRESS ENTER TO CONTINUE')
            print()
            print()
                        
      elif c1=='7':
            
            break
      
      else:
            
            print('WRONG CHOICE ENTERED')
            print()
            e=input('PRESS ENTER TO CONTINUE')
            print()
            print()
print('THANKS FOR FEELn THE BURNs!!! SEE YOU SOON!!! :) ;)')



            
      
      
