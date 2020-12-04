class File:
    def __init__(self):
        self.__name = None

    def get_file_name(self):
        '''Returns attribute name.'''

        return self.__name

    def set_file_name(self, name):
        '''Sets attribute name to the given value if the file exists, otherwise to empty string.'''

        if name=='cos_img':
            self.__name = name
            return True

        try:
            file = open(name, 'r')
            file.close()
            self.__name = name
            image_path = name
            print("setting filename to: {}. ".format(name))
            return True
        except:
            self.__name = ''
            print("setting filename to: <empty>. ")
            return False
