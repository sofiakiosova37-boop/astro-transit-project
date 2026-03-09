from lightkurve import search_targetpixelfile

def get_kepler_data(target_id="KIC 6922244", q=4):
    pixelfile = search_targetpixelfile(target_id, author="Kepler", cadence="long", quarter=q).download()
    return pixelfile

def plot_frame(pixelfile, frame_number=42):
    """Малює графік конкретного кадру."""
    pixelfile.plot(frame=frame_number)
# from lightkurve import TessTargetPixelFile
# import lightkurve as 1k
# import numpy as np
# pixelFile = search_targetpixelfile("KIC 6922244", author="Kepler", cadence="long", quarter=4).download()
# pixelFile.plot(frame=42)