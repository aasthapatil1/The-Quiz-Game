'''GROUP-3 - THE QUIZ GAME
             1. Aastha Patil
             2. Gayatru Kuthe
             3. Hishita Sangtani
             4. Shital Kanojiya
             5. Aditya Hirekhan'''

score=0
question=0
Game_running=True
name=str(input('Enter your name : '))
print(''' Welcome to THE QUIZ GAME''',name)
def categories():
    cat1="Bollywood"
    cat2="Songs"
    cat3="Aptitude"
    cat4="General knowledge"
    print('-----------------------------------------')
    print("1.",cat1)
    print("2.",cat2)
    print("3.",cat3)
    print("4.",cat4)

                                                        # BOLLYWOOD

def bolly():
    global score
    print('Lets begin with Bollywood Quiz!')

    print('-----------------------------------------')

    print('''Q1. Famous Bollywood Actress “Priyanka Chopra” first movie in Hollywood was ___.
    A. Baywatch
    B. Terminator
    C. Force
    D. Women in Black''')

    q1=str(input('Ans: '))
    if q1=='A' or q1=='a' or q1=='Baywatch' or q1=='baywatch':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌
        The correct answer is "Baywatch"''')

    print('-----------------------------------------')

    print('''Q2. Jhanvi kapoor is the daughter of which veteran Actress ?
    A. Juhi chawla
    B. Sonali bendre
    C. Sridevi
    D. Babita Kapoor''')

    q2=str(input('Ans: '))
    if q2=='C' or q2=='c' or q2=='Sridevi' or q2=='sridevi':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
        The correct answer is "Sridevi"''')

    print('-----------------------------------------')

    print('''Q3. Which Following Actress debuted opposite Shahrukh Khan in movie “Om shanti Om”?
    A. Sonam Kapoor
    B. Anushka Sharma
    C. Deepika Padukone
    D. Priyanka Chopra''')

    q3=str(input('Ans: '))
    if q3 == 'C' or q3 =='c' or q3 =='Deepika Padukone' or q3 =='deepika padukone':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
        The correct answer is "Deepika Padukone"''')

    print('-----------------------------------------')

    print('''Q4. Which Shah Rukh Film has the tagline ‘Ready Steady Po’ ?
    A. Dil Toh Pagal Hai
    B. Jab Tak Hai Jaan
    C. Chennai Express
    D. Khiladi 786''')

    q4=str(input('Ans: '))
    if q4 == 'C' or q4 =='c' or q4 =='Chennai Express' or q4 =='chennai express':
        print('Correct!✅')
        score+=1
    else:
       print('''oops wrong answer!❌ 
       The correct answer is "Chennai Express"''')

    print('-----------------------------------------')

    print('''Q5. What is the Name of Nana Patekar’s character in ‘WELCOME’ ?
    A. Majnu Shetty
    B. Nana Das
    C. Uday Shetty
    D. Santa Singh''')

    q5=str(input('Ans: '))
    if q5 == 'C' or q5 =='c' or q5 =='Uday Shetty' or q5 =='uday shetty':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
        The correct answer is "Uday Shetty"''')

    print('you Score is :',score)

    if score==2 or score==3:
        print('AMAZING PERFORMANCE!',name)
    elif score==4 or score==5:
        print('EXCELLENT!',name)
    else:
        print('HARD LUCK!',name, 'maybe try another category')

                                                          # SONGS

