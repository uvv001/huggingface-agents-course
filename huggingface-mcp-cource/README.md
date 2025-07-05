# The 🤗 Model Context Protocol (MCP) Course
Source https://huggingface.co/learn/mcp-course/unit0/introduction

# Prepare environment

## Install tools

```shell
# uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# pnpm
curl -fsSL https://get.pnpm.io/install.sh | sh -
source ~/.bashrc

# download and activate Node.js LTS
pnpm env use --global lts
```

## Install dependencies

```shell
uv sync
```

## Run script or file

```shell
uv run -- mcp dev 1000_mcp_sdk_intro.py
```
