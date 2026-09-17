# System & Tooling Discovery Audit: Agent Runtime Environment

## 1. Native Function Tools

The following table lists the internal LLM tools and APIs available for the agent to interact with the system, modify code, and manage the workflow:

| Tool / Function Name | Parameters / Signature | Description |
|----------------------|-----------------------|-------------|
| `list_files` | `path: STRING` | Lists all files and directories under the given directory. |
| `read_file` | `filepath: STRING` | Reads the content of the specified file in the repository. |
| `write_file` | `filepath: STRING, content: STRING` | Creates a new file or overwrites an existing file. |
| `delete_file` | `filepath: STRING` | Deletes the specified file. |
| `rename_file` | `filepath: STRING, new_filepath: STRING` | Renames and/or moves files and directories. |
| `replace_with_git_merge_diff` | `filepath: STRING, merge_diff: STRING` | Performs targeted search-and-replace using a Git merge diff block. |
| `run_in_bash_session` | `command: STRING` | Runs bash commands in a persistent sandbox session (always rooted at repo root). |
| `view_image` / `read_image_file` / `read_media_file` | `url: STRING` / `filepath: STRING` | Tools to view online images, or read local image and video media for context. |
| `google_search` | `query: STRING` | Searches Google online to retrieve up-to-date information. |
| `view_text_website` | `url: STRING` | Fetches the content of a website as plain text for context and docs. |
| `set_plan` | `plan: STRING` | Sets or updates the markdown-formatted execution plan. |
| `plan_step_complete` | `message: STRING` | Marks a plan step as complete with an explanatory message. |
| `pre_commit_instructions` | (none) | Retrieves steps required prior to submitting code. |
| `submit` | `branch_name: STRING, commit_message: STRING, description: STRING, title: STRING` | Commits changes and initiates a PR submission workflow. |
| `message_user` / `request_user_input` | `message: STRING`, `continue_working: BOOLEAN` | Tools for communicating with or requesting explicit input/clarification from the user. |
| `reset_all` / `restore_file` | `filepath: STRING` | Tools for reverting changes locally or entirely. |
| `frontend_verification_instructions` / `start_live_preview_instructions` | (none) | Instructions for UI/frontend testing setup. |
| `frontend_verification_complete` | `screenshot_path: STRING, additional_media_paths: ARRAY` | Asserts UI checks have succeeded with proof. |

> *Note: Legacy/deprecated tools (`grep`, `create_file_with_block`, `overwrite_file_with_block`) are omitted as they are superseded by `run_in_bash_session` and `write_file`.*

## 2. Environment Specifications

The underlying sandbox container environment was inspected via bash session:

- **OS & Kernel**: Linux devbox 6.8.0 #1 SMP PREEMPT_DYNAMIC x86_64 GNU/Linux.
- **User Permissions**: Running as user `jules` (uid=1001, gid=1001). Privileged access is available via membership in `sudo` (27) and `docker` (103) groups.
- **Mounted Volumes**: 
  - Root `/` operates on overlayfs (`/dev/vdb`).
  - `/dev` on devtmpfs.
  - `/run` on tmpfs.
  - Temporary and user directories are present and writable (`/run/user/1001`).
- **Available CLI Binaries**:
  - `python3`: `/home/jules/.pyenv/shims/python3`
  - `node`: `/home/jules/.nvm/versions/node/v22.22.1/bin/node`
  - `git`: `/usr/bin/git`
  - `curl`: `/usr/bin/curl`
  - `jq`: `/usr/bin/jq`
  - *Note: `gh` (GitHub CLI) is not installed by default.*

## 3. Web & Search Capabilities

The agent has unrestricted outward-bound internet access for information gathering:

- **Network Reachability**: The environment possesses direct internet access (tested against `https://google.com`, which returns expected HTTP 301/200 responses).
- **Search Wrapper**: `google_search` enables structured retrieval of current search results, returning snippets and top URLs.
- **Web-Fetching Capabilities**: `view_text_website` can perform HTTP GET requests to fetch raw textual content from reachable URLs, ideal for pulling documentation or plaintext files not indexed directly.
- **CLI Fallback**: `curl` and `wget` (if needed) are fully usable within the bash sandbox, giving alternative ways to pull API payloads, HTML, or JSON.
