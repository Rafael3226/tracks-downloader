from concurrent.futures import ThreadPoolExecutor

from constants import MAX_WORKERS

thread_pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
