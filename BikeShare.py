
# this project use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City,
import pandas as pd
import time
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
       
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ' '
    while(city.lower() not in CITY_DATA):
        city = input('\nHello! Let\'s explore some US bikeshare data! \n'
                     'Wanna see the data for Chicago, New York city, or Washington?\n')
        city = city.lower()
        if city not in CITY_DATA:
            print('Sorry, Your input is not valid. Please pick a valid city from Chicago, New York city, or Washington.')
        else:
            break
            
    # get user input for month (all, january, february, ... , june)
    month = ' '
                        
    while(month.lower() not in months):
        month = input('\nEnter name of month (jan, feb, mar, apr, may, jun) to explore the data:')
        month = month.lower()
        if month not in months:
            print('Sorry, I do not understand your input. Please type in a month between Jan and Jun')
        else:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ' '
    while(day.lower() not in days):
        day = input('\n Enter the day of week (monday, tuesday, so on....) to explore the data: ')
        day = day.lower()
        if day not in days:
            print('\n Sorry, I do not understand your input. Please enter a correct day of the week. Try again..')
        else: 
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
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    month = months.index(month) + 1
    
    # filter by month to create new dataframe
    df = df[df['month'] == month]

    # filter by day of week to create the new dataframe
    df = df[df['day_of_week'] == day.title()]        
    

    return df

def GPA():
    print("5 out of 3")
def  Description():
    print("this is my first project for me in data analysis")   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The month picked is:', months[df['month'].mode()[0] - 1].title())

    
    # display the most common day of week
    print('The most common day of week:', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('The most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station: ', df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    num_trips = df.groupby(['Start Station', 'End Station']).size()
    print('The most frequent combination of start station and end station trip:\n', num_trips[num_trips == num_trips.max()])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # display mean travel time
    print("\nMean travel time:", df['Trip Duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # Since Gender and birth year of washington is not in the CSV file, exception being handled.
    if city == 'washington':
        print('\n The Gender and Birth Year information is not available for Washington.')
    else:    
        # Display counts of gender
        print('\nCounts of gender:\n', df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('\nThe Earliest year of birth: ', int(df['Birth Year'].min()))
        print('\n Most common year of birth: ', int(df['Birth Year'].mode()[0]))
        print('\n The latest year of birth: ', int(df['Birth Year'].max()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        while True:
            show_data = input('\nDo you want to explore the raw data? Enter yes or no.: \n')
            if show_data.lower() != 'yes':
                break
            else:
                print('\nAfter applying filters, the dataset for {} contains {} rows.'.format(city,df.shape[0]))
                print('The raw data is displayed below as requested.\n', df.head(5))
                head = 0
                tail = 5
                while True:
                    display_more = (input('\n Do u want to display more data.? Enter yes or no.: \n '))
                    if display_more.lower() == 'yes':
                        head += 5
                        tail += 5
                        print(df[df.columns[0:-1]].iloc[head:tail])
                    elif display_more.lower() == 'no':
                        break
                break
                        
        


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


     
