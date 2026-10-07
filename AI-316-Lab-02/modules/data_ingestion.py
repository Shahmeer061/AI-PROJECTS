
class DataIngestion:
    """
    Handles camera/video input and provides frames to the AI pipeline.
    """

    def __init__(self, source: str):
        self.source = source

    def start_stream(self) -> bool:
        """Start the camera or video stream."""
        pass

    def get_frame(self):
        """Capture and return the next video frame."""
        pass

    def stop_stream(self) -> None:
        """Stop the video stream."""
        pass
