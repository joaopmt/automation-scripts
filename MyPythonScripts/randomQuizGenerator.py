#! /usr/bin/python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico':
    'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
    'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Generate 35 quiz files
for quizNum in range(35):
    # create the quiz file and answer key file
    quizFile = open('capitalsQuiz%d.txt' %(quizNum + 1), 'w')
    answerKeyFile = open('capitalsQuiz_ans%d' %(quizNum + 1), 'w')
    # create a header for the student to fill
    quizFile.write('Name:\n\nDate:\n\nRA:\n\n')
    quizFile.write(''*20 + 'State Capitals Quiz (Num %d)' %(quizNum + 1))
    quizFile.write('\n\n')
    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]  # get the correct answer from the dict
        wrongAnswers = list(capitals.values())  # get a list of all answers (capitals/values)
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # del the correct answer from the list
        wrongAnswers = random.sample(wrongAnswers, 3)  # get a sample of size 3 from the list
        answerOptions = wrongAnswers + [correctAnswer]  # join the correct ans with the wrong answers
        random.shuffle(answerOptions)  # randomize the list so the correct ans isnt always D
        # Write the question and the answer options to the quiz file.
        quizFile.write('%d. What is the capital of %s?\n\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('  %s. %s\n' %('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' %(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

    
