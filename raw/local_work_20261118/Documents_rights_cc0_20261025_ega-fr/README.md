# Local work saved on 18 November 2026: `Documents_rights_cc0_20261025_ega-fr`

Work that existed only in a local clone (`Documents\rights_cc0_20261025\ega-fr`), found by the scan of 18 Nov 2026 and saved here as raw material. Not reviewed; nothing is merged.

- `uncommitted.patch` (15,163 bytes): uncommitted changes of the working tree and index (git diff HEAD).
- `stash0.patch` (125,215 bytes): the newest stash (git stash show -p stash@{0}).

## How to apply

- A patch: on the clone's branch, `git apply uncommitted.patch` (or `stash0.patch`).
- The bundle: `git bundle verify local.bundle`, then `git fetch local.bundle 'refs/heads/*:refs/remotes/rescued/*'`.
- Untracked files: `tar -xzf untracked.tar.gz` at the root of the working tree.
