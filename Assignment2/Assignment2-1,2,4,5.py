import OrderedDict
import csv

from collections import OrderedDict

class DataFrame(object):

    @classmethod
    def from_csv(cls, file_path, delimiting_character=',', quote_character='"'):
        with open(file_path, 'rU') as infile:
            reader = csv.reader(infile, delimiter=delimiting_character, quotechar=quote_character)
            data = []

            for row in reader:
                data.append(row)

            return cls(list_of_lists=data)



    def __init__(self, list_of_lists, header=True):
        for i in list_of_lists:
            i = str(i).strip()
            print list_of_lists

        if header:
            self.header = list_of_lists[0]
            self.data = list_of_lists[1:]
        else:
            self.header = ['column' + str(index + 1) for index, column in enumerate(list_of_lists[0])]
            self.data = list_of_lists

            #Task1
            if len(set(self.header)) != len(self.header):
                raise Exception('Found a duplicate')
            else:
                print "good to go"
            #Task2
            self.data = [map(lambda z: z.strip(), row) for row in self.data]
            self.data = [OrderedDict(zip(self.header, row)) for row in self.data]


        self.data = [OrderedDict(zip(self.header, row)) for row in self.data]


    def __getitem__(self, item):
        # this is for rows only
        if isinstance(item, (int, slice)):
            return self.data[item]

        # this is for columns only
        elif isinstance(item, (str, unicode)):
            return [row[item] for row in self.data]

        # this is for rows and columns
        elif isinstance(item, tuple):
            if isinstance(item[0], list) or isinstance(item[1], list):

                if isinstance(item[0], list):
                    rowz = [row for index, row in enumerate(self.data) if index in item[0]]
                else:
                    rowz = self.data[item[0]]

                if isinstance(item[1], list):
                    if all([isinstance(thing, int) for thing in item[1]]):
                        return [[column_value for index, column_value in enumerate([value for value in row.itervalues()]) if index in item[1]] for row in rowz]
                    elif all([isinstance(thing, (str, unicode)) for thing in item[1]]):
                        return [[row[column_name] for column_name in item[1]] for row in rowz]
                    else:
                        raise TypeError('What the hell is this?')

                else:
                    return [[value for value in row.itervalues()][item[1]] for row in rowz]
            else:
                if isinstance(item[1], (int, slice)):
                    return [[value for value in row.itervalues()][item[1]] for row in self.data[item[0]]]
                elif isinstance(item[1], (str, unicode)):
                    return [row[item[1]] for row in self.data[item[0]]]
                else:
                    raise TypeError('I don\'t know how to handle this...')

        # only for lists of column names
        elif isinstance(item, list):
            return [[row[column_name] for column_name in item] for row in self.data]

    def get_rows_where_column_has_value(self, column_name, value, index_only=False):
        if index_only:
            return [index for index, row_value in enumerate(self[column_name]) if row_value==value]
        else:
            return [row for row in self.data if row[column_name]==value]

    #Task4
    def add_rows(self,list_of_lists):
        col_count = len(self.header)
        if sum([len(row) == col_count for row in list_of_lists]) == len(list_of_lists):
            self.data = self.data +[OrderedDict(zip(self.header, row)) for row in list_of_lists]
            return self
        else:
            raise Exception('incorrect  number')

    #Task5
    def add_columns(self,list_of_values,columnn_name):
        if len(list_of_values)==len(self.data):
            self.header = self.header + column_name
            self.data = [OrderedDict(zip(list(old_row.keys()) + column_name,list(old_row.values()) + added_values))
                         for old_row, added_values in zip(self.data, list_of_values)]
            return self
        else:
            raise Exception('incorrect number')

        

