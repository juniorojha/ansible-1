- [5. script in the server is triggered to update the app codes and restart the webserver](#5-script-in-the-server-is-triggered-to-update-the-app-codes-and-restart-the-webserver)
- [> Github: each project has its webhook service registered under the repo's setting](#github-each-project-has-its-webhook-service-registered-under-the-repos-setting)
- [webhook settings](#webhook-settings)
- [webhook service creation](#webhook-service-creation)
- [webhook sh file](#webhook-sh-file)
      - [DIRECTORY TO THE REPOSITORY](#directory-to-the-repository)
  - [based on the following repo](#based-on-the-following-repo)


Welcome to the ansible wiki!
### process overview
![webHook](https://user-images.githubusercontent.com/56853822/68566552-072bb100-049a-11ea-84e6-6e3f585b5e1c.png)

> Five steps to automate management of multi-sites (besides ci tools such as Jenkins or Team City)
1. source codes are pushed to a <u>private remote repository</u>
2. gh-release or use of git flow [gitflow](git-flow_cheatsheet.md)
3. webhook processes the receipt of tag generation and services the event
4. webhook service triggers applicable scripts based on the tag information (shell script per repo)
5. script in the server is triggered to update the app codes and restart the webserver
---
> Webhook service: prepare scripts targeted to the server or servers \
> Web Server: should be connected to the git repo on ssh \
> Github: each project has its webhook service registered under the repo's setting
---
:checkered_flat: Example of gh-release
`“scripts”: {
  “release”: “node_modules/.bin/gh-release -t $VER -n $VER -c master -b init”
}`

:warning: how to automate this process as well instead of entering the version number manually to the file 

## webhook settings
1. payload URL
2. Content type
  -- application/json
  -- application/x-www-form-urlencoded
3. Secret
  -- either hard coded in the file or enter the passwd here
4. Which events would you like to trigger the webhook?
  -- Branch or tag creation / releases / deploy

## webhook service creation
> index.js (webhook service application)
  [webhook index.js](https://github.com/aiegoo/ansible/blob/ansible/index.js)

## webhook sh file 
> example 1 (./filename.sh)

`#!/bin/bash
##### DIRECTORY TO THE REPOSITORY
REPOSITORY=”/var/www/virtualhosts/returnvalues-academy/frontend”
echo $1 >> logs/returnvalues-academy-$1.txt
cd $REPOSITORY
VER=$1 npm run www:webhook
`

> example 2 (package.json)

`
“scripts”: {
  “www:webhook”: “git fetch origin refs/tags/$VER:refs/tags/$VER && git checkout $VER”
},
`

### based on the following repo
[returnvalues](https://github.com/returnvalues/webhook-public)

##git-flow 

[git flow commands]
![gitflow](https://user-images.githubusercontent.com/56853822/68566802-b8cae200-049a-11ea-930b-127a8e8373f3.png)

:clapper:
[1]: https://github.com/aiegoo/ansible/blob/develop/git-flow_cheatsheet.md
