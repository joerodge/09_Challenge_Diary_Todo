import math

#TODO intergrate TodoList into Diary

class Diary:

    def __init__(self):
        self.entries = []
        self.contacts = {}
        self.entry_index = 0


    def add(self, entry):
        """Parameters:
            entry: an instance of DiaryEntry
        Returns:
            Nothing
        Side-effects:
            Adds the entry to the entries list"""
        if type(entry) == DiaryEntry:
            self.entries.append(entry)


    def all(self):
        """Returns:
            A list of instances of DiaryEntry"""
        return self.entries
    

    def read_next(self):
        """Returns:
            A string of next entry to be read. Next time it
            is called it returns the next one. Format '{title:contents}' """
        entry_to_be_read = self.entries[self.entry_index]
        self.entry_index += 1

        # Start reading from the start again after last entry is read
        if self.entry_index == len(self.entries):
            self.entry_index = 0

        return f"{entry_to_be_read.title}: {entry_to_be_read.contents}"


    def read_all(self):
        """Returns:
            A string of all entries separated by newline"""
        return '\n'.join([f"{entry.title}: {entry.contents}" for entry in self.entries])


    def count_all_words(self):
        """Returns:
            An integer representing the number of words in all diary entries"""
        return sum(entry.count_words() for entry in self.entries)


    def reading_time(self, wpm):
        """Parameters:
            wpm: an integer representing the number of words the user can read
                per minute
        Returns:
            An integer representing an estimate of the reading time in minutes
            if the user were to read all entries in the diary."""
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")
        
        return math.ceil(self.count_all_words() / wpm)


    def find_best_entry_for_reading_time(self, wpm, minutes):
        """Parameters:
                wpm: an integer representing the number of words the user can
                    read per minute
                minutes: an integer representing the number of minutes the user has
                    to read
            Returns:
                An instance of DiaryEntry representing the entry that is closest to,
                but not over, the length that the user could read in the minutes
                they have available given their reading speed."""
        no_of_words = wpm * minutes
        closest_count = 0
        best_entry = None
        for entry in self.entries:
            if no_of_words > entry.count_words() > closest_count:
                best_entry = entry
                closest_count = entry.count_words()

        return best_entry
    
    def add_contact(self, name, number):
        """Params:
            A str representing the name of the contact
            A str representing the phone number of the contact
                (str rather than int because it will have a leading 0 or +)
        Returns:
            None
        Side effects:
            Adds contact to contacts dict. key=name, value=number"""
        self.contacts[name] = number

    def get_contacts(self):
        """Returns:
            A str of all contacts separated by new line
            formatted '{name}: {number}' """
        return '\n'.join([f"{name}: {number}" for name, number in self.contacts.items()])



class DiaryEntry:

    def __init__(self, title, contents): # title, contents are strings
        """Side-effects:
            Sets the title and contents properties"""
        self.title = title
        self.contents = contents
        self.words = contents.split()
        self.word_count = len(self.words)
        self.index = 0


    def count_words(self):
        """Returns:
            An integer representing the number of words in the contents"""
        return len(self.contents.split())


    def reading_time(self, wpm):
        """Parameters:
                wpm: an integer representing the number of words the user can read
                    per minute
            Returns:
                An integer representing an estimate of the reading time in minutes
                for the contents at the given wpm."""
        if wpm <= 0:
            raise Exception("WPM must be greater than 0")
        
        return math.ceil(self.count_words() / wpm)


    def reading_chunk(self, wpm, minutes):
        """Parameters:
                wpm: an integer representing the number of words the user can read
                    per minute
                minutes: an integer representing the number of minutes the user has
                    to read
        Returns:
            A string representing a chunk of the contents that the user could
            read in the given number of minutes.
            If called again, `reading_chunk` should return the next chunk,
            skipping what has already been read, until the contents is fully read.
            The next call after that it should restart from the beginning."""
        chunk_size = wpm * minutes
        text_chunk = ' '.join(self.words[self.index:self.index + chunk_size])
        self.index += chunk_size
        
        # Loop round to start reading from the start again if all text read
        if self.index >= self.word_count:
            self.index = 0
            
        return text_chunk

