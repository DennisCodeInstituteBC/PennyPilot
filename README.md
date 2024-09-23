## Overview

 The Expense Tracker helps users manage and analyze their spending with a simple platform for recording expenses, categorizing them, and generating reports. It aims to make personal finance management easy and effective, supporting better budgeting and financial decision-making.

**Target Audience:**
- Individuals: People who want to track and control personal spending.
- Budget-Conscious Users: People needing to look into a budget or understand spending patterns.
- Young Individuals/Students: New to managing finances, seeking an easy-to-use tool.

## Wireframe
The wireframes for PennyPilot provide a visual guide to the user interface and layout. They outline key pages, including the login, signup, dashboard, and expense management screens. Each wireframe illustrates the placement of essential elements, such as navigation menus, input fields, and buttons, ensuring a user-friendly experience. By mapping out the user journey and interaction flow, these wireframes serve as a foundation for the application's design and development, helping to visualize the overall user experience before implementation.
<details>
 <summary> LogIn / Sign Up Page </summary>
 
![LoginPage-Wireframe](https://github.com/user-attachments/assets/b92c121c-734d-4076-a433-a839f02f8a6b)

![SignUpPage - Wireframe](https://github.com/user-attachments/assets/d2e636b1-e9c9-4274-a218-25708e37421f)

![LogIn+SignUp Page - Tablet - Wireframe](https://github.com/user-attachments/assets/c2693296-fbb5-4dfb-8a6a-d4878807b74c)

</details>
<details>
<summary> Dashboard </summary>
 
 ![DashBoard - Wireframe](https://github.com/user-attachments/assets/cfc55560-d327-45c5-b19a-f912e72fe221)
 ![DashBoard - Tablet - Wireframe](https://github.com/user-attachments/assets/d629d2a5-197b-4c56-be58-5a675de288a5)
</details>
<details>
<summary> Expense Page </summary>
 
![Expense Page - Wireframe](https://github.com/user-attachments/assets/f3014c44-f033-47a2-89fa-16d885b49a3d)
![Add Expense Page - Wireframe](https://github.com/user-attachments/assets/d4504e30-64a1-4df8-9421-d172f248f844)
![Expense - Tablet - Wireframe](https://github.com/user-attachments/assets/92019a7e-4112-4661-ac6b-44706d6e8028)
</details>
<details>
<summary> UserAccount </summary>
 
![UserAccount - Wireframe](https://github.com/user-attachments/assets/f43045b8-3ef6-47e3-b55f-0f952ea4223f)
![Update Password - Wireframe](https://github.com/user-attachments/assets/86b677f9-0188-446a-93e8-3d41ce503d7a)
![Account - Tablet - Wireframe](https://github.com/user-attachments/assets/bb35d88d-e4ce-4eae-a54b-b5df62fe916f)
</details>

<details>
<summary> Side Navbar </summary>
 
![Tablet - SideNav - Wireframe](https://github.com/user-attachments/assets/a4fa13e5-bcb4-4c83-b7d3-ed0a4481eac1)
</details>

## Entity-Relationship Diagram 
<details>
 <summary> The Entity-Relationship (ER) diagram serves as a visual blueprint of the database structure, illustrating the relationships between different entities. 
  The database structure for PennyPolit includes entities such as Users, Expense, Category, and Notifications, with defined relationships </summary>

![image](https://github.com/user-attachments/assets/cec62158-87b3-4586-bbbf-aaf8e27048c2)
</details>

## User Stories
User stories are used to help define the functionality from the user's perspective. Each story describes a feature or requirement straightforwardly, focusing on the user's needs and goals. 

1. As a new user, I want to create an account to securely track my expenses and access my data from any device.
 
    **Acceptance Criteria:**
   
        - Users can sign up with an email and password.
        - Users can log in with credentials.

3. As a user, I want to add my daily expenses easily so that I can keep track of my spending in real-time.
   
   **Acceptance Criteria:**
   
       - Users can enter the expense amount, category, date, and notes.
       - Users can save the expense entry.
       - The user receives confirmation that the expense has been added.

3. As a user, I want to categorize my expenses so that I can better understand where my money is going.

   **Acceptance Criteria:**

       - Users can select from predefined categories or create custom categories.
       - Users can view and edit categories.

3. As a user, I want to view a summary of my expenses by category and date range so that I can see where I’m spending the most.

    **Acceptance Criteria:**
            
       - Users can generate and view reports with graphs and charts.
       - Users can filter the summary by category and date range.

4. As a user, I want to search for specific expenses by keyword so that I can easily find and review past entries.
      **Acceptance Criteria**:
   
       - Users can enter a search term to find expenses.
       - Search results display matching entries.
5. As a user, I want to be able to edit or delete my expenses to correct mistakes or remove incorrect entries.

     **Acceptance Criteria:**

       - Users can edit expense details (amount, category, date, notes).
       - Users can delete expenses.
       - The user receives a confirmation of changes or deletions.
6. As a user, I want to receive reminders to add my expenses so I don’t forget to track my spending regularly.

   **Acceptance Criteria**:
   
       - Users can set up reminders for adding expenses.
       - Users receive notifications according to their preferences.
7. As a user, I want to securely log in and manage my account details so that my data is protected and I can keep my information up to date.

   **Acceptance Criteria:**

       - Users can log in and log out securely.
       - Users can update their profile information and change their password.
8. As a user, I want to filter my expenses by amount, category, and date range to analyze specific segments of my spending.

   **Acceptance Criteria:**

       - Users can apply filters to view expenses by amount, category, and date range.
       - Filtered results are displayed accurately.
##Scope
- Users being able to create and log in with their accounts
- Users adding in expenses and being able to see it updated on the expense sheet
- Users able to edit and delete existing expense

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
