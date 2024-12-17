# Todo4NFDI

- This Documentation is licenced under the Creative Commons CC-BY-SA-4.0 licence.

## Local development
Clone the repository via git, either via ssh or via https:

Install the requirements via python.
```bash
py -m pip install -r requirements.txt
```

Run a local watchdog and http server to generate a temporary build of the latest revision.
```bash
(cd config; mkdocs serve)
```

Access the resulting URL via your web browser. You will now see the website update anytime you make changes.

If you are satisfied with your changes, create a new branch (choose an appropriate name as a replacement for `MY_NEW_BRANCH_NAME`) and request a merge.

```bash
git config --local user.name "Your name"
git config --local user.email "Your email (you may use the commit email in your GitLab profile)"
git stash
git checkout -b MY_NEW_BRANCH_NAME
git stash pop
git add *
# you could describe all changes in all files via 
git commit -am "Describe your changes here" 
# you're also welcome to
# describe your changes per file, using:
git commit -m "Describe your changes here"  <file>
git push
```
