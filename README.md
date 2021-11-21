# User_create_unix/Password_reset_unix
Performs the creation and setting required User ID attributes in Unix systems(Linux and AIX). 


__Summary__: Will automate UNIX user creation using Ansible CACF. It can set password, perform password reset and update all user realted attributes. Gives an Option to send reset password via email


__Features__: 
1. The user can decide whether to specify a group for the user to be a member of and can decide to create that group if create_group is set to Yes, and it gives the user to interactively pass multiple arguments and parameters required for User ID creation for Linux and Linux systems

2. Handles all the chuser options for the user attributes to be set or updated for AIX servers user ID7s

3. Set or reset a user's password.
It can manage the password setting and reset of password of a user.
Python script used for generating random password and passed as a secure variable to the playbook as per IBm security standards, have  option for same initial password for multiple user id's or unique password for each user ID

4. Option to send the user's password securely to user by email after user creation.

__Requirements:__
1. Need to pass the User Id's as a list of dictionary items.
Eg: If you wish to create user id's test1 and test2 on a particular host

```
USER_ID_details:
      - user_id: testid1
        groups: sy,playbook
        real_name: XXX_TESTID2
        email_id: abc@ibm.com
      - user_id: testid2
        groups: sy
        real_name: XXX_TESTID2
        email_id: abc@ibm.com
```


USER_ID_details -- Is the list of user id and attributes which will be passed to the execution

2. Emailing the password to the user:
If you are looking to use the email function to email the password to the user then please add the below in the job template extra vars section. We can make it more secure by adding the password with a encrypted zip option.

```
email_user: True 
```
***OPTION to send the password to the user in a secure password encrypted zip file.
Add the Zip file password as a secure variable from the ansible tower survey options
![ScreenShot](https://github.kyndryl.net/CACF-JP-HCAM-Generic/User_Create_Password_Reset_Unix/blob/master/roles/image.png)

<br />
<br />

__Variables:__

|Parameter | Defaults|Comments|
|----------|-----------------|--------|
|__affected_host__ (String) | Empty string "" | Give the list of hosts where you want the user id's to be created, field mandatory and passed through AT Job template after mentioning the Inventory. Eg: affected_host: "host1, host2, host3" |
|__user_id__ (String) | Empty string "" | The name of the user id to be created, field mandatory and passed through AT |
|__group_name__ (String) | Empty string "" | A group to which the user should be added. Can be left blank for default group only|
|__groups__ (String) | Empty string "" | Secondary groups, Need to be passed as a List in form of dictionary from AT This field is mandatory.|
|__real_name__ (String) | Empty string "" | Full name, or gecos information for the user. This field is mandatory to be passed from AT.|
|__pass_reg__ (String) | Empty string "" | The user's initial password. It will be encrypted on linux, but not AIX. This field is obligatory.|
|__umask_value__ (String) | 3 digit Integer value "" | For AIX user, need to mention this value.(Optional)|
|__rlogin__ (String) | Boolean value "" | For AIX user, need to mention this value.(Optional)|
|__su__ (String) | Boolean value "" | For AIX user, need to mention this value.(Optional)|
|__loginretries__ (String) | Boolean value "" | For AIX user, need to mention this value.(Optional)|


<br />
<br />

__Dependencies:__

__Ansible Tower Setup:__

Need to create separate templates for the below playbosks to be run from Ansible tower

user_create_playbook.yml

user_password_reset.yml

### Creating the Tower Project

Create a project using the following values

```
Name: ???_project_user_create_unix
Description: For unix user create and password reset
Organization: ???
SCM type: Git
SCM URL: 
SCM Branch: master
SCM Credential: <your git credential>
SCM Update Options: Clean, Update Revision on Launch 
```
### Creating the Tower Job Templates
Create a new Job Template with the following values for User create and Unix user password reset

```
Name: ???_jobtemplate_User_create_unix
Description: To perform User create in  Unix systems
Job Type: Run
Inventory: *Leave blank and select *Prompt on Launch"*
Project: ???_project_unix_create_user
Playbook: user_create_playbook.yml
Credentials: *add the required Jumphost and endpoint credentials,
and select "Prompt on Launch" to be able to add specific Machine creds later*

Also please specify the extra vars as indicated previously in Requirements sections
```

```
Name: ???_jobtemplate_User_password_reset_unix
Description: To perform password reset for Unix systems User id's
Job Type: Run
Inventory: *Leave blank and select *Prompt on Launch"*
Project: ???_project_unix_password_reset
Playbook: user_password_reset.yml
Credentials: *add the required Jumphost and endpoint credentials,
and select "Prompt on Launch" to be able to add specific Machine creds later*

Also please specify the extra vars as indicated previously in Requirements sections
```

***More information to be updated


#### Playbook Developer

Deepak Yachamaneni (deepak.yachamaneni@ibm.com)
