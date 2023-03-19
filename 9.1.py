def initiation():
    """
    Set all the parameter needed.
    
    Returns:
    guess_log -- a empty list container of all the guesses.
    answer -- a 4-digital number string of right answer.
    """
    import random
    
    print('Welcome to the Cows and Bulls Game!')
    guess_log = ['']
    answer = random.randint(0,9999)
    answer = '{0:04d}'.format(answer)
    return guess_log, answer

def get_guess(guess_log):
    """
    Append a new guess to the previous log.
    
    Arguments:
    guess_log -- a list contain all the guess(es).
    
    Returns:
    guess_log -- a list contain all the guess(es).
    """
    guess = input('Enter a number:')
    guess_log.append(guess)
    return guess_log

def compare(guess, answer):
    """
    Compare guess and answer
    
    Arguments:
    guess -- a 4-digital number string of the guess.
    answer -- a 4-digital number string of right answer.
    
    Returns:
    cow -- a number of the user guessed correctly in the correct place.
    bull -- a number of the user guessed correctly in the wrong place.
    """
    cow = 0
    bull = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            cow += 1
        if guess[i] in answer:
            bull += 1 
    bull = bull - cow
    return cow, bull

def main():
    guess_log, answer = initiation()
    while guess_log[-1] != answer:
        guess_log = get_guess(guess_log)
        cow, bull = compare(guess_log[-1], answer)
        print('{} cows, {} bulls'.format(cow, bull))
    print('Your are right! After {} guess(es) you finally get it!\nYour logs:'.format(len(guess_log)-1), guess_log[1:])
              
if __name__ == "__main__":
    main()