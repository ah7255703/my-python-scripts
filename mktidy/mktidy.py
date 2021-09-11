'Files Archiver'
import os
import glob
import shutil


class Folder():
    def __init__(self):
        self.__dirname = None
        self.files = None
        self.__file_types = []
        self.this_file_name = os.path.basename(__file__)

    def dir_name(self):
        self.__dirname = os.path.dirname(__file__)
        return self.__dirname

    def dir_files(self):
        dir_path = self.__dirname
        self.files = os.listdir(dir_path)

    def file_types(self):
        Folder.dir_name(self)
        Folder.dir_files(self)
        for item in self.files:
            try:
                type = item.split('.')[-1]
                if type not in self.__file_types:
                    self.__file_types.append(type)
            except:
                pass
        return self.__file_types

    def make_dirs(self):

        for typ in self.__file_types:
            destinition_dir = rf'{self.__dirname}/{typ}-files'
            try:
                os.makedirs(rf'{self.__dirname}/{typ}-files')
            except FileExistsError:
                print('Cannot create a file when that file already exists')
                pass

            for file in glob.glob(f'{self.__dirname}/*.{typ}'):
                if os.path.basename(file) != self.this_file_name:
                    shutil.move(file, destinition_dir)


folder = Folder()
folder.file_types()
folder.make_dirs()
