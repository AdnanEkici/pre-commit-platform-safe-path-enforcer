# Pre-commit Safe Path Enforcer

This pre-commit hook is designed to enhance the portability of Python code by flagging instances of hard-coded path separators in string literals that are likely to represent file paths. It suggests the use of `os.path.join` or `os.sep` for better cross-platform compatibility.

## Motivation

Different operating systems use different characters as path separators (`/` for Unix/Linux, and `\\` for Windows). Using hard-coded path separators can therefore cause issues when your code is run on different operating systems.

By checking for hard-coded path separators at commit time, this pre-commit hook helps to prevent potential file path issues before they enter your codebase.

## Usage

1. First, ensure that you have pre-commit installed. If not, you can install it using pip:

    ```bash
    pip install pre-commit
    ```

2. Add the following to your `.pre-commit-config.yaml` file:

    ```yaml
       repos:
        - repo: https://github.com/AdnanEkici/pre-commit-platform-safe-path-enforcer
          rev: v0.0.1
          hooks:
            - id: pre-commit-platform-safe-path-enforcer
              name: 'Check Path Separator'
              entry: hooks/check_paths.py
              language: script
              types: [python]
    ```

3. Run pre-commit:

    ```bash
    pre-commit run --all-files
    ```

If the hook finds any hard-coded path separators in your Python files, it will output a message and fail, preventing the commit. You can then fix the issue before retrying the commit.

## Suppressing Warnings

If there's a particular line of code where you want to intentionally use a hard-coded path separator, you can suppress the warning from this pre-commit hook by appending `# noqa` at the end of the line. This tells the hook to ignore this line.

For example:

```python
path = 'path/to/folder'  # noqa
```

## Contributing

Contributions to this pre-commit hook are welcome. If you find a bug or have a suggestion for improvement, please open an issue or pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Upcoming Features

In the next version (0.0.2) of my Pre-commit Safe Path Enforcer hook, I am planning to introduce the following features and improvements:

- **Enhanced detection**: I aim to improve the accuracy of path detection to further minimize false positives.

- **Performance optimization**: I will be optimizing the script to reduce the overall time it takes to check larger codebases.

- **Expanded language support**: I plan to extend our hook to support more programming languages beyond Python.

- **Exclude List Improvement**: I am working on making the `exclude` feature more intuitive and robust, making it easier to specify files or folders that you want the hook to skip.

- **Customization options**: I am planning to introduce more customization options so that users can better tailor the tool to their needs.

- **Unit Tests**: - **Unit Tests**: I understand the importance of reliability in a tool like ours. 
  That's why I have introduced unit tests to ensure the integrity of our code. 
  With the upcoming 0.0.2 version, Check Path Separator pre-commit hook becomes more reliable with comprehensive unit tests designed to cover a wide range of scenarios and edge cases. 
  These tests help us to prevent regressions, ensure the quality of our work, and move towards updates and improvements with confidence. 
  They make our hook more robust and dependable, providing users with the reassurance that the tool will perform consistently.

Stay tuned for these updates!
