# CircusCircus
This is a minimal forum written in python with Flask. It supports only the bare minumum of features to allow discussions, including user accounts, threads, and comments.

On first run, the default subforums will be created. Although custom subforums are not supported through any user interface, it is possible to modify forum/setup.py to create custom subforums.

## Features Added

  - Ability to like each post
  - Added photo upload option when creating posts.
  - New logo and theme, inspired by the fashion sense of a certain individual.
  - Users can now add about me pages, which also show their post history. Relevant links added in templates.
  - Posts can be marked public or private, with private requiring a user to sign in to view.
  - Markdown is available for posts, about me sections, and comments.

## Features to Add

- dislike/heart/etc emojis on posts
- direct messages from one user to another. IM system WIP with plenty of progress.
- insert video links
- additional user settings


This currently puts a sqlite3 db in the /tmp directory.

```
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./run.sh
```

and it should appear on port 5000

`http://0.0.0.0:5000`
