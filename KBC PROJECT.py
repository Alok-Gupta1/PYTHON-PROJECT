ques={'Which planet in the solar system is known as the Red Planet?':'c',
      'What is the capital of Japan?':'b',
      "Which river is the longest in the world?":'c',
      "What gas is used to extinguish fires?":'b',
      "Which animal is the national symbol of Australia?":'a',
      "Which of the following planets is not a gas giant?":'a',
      "What is the name of the process by which plants convert sunlight into energy?":'b',
      "In what year did the Great October Socialist Revolution take place?":'a',
      "What is the largest lake in the world?":'b',
      "Who wrote the novel War and Peace?":'c',
      "Which chemical element is designated as Hg?":'d',
      "In what year was the first international modern Olympiad held?":"a"}
option=[['Venus','earth','mars','jupiter'],
        ['beijing','tokyo','seoul','bangkok'],
        ['Amazon','mississipi','nile','yangtze'],
        ['oxygen','carbon dioxide','nitrogen','hydrogen'],
        ['kangaroo','koala','emu','crocodile'],
        ['mars','jupiter','saturn','uranus'],
        ['respiration','photosynthesis','oxidation','evolution'],
        ['1917','1923','1914','1920'],
        ['capsian sea','baikal','lake superior','ontario'],
        ['Anton chekhov','Fydor Dostoevsky','Leo Tolstoy','Ivan Turgenev'],
        ['silver','tin','copper','mercury'],
        ['1896','1900','1912','1924']]
m=0
l=0
money=['500','1000','2000','10000','20000','50000','100000','200000','500000','1000000','2500000','1 CRORE']
n=0
print('NAMASKAR DEVIYO AUR SAJJANO AAPKA SWAGAT H KON BANEGA CROREPATI MEIN')
for i in range(0,len(option)):
        for k,v in ques.items():
            print(k.title())
            print('(a)', option[n][0]    ,    '(c)', option[n][2])
            print('(b)', option[n][1]      ,  '(d)', option[n][3])
            ans=input('ENTER OPTION')
            if ans.lower()==v.lower():
                 print('CORRECT ANSWER')
                 print('ESSI KE SATH AAP JEET CHUKE HO RS.',money[m])
                 n+=1
                 m+=1
                 continue
            else:
                print('BADE HE DUKH KE SATH KEHNA PAD RHA H KI YE JAWAB GALAT H')
                if n in [3,4,5]:
                     print('AAPNE JEETA HAI RS.',money[3])
                     break
                elif n in [6,7,8]:
                     print('AAPNE JEETA HAI RS.',money[6])
                     break;
                elif n in [9,10,11]:
                     print('AAPNE JEETA HAI RS.',money[9])
                     break
                else:
                     print('AAPNE JEETA HAI RS.',0)
                     break
        break        
