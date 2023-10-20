import base64
import sys


def encode(data):
    try:
        encoded = base64.b64encode(data.encode()).decode()
        print("Encoded:", encoded)
    except Exception as e:
        print(f"Error encoding: {e}")


def decode(data):
    try:
        decoded = base64.b64decode(data).decode()
        print("Decoded:", decoded)
    except Exception as e:
        print(f"Error decoding: {e}")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python base64_tool.py -e <data>")
        print("  python base64_tool.py -d <data>")
        sys.exit(1)

    action = sys.argv[1]
    data = sys.argv[2]

    if action == "-e":
        encode(data)
    elif action == "-d":
        decode(data)
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()
