import time
from tqdm import tqdm


def run_progress_bar(sec):
    '''
    Function to display progress bar while training, classification,
    and/or training and classification processes execute.

            Parameter:
                sec: (int) number of seconds progress bar will run
    '''
    for index in tqdm(range(sec)):
        time.sleep(1)
    print('\n')
