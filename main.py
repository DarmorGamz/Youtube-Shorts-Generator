import sys
from typing import NoReturn

print(
    """
 __     _________    _____ _    _  ____  _____ _______    _____ ______ _   _ 
 \ \   / /__   __|  / ____| |  | |/ __ \|  __ \__   __|  / ____|  ____| \ | |
  \ \_/ /   | |    | (___ | |__| | |  | | |__) | | |    | |  __| |__  |  \| |
   \   /    | |     \___ \|  __  | |  | |  _  /  | |    | | |_ |  __| | . ` |
    | |     | |     ____) | |  | | |__| | | \ \  | |    | |__| | |____| |\  |
    |_|     |_|    |_____/|_|  |_|\____/|_|  \_\ |_|     \_____|______|_| \_|                                                   
"""
)


def main() -> None:
    pass

def shutdown() -> NoReturn:
    print("Exiting...")
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        shutdown()
    except Exception as err:
        raise err
