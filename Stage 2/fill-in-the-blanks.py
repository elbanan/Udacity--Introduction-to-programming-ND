# This is my code for stage 2 final project : my own quiz (Mohamed Elbanan, 2/28/2016)


#list of paragraphs for each level
strings = ["__1__ is an interesting branch in clinical sciences. It was discovered in 1895 by german physicist __2__. For nearly a century afterwards, __1__ consisted only of plain __3__ films. Nowadays, we have computed __4__ machines as well as other modalities.",
           "The __1__  tomography machine was introduced in the 1970s. It uses multiple __2__ tubes to construct a multi-angle image of the body. These tubes __3__ around the body in an extremely fast speed. Data acquired from __1__ tomography scanners need special __4__ software to re-construct it into readable images.",
           "Magnetic __1__ imaging was discovered in the 1980s. It uses __2__ signals to obtain images of different body parts depending on concentration of __3__ atom in them. It became one of the most of the widely used __4__ modalities nowadays."]

#list of answers per each level
answers = [["radiology", "rontgen", "x-ray", "tomography"],["computed", "x-ray","rotate","computer"],["resonance", "magnetic","hydrogen","imaging"]]

#list of names of missing words
missing_words = ["__1__", "__2__", "__3__", "__4__"]

#list of available levels
levels = ["easy","medium","hard"]


print '''
 ______________________________
| Welcome to My Radiology Quiz |
|______________________________|

  '''


#This is the module for selecting game difficulty

def level_selector ():
    user_input_level = (raw_input ("Please select game difficulty level: easy, medium, or hard : ")).lower()
    level_string = ' '
    while user_input_level in levels :
        string_index = levels.index(user_input_level)
        level_string = strings[string_index]
        list = [user_input_level , level_string]
        print "You selected "+user_input_level+ " !"
        return list
    else:
        print "Sorry, this level is not available"
        return level_selector ()




#This is the module for selecting the number of attempts

def attempts_selector ():
    attempts = int(raw_input("Please enter the number of attempts for each word: "))
    if attempts <=0 :
        print "Please enter a positive number"
        return attempts_selector()
    else:
        return attempts





level_selector_output = level_selector()                            # returns output of level selector function
game_level = level_selector_output[0]                               # selects gamel level from level selector function
level_string = level_selector_output[1]                               # selects level text from level selector function
allowed_attempts = attempts_selector ()                             # returns allowed attempts from attempts selector
level_specific_answers = answers[levels.index(game_level)]          # selects answers depending on game level




print '''
Please complete the missing words in the following paragraph:
'''




#Main game module

def game():
    output = level_string
    print output
    for word in missing_words:
        attempts = 1
        while attempts <= allowed_attempts:
            user_input_answer = (raw_input("Please enter your answer for "+ word + " : ")).lower()
            answer_index = int((word.translate(None,"_")))-1
            if user_input_answer == level_specific_answers [answer_index]:
                output =  output.replace(word,user_input_answer)
                print output
                break
            else:
                print "That's not a correct answer. Please try again. Only "+str(allowed_attempts-attempts)+" attempts are left "
                attempts = attempts+1
        else:
            exit()





# runs the game module

game()











