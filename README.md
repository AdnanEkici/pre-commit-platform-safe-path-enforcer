# pre-commit-platform-safe-path-enforcer
This pre-commit hook flags hard-coded path separators in Python code to enhance cross-platform compatibility. It recommends os.path.join or os.sep over '/' or '\'.