def song():
    global score
    print('Lets begin with Song Quiz!')

    print('-----------------------------------------')

    print('''Q1. Which movie is the song "bezubaan phir se" from
        A. ABCD 2
        B. Heropanti
        C. Dilwale
        D. The Sky Is Pink''')

    q1 = str(input('Ans: '))
    if q1 == 'A' or q1 == 'a' or q1 == 'ABCD 2' or q1 == 'abcd 2':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌
            The correct answer is "ABCD 2"''')

    print('-----------------------------------------')

    print('''Q2. Which Indian song won the oscar award in 2023? ?
        A. Badtameez dil
        B. Fukrey
        C. Naatu Naatu
        D. Raabta''')

    q2 = str(input('Ans: '))
    if q2 == 'C' or q2 == 'c' or q2 == 'Naatu Naatu' or q2 == 'naatu naatu':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
            The correct answer is "Naatu Naatu"''')

    print('-----------------------------------------')

    print('''Q3. What movie is the song "Locha-e-ulfat" from?
        A. 2 States
        B. Pathan
        C. Ki and Ka
        D. Ram Leela''')

    q3 = str(input('Ans: '))
    if q3 == 'A' or q3 == 'a' or q3 == ' 2 States' or q3 == ' 2 states':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
            The correct answer is " 2 States"''')

    print('-----------------------------------------')

    print('''Q4. Who is the singer of the song "Saiyaan" ?
        A. Atif Aslam
        B. Arijit Singh
        C. AR Rehman
        D. Kailash Kher''')

    q4 = str(input('Ans: '))
    if q4 == 'D' or q4 == 'd' or q4 == 'Kailash Kher' or q4 == 'kailash kher':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
           The correct answer is "Kailash Kher"''')

    print('-----------------------------------------')

    print('''Q5. Who is the singer of "tum hi ho" ?
        A. Sonu Nigam
        B. Darshan Raval
        C. Arijit Singh
        D. Tony Kakkar''')

    q5 = str(input('Ans: '))
    if q5 == 'C' or q5 == 'c' or q5 == 'Arijit Singh' or q5 == 'arijit singh':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
            The correct answer is "Arijit Singh"''')

    print('you Score is :', score)

    if score==2 or score==3:
        print('AMAZING PERFORMANCE!',name)
    elif score==4 or score==5:
        print('EXCELLENT!',name)
    else:
        print('HARD LUCK!',name, 'maybe try another category')

                                                     # APTITUDE

def apti():
    global score
    print('Lets begin with Aptitude Quiz!')

    print('-----------------------------------------')

    print('''Q1.What is the average of first five multiples of 12?
            A. 36
            B. 38
            C. 40
            D. 42''')

    q1 = str(input('Ans: '))
    if q1 == 'A' or q1 == 'a' or q1 == '36':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌
                The correct answer is "36"''')

    print('-----------------------------------------')

    print('''Q2.I saw a ...... of cows in the field.
           A. Group
           B. Herd
           C. Swarm
           D. Flock''')

    q2 = str(input('Ans: '))
    if q2 == 'D' or q2 == 'd' or q2 == 'Flock' or q2 == 'flock':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Flock"''')

    print('-----------------------------------------')

    print('''Q3. Today it is Thursday.After 132 days,it will be
          A. Monday
          B. Sunday
          C. Wednesday
          D. Thursday''')

    q3 = str(input('Ans: '))
    if q3 == 'C' or q3 == 'c' or q3 == 'Wednesdays' or q3 == 'wednesday':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Wednesday"''')

    print('-----------------------------------------')

    print('''Q4. 2, 6, 12, 20, 30, 42, 56, ?
           (A) 61
           (B) 64
           (C) 70
           (D) 72''')

    q4 = str(input('Ans: '))
    if q4 == 'D' or q4 == 'd' or q4 == '72':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
               The correct answer is "72"
               Explanation :
               The pattern is 1 x 2, 2 x 3, 3 x 4, 4 x 5, 5 x 6, 6 x 7, 7 x 8.
               So, the next number is 8 x 9 = 72.''')

    print('-----------------------------------------')

    print('''Q5. The grapes are now ...... enough to be picked.
            A. Ready
            B. Mature
            C. Ripe
            D. Advanced''')

    q5 = str(input('Ans: '))
    if q5 == 'C' or q5 == 'c' or q5 == 'Ripe' or q5 == 'ripe':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Ripe"''')

    print('you Score is :', score)

    if score==2 or score==3:
        print('AMAZING PERFORMANCE!',name)
    elif score==4 or score==5:
        print('EXCELLENT!',name)
    else:
        print('HARD LUCK!',name, 'maybe try another category')

                                                      # GK

def gk():
    global score
    print('Lets begin with GK Quiz!')

    print('-----------------------------------------')

    print('''Q1. Patanjali is well known for the compilation of –
         (a) Yoga Sutra
         (b) Panchatantra
         (c) Brahma Sutra
         (d) Ayurveda''')

    q1 = str(input('Ans: '))
    if q1 == 'A' or q1 == 'a' or q1 == 'Yoga Sutra' or q1 == 'yoga sutra':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌
                The correct answer is "Yoga Sutra"''')

    print('-----------------------------------------')

    print('''Q2. Tsunamis are not caused by
          (a) Hurricanes
          (b) Earthquakes
          (c) Undersea landslides
          (d) Volcanic eruptions''')

    q2 = str(input('Ans: '))
    if q2 == 'A' or q2 == 'a' or q2 == 'Hurricanes' or q2 == 'hurricanes':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Hurricanes"''')

    print('-----------------------------------------')

    print('''Q3. The hottest planet in the solar system?
           (a) Mercury
           (b) Venus
           (c) Mars
           (d) Jupiter''')

    q3 = str(input('Ans: '))
    if q3 == 'B' or q3 == 'b' or q3 == ' Venus' or q3 == ' venus':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Venus"''')

    print('-----------------------------------------')

    print('''Q4. Friction can be reduced by changing from
           A. Rolling to Sliding
           B. Sliding to Rolling
           C. Dynamic to Static
           D. Potential energy to Kinetic energy''')

    q4 = str(input('Ans: '))
    if q4 == 'A' or q4 == 'a' or q4 == 'rolling to sliding' or q4 == 'Rolling to Sliding':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
               The correct answer is "Rolling to Sliding"''')

    print('-----------------------------------------')

    print('''Q5. The biggest part of the brain is
           a) Spinal cord
           b) Cerebellum
           c) Cerebrum
           d) Brain Stem''')

    q5 = str(input('Ans: '))
    if q5 == 'C' or q5 == 'c' or q5 == 'Cerebrum' or q5 == 'cerebrum':
        print('Correct!✅')
        score+=1
    else:
        print('''oops wrong answer!❌ 
                The correct answer is "Cerebrum"''')

    print('you Score is :', score)

    if score==2 or score==3:
        print('AMAZING PERFORMANCE!',name)
    elif score==4 or score==5:
        print('EXCELLENT!',name)
    else:
        print('HARD LUCK!',name, 'maybe try another category')

def exit():
    global Game_running
    a = input("Do you want to exit this game? (Yes/No)")
    if a == "no" or a=='No':
        print("ok then, select category")
    else:
        Game_running = False

while Game_running==True:
    categories()
    cat=int(input("Enter your category: "))
    if cat==1 or cat=='Bollywood' or cat=='bollywood':
        bolly()
        exit()
    elif cat==2 or cat=='Songs' or cat=='songs':
        song()
        exit()
    elif cat==3 or cat=='Aptiude' or cat=='aptitude':
        apti()
        exit()
    elif cat==4 or cat=='GK' or cat=='gk' or cat=='General Knowledge' or cat=='general knowledge':
        gk()
        exit()
    else:
        print('INVALID Category!')