# ggGit <!-- omit in toc -->

***Fast Git commands with full support for Conventional Commits***

<div align="center">

&nbsp;

[![License: NIL](https://img.shields.io/badge/License-NIL-yellow.svg)](./LICENSE)
[![Contributor covenant: 3.0](https://img.shields.io/badge/Contributor%20Covenant-3.0-4baaaa.svg)](./CODE_OF_CONDUCT.md)
[![Semantic Versioning: 2.0.0](https://img.shields.io/badge/Semantic--Versioning-2.0.0-a05f79?logo=semantic-release&logoColor=f97ff0)](https://semver.org/)

[![Labeling](https://github.com/novafuria/ggGit/actions/workflows/labeling.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/labeling.yml)
[![Tests](https://github.com/novafuria/ggGit/actions/workflows/tests.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/tests.yml)
[![Liberation](https://github.com/novafuria/ggGit/actions/workflows/liberation.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/liberation.yml)
[![Deploy Release](https://github.com/novafuria/ggGit/actions/workflows/deploy-release.yml/badge.svg)](https://github.com/novafuria/ggGit/actions/workflows/deploy-release.yml)

[Bug Report](./issues/new?assignees=&labels=bug%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=1-bug-report.yml&title=...+is+broken)
⭕
[Feature Request](./issues/new?assignees=&labels=enhancement%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=2-feature-request.yml&title=As+a+%5Btype+of+user%5D%2C+I+want+%5Ba+goal%5D+so+that+%5Bbenefit%5D)
⭕
[Help Wanted](./issues/new?assignees=&labels=help+wanted%2Clifecycle%2Fneeds-triage&projects=novafuria%2F20&template=3-help-wanted.yml&title=I+need+help+with...)

[![Share on X](https://img.shields.io/twitter/url?label=Share%20on%20Twitter&style=social&url=https%3A%2F%2Fgithub.com%2Fatapas%2Fmodel-repo)](https://twitter.com/intent/tweet?text=👋%20Check%20this%20amazing%20repo%20https://github.com/novafuria/ggGit,%20created%20by%20@_novafuria%0A%0A%23Git%20%23Coding%20%23DevOps)

&nbsp;

</div>

&nbsp;

## ✋ Introducing `ggGit`

`ggGit` is a fast Git command line tool with full support for Conventional Commits. Contains a set of commands to help you to work with Git in a more efficient way and easy to understand.

Internally, `ggGit` uses the `git` command to execute the operations.


## Installation

The installation process is simple and fast. You need to clone the repository and add the Bash or PowerShell scripts path to the `PATH` environment variable.

### Install in Linux Systems

> [!NOTE]
> The installation process is the same for Bash emulation in Windows.

Clone the repository

```bash
git clone https://github.com/novafuria/ggGit
```

Add the path to the `PATH` environment variable in the `.bashrc` file

```bash
echo "export PATH=\$PATH:$(pwd)/ggGit/bash" >> ~/.bashrc
```

> [!NOTE]
> If you are using `zsh`, you need to add the path to the `PATH` environment variable in the `.zshrc` file.

Reload the `.bashrc` file

```bash
source ~/.bashrc
```

Check the installation

```bash
ggv
```

## Contributing

`/CONTRIBUTING.md`

This file contains the contributing guidelines. You can replace it with the contributing guidelines you want to use.

## Code of conduct

`/CODE_OF_CONDUCT.md`

This code is based on the covenant code. He is only required to specify an email address to the community to send his messages. Now, this email is [mauroa.alderete@novafuria.com](mailto:mauro.alderete@novafuria.com).

## License

`/LICENSE`

This file contains the MIT license. You can replace it with the license you want to use.
