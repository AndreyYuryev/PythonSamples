import progressbar
import time

progress = progressbar.ProgressBar()
for i in progress(range(80)):
    time.sleep(0.1)