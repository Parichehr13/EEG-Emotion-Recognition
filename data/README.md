# Local Dataset Instructions

This repository is configured to keep large raw datasets out of normal Git history.

## Recommended Setup

Keep the original dataset on your machine, for example:

`D:\emotion\Dataset`

Then expose it inside this repository through a local folder path such as:

`data\Dataset`

On Windows, you can create a junction so the repository can access the dataset without duplicating the files:

```powershell
New-Item -ItemType Junction -Path .\data\Dataset -Target "D:\emotion\Dataset"
```

## Why This Setup

- avoids pushing heavy dataset files to GitHub
- keeps repository clones smaller and faster
- makes it easier to share code without redistributing restricted datasets

## If You Really Need GitHub Storage

If you later decide to upload the dataset, use Git LFS instead of regular Git for large files.
