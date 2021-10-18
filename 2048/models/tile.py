class Tile:
    def __init__(self, value, merged_once):
        self.value = value
        self.merged_once = merged_once
    
    def get_value(self):
        """Gets the value corresponding a given tile

        Arguments:
            None

        Returns:
            int: Value corresponding a given tile
        """
        return self.value

    def set_value(self, value):
        self.value = value

    def is_merged_once(self):
        return self.merged_once
    
    def set_merged_once(self, merged):
        """Sets the merged_once value

        Returns:
            bool: Returns id the tile is merged once
        """
        self.merged_once = merged
