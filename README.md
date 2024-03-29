python-packer
=============

A Python interface for [packer.io](http://www.packer.io)

## Compatibility

| Python Packer Release | Packer Release |
| --------------------- | -------------- |
| v1.0.0                | v1.7.4         |
| v1.0.1                | v1.7.4         |
| v1.0.2                | v1.7.4         |
| v1.0.3                | v1.7.4         |
| v1.0.4                | v1.7.4         |
| v1.0.5                | v1.7.4         |
| v1.0.6                | v1.7.4         |

## Installation

You must have Packer installed prior to using this client though as installer class is provided to install packer for you.

```shell
pip install git+https://github.com/abhi1693/python-packer@main
```

## Usage Examples

### [Packer.build()](https://www.packer.io/docs/command-line/build.html)

```python
import packer

template = 'path/to/template'
exc = []
only = ['my_first_image', 'my_second_image']
vars = {"variable1": "value1", "variable2": "value2"}
var_file = 'path/to/var/file'
packer_exec_path = '/usr/bin/packer'

p = packer.Packer(template=template, exc=exc, only=only, vars=vars,
                  var_file=var_file, exec_path=packer_exec_path)
p.build(parallel=True, debug=False, force=False)
```


### [Packer.fix()](https://www.packer.io/docs/command-line/fix.html)

```python
...

p = packer.Packer(template, ...)
output_file = '/tmp/template_fixed.json'
print(p.fix(output_file))
```

The `output_file` parameter will write the output of the `fix` function to a file.


### [Packer.inspect()](https://www.packer.io/docs/command-line/inspect.html)

A `-machine-readable` (mrf) argument is provided.

If the `mrf` argument is set to `True`, the output will be parsed and an object containing the parsed output will be exposed as a dictionary containing the components:

```python
import packer

p = packer.Packer(template, ...)
result = p.inspect(mrf=True)
print(result.parsed_output)
# print(result.stdout) can also be used here
```

```json
"variables": [
  {
    "name": "aws_access_key",
    "value": "{{env `AWS_ACCESS_KEY_ID`}}"
  },
  {
    "name": "aws_secret_key",
    "value": "{{env `AWS_ACCESS_KEY`}}"
  }
],
"provisioners": [
  {
    "type": "shell"
  }
],
"builders": [
  {
    "type": "amazon-ebs",
    "name": "amazon"
  }
]
```

If the `mrf` argument is set to `False`, the output will not be parsed but rather returned as is:

```python
...

p = packer.Packer(template, ...)
result = p.inspect(mrf=True)
print(result.stdout)

# output:
Optional variables and their defaults:

  aws_access_key          = {{env `AWS_ACCESS_KEY_ID`}}
  aws_secret_key          = {{env `AWS_ACCESS_KEY`}}

Builders:

  amazon                   (amazon-ebs)

Provisioners:

  shell

...

```


### [Packer.push()](https://www.packer.io/docs/command-line/push.html)

You must be logged into Atlas to use the `push` function:

```python
...

p = packer.Packer(template, ...)
atlas_token = 'oi21mok3mwqtk31om51o2joj213m1oo1i23n1o2'
p.push(create=True, token=atlas_token)
```

### [Packer.validate()](https://www.packer.io/docs/command-line/validate.html)

```python
...

p = packer.Packer(template, ...)
p.validate(syntax_only=False)
```

### Packer.version()

```python
...

p = packer.Packer(template, ...)
print(p.version())
```

### PackerInstaller.install()

This installs packer to `packer_path` using the `installer_path` and verifies that the installation was successful.

```python

packer_path = '/usr/bin/'
installer_path = 'Downloads/packer_1.7.4_linux_amd64.zip'

p = packer.Installer(packer_path, installer_path)
p.install()
```

## Shell Interaction

The [sh](http://amoffat.github.io/sh/) Python module is used to execute Packer.
As such, return values from all functional methods (`validate`, `build`, etc..) other than the `version` method
will return an `sh` execution object. This is meant for you to be able to read stdout, stderr, exit codes and more after executing the commands. With the progression of `python-packer` less abstract objects will return and more concise return values will be provided.

Additionally, to verify that all errors return with as much info as possible, error handling is done gently. Most errors will raise an `sh` exception so that you're able to interact with them. Again, as this module progresses, these exceptions will be handled properly.


## Testing

Tests have not been developed yet.

```shell
git clone git@github.com:abhi1693/python-packer.git
cd python-packer
pip install tox
tox
```

## Contributions..

..are always welcome.
