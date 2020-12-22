class Probability():
    def pairs(self, diction):
        combin = {}
        combin['prob_pairs'] = 0
        combin['pocked'] = 0
        tablecards = [diction['tablecard' + str(i)] for i in range(1, 6)]
        tablebefore = [card[:-1] for card in tablecards if card != '?']
        print('pairs' + str(tablebefore))
        free_pos = 5 - sum([1 for i in tablecards if i != '?'])
        if diction['card1'][:-1] == diction['card2'][:-1]:
            combin['card'] = diction['card1'][:-1]
            combin['prob_pairs'] = 1
            combin['pocked'] = 1
            combin['prob_all'] = 1
            return combin
        elif len(set(tablebefore)) != len(tablebefore):
            for tablecard in tablebefore:
                if tablebefore.count(tablecard) > 1:
                    combin['card'] = tablecard
                    combin['prob_pairs'] = 1
                    combin['prob_all'] = 1
                    return combin
        else:
            for card in [diction['card1'], diction['card2']]:
                if tablebefore.count(card[:-1]) == 1:
                    combin['card'] = card
                    combin['pocked'] = 0
                    combin['prob_pairs'] = 1
                    combin['prob_all'] = 1
                    return combin
                combin['prob_pairs'] += 3 / (52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
        combin['prob_all'] = combin['prob_pairs'] + 3 / (
                52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos * (5 - free_pos)
        return combin

    def two_pairs(self, diction):
        combin = {}
        combin['prob_two_pairs'] = 0
        tablecards = [diction['tablecard' + str(i)] for i in range(1, 6)]
        tablebefore = [card[:-1] for card in tablecards if card != '?']
        free_pos = 5 - sum([1 for i in tablecards if i != '?'])
        pairs = self.pairs(diction)
        if pairs['pocked'] == 1:
            if len(set(tablebefore)) != len(tablebefore):
                combin['prob_two_pairs'] = 1
                combin['prob_all'] = 1
                return combin
            else:
                combin['prob_two_pairs'] = 3 / (52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
                combin['prob_all'] = combin['prob_two_pairs'] * (5 - free_pos)
                return combin
        else:
            if tablebefore.count(diction['card1'][:-1]) == 1 and tablebefore.count(diction['card2'][:-1]) == 1:
                combin['prob_two_pairs'] = 1
                combin['prob_all'] = 1
                return combin
            elif (tablebefore.count(diction['card1'][:-1]) == 1 or tablebefore.count(diction['card1'][:-1])):
                if len(set(tablebefore)) != len(tablebefore):
                    combin['prob_two_pairs'] = 1
                    combin['prob_all'] = 1
                    return combin
                else:
                    combin['prob_two_pairs'] = 3 / (52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
                    combin['prob_all'] = combin['prob_two_pairs'] * (4 - free_pos)
                    return combin
            elif len(set(tablebefore)) != len(tablebefore):
                for tablecard in tablebefore:
                    if tablebefore.count(tablecard) == 2 and len(
                            [card for card in tablebefore if card != tablecard]) != len(
                        set([card for card in tablebefore if card != tablecard])):
                        combin['prob_two_pairs'] = 1
                        combin['prob_all'] = 1
                        return combin
                combin['prob_two_pairs'] = 3 / (52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
                combin['prob_all'] = combin['prob_two_pairs'] * (4 - free_pos)
                return combin
            else:
                if free_pos <= 1:
                    combin['prob_all'] = 0
                    return combin
                else:
                    combin['prob_two_pairs'] += 3 / (
                            52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos * 3 / (
                                                        52 - (5 - free_pos)) * free_pos
                    combin['prob_all'] = combin['prob_two_pairs'] * (5 - free_pos)
                    return combin

    def sets(self, diction):
        combin = {}
        combin['prob_set'] = 0
        combin['pocked'] = 0
        tablecards = [diction['tablecard' + str(i)] for i in range(1, 6)]
        tablebefore = [card[:-1] for card in tablecards if card != '?']
        free_pos = 5 - sum([1 for i in tablecards if i != '?'])
        print('set' + str(tablebefore))
        pairs = self.pairs(diction)
        if pairs['prob_pairs'] == 1 and tablebefore.count(pairs['card'][:-1]) == 1:
            combin['prob_set'] = 1
            combin['prob_all'] = 1
            return combin
        elif len(set(tablebefore)) == 5 - free_pos - 2 and self.two_pairs(diction)['prob_two_pairs'] != 1:
            combin['prob_set'] = 1
            combin['prob_all'] = 1
            return combin
        elif len(set(tablebefore)) == 5 - free_pos - 2 and self.two_pairs(diction)['prob_two_pairs'] == 1:
            combin['prob_set'] += 2 / (52 - 1 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
            combin['prob_all'] = combin['prob_set'] * 2
            return combin
        else:
            for card in [diction['card1'], diction['card2']]:
                if tablebefore.count(card[:-1]) == 2:
                    combin['prob_set'] = 1
                    combin['prob_all'] = 1
                    return combin
                else:
                    for tablecard in tablecards:
                        if tablebefore.count(card[:-1]) == 2:
                            combin['prob_set'] = 1
                            combin['prob_all'] = 1
                            return combin
                        elif card[:-2] == tablecard[:-1]:
                            combin['prob_set'] += 2 / (
                                    52 - 1 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos
                        else:
                            combin['prob_set'] += 3 / (
                                    52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos * 2 / (
                                                          52 - 1 - (5 - free_pos) + (
                                                          diction['players'] - 1) * 2) * free_pos
        if free_pos == 2:
            combin['prob_all'] = combin['prob_set'] + 3 / (
                    52 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos * 2 / (
                                         52 - 1 - (5 - free_pos) + (diction['players'] - 1) * 2) * free_pos * (
                                         5 - free_pos)
            return combin
        else:
            combin['prob_all'] = combin['prob_set']
            return combin

    def street(self, diction):
        # street= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        combin = {}
        combin['prob_street'] = 0
        combin['prob_all'] = 0
        combin['pocked'] = 0
        tablecards = [diction['tablecard' + str(i)] for i in range(1, 6)]
        tablecards.append(diction['card1'])
        tablecards.append(diction['card2'])
        tablebefore = [card[:-1] for card in tablecards if card != '?']
        print('street' + str(tablebefore))
        for i in range(len(tablebefore)):
            if tablebefore[i] == 'A':
                if '2' not in tablebefore and 2 not in tablebefore:
                    tablebefore[i] = 14
                else:
                    tablebefore[i] = 1
            if tablebefore[i] == 'Q':
                tablebefore[i] = 12
            if tablebefore[i] == 'Q':
                tablebefore[i] = 12
            if tablebefore[i] == 'J':
                tablebefore[i] = 11
            else:
                tablebefore[i] = int(tablebefore[i])
        print('street' + str(tablebefore))
        free_pos = 5 - sum([1 for i in tablecards if i != '?'])
        len_street = 1
        maxlen = 1
        setcards = list(set(tablebefore))
        for i in range(len(setcards) - 1):
            if int(setcards[i]) == int(setcards[i + 1]) - 1:
                len_street += 1
                if len_street > maxlen:
                    maxlen = len_street
            else:
                len_street = 1
        if maxlen == 5:
            combin['prob_all'] = 1
        elif 5 - maxlen < free_pos:
            combin['prob_all'] = 0
        else:
            combin['prob_all'] = sum(
                [3 / (52 - i + 1 - (5 - free_pos) + (diction['players'] - 1) * 2) for i in range(1, 6 - maxlen)]) * 2
        return combin

    def flash(self, diction):
        # street= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        combin = {}
        combin['prob_flash'] = 0
        combin['prob_all'] = 0
        combin['pocked'] = 0
        tablecards = [diction['tablecard' + str(i)] for i in range(1, 6)]
        tablecards.append(diction['card1'])
        tablecards.append(diction['card2'])
        tablebefore = [card[-1] for card in tablecards if card != '?']
        print(tablebefore)
        free_pos = 7 - sum([1 for i in tablecards if i != '?'])
        len_flash = 1
        maxlen = 1
        for suit in tablebefore:
            len_street = tablebefore.count(suit)
            if len_street > maxlen:
                maxlen = len_street
        if maxlen == 5:
            combin['prob_all'] = 1
        elif 5 - maxlen > free_pos:
            print('here')
            combin['prob_all'] = 0
        else:
            combin['prob_all'] = 1
            for i in range(free_pos):
                combin['prob_all'] *= (13 - i - maxlen) / (52 - i + 1 - (5 - free_pos) + (diction['players'] - 1) * 2)
        return combin
