from itertools import count
from queue import Empty, Queue
from time import sleep


request_queue: Queue[int] = Queue()
request_ids = count(1)


def generate_request() -> int:
    """Create a request with a unique ID and add it to the queue."""
    request_id = next(request_ids)
    request_queue.put(request_id)
    print(f"Generated request #{request_id}.")
    return request_id


def process_request() -> int | None:
    """Process the oldest request, or report that the queue is empty."""
    try:
        request_id = request_queue.get_nowait()
    except Empty:
        print("The request queue is empty.")
        return None

    print(f"Processed request #{request_id}.")
    request_queue.task_done()
    return request_id


def main() -> None:
    print("Service center simulation. Press Ctrl+C to exit.")

    try:
        while True:
            generate_request()
            process_request()
            sleep(1)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")


if __name__ == "__main__":
    main()
