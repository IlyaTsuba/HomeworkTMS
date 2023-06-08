class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"You have soda with {self.taste} taste."
        else:
            return "You have soda with no taste."

