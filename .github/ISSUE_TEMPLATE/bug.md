---
name: Bug Report
about: Report a bug
labels: bug
---

## What happened?

## What should've happened instead?

## Additional details

<!-- To assist you best, please include commands that you've run, options you've selected and any relevant logs -->

- Host system configuration:

  - Version of devxhub_python CLI (get it with `devxhub_python --version`):
  - OS name and version:

    On Linux, run

    ```bash
    lsb_release -a 2> /dev/null || cat /etc/redhat-release 2> /dev/null || cat /etc/*-release 2> /dev/null || cat /etc/issue 2> /dev/null
    ```

    On MacOs, run

    ```bash
    sw_vers
    ```

    On Windows, via CMD, run

    ```
    systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
    ```

    ```bash
    # Insert here the OS name and version

    ```

  - Python version, run `python3 -V`:
  - Docker version (if using Docker), run `docker --version`:
  - docker-compose version (if using Docker), run `docker-compose --version`:
  - ...

- Options selected and/or [replay file](https://devxhub_python.readthedocs.io/en/latest/advanced/replay.html):
  On Linux and macOS: `cat ${HOME}/.devxhub_python_replay/devxhub_python-django.json`
  (Please, take care to remove sensitive information)

```json

```

<summary>
Logs:
<details>
<pre>
$ devxhub_python https://github.com/devxhub_python/devxhub_python-django
project_name [Project Name]: ...
</pre>
</details>
</summary>
