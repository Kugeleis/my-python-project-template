from my_python_project_template import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from my-python-project-template!\n"
