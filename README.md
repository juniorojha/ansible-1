# Install Ansible
Follow this - https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html 

# Configure
See config variables in the file playbooks/roles/git_update/defaults/main.yml

GITHUB_BASE_URL
This is the base URL for the repo. For repos hosted on github.com, this will be 'https://github.com'.
For a bare repo on, say 52.79.239.222, this will be 'ssh://root@52.79.239.222:'
For the latter case, make sure you have passwordless ssh auth from that location and don't forget the colon at the end.

GITHUB_REPO_NAME
This is the complete repo name. For repos hosted on github.com, include the username too, e.g. 'aiegoo/hanuman'
For bare repos, this is the full path e.g. 'root/repos/project.git'.
Please note that a '/' is automatically added preceding this value to conjunct correctly with GITHUB_BASE_URL.

GITHUB_LOCALDIR
Path where the repo should be cloned in the target server
Default branch to clone
GITHUB_DEFAULT_BRANCH
Branch of the repo to be cloned

Next, configure the list of servers in playbooks/inventory.ini
Comment out the [localhost] and add each new server in a new block, e.g.,

[vm1]
ip_addr ansible_connection=ssh ansible_user=user ansible_ssh_private_key_file=/home/user/.ssh/id_rsa

Make sure the servers you add here with ansible_connection=ssh allow passwordless ssh connection from the machine where you run ansible.
To enable this, follow this guide https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login

# Run
Make sure the file server-update-ansible is executable
Then simply ./server-update-ansible <repo-name>

