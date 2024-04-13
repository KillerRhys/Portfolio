""" Lotto Linter
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.07.23-1049 """
import datetime
import tkinter
import urllib.request
import pandas as pd


# VARS
version = 1.1
current_year = datetime.datetime.today().year
target_year = current_year - 5


# Get csv data for last five years of drawings.
def get_nums():
    mega_millions_url = ('https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/'
                         'megamillions.csv')
    power_ball_url = 'https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv'
    urllib.request.urlretrieve(mega_millions_url, f'data/mm{current_year}.csv')
    urllib.request.urlretrieve(power_ball_url, f'data/pb{current_year}.csv')
    mega_millions_data = pd.read_csv(f'data/mm{current_year}.csv')
    power_ball_data = pd.read_csv(f'data/pb{current_year}.csv')
    header_list = ['Lotto', 'Month', 'Day', 'Year', 'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'MegaPower', 'Multiply']
    mega_millions_data.to_csv(f'data/mm{current_year}.csv', header=header_list, index=False)
    power_ball_data.to_csv(f'data/pb{current_year}.csv', header=header_list, index=False)
    mega_millions = pd.read_csv(f'data/mm{current_year}.csv')
    mega_million = mega_millions[mega_millions['Year'] >= target_year]
    power_balls = pd.read_csv(f'data/pb{current_year}.csv')
    power_ball = power_balls[power_balls['Year'] >= target_year]

    # Create list for Frequently used | Rarely used numbers.
    mega_list_common = []
    mega_list_rare = []
    power_list_common = []
    power_list_rare = []

    # Use Pandas to build and fill list by most and least used.
    fetch = ['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'MegaPower']
    for item in fetch:
        s = mega_million[item].value_counts()
        highest = s.index[0]
        lowest = s.index[-1]
        mega_list_common.append(highest)
        mega_list_rare.append(lowest)
        # pick = mega_million[item].mode().iloc[0]
        # mega_list.append(pick)

    for item in fetch:
        s = power_ball[item].value_counts()
        highest = s.index[0]
        lowest = s.index[-1]
        power_list_common.append(highest)
        power_list_rare.append(lowest)
        # pick = power_ball[item].mode().iloc[0]
        # power_list.append(pick)

    mega_label['text'] = f'Mega Millions: {mega_list_common} || {mega_list_rare}'
    power_label['text'] = f'Power Ball: {power_list_common} || {power_list_rare}'


# Display GUI with tkinter.
display = tkinter.Tk()
display.title(f'Lotto Linter {version}')
display.configure(bg='black')
display.minsize(width=600, height=200)
mega_label = tkinter.Label(text='Mega Millions!', font=('Arial', 24, 'bold'), bg='black', fg='teal')
power_label = tkinter.Label(text='Power Ball', font=('Arial', 24, 'bold'), bg='black', fg='teal')
magic_button = tkinter.Button(text='Got dem nums?', command=get_nums, bg='black', fg='purple',
                              font=('Arial', 24, 'bold'))
mega_label.pack()
power_label.pack()
magic_button.pack()


display.mainloop()
