import aircv as ac
from client import Client
from time import sleep, time

def locate_image(screenshot, reference, threshold = 0.8):
    print(f"Looking for {reference}")
    result = ac.find_template(screenshot, ac.imread(f"assets/{reference}"), threshold)
    return result['result'][:2] if result is not None else None

def keep_looking_for_image(client: Client, reference, timeout = 60):    
    start_time = time()
    location = None
    while location is None:            
        screenshot = client.capture_screen()
        location = locate_image(screenshot, reference)
        if location is None:
            sleep(5)
        if (time() - start_time > timeout):
            exception_text = f"Could not find {reference}"
            raise Exception(exception_text)
    return location