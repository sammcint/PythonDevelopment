import time
import pandas as pd
import numpy as np
E
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturdayr', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please enter chicago, new york city or washington: ")
        if city.lower() in CITY_DATA.keys():
            city = city.lower()
            break

    #get user input for month (all, january, february, ... , june)
    monthly_analysis = input ("Do you want to search by month? Please answer yes or no: ")
    if monthly_analysis == 'no':
        month = 'all'
    else:
        while True:
            month = input("Please the month you'd like to chose from january, february, march, april, may or june in lower case format: ")
            if month.lower() in months:
                month = month.lower()
                break
    #get user input for day of week (all, monday, tuesday, ... sunday)
    day_analysis = input ("Do you want to search by day? Please answer yes or no: ")
    if day_analysis == 'no':
        day = 'all'
    else:
        while True:
            day = input("Please the month you'd like to chose in lower case format. Please answer sunday, monday, tuesday, wednesday, thursday, friday or saturday: ")
            if day in days:
                day
                break
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    #if there is a month filter, we need to assign the month to the right integer (i.e. January = 1) for purposes of analysis
    if month != "all":
        month = months.index(month)+1
        df = df[df['month'] == month]
    #filtered by day and we need to capitalize it given the
    if day != "all":
        df = df[df['day']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Common Month:', popular_month)

    #Display the most common day of week
    popular_day = df['day'].mode()[0]

    print('Most Popular Start Day:', popular_day)

    #Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Display most commonly used start station
    popular_StartStation = df['Start Station'].mode()[0]
    print('Most Popular Start Station:{}'.format(popular_StartStation))

    #Display most commonly used end station
    popular_EndStation = df['End Station'].mode()[0]
    print('Most Popular End Station:{}'.format(popular_EndStation))

    #Display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time:{} '.format(travel_time))

    #Display mean travel time
    avg_duration = (df['Trip Duration'].mean())
    print('Average travel time:{} '.format(avg_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts of user types:\n{} '.format(user_type))

    #Display counts of gender
    gender = df['Gender'].value_counts()
    print('Counts of genders:\n{} '.format(gender))

    #Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    most_recent = int(df['Birth Year'].max())
    most_common = int(df['Birth Year'].mode()[0])
    print('Earlist common year of birth:{} '.format(earliest))
    print('Most recent year of birth:{} '.format(most_recent))
    print('Most common year of birth:{} '.format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
