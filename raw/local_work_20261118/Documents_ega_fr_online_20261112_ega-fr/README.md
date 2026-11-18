# Local work saved on 18 November 2026: `Documents_ega_fr_online_20261112_ega-fr`

Work that existed only in a local clone (`Documents\ega_fr_online_20261112\ega-fr`), found by the scan of 18 Nov 2026 and saved here as raw material. Not reviewed; nothing is merged.

- `uncommitted.patch` (116,195 bytes): uncommitted changes of the working tree and index (git diff HEAD).

## How to apply

- A patch: on the clone's branch, `git apply uncommitted.patch` (or `stash0.patch`).
- The bundle: `git bundle verify local.bundle`, then `git fetch local.bundle 'refs/heads/*:refs/remotes/rescued/*'`.
- Untracked files: `tar -xzf untracked.tar.gz` at the root of the working tree.
