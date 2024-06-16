def title_case(title, minor_words=''):
    
    words = title.lower().split(' ')

    check_m_words = {word.lower() for word in minor_words.split(' ')}

    for i, w in enumerate(words):
        if i == 0 or w not in check_m_words:
            words[i] = w.title()


    words = ' '.join(words)
    print(words)

title_case('THE WIND IN THE WILLOWS', 'The In')