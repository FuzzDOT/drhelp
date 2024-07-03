## Project File Structure

The project file structure for the `drhelp` project is as follows:

```
drhelp
├── src
│   ├── appLogic
│   │   ├── description.md
│   │   ├── backEnd
│   │   │   ├── models
│   │   │   │   ├── input
│   │   │   │   ├── processing
│   │   │   │   └── output
│   │   │   ├── static
│   │   │   ├── __pycache__
│   │   │   ├── main.py
│   ├── webApp
├── .github
├── CHANGELOG.md
├── LICENSE.md
├── README.md
└── SECURITY.md
```

The `drhelp` project consists of the following directories and files:

- `src`: This directory contains the main source code of the project.
    - `appLogic`: This directory contains the application logic code.
        - `description.md`: This file contains the description of the appLogic module.
        - `backEnd`: This directory contains the backend code.
            - `models`: This directory contains the models for the chatbot.
                - `input`: This directory contains the input-related code.
                - `processing`: This directory contains the processing-related code.
                - `output`: This directory contains the output-related code.
            - `static`: This directory contains the served static files for the backend.
            - `__pycache__`: This directory contains the cached Python bytecode.
            - `main.py`: This file contains the FastAPI framework for the backend.
    - `webApp`: This directory contains the web application code.
- `.github`: This directory contains the GitHub-related files and configurations.
- `CHANGELOG.md`: This file contains the project's changelog.
- `LICENSE.md`: This file contains the project's license information.
- `README.md`: This file contains the project's README documentation.
- `SECURITY.md`: This file contains the project's security information.

