**AI DIET RECOMMENDATION BOT SYSTEM**

**ABOUT**

The AI Diet Recommendation Chatbot System is a web-based intelligent application designed to provide personalized diet plans through an interactive chatbot interface.
The system collects user health and lifestyle information such as age, weight, height, activity level, dietary habits, and medical conditions through a sequence of structured questions. 
Using predefined diet logic implemented in Python, the system generates a customized weekly diet plan to support healthy eating habits.
The application is developed using Flask and provides real-time responses through a simple and user-friendly interface.

**FEATURES**

**Interactive Chatbot Interface**: 
    Collects user health and lifestyle details through conversational questions.
    
**BMI & Lifestyle Assessment**: 
    Evaluates user inputs such as height, weight, sleep, water intake, and exercise habits.
    
**Personalized Weekly Diet Plan**: 
    Generates a customized weekly diet plan based on user goals and preferences.
    
**Diet Preference Support**: 
    Handles vegetarian and non-vegetarian diet choices.
    
**Health Condition Awareness**: 
    Includes basic checks for conditions like diabetes.
    
**Web-Based Access**: 
Accessible through a browser using Flask backend and HTML/CSS/JavaScript frontend.

**Meal Planning and Tracking**
It suggests daily and weekly meal plans and helps users maintain consistency in healthy eating habits.

**REQUIREMENTS**

**Operating System**: Windows 10/11 or Linux

**Programming Language**: Python 3.8 or later

**Backend Framework**: Flask

**Frontend Technologies**: HTML, CSS, JavaScript

**Libraries**: Flask-CORS

**Development Tools**: Visual Studio Code

**Version Control**: Git

**SYSTEM ARCHITECTURE**

The system consists of the following functional modules:
User Interface Module:
Provides a chat-based interface where users answer health-related questions.
Input Handling Module:
Receives user responses through POST requests and stores them sequentially.
Diet Logic Module:
Implements rule-based logic in diet_logic.py to analyze user data and generate a weekly diet plan.
Flask Backend Module:
Manages routing, API endpoints, and communication between frontend and backend.
Response Generation Module:
Sends diet recommendations back to the user in real time through the chatbot.

**PROJECT DIRECTORY STRUCTURE**

<img width="531" height="338" alt="image" src="https://github.com/user-attachments/assets/4e8bce3f-a1f4-4e1d-b1e0-ff5e3d94c35b" />

**INPUT PARAMETERS**
The chatbot collects the following information from the user:

Age

Weight (kg)

Height (cm)

Gender

Activity level (low / moderate / high)

Health goal (weight loss / gain / maintain)

Diet preference (vegetarian / non-vegetarian)

Meals per day

Breakfast habit

Daily water intake

Sleep duration

Exercise frequency and type

Diabetes condition

**OUTPUT AND RESULTS**

The system generates:

User lifestyle summary
Weekly diet plan recommendation
Health-focused meal suggestions
The output is displayed directly in the chatbot interface after all questions are answered, ensuring a smooth and interactive user experience.

<img width="786" height="398" alt="image" src="https://github.com/user-attachments/assets/2ed45d91-f1e6-48ab-8e3e-fc4b5cdcc865" />

<img width="651" height="398" alt="image" src="https://github.com/user-attachments/assets/e4b74e4a-2c51-474c-a344-72f5dfd098d4" />

<img width="764" height="494" alt="image" src="https://github.com/user-attachments/assets/49a85bd5-d2c1-42c0-a6c7-c53535c240a6" />

**FUTURE ENHANCEMENTS**

Integration of machine learning models for smarter recommendations
BMI visualization and calorie charts
Mobile application deployment
Voice-based chatbot support
Integration with fitness trackers

**REFERENCES**

World Health Organization (WHO),
“Healthy Diet – Fact Sheet,” WHO, Geneva.
Explains nutritional requirements and healthy eating guidelines.

USDA FoodData Central,
United States Department of Agriculture Food Nutrition Database.
Used for calorie, protein, carbohydrate, and fat information.

Scikit-learn Documentation,
https://scikit-learn.org

Reference for machine learning algorithms used in recommendation systems.

J. Han, M. Kamber, and J. Pei,
Data Mining: Concepts and Techniques, 3rd Edition, Elsevier, 2012.
Provides foundational knowledge on data preprocessing and classification.

R. Burke,
“Hybrid Recommender Systems: Survey and Experiments,” User Modeling and User-Adapted Interaction, 2002.
Explains recommendation system concepts applicable to diet planning.

S. Min, B. Lee, and S. Yoon,
“Deep Learning in Healthcare,” Briefings in Bioinformatics, 2017.
Discusses AI-based personalization in healthcare applications.

**CONTRIBUTORS**

This project was developed as part of an academic AI/ML Mini Project.# miniproject
