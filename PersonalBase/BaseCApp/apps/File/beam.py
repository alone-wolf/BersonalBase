class FileNodeCode:
    def __init__(self, filename_original, file_type, note):
        self.FilenameOriginal = filename_original
        self.FileType = file_type  # text binary
        self.Note = note

    def to_object(self):
        return self.__dict__
