class Greeter(object):

    def __init__(self, message):
        """Creates a new :class:`HelloSphinx` instance.

        :param message: a suitable greeting message
        :type message: str
        """
        self.message = message

    def speak(self):
        """Prints the message back to the user.
        """
        print self.message