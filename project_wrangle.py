# This is a wrangle file used for my mini time series project

def get_info(df):
    '''
    This function takes in a dataframe and prints out information about the dataframe.
    '''

    print(df.info())
    print()
    print('------------------------')
    print()
    print('This dataframe has', df.shape[0], 'rows and', df.shape[1], 'columns.')
    print()
    print('------------------------')
    print()
    print('Null count in dataframe:')
    print('------------------------')
    print(df.isnull().sum())
    print()
    print('------------------------')
    print(' Dataframe sample:')
    print()
    return df.sample(3)


def value_counts(df, column):
    '''
    This function takes in a dataframe and list of columns and prints value counts for each column.
    '''
    for col in column:
        print(col)
        print(df[col].value_counts())
        print('-------------')



def time_series_split_data(df):
    '''
    This function takes in a dataframe and splits it into a train, validate, and test set
    with respect to time
    '''
    
    # assign lengtgs of each dataframe
    train_size = int(len(df) * 0.6)
    validate_size = int(len(df) * 0.3)
    test_size = int(len(df) - train_size - validate_size)
    
    validate_end_index = train_size + validate_size
    
    # assign rows to each dataframe
    train = df[:train_size]
    validate = df[train_size:validate_end_index]
    test = df[validate_end_index:]
    
    return train, validate, test


def verify_split_graph(train, validate, test):
    '''
    This function takes in three split dataframes and graphs them to verify the split was done correctly
    '''
    for col in train.columns:
        plt.figure(figsize=(12,4))
        plt.plot(train[col])
        plt.plot(validate[col])
        plt.plot(test[col])
        plt.ylabel(col)
        plt.title(col)
        plt.show()

