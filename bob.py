def hey(phrase):
    if phrase.endswith("?"):
        return('Sure.')
    elif phrase.isupper():
        if phrase.endswith("!") or phrase.endswith(""):
            return('Whoa, chill out!')
        elif phrase.endswith("?"):
            return('Calm down, I know what i\'m doing!')
    elif not phrase:
        return('Fine. Be that way!')
    else:
        return('Whatever.')
hey('')
