
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto
# protoc -I=. --python_out=. ./addressbook.proto

# https://github.com/protocolbuffers/protobuf/tree/master/examples
# https://developers.google.com/protocol-buffers/docs/pythontutorial


# python sender.py ADDRESS_BOOK_FILE
# python receiver.py ADDRESS_BOOK_FILE