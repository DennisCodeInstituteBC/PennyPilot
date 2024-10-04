## Overview
[Live View](https://pennypilot-ed4fcf68cb92.herokuapp.com/accounts/login/)

![image](https://github.com/user-attachments/assets/5834c6f4-3a7b-4c24-a565-33f6f227edf5)
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
## Scope
- Users being able to create and log in with their accounts
- Users adding in expenses and being able to see it updated on the expense sheet
- Users can edit and delete existing expense

## Colour Scheme/ Font-Family
<details>
 <summary> Colour Scheme </summary>
1. Primary Colour: Blue (#007BFF) 

 - A calm and trustworthy colour often which provides a professional feel while not being overwhelming.
 
 ![image](https://github.com/user-attachments/assets/d28e3c3f-8093-4dd3-9ddd-3bda689f7e28)
 
 2. Accent Colors: Green (#28A745) Orange (#FFC107)

- Green is often used for key elements like buttons for actions (e.g., 'Save' or 'Add Expense') and positive indicators (e.g., staying under budget), symbolizing successful transactions and financial stability.
- Orange is an energetic colour commonly used to highlight important elements like warning messages, or key graphics, ensuring they stand out and capture user attention.
  
 ![image](https://github.com/user-attachments/assets/9f72808f-55c8-4085-90bb-ce1580776795)
 ![image](https://github.com/user-attachments/assets/a9b0f52e-2c49-4057-9a2a-871eea6849b8)

5. Neutral Background Colors: Light Gray (#F8F9FA) White (#FFFFFF)

- Light Gray is ideal for large background areas such as the main content sections or sidebars, offering a soft contrast that helps key elements like text, buttons, and graphics stand out while keeping the layout open and modern.
- White, commonly used for background areas like forms, cards, or key content sections, ensuring maximum clarity for text and interface elements, giving the design a clean and crisp appearance."
   
 ![image](https://github.com/user-attachments/assets/85bfbe86-5587-4070-b91c-f23c950a9b2f)
 ![image](https://github.com/user-attachments/assets/4a2650fb-799e-47e2-973c-d754b3e876bb)

8. Text Colors: Black (#000000) White (#FFFFFF)

- Black will be used for headings or important text, creating a bold contrast to draw attention and emphasize key information or section titles.
- White will be utilized to contrast with the button colours, enhancing readability and ensuring the button text stands out clearly.

![image](https://github.com/user-attachments/assets/e9f7fc58-b1d2-4a24-81c1-be6b2fe4af20)
![image](https://github.com/user-attachments/assets/4a2650fb-799e-47e2-973c-d754b3e876bb)
</details>

<details>
 <summary> Font Selection from Google Fonts </summary>
 
1. **[Montserrat](https://fonts.google.com/specimen/Montserrat)**: A contemporary, stylish sans-serif font with a strong impact, perfect for headings and titles. It delivers a bold, reliable, and professional appearance.  
2. **[Roboto](https://fonts.google.com/specimen/Roboto)**: A clean and highly legible sans-serif font ideal for body text. Its widespread use in web applications attests to its readability and modern aesthetic.

</details>

## Agile Methodology

[PennyPilot Project Page](https://github.com/users/DennisCodeInstituteBC/projects/4)

The website's development followed an Agile methodology, using GitHub Projects to organize and manage User Stories. The project started with a week of planning, including a meeting with the mentors to outline the timeline. The initial sprint ran for three weeks, concluding with a mentor review to assess progress and identify areas for improvement. Over the next three weeks, additional features were added, testing was conducted, issues were resolved, and documentation was completed, all leading up to the final review of the finished project.

## Technologies Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5): Markup Language
- [CSS3](https://en.wikipedia.org/wiki/CSS): Styling
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript): Programming Language
- [Python3](https://www.python.org/download/releases/3.0/):  Programming Language
- [Django 5.1.1](https://docs.djangoproject.com/en/5.1/releases/5.1.1/): Python-based web framework
- [Git](https://git-scm.com/): Version control system
- [GitHub](https://github.com/): Hosting Repository
- [Heroku](https://www.heroku.com/): Cloud-based platform
- [Blasmiq](https://balsamiq.com/): Mockup tool
- [Moqups](https://app.moqups.com/): Entity Relationship Diagram

## Features

### Login/Signup Page

The login page serves as the initial screen for both new and returning users upon accessing the website. It follows a consistent theme and layout to ensure a cohesive user experience throughout the platform. The page is designed to be fully responsive, offering an optimized experience across devices, including mobile. Accessibility standards are also prioritized, with clear input fields, error handling, and keyboard navigation. Additionally, security measures, such as password encryption, are in place to protect user data.
<details>
 <summary> Images </summary>
 
![image](https://github.com/user-attachments/assets/eca5e6a6-71e7-461a-a091-eab80d21597a)
![image](https://github.com/user-attachments/assets/af80eaa1-6e55-4f79-bae1-4578ca12226e)
</details>

### Expense Page

The expense page is designed with simplicity and ease of navigation in mind, featuring a clean layout with a straightforward colour scheme. Clear colour contrasts and button colour coding enhance usability, while key information is centred for quick access. The page is fully responsive, ensuring an optimized experience across all devices, including mobile and tablets. Real-time data updates allow users to instantly see any changes made to their expenses, whether they are adding, editing, or deleting entries, without the need to refresh the page. Additional features such as search filters and sorting options make managing expenses efficient and user-friendly.
<details>
 <summary> Images </summary>
 
![image](https://github.com/user-attachments/assets/d14352f1-cde2-4f10-87d6-c878b18c108d)
![image](https://github.com/user-attachments/assets/1d4b2410-163d-4cfc-b29a-b150e24d5091)
</details>


### Navigation Bar

The navigation bar is consistent across all pages once a user is logged in, maintaining a unified look and feel throughout the site. It features a hover effect that highlights links as users interact with them, making navigation more intuitive. The layout is simple, with a visible logout button set apart from the other menu items to prevent confusion. This design ensures easy navigation while providing a smooth user experience.
<details>
 <summary> Images </summary>
 
![image](https://github.com/user-attachments/assets/367c77c8-a67d-47a2-8fd3-cc32a6a24bf1)
![image](https://github.com/user-attachments/assets/d6361f50-80fd-4163-856f-013c2cae5413)
</details>

### Account Page

The Accounts section of the app allows users to manage their personal information and account settings easily. Users can update their passwords for enhanced security, ensuring that they maintain their account's confidentiality by changing their passwords whenever necessary. This process is simple and user-friendly, guiding users through the necessary steps to create a new password. Additionally, users can view their profile information, including their username, email address, profile picture (if added). This feature enables users to review their details for accuracy and make any necessary updates to their profile information.
<details>
 <summary> Images </summary>
 
![image](https://github.com/user-attachments/assets/e76c6f3e-693b-49cc-834f-16fba5a1b72e)
![image](https://github.com/user-attachments/assets/0a6ddaba-261b-4641-a93f-2e4665b12800)
</details>

## Testing
I acknowledge the importance of keeping the secret key confidential. Although it was unintentionally exposed in earlier commits, this issue has been rectified in subsequent updates to ensure that the key remains hidden

This project utilizes the [W3C HTML Validator](https://validator.w3.org/) to ensure code quality and compliance with HTML standards, helping to identify errors and improve user experience across different browsers.
<details>
<summary> HTML Validator </summary>
 
![image](https://github.com/user-attachments/assets/0ecd1854-1d82-40a0-8587-229d58008800)
</details>

This project utilizes the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure code quality and compliance with CSS standards, helping to identify errors and enhance the styling of the application.
<details>
<summary> CSS Validator </summary>
 
![image](https://github.com/user-attachments/assets/49bcd009-b574-4739-978b-d9dc0a6df4ab)
</details>

This project utilizes [PEP8 CI](https://pep8ci.herokuapp.com/) to ensure adherence to Python coding standards, helping to identify style violations and improve code readability and maintainability.
<details>
 <summary>CI Python Linter Validator</summary>
 
 ![image](https://github.com/user-attachments/assets/2750b35c-8c3a-43f3-aeb1-f779884233e8)
</details>

### Lighthouse Testing
This project employs Lighthouse to assess web performance, accessibility, and SEO, providing insights and recommendations to enhance user experience and optimize overall site quality.
![image](https://github.com/user-attachments/assets/8d12c7ba-3dd5-4544-afe4-b71667aa3f4e)


### Functionality Testing

This section outlines the functionality testing conducted for the application, ensuring that all features meet user requirements. Each user story is assessed against acceptance criteria to verify proper implementation. The results indicate whether each test passed or failed, providing insights into areas for improvement.

| Test Number | User Story | Acceptance Criteria | Pass| Fail | 
| --- | --- | --- | --- | --- |
| No.1 | As a new user, I want to create an account to securely track my expenses and access my data from any device. | Users can sign up using an email and password. | ✔️ |  |
| | |Users can log in with credentials. | ✔️ |  |
| No.2 |As a user, I want to add my daily expenses easily to keep track of my spending in real-time.| Users can enter the expense amount, category, date, and notes. | ✔️ |  |
| | | Users can save the expense entry. | ✔️ |  |
| | | User receives confirmation that the expense has been added. |  | ❌ |
| No.3 |As a user, I want to categorise my expenses so that I can better understand where my money is going. | Users can select from predefined categories or create custom categories. | ✔️ |  |
| | | Users can view and edit categories. | ✔️ |  |
| No.4 |As a user, I want to view a summary of my expenses by category and date range so that I can see where I’m spending the most. | Users can generate and view reports with graphs and charts. |  | ❌ |
| | | As a user, I want to categorise my expenses so that I can better understand where my money is going. |  | ❌ |
| No.5 |As a user, I want to be able to edit or delete my expenses so that I can correct mistakes or remove incorrect entries. | Users can edit expense details (amount, category, date, notes). | ✔️ |  |
| | | Users can delete expenses. | ✔️ |  |
| | | User receives a confirmation of changes or deletions. | ✔️ |  |
| No.6 |As a user, I want to securely log in and manage my account details so that my data is protected and I can keep my information up to date. | Users can log in and log out securely. | ✔️ |  |
| | | Users can update profile information and change the password. | ✔️ |  |
| No.7 |As a user, I want to search for specific expenses by keyword so that I can easily find and review past entries. | Users can enter a search term to find expenses. |  | ❌ |
| | | Search results display matching entries.|  | ❌ |
| No.8 |As a user, I want to receive reminders to add my expenses so that I don’t forget to track my spending regularly. | Users can set up reminders for adding expenses. |  | ❌ |
| | | Users receive notifications according to their preferences. |  | ❌ |
| No.9 |As a user, I want to filter my expenses by amount, category, and date range so that I can analyse specific segments of my spending. | Users can apply filters to view expenses by amount, category, and date range.|  | ❌ |
| | | Filtered results display accurately. |  | ❌ |

### Further Feature

To enhance the user experience and functionality of the application, several key features are planned for future development. First, the implementation of filtering options will allow users to customize their expense views by various parameters such as amount, category, and date range, making it easier to analyze spending habits. Additionally, search functionality will be introduced to enable users to quickly find specific expenses by entering relevant keywords, streamlining the process of reviewing past entries.

Furthermore, the incorporation of data visualization tools, including charts and graphs, will provide users with a clear and engaging summary of their spending patterns over time, helping them make informed financial decisions based on tracked expenses. Lastly, allowing users to upload profile images will add a personal touch to their accounts and enhance the overall user interface. These features will improve the application's usability and empower users to manage their finances more effectively.

## Deployment

### Prepare the Environment and settings.py

Create the env.py file:

In your project root directory (e.g., /workspace/your_project), create an env.py file.

Add your environment variables, such as the SECRET_KEY, and DATABASE_URL.

```
import os

os.environ["SECRET_KEY"] = "your-secret-key"
os.environ["DATABASE_URL"] = "your-database-url"
```

Update settings.py:

Import your env.py file in settings.py:

```
import os
if os.path.isfile("env.py"):
    import env
```
Update the following parts in settings.py:

Set the SECRET_KEY and DATABASE_URL from environment variables:

```
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}
```

### Steps to Deploy on Heroku:

Install dependencies:

```
pip3 install -r requirements.txt
```
Create a Procfile with the following content:
```
web: gunicorn pennypilot.wsgi
```
Ensure the ALLOWED_HOSTS in your settings.py includes the Heroku domain:

```
ALLOWED_HOSTS = ['pennypilot-ed4fcf68cb92.herokuapp.com']
```
Open your (Sign up or Log in) Heroku app:

- If you don’t have a Heroku account, visit [Heroku's](https://www.heroku.com/) website and sign up for an account. If you already have an account, log in.

Create a New App:

- Once logged in, go to the Heroku Dashboard.
- Click on the “New” button in the top right corner and select “Create new app.”

- Choose a unique name for your app and select your preferred region, then click “Create app.”

Connect to Your GitHub Repository:

- On your app’s dashboard, navigate to the “Deploy” tab.
- In the “Deployment method” section, select “GitHub.”

- Authorize Heroku to access your GitHub account if prompted.
- Search for your repository and click “Connect.”

Configure Environment Variables:

- Navigate to the “Settings” tab.
- Click on “Reveal Config Vars.”
- Add your environment variables, such as **SECRET_KEY** and **DATABASE_URL** by entering the key in the "KEY" field and the value in the "VALUE" field.

Deploy Your App:

- In the “Deploy” tab, scroll down to the “Manual Deploy” section.
- Choose the branch you want to deploy (usually main) and click “Deploy Branch.”
- Heroku will start the deployment process. You can view the logs for any errors or confirmation messages during this process.

Run Database Migrations:

- Once the deployment is complete, navigate to the “More” button in the top right corner of the dashboard and select “Run console.”

- In the command line interface, run:
```
python manage.py migrate
```
Collect Static Files:
- Still in the console, run the following command to collect static files:
```
python manage.py collectstatic
```
Open Your App:

After deployment and migrations are complete, go back to the “Overview” tab.

Click on the “Open app” button to view your live application.

## Credits
- [W3School](https://www.w3schools.com/)
- [DjangoProjects](https://docs.djangoproject.com/en/5.1/topics/db/models/)
- [Code Institute](/learn.codeinstitute.net/)
- Youtube Tutorials
    - [Django Tutorial #3 - URLs and Views](https://www.youtube.com/watch?v=TblSa29DX6I&ab_channel=NetNinja)
    - [Django Tutorial #6 - Django Models](https://www.youtube.com/watch?v=5zNR3E6WRLE&ab_channel=NetNinja)
- [Djecrety](https://djecrety.ir/)
- [Django-AllAuth](https://docs.allauth.org/en/latest/)
- Image stocks
   - [Pexels](https://www.pexels.com/)
   - [Unsplash](https://unsplash.com/)
   - [Stockvault](https://www.stockvault.net/)
   - [Pixabay](https://pixabay.com/)

