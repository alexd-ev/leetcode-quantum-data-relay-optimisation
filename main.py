#!/usr/bin/env python3

import sys
from quantum_data_relay import optimise_relay


def main() -> int:
    # Example Input: 3 data streams producing unsorted data packets
    stream_1 = [10, 5, 3]
    stream_2 = [7, 14, 2]
    stream_3 = [4, 18, 1]
    raw_streams = [stream_1, stream_2, stream_3]
    boxes = 2
    
    result = optimise_relay(raw_streams, boxes)
    
    print(f"Sorted Streams: {raw_streams}")
    print(f"Maximum Total Compression Value: {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
