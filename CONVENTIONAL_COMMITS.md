# Conventional Commits

This project follows the conventional commits specification for commit messages. Conventional commits provide a standardized format for commit messages, making it easier to understand the history of the project.

## Commit Types

1. **feat:** (new feature for the user, not a new feature for build script)
   - Example: `feat: add user authentication`

2. **fix:** (bug fix for the user, not a fix to a build script)
   - Example: `fix: resolve issue with data not saving`

3. **docs:** (changes to the documentation)
   - Example: `docs: update installation instructions`

4. **refactor:** (refactoring code, e.g., renaming a variable)
   - Example: `refactor: improve code readability in module`

5. **chore:** (routine tasks, maintenance, or tooling changes)
   - Example: `chore: update dependencies`

6. **style:** (code style changes, e.g., formatting)
   - Example: `style: apply consistent indentation`

7. **test:** (adding or modifying tests)
   - Example: `test: add unit tests for utility functions`

## Commit Message Format

Each commit message should have the following format:
```bash
<type>(<scope>): <description>
[optional body]
[optional footer]
```


- **type:** The type of change (e.g., feat, fix, docs).
- **scope:** (optional) The scope of the change (e.g., module name).
- **description:** A concise and clear description of the change.
- **body:** (optional) Additional details or context.
- **footer:** (optional) Closing issues or referencing related pull requests.


