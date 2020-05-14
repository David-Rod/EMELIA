import time
from tqdm import tqdm


def run_progress_bar(num_sec):
    '''
    Function to display progress bar while training, classification,
    and/or training and classification processes execute.

    Parameter:

    num_sec: number of seconds (int) for the progress bar to run
    '''
    for index in tqdm(range(num_sec)):
        time.sleep(1)
    print('\n')
