import time
from tqdm import tqdm


def run_progress_bar(num_sec):
    for index in tqdm(range(num_sec)):
        time.sleep(1)
    print('\n')
