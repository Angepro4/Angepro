beurs = open('symbolen.txt','w')
beurs.write('YAHOO:YHOO\nGOOGLE INC:GOOG\nHarley-Davidson:HOG\nYamana Gold:AUY\nSotheby’s:BID\ninBev:BUD\n')
beurs.close()

def ticker():
    infile = open('symbolen.txt')
    inhoud = infile.readlines()
    infile.close()
    ticker_dict = {}

    for regel in inhoud:
        tickerinfo = regel.split(':')

        bedrijfsnaam = tickerinfo[0]
        symbol = tickerinfo[1]

        ticker_dict[symbol] = bedrijfsnaam

        return ticker_dict

    tickers = ticker()
    name = input('Enter company name:')
    for item in ticker.items():
        if item[1] == name:
            print('Ticker symbol:'+item[0])
        symbol = input('Enter ticker symbol:')
        print('Bedrijfsnaam'+ tickers[symbol])









