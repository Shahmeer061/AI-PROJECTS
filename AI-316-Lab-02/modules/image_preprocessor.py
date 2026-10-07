
class ImagePreprocessor:
    """
    Prepares raw camera frames for AI model inference.
    """

    def __init__(self, target_size: tuple):
        self.target_size = target_size

    def resize(self, frame):
        """Resize the input frame."""
        pass

    def normalize(self, frame):
        """Normalize image pixel values."""
        pass

    def preprocess(self, frame):
        """Perform complete preprocessing."""
        pass
