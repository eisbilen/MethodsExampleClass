import pandas as pd
import random

PATH = "/Users/erdemisbilen/Lessons/"
FILE_NAME_01 = "data_by_artists.csv"
FILE_NAME_02 = "data_by_genres.csv"

class CSVGetInfo:
    """ This class displays the summary of the tabular data contained in a CSV file """
    instance_count = 0

    # Initializer / Instance Attributes
    def __init__(self, path, file_name):
        CSVGetInfo.increase_instance_count()
        self.path = path
        self.file_name = file_name

    # Instance Method
    def display_summary(self):
        data = pd.read_csv(self.path + self.file_name)
        print(self.file_name)
        print(data.head(self.generate_random_number(10)))
        print(data.info())

    # Class Method
    @classmethod
    def increase_instance_count(cls):
        cls.instance_count += 1
        print(cls.instance_count)

    @classmethod
    def read_file_1(cls):
        return cls("/Users/erdemisbilen/Lessons/", "data_by_artists.csv")
    
    @classmethod
    def read_file_2(cls):
        return cls("/Users/erdemisbilen/Lessons/", "data_by_genres.csv")

    # Static Methods
    @staticmethod
    def generate_random_number(limit):
        return random.randint(1, limit)
        

if __name__ == '__main__':

    data_by_artists = CSVGetInfo.read_file_1()
    data_by_genres = CSVGetInfo.read_file_2()

    data_by_artists.display_summary()
    data_by_genres.display_summary()
    
