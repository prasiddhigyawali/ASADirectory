import pandas

if __name__ == "__main__":
    memeberDirectory = []
    with open('sample.txt') as f:
        lines = f.readlines()
    for l in lines:
        member = l.split(" ");
        memeberDirectory.append(member)
