from utils.Section import Section


def test_parse_tasks():
    mock_tasks = ["- Test",
                  "\t- Test 1",
                  "\t\t+ Test 2",
                  "\t\t\t - Test 3"]
    tasks = Section().parse_tasks(mock_tasks)
    assert len(tasks) == 1
    assert tasks[0].message == "Test"
    assert tasks[0].complete == False
    assert tasks[0].level == 0

    assert len(tasks[0].subtasks) == 1
    assert tasks[0].subtasks[0].message == "Test 1"
    assert tasks[0].subtasks[0].complete == False
    assert tasks[0].subtasks[0].level == 1

    assert len(tasks[0].subtasks[0].subtasks) == 1
    assert tasks[0].subtasks[0].subtasks[0].message == "Test 2"
    assert tasks[0].subtasks[0].subtasks[0].complete == True
    assert tasks[0].subtasks[0].subtasks[0].level == 2

    print(tasks[0].subtasks[0].subtasks[0])
    assert len(tasks[0].subtasks[0].subtasks[0].subtasks) == 1
    # assert tasks[0].subtasks[0].subtasks[0].subtasks[0].message == "Test 3"
    # assert tasks[0].subtasks[0].subtasks[0].subtasks[0].complete == False
    # assert tasks[0].subtasks[0].subtasks[0].subtasks[0].level == 3
