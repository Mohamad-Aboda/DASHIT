# ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) DASHIT

 <hr>

# ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) Description

**A website analytics dashboard is a reporting tool that enables you to track your website performance metrics like page views, conversion rate, bounce rate, and more.**

# ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) Project Structure

```
├───CSV
│   └───user
|
├───static
│   └───img
│       └───POS
|
└───templates
    ├───Base
    │   └───includes
    ├───includes
    └───user
        └───includes

```

- CSV: contains csv data for every User
- static: contains static files (css, javascript)
- templates: contains html for the application
- Python files for the application

## Frameworks and Libraries used

- Flask: For the Website backend
- Pandas: Reading CSV files to process them
- Pickle: Save the ML Model for deployment
- Apache ECharts: For generating the Charts

## Usage

- run `pip install -r requirements.txt` to install all packages and libraries needed for the project
- navigate to `flask_project` then run `flask run`
- The application will run at http://127.0.0.1:5000/

# ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) Overview & Result

Signup

![singup](https://user-images.githubusercontent.com/41721894/114431352-b143c700-9bbf-11eb-833b-bbf41c18a0ec.gif) <hr>
Login

![login](https://user-images.githubusercontent.com/41721894/114431623-fec03400-9bbf-11eb-840a-aefdc7d9be69.gif) <hr>
Create Dashboard

![createPOS](https://user-images.githubusercontent.com/41721894/114431560-ebad6400-9bbf-11eb-973d-aa70c3a12c78.gif) <hr>
Upload data and use filters

![Template](https://user-images.githubusercontent.com/41721894/114431470-cf112c00-9bbf-11eb-999f-f9b84ff64d39.gif) <hr>
Create General Dashboard

![generalDashBoard](https://user-images.githubusercontent.com/41721894/114445358-46e75280-9bd0-11eb-80bd-b18a796e105c.gif) <hr>
Access more types of Dashboards at http://127.0.0.1:5000/all

![All](https://user-images.githubusercontent.com/41721894/114450006-c3306480-9bd5-11eb-9aec-cc2f611e83e4.gif) <hr>

## Notes

| Function   | Number of rows | example of columns | Operation                                                                    |
| ---------- | -------------- | ------------------ | ---------------------------------------------------------------------------- |
| SUM        | 1              | A                  | sum all the values of 'A' columns                                            |
| AVERAGE    | 1              | A                  | sum all the values of 'A' columns / number of rows                           |
| ADD        | 2              | A,B                | sum all the values of 'A' columns + sum all the values of 'B' columns        |
| SUBTRACT   | 2              | A,B                | sum all the values of 'A' columns - sum all the values of 'B' columns        |
| DIVIDE     | 2              | A,B                | sum all the values of 'A' columns / sum all the values of 'B' columns        |
| PERCENTAGE | 2              | A,B                | sum all the values of 'A' columns \* 100 / sum all the values of 'B' columns |
| AllCHARTS  | 2              | A,B                | X-Axises = A & Y-Axises = B                                                  |

- column names shouldn't have spaces

# ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Contributors (SpamBytes team)

- Mohamed Magdi
- Hossam Assad
- Eslam Elgendy
- Mohamed Abdelhamid
