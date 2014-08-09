from test_helper import run_common_tests, passed, failed, import_task_file, get_task_windows


def test_value():
    file = import_task_file()
    if file.exclamation == "!":
        passed()
    else:
        failed("Use negative index.")


def test_negative_index():
    window = get_task_windows()[0]
    if "-1" in window:
        passed()
    else:
        failed("Use -1 index to get the last character")

if __name__ == '__main__':
    run_common_tests()

    test_value()
    test_negative_index()
