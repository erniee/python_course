import subprocess


def main() -> object:
    process = subprocess.Popen(['ls', '/'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    # print(out)
    # decode bytes to python string
    out = out.decode('utf-8')
    # print(out)
    # convert to python list
    out = out.split('\n')
    # print(out)
    for o in out:
        print(o)


if __name__ == "__main__":
    main()