# Introduction

This project will take an input from the user, of a filepath to examine.
It will iterate over any files or folders within the specified path, and output the results in JSON format.
Results will also show file size, in bytes.

## Usage

Command: `python dir_list.py </path/to/examine>`

Example Input: `python dir_list.py /home/lenny/Downloads`

Example Output:

```python
{
      "type": "file",
      "name": "/home/lenny/Projects/learningPython/dir_list.py",
      "size": "675 B"
    },
    {
      "type": "file",
      "name": "/home/lenny/Projects/learningPython/README.md",
      "size": "376 B"
}
```

## Assumptions

Code assumes you have the following modules in your Python environment:
`os`
`json`
`sys`