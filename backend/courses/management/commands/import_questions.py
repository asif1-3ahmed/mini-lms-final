from django.core.management.base import BaseCommand
from courses.models import Course, Question

class Command(BaseCommand):
    help = "Bulk import MCQ questions for courses"

    def handle(self, *args, **kwargs):

        DATA = {
           290: [
    {
        "question_text": "What is Tableau primarily used for?",
        "option_a": "Game development",
        "option_b": "Data visualization and dashboard creation",
        "option_c": "Web server management",
        "option_d": "Database indexing",
        "correct_answer": "B"
    },
    {
        "question_text": "Which Tableau feature allows users to filter data interactively?",
        "option_a": "Joins",
        "option_b": "Actions",
        "option_c": "Groups",
        "option_d": "Bins",
        "correct_answer": "B"
    },
    {
        "question_text": "What is a Tableau Worksheet?",
        "option_a": "A collection of dashboards",
        "option_b": "A single view containing charts and graphs",
        "option_c": "A SQL editor",
        "option_d": "A Python script editor",
        "correct_answer": "B"
    },
    {
        "question_text": "Dashboards in Tableau are used for:",
        "option_a": "Displaying multiple visualizations together",
        "option_b": "Running SQL queries",
        "option_c": "Managing databases",
        "option_d": "Editing CSV files",
        "correct_answer": "A"
    },
    {
        "question_text": "Which file type represents a Tableau Workbook?",
        "option_a": ".twb or .twbx",
        "option_b": ".xlsx",
        "option_c": ".json",
        "option_d": ".db",
        "correct_answer": "A"
    },
    {
        "question_text": "Filters in Tableau allow users to:",
        "option_a": "Modify server configurations",
        "option_b": "Limit the data shown in a visualization",
        "option_c": "Create machine learning models",
        "option_d": "Write code snippets",
        "correct_answer": "B"
    },
    {
        "question_text": "What does a Tableau Data Source represent?",
        "option_a": "Only Excel files",
        "option_b": "Any connected dataset such as Excel, CSV, SQL",
        "option_c": "Only online databases",
        "option_d": "Only cloud storage",
        "correct_answer": "B"
    },
    {
        "question_text": "Which Tableau feature controls color, size and detail?",
        "option_a": "Marks card",
        "option_b": "SQL editor",
        "option_c": "Workbook panel",
        "option_d": "Schema viewer",
        "correct_answer": "A"
    },
    {
        "question_text": "What is the purpose of Tableau Extracts?",
        "option_a": "Store passwords",
        "option_b": "Optimize datasets into a compressed format",
        "option_c": "Deploy cloud dashboards",
        "option_d": "Create UI templates",
        "correct_answer": "B"
    },
    {
        "question_text": "A Tableau Story is used to:",
        "option_a": "Write documentation",
        "option_b": "Present a sequence of insights",
        "option_c": "Run Python scripts",
        "option_d": "Generate random graphs",
        "correct_answer": "B"
    }
],
289: [
    {
        "question_text": "What is Power BI mainly used for?",
        "option_a": "Building mobile apps",
        "option_b": "Data visualization and reporting",
        "option_c": "Network configuration",
        "option_d": "3D animation",
        "correct_answer": "B"
    },
    {
        "question_text": "Which Power BI component is used to create dashboards?",
        "option_a": "Power BI Desktop",
        "option_b": "Power BI Service",
        "option_c": "Power Query",
        "option_d": "DAX Studio",
        "correct_answer": "B"
    },
    {
        "question_text": "What does DAX stand for?",
        "option_a": "Data Analysis Expressions",
        "option_b": "Dynamic Application XML",
        "option_c": "Data Automation Extension",
        "option_d": "Dashboard Analytics Xpress",
        "correct_answer": "A"
    },
    {
        "question_text": "Power Query is mainly used for:",
        "option_a": "Data cleaning and transformation",
        "option_b": "Frontend web design",
        "option_c": "Creating animations",
        "option_d": "Managing cloud servers",
        "correct_answer": "A"
    },
    {
        "question_text": "Which file format is used to save Power BI reports?",
        "option_a": ".pbix",
        "option_b": ".xlsx",
        "option_c": ".pbi",
        "option_d": ".json",
        "correct_answer": "A"
    },
    {
        "question_text": "What is a Power BI Dashboard?",
        "option_a": "A document editor",
        "option_b": "A collection of visuals on one canvas",
        "option_c": "An email notification tool",
        "option_d": "A mobile app builder",
        "correct_answer": "B"
    },
    {
        "question_text": "Which feature refreshes data automatically?",
        "option_a": "Dynamic sync",
        "option_b": "Scheduled refresh",
        "option_c": "Auto reload",
        "option_d": "Data booster",
        "correct_answer": "B"
    },
    {
        "question_text": "Power BI supports which type of join?",
        "option_a": "Full outer",
        "option_b": "Left outer",
        "option_c": "Inner join",
        "option_d": "All of the above",
        "correct_answer": "D"
    },
    {
        "question_text": "Where can you publish Power BI reports?",
        "option_a": "Local filesystem",
        "option_b": "Power BI Service",
        "option_c": "Photoshop cloud",
        "option_d": "Docker Hub",
        "correct_answer": "B"
    },
    {
        "question_text": "DAX is used for:",
        "option_a": "Formatting visual styles",
        "option_b": "Data modeling and calculations",
        "option_c": "Network routing",
        "option_d": "Creating images",
        "correct_answer": "B"
    }
],

288: [
    {
        "question_text": "What is Big Data primarily about?",
        "option_a": "Small datasets stored locally",
        "option_b": "Large, complex datasets that traditional tools cannot handle",
        "option_c": "Video rendering",
        "option_d": "Simple spreadsheets",
        "correct_answer": "B"
    },
    {
        "question_text": "Which technology is used for distributed storage?",
        "option_a": "SQL Server",
        "option_b": "Hadoop HDFS",
        "option_c": "Photoshop",
        "option_d": "React Native",
        "correct_answer": "B"
    },
    {
        "question_text": "MapReduce is used for:",
        "option_a": "Game mechanics",
        "option_b": "Distributed parallel processing",
        "option_c": "UI development",
        "option_d": "Recording audio",
        "correct_answer": "B"
    },
    {
        "question_text": "Spark is known for being:",
        "option_a": "Slow and outdated",
        "option_b": "Fast in-memory processing",
        "option_c": "A mobile OS",
        "option_d": "An image editor",
        "correct_answer": "B"
    },
    {
        "question_text": "Hadoop components mainly include:",
        "option_a": "HDFS + MapReduce",
        "option_b": "Photoshop + Lightroom",
        "option_c": "React + Vue",
        "option_d": "AWS + Azure",
        "correct_answer": "A"
    },
    {
        "question_text": "Big Data is often used in:",
        "option_a": "Basic calculators",
        "option_b": "IoT analytics, fraud detection, recommendations",
        "option_c": "Screenshot editing",
        "option_d": "Offline games",
        "correct_answer": "B"
    },
    {
        "question_text": "Which feature of Big Data refers to 'speed'?",
        "option_a": "Variety",
        "option_b": "Volume",
        "option_c": "Velocity",
        "option_d": "Viability",
        "correct_answer": "C"
    },
    {
        "question_text": "Which NoSQL database is often used with Big Data?",
        "option_a": "MongoDB",
        "option_b": "MySQL",
        "option_c": "Excel",
        "option_d": "SQLite",
        "correct_answer": "A"
    },
    {
        "question_text": "Big Data pipelines help in:",
        "option_a": "Data ingestion, storage and processing",
        "option_b": "Music composition",
        "option_c": "Painting",
        "option_d": "File compression",
        "correct_answer": "A"
    },
    {
        "question_text": "Real-time Big Data processing uses:",
        "option_a": "Apache Spark Streaming",
        "option_b": "MS Paint",
        "option_c": "React hooks",
        "option_d": "PHPMyAdmin",
        "correct_answer": "A"
    }
],
287: [
    {
        "question_text": "What is the main purpose of database normalization?",
        "option_a": "To speed up CSS rendering",
        "option_b": "To reduce redundancy and improve consistency",
        "option_c": "To create dashboards",
        "option_d": "To manage APIs",
        "correct_answer": "B"
    },
    {
        "question_text": "Which diagram is essential for database design?",
        "option_a": "Gantt chart",
        "option_b": "ER Diagram",
        "option_c": "Histogram",
        "option_d": "Pie chart",
        "correct_answer": "B"
    },
    {
        "question_text": "A primary key is:",
        "option_a": "A field that uniquely identifies a record",
        "option_b": "A duplicate field",
        "option_c": "A style in frontend",
        "option_d": "A backup table",
        "correct_answer": "A"
    },
    {
        "question_text": "What does an ER Diagram show?",
        "option_a": "Entity relationships",
        "option_b": "Network topology",
        "option_c": "CSS layouts",
        "option_d": "Server components",
        "correct_answer": "A"
    },
    {
        "question_text": "1NF ensures:",
        "option_a": "Every column has atomic values",
        "option_b": "Only numeric data is used",
        "option_c": "Tables have animations",
        "option_d": "Only three columns exist",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is a type of database constraint?",
        "option_a": "Foreign key",
        "option_b": "Padding",
        "option_c": "Margin",
        "option_d": "Gradient",
        "correct_answer": "A"
    },
    {
        "question_text": "A foreign key:",
        "option_a": "Links two tables",
        "option_b": "Styles a table",
        "option_c": "Processes images",
        "option_d": "Creates animations",
        "correct_answer": "A"
    },
    {
        "question_text": "Database indexing improves:",
        "option_a": "Audio clarity",
        "option_b": "Query processing speed",
        "option_c": "Image resolution",
        "option_d": "Dashboard colors",
        "correct_answer": "B"
    },
    {
        "question_text": "A schema is:",
        "option_a": "Database structure",
        "option_b": "Frontend layout",
        "option_c": "API token",
        "option_d": "Animation effect",
        "correct_answer": "A"
    },
    {
        "question_text": "Composite keys consist of:",
        "option_a": "Two or more columns",
        "option_b": "Images and audio",
        "option_c": "Only one field",
        "option_d": "Tables and CSS",
        "correct_answer": "A"
    }
],
286: [
    {
        "question_text": "Solidity is mainly used on which blockchain?",
        "option_a": "Bitcoin",
        "option_b": "Ethereum",
        "option_c": "Solana",
        "option_d": "Cardano",
        "correct_answer": "B"
    },
    {
        "question_text": "A smart contract is:",
        "option_a": "A legal document",
        "option_b": "Self-executing code on blockchain",
        "option_c": "A PDF form",
        "option_d": "A cloud container",
        "correct_answer": "B"
    },
    {
        "question_text": "Which file extension is used for Solidity?",
        "option_a": ".py",
        "option_b": ".sol",
        "option_c": ".js",
        "option_d": ".rb",
        "correct_answer": "B"
    },
    {
        "question_text": "Which keyword defines a smart contract?",
        "option_a": "class",
        "option_b": "contract",
        "option_c": "function",
        "option_d": "module",
        "correct_answer": "B"
    },
    {
        "question_text": "What is gas in Ethereum?",
        "option_a": "Air pressure",
        "option_b": "Cost of executing operations",
        "option_c": "Local storage",
        "option_d": "RAM usage",
        "correct_answer": "B"
    },
    {
        "question_text": "Which type of function can accept funds?",
        "option_a": "loader()",
        "option_b": "payable",
        "option_c": "receiveData()",
        "option_d": "transferable",
        "correct_answer": "B"
    },
    {
        "question_text": "Events in Solidity are used for:",
        "option_a": "Logging information",
        "option_b": "Creating tokens",
        "option_c": "Mining blocks",
        "option_d": "Gas refund",
        "correct_answer": "A"
    },
    {
        "question_text": "The 'address' type stores:",
        "option_a": "Email address",
        "option_b": "Ethereum wallet address",
        "option_c": "Home address",
        "option_d": "IP address",
        "correct_answer": "B"
    },
    {
        "question_text": "Which IDE is widely used for Solidity?",
        "option_a": "VS Code only",
        "option_b": "Remix IDE",
        "option_c": "Eclipse",
        "option_d": "PyCharm",
        "correct_answer": "B"
    },
    {
        "question_text": "Smart contracts are:",
        "option_a": "Immutable once deployed",
        "option_b": "Editable anytime",
        "option_c": "Stored in OneDrive",
        "option_d": "Temporary files",
        "correct_answer": "A"
    }
],
285: [
    {
        "question_text": "A blockchain is a:",
        "option_a": "Spreadsheet",
        "option_b": "Distributed ledger",
        "option_c": "Database on one server",
        "option_d": "Video file",
        "correct_answer": "B"
    },
    {
        "question_text": "Blocks are linked using:",
        "option_a": "Ropes",
        "option_b": "Hashes",
        "option_c": "Cables",
        "option_d": "WiFi",
        "correct_answer": "B"
    },
    {
        "question_text": "Mining is used to:",
        "option_a": "Render images",
        "option_b": "Validate and add blocks",
        "option_c": "Upload videos",
        "option_d": "Host websites",
        "correct_answer": "B"
    },
    {
        "question_text": "Smart contracts run on:",
        "option_a": "Excel",
        "option_b": "Blockchain networks",
        "option_c": "PDF readers",
        "option_d": "Browsers only",
        "correct_answer": "B"
    },
    {
        "question_text": "Ethereum is known for:",
        "option_a": "AI",
        "option_b": "Smart contract support",
        "option_c": "Web hosting",
        "option_d": "Mobile apps",
        "correct_answer": "B"
    },
    {
        "question_text": "A private key is used to:",
        "option_a": "Login to Gmail",
        "option_b": "Sign blockchain transactions",
        "option_c": "Play games",
        "option_d": "Change WiFi password",
        "correct_answer": "B"
    },
    {
        "question_text": "Decentralization means:",
        "option_a": "One central authority controls everything",
        "option_b": "Control is distributed across nodes",
        "option_c": "Only one miner exists",
        "option_d": "Only the government manages blocks",
        "correct_answer": "B"
    },
    {
        "question_text": "Cryptographic hashing provides:",
        "option_a": "Music playback",
        "option_b": "Data integrity",
        "option_c": "Web templates",
        "option_d": "Game textures",
        "correct_answer": "B"
    },
    {
        "question_text": "A blockchain wallet stores:",
        "option_a": "Emails",
        "option_b": "Private/public keys",
        "option_c": "Movies",
        "option_d": "Pictures",
        "correct_answer": "B"
    },
    {
        "question_text": "Consensus mechanisms include:",
        "option_a": "Proof of Work",
        "option_b": "Proof of Stake",
        "option_c": "Both A and B",
        "option_d": "Only VPN",
        "correct_answer": "C"
    }
],
284: [
    {
        "question_text": "Laravel is a framework for which programming language?",
        "option_a": "Java",
        "option_b": "Python",
        "option_c": "PHP",
        "option_d": "C++",
        "correct_answer": "C"
    },
    {
        "question_text": "Which architecture pattern does Laravel follow?",
        "option_a": "MVP",
        "option_b": "MVC",
        "option_c": "MVVM",
        "option_d": "FLUX",
        "correct_answer": "B"
    },
    {
        "question_text": "What is Artisan in Laravel?",
        "option_a": "API testing tool",
        "option_b": "Command-line interface",
        "option_c": "Database engine",
        "option_d": "Frontend compiler",
        "correct_answer": "B"
    },
    {
        "question_text": "Which Laravel feature handles URL routing?",
        "option_a": "ORM",
        "option_b": "Blade",
        "option_c": "Routes",
        "option_d": "Composer",
        "correct_answer": "C"
    },
    {
        "question_text": "Laravel uses which ORM?",
        "option_a": "Hibernate",
        "option_b": "Eloquent",
        "option_c": "Django ORM",
        "option_d": "ActiveRecord",
        "correct_answer": "B"
    },
    {
        "question_text": "Blade is:",
        "option_a": "Laravel’s templating engine",
        "option_b": "A CSS framework",
        "option_c": "A JS runtime",
        "option_d": "A database",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command creates a controller?",
        "option_a": "php artisan make:controller",
        "option_b": "php create controller",
        "option_c": "composer controller",
        "option_d": "php new controller",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware in Laravel is used for:",
        "option_a": "Image compression",
        "option_b": "Request filtering",
        "option_c": "CSS generation",
        "option_d": "Database backup",
        "correct_answer": "B"
    },
    {
        "question_text": "Laravel migrations are used for:",
        "option_a": "Frontend styling",
        "option_b": "Database version control",
        "option_c": "Session handling",
        "option_d": "API caching",
        "correct_answer": "B"
    },
    {
        "question_text": "Laravel’s service container is used for:",
        "option_a": "Dependency injection",
        "option_b": "Image rendering",
        "option_c": "File uploads",
        "option_d": "Caching views",
        "correct_answer": "A"
    }
],
283: [
    {
        "question_text": "Spring Boot is built on top of which framework?",
        "option_a": "Django",
        "option_b": "Spring Framework",
        "option_c": "Laravel",
        "option_d": "React",
        "correct_answer": "B"
    },
    {
        "question_text": "Spring Boot helps developers by:",
        "option_a": "Removing boilerplate configuration",
        "option_b": "Creating 3D models",
        "option_c": "Building video games",
        "option_d": "Providing CSS templates",
        "correct_answer": "A"
    },
    {
        "question_text": "Which file stores Spring Boot application properties?",
        "option_a": "config.js",
        "option_b": "settings.py",
        "option_c": "application.properties",
        "option_d": "env.txt",
        "correct_answer": "C"
    },
    {
        "question_text": "Spring Boot uses which server by default?",
        "option_a": "Apache",
        "option_b": "Nginx",
        "option_c": "Tomcat",
        "option_d": "IIS",
        "correct_answer": "C"
    },
    {
        "question_text": "What annotation starts a Spring Boot application?",
        "option_a": "@EnableBoot",
        "option_b": "@SpringApplication",
        "option_c": "@SpringBootApplication",
        "option_d": "@RestApp",
        "correct_answer": "C"
    },
    {
        "question_text": "Which annotation is used to create REST APIs?",
        "option_a": "@Controller",
        "option_b": "@RestController",
        "option_c": "@APIService",
        "option_d": "@ServiceAPI",
        "correct_answer": "B"
    },
    {
        "question_text": "Spring Data JPA is used for:",
        "option_a": "Database operations",
        "option_b": "Camera access",
        "option_c": "Animations",
        "option_d": "Mobile sensors",
        "correct_answer": "A"
    },
    {
        "question_text": "Which annotation injects dependencies?",
        "option_a": "@Inject",
        "option_b": "@Autowired",
        "option_c": "@Include",
        "option_d": "@DI",
        "correct_answer": "B"
    },
    {
        "question_text": "Spring Boot Actuator is used for:",
        "option_a": "Performance monitoring",
        "option_b": "HTML design",
        "option_c": "Dark mode",
        "option_d": "Unit testing",
        "correct_answer": "A"
    },
    {
        "question_text": "What is the default port for Spring Boot?",
        "option_a": "8000",
        "option_b": "3000",
        "option_c": "8080",
        "option_d": "443",
        "correct_answer": "C"
    }
],
282: [
    {
        "question_text": "OOP stands for:",
        "option_a": "Object-Oriented Programming",
        "option_b": "Online Operations Program",
        "option_c": "Object Output Process",
        "option_d": "Optimized Operating Platform",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is NOT an OOP concept?",
        "option_a": "Encapsulation",
        "option_b": "Inheritance",
        "option_c": "Polymorphism",
        "option_d": "Compilation",
        "correct_answer": "D"
    },
    {
        "question_text": "Which keyword is used to create an object?",
        "option_a": "build",
        "option_b": "object",
        "option_c": "new",
        "option_d": "create",
        "correct_answer": "C"
    },
    {
        "question_text": "Which keyword prevents inheritance?",
        "option_a": "static",
        "option_b": "final",
        "option_c": "private",
        "option_d": "sealed",
        "correct_answer": "B"
    },
    {
        "question_text": "Method overloading means:",
        "option_a": "Methods with same name, different parameters",
        "option_b": "Methods with different names",
        "option_c": "Methods in different classes",
        "option_d": "Using too many methods",
        "correct_answer": "A"
    },
    {
        "question_text": "Constructor is called when:",
        "option_a": "Object is created",
        "option_b": "Program ends",
        "option_c": "A variable is declared",
        "option_d": "File uploads",
        "correct_answer": "A"
    },
    {
        "question_text": "Which access modifier gives maximum restriction?",
        "option_a": "public",
        "option_b": "protected",
        "option_c": "package-private",
        "option_d": "private",
        "correct_answer": "D"
    },
    {
        "question_text": "Abstract classes can:",
        "option_a": "Have both abstract and normal methods",
        "option_b": "Only have concrete methods",
        "option_c": "Only have variables",
        "option_d": "Be instantiated directly",
        "correct_answer": "A"
    },
    {
        "question_text": "Interfaces in Java:",
        "option_a": "Support multiple inheritance",
        "option_b": "Cannot contain methods",
        "option_c": "Are database files",
        "option_d": "Are keywords",
        "correct_answer": "A"
    },
    {
        "question_text": "Encapsulation means:",
        "option_a": "Hiding data using access modifiers",
        "option_b": "Writing long code",
        "option_c": "Sorting objects",
        "option_d": "Printing logs",
        "correct_answer": "A"
    }
],
281: [
    {
        "question_text": "Which of the following is NOT a pillar of OOP in C++?",
        "option_a": "Encapsulation",
        "option_b": "Abstraction",
        "option_c": "Polymorphism",
        "option_d": "Compilation",
        "correct_answer": "D"
    },
    {
        "question_text": "Which header is used for vectors in C++ STL?",
        "option_a": "<vector>",
        "option_b": "<list>",
        "option_c": "<map>",
        "option_d": "<set>",
        "correct_answer": "A"
    },
    {
        "question_text": "Which STL container stores key-value pairs?",
        "option_a": "vector",
        "option_b": "map",
        "option_c": "stack",
        "option_d": "queue",
        "correct_answer": "B"
    },
    {
        "question_text": "Which keyword is used to inherit a class in C++?",
        "option_a": "inherits",
        "option_b": "extends",
        "option_c": ":",
        "option_d": "->",
        "correct_answer": "C"
    },
    {
        "question_text": "Which STL container follows FIFO?",
        "option_a": "stack",
        "option_b": "queue",
        "option_c": "set",
        "option_d": "map",
        "correct_answer": "B"
    },
    {
        "question_text": "Which method adds an element to a vector?",
        "option_a": "add()",
        "option_b": "insert()",
        "option_c": "push_back()",
        "option_d": "append()",
        "correct_answer": "C"
    },
    {
        "question_text": "Which C++ feature allows the same function name with different parameters?",
        "option_a": "Function overriding",
        "option_b": "Function overloading",
        "option_c": "Operator masking",
        "option_d": "Code expansion",
        "correct_answer": "B"
    },
    {
        "question_text": "Which container does NOT allow duplicate values?",
        "option_a": "vector",
        "option_b": "list",
        "option_c": "set",
        "option_d": "queue",
        "correct_answer": "C"
    },
    {
        "question_text": "The top element of a stack is accessed using:",
        "option_a": "front()",
        "option_b": "peek()",
        "option_c": "top()",
        "option_d": "head()",
        "correct_answer": "C"
    },
    {
        "question_text": "Which keyword is used to create an object dynamically?",
        "option_a": "malloc",
        "option_b": "alloc",
        "option_c": "new",
        "option_d": "create",
        "correct_answer": "C"
    }
],
280: [
    {
        "question_text": "Which data structure uses LIFO?",
        "option_a": "Queue",
        "option_b": "Stack",
        "option_c": "Tree",
        "option_d": "Graph",
        "correct_answer": "B"
    },
    {
        "question_text": "Which of the following is not a linear data structure?",
        "option_a": "Array",
        "option_b": "Linked List",
        "option_c": "Stack",
        "option_d": "Binary Tree",
        "correct_answer": "D"
    },
    {
        "question_text": "Which sorting algorithm has the best average-case performance?",
        "option_a": "Bubble Sort",
        "option_b": "Selection Sort",
        "option_c": "Quick Sort",
        "option_d": "Insertion Sort",
        "correct_answer": "C"
    },
    {
        "question_text": "Which pointer points to the next node in a linked list?",
        "option_a": "prev",
        "option_b": "next",
        "option_c": "head",
        "option_d": "ptr",
        "correct_answer": "B"
    },
    {
        "question_text": "Which traversal is used in BFS?",
        "option_a": "Stack",
        "option_b": "Queue",
        "option_c": "Vector",
        "option_d": "Array",
        "correct_answer": "B"
    },
    {
        "question_text": "Binary search requires:",
        "option_a": "Unsorted array",
        "option_b": "Sorted array",
        "option_c": "Hash table",
        "option_d": "Graph input",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is the complexity of searching in a linked list?",
        "option_a": "O(1)",
        "option_b": "O(n)",
        "option_c": "O(log n)",
        "option_d": "O(n log n)",
        "correct_answer": "B"
    },
    {
        "question_text": "Trees with left and right children are:",
        "option_a": "Arrays",
        "option_b": "Linked lists",
        "option_c": "Binary trees",
        "option_d": "Graphs",
        "correct_answer": "C"
    },
    {
        "question_text": "Which algorithm is used for finding shortest path in weighted graphs?",
        "option_a": "DFS",
        "option_b": "Binary Search",
        "option_c": "Dijkstra",
        "option_d": "Bubble Sort",
        "correct_answer": "C"
    },
    {
        "question_text": "Which data structure uses FIFO?",
        "option_a": "Stack",
        "option_b": "Queue",
        "option_c": "Tree",
        "option_d": "Graph",
        "correct_answer": "B"
    }
],
279: [
    {
        "question_text": "Bootstrap is primarily used for:",
        "option_a": "Backend development",
        "option_b": "Data science",
        "option_c": "Responsive UI design",
        "option_d": "Operating systems",
        "correct_answer": "C"
    },
    {
        "question_text": "Which class makes a button blue by default?",
        "option_a": "btn-primary",
        "option_b": "btn-blue",
        "option_c": "btn-main",
        "option_d": "btn-default",
        "correct_answer": "A"
    },
    {
        "question_text": "Bootstrap uses which CSS layout system?",
        "option_a": "Flexbox and Grid",
        "option_b": "Float only",
        "option_c": "Tables",
        "option_d": "Absolute positioning",
        "correct_answer": "A"
    },
    {
        "question_text": "Which class makes an element full width on all screens?",
        "option_a": "col-sm-12",
        "option_b": "col-md-6",
        "option_c": "col-lg-3",
        "option_d": "col-auto",
        "correct_answer": "A"
    },
    {
        "question_text": "Which component is used for modals in Bootstrap?",
        "option_a": "dialog",
        "option_b": ".modal",
        "option_c": ".popup",
        "option_d": ".overlay",
        "correct_answer": "B"
    },
    {
        "question_text": "Which class adds padding?",
        "option_a": "pt-3",
        "option_b": "pad-3",
        "option_c": "mg-3",
        "option_d": "offset-3",
        "correct_answer": "A"
    },
    {
        "question_text": "Which class centers text?",
        "option_a": "text-mid",
        "option_b": "text-center",
        "option_c": "center-text",
        "option_d": "align-mid",
        "correct_answer": "B"
    },
    {
        "question_text": "Bootstrap is maintained by:",
        "option_a": "Meta",
        "option_b": "Twitter",
        "option_c": "Google",
        "option_d": "Microsoft",
        "correct_answer": "B"
    },
    {
        "question_text": "Which JS library does Bootstrap 4 depend on?",
        "option_a": "React",
        "option_b": "Vue",
        "option_c": "jQuery",
        "option_d": "Svelte",
        "correct_answer": "C"
    },
    {
        "question_text": "Bootstrap’s grid has how many columns?",
        "option_a": "10",
        "option_b": "12",
        "option_c": "8",
        "option_d": "16",
        "correct_answer": "B"
    }
],

278: [
    {
        "question_text": "HTML stands for:",
        "option_a": "Hyperlink Text Markup Language",
        "option_b": "Hyper Text Markup Language",
        "option_c": "High Transfer Markup Language",
        "option_d": "Hyper Tool Markup Language",
        "correct_answer": "B"
    },
    {
        "question_text": "Which tag is used for the largest heading?",
        "option_a": "<h1>",
        "option_b": "<head>",
        "option_c": "<title>",
        "option_d": "<h6>",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS is used for:",
        "option_a": "Database queries",
        "option_b": "Backend logic",
        "option_c": "Styling web pages",
        "option_d": "Routing APIs",
        "correct_answer": "C"
    },
    {
        "question_text": "Which display mode uses flexbox?",
        "option_a": "display: grid;",
        "option_b": "display: flex;",
        "option_c": "display: table;",
        "option_d": "display: none;",
        "correct_answer": "B"
    },
    {
        "question_text": "Which tag is used for a paragraph?",
        "option_a": "<p>",
        "option_b": "<text>",
        "option_c": "<para>",
        "option_d": "<pr>",
        "correct_answer": "A"
    },
    {
        "question_text": "Which attribute sets an image source?",
        "option_a": "src",
        "option_b": "href",
        "option_c": "link",
        "option_d": "img",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS stands for:",
        "option_a": "Cascading Style Sheets",
        "option_b": "Creative Style System",
        "option_c": "Coded Style Sheets",
        "option_d": "Control Sheet System",
        "correct_answer": "A"
    },
    {
        "question_text": "Which CSS property changes text color?",
        "option_a": "color",
        "option_b": "text-color",
        "option_c": "font-color",
        "option_d": "style-color",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tag is used for links?",
        "option_a": "<link>",
        "option_b": "<goto>",
        "option_c": "<a>",
        "option_d": "<url>",
        "correct_answer": "C"
    },
    {
        "question_text": "Which HTML element contains all visible content?",
        "option_a": "<html>",
        "option_b": "<body>",
        "option_c": "<main>",
        "option_d": "<section>",
        "correct_answer": "B"
    }
],

277: [
    {
        "question_text": "Microservices architecture consists of:",
        "option_a": "One large monolithic application",
        "option_b": "Multiple small independent services",
        "option_c": "Frontend-only components",
        "option_d": "Only database modules",
        "correct_answer": "B"
    },
    {
        "question_text": "Microservices typically communicate via:",
        "option_a": "Email",
        "option_b": "REST APIs",
        "option_c": "Photos",
        "option_d": "CSS",
        "correct_answer": "B"
    },
    {
        "question_text": "A key advantage of microservices is:",
        "option_a": "Tightly coupled systems",
        "option_b": "Independent deployment",
        "option_c": "Single-point failure",
        "option_d": "Slow scaling",
        "correct_answer": "B"
    },
    {
        "question_text": "Which tool is used for service discovery?",
        "option_a": "Docker",
        "option_b": "Eureka",
        "option_c": "Figma",
        "option_d": "NPM",
        "correct_answer": "B"
    },
    {
        "question_text": "API Gateway is used for:",
        "option_a": "Image editing",
        "option_b": "Routing requests to microservices",
        "option_c": "Creating UI",
        "option_d": "Data encryption",
        "correct_answer": "B"
    },
    {
        "question_text": "Which pattern helps services communicate asynchronously?",
        "option_a": "Message queues",
        "option_b": "Local functions",
        "option_c": "Monolithic logic",
        "option_d": "CSS grids",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is a container orchestration tool?",
        "option_a": "Jenkins",
        "option_b": "Kubernetes",
        "option_c": "Photoshop",
        "option_d": "Premiere Pro",
        "correct_answer": "B"
    },
    {
        "question_text": "Microservices should be:",
        "option_a": "Highly dependent",
        "option_b": "Loosely coupled",
        "option_c": "Merged tightly",
        "option_d": "UI-driven",
        "correct_answer": "B"
    },
    {
        "question_text": "Which database style is often used in microservices?",
        "option_a": "Single shared DB",
        "option_b": "Database-per-service",
        "option_c": "Excel sheets",
        "option_d": "Word files",
        "correct_answer": "B"
    },
    {
        "question_text": "Docker helps microservices by:",
        "option_a": "Providing containers for isolation",
        "option_b": "Creating animations",
        "option_c": "Making UI layouts",
        "option_d": "Managing users",
        "correct_answer": "A"
    }
],

276: [
    {
        "question_text": "System design focuses on:",
        "option_a": "Hyper-realistic 3D modeling",
        "option_b": "High-level architecture of software systems",
        "option_c": "Image compression",
        "option_d": "Sound processing",
        "correct_answer": "B"
    },
    {
        "question_text": "Load balancers are used to:",
        "option_a": "Store images",
        "option_b": "Distribute traffic across servers",
        "option_c": "Resize windows",
        "option_d": "Format databases",
        "correct_answer": "B"
    },
    {
        "question_text": "Caching improves:",
        "option_a": "Storage cost",
        "option_b": "Response speed",
        "option_c": "UI design",
        "option_d": "File encryption",
        "correct_answer": "B"
    },
    {
        "question_text": "Which database is used for horizontal scaling?",
        "option_a": "SQL",
        "option_b": "NoSQL",
        "option_c": "Excel",
        "option_d": "CSV",
        "correct_answer": "B"
    },
    {
        "question_text": "A CDN is used for:",
        "option_a": "Text translation",
        "option_b": "Delivering static files fast",
        "option_c": "File deletion",
        "option_d": "Server shutdown",
        "correct_answer": "B"
    },
    {
        "question_text": "Sharding means:",
        "option_a": "Encrypting files",
        "option_b": "Splitting databases into smaller parts",
        "option_c": "Improving UI design",
        "option_d": "Logging errors",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is an example of asynchronous communication?",
        "option_a": "Message queues",
        "option_b": "Synchronous API calls",
        "option_c": "Direct SQL queries",
        "option_d": "CSS flex layouts",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tool monitors system metrics?",
        "option_a": "Prometheus",
        "option_b": "Photoshop",
        "option_c": "Illustrator",
        "option_d": "Notepad",
        "correct_answer": "A"
    },
    {
        "question_text": "A database index improves:",
        "option_a": "UI color",
        "option_b": "Query performance",
        "option_c": "Animation speed",
        "option_d": "Cloud cost",
        "correct_answer": "B"
    },
    {
        "question_text": "Replication helps by:",
        "option_a": "Deleting old data",
        "option_b": "Providing redundancy",
        "option_c": "Creating schemas",
        "option_d": "Optimizing CSS",
        "correct_answer": "B"
    }
],

275: [
    {
        "question_text": "SDLC stands for:",
        "option_a": "Software Development Life Cycle",
        "option_b": "System Data Layer Control",
        "option_c": "Software Deployment Logic Cycle",
        "option_d": "Service Data Logic Component",
        "correct_answer": "A"
    },
    {
        "question_text": "Which SDLC model is linear?",
        "option_a": "Agile",
        "option_b": "Scrum",
        "option_c": "Waterfall",
        "option_d": "Iterative",
        "correct_answer": "C"
    },
    {
        "question_text": "UML diagrams are used for:",
        "option_a": "Database storage",
        "option_b": "Visual modeling",
        "option_c": "CSS animations",
        "option_d": "Logs",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is NOT a software testing type?",
        "option_a": "Unit testing",
        "option_b": "Integration testing",
        "option_c": "System testing",
        "option_d": "Farming testing",
        "correct_answer": "D"
    },
    {
        "question_text": "Version control manages:",
        "option_a": "File backups",
        "option_b": "Code changes",
        "option_c": "Music",
        "option_d": "Themes",
        "correct_answer": "B"
    },
    {
        "question_text": "A bug report should include:",
        "option_a": "User's favorite color",
        "option_b": "Steps to reproduce",
        "option_c": "Developer salary",
        "option_d": "Unused files",
        "correct_answer": "B"
    },
    {
        "question_text": "Which model encourages continuous delivery?",
        "option_a": "Waterfall",
        "option_b": "Agile",
        "option_c": "V-model",
        "option_d": "Big-bang",
        "correct_answer": "B"
    },
    {
        "question_text": "Which diagram shows system workflow?",
        "option_a": "Activity diagram",
        "option_b": "Class diagram",
        "option_c": "ER diagram",
        "option_d": "Brain map",
        "correct_answer": "A"
    },
    {
        "question_text": "Who is responsible for product backlog?",
        "option_a": "Developer",
        "option_b": "Tester",
        "option_c": "Product Owner",
        "option_d": "Client",
        "correct_answer": "C"
    },
    {
        "question_text": "A sprint typically lasts:",
        "option_a": "1–4 weeks",
        "option_b": "6 months",
        "option_c": "1 year",
        "option_d": "12 hours",
        "correct_answer": "A"
    }
],

274: [
    {
        "question_text": "Git is a:",
        "option_a": "Programming language",
        "option_b": "Version control system",
        "option_c": "Database",
        "option_d": "Game engine",
        "correct_answer": "B"
    },
    {
        "question_text": "Which command creates a new Git repository?",
        "option_a": "git start",
        "option_b": "git init",
        "option_c": "git begin",
        "option_d": "git new",
        "correct_answer": "B"
    },
    {
        "question_text": "Which command stages files?",
        "option_a": "git push",
        "option_b": "git add",
        "option_c": "git commit",
        "option_d": "git log",
        "correct_answer": "B"
    },
    {
        "question_text": "Which command shows commit history?",
        "option_a": "git view",
        "option_b": "git show",
        "option_c": "git log",
        "option_d": "git history",
        "correct_answer": "C"
    },
    {
        "question_text": "GitHub is primarily used for:",
        "option_a": "Hosting Git repositories",
        "option_b": "Image editing",
        "option_c": "Video editing",
        "option_d": "3D modeling",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command commits changes?",
        "option_a": "git push",
        "option_b": "git commit -m",
        "option_c": "git add -m",
        "option_d": "git update",
        "correct_answer": "B"
    },
    {
        "question_text": "Which command downloads a repo?",
        "option_a": "git copy",
        "option_b": "git clone",
        "option_c": "git take",
        "option_d": "git download",
        "correct_answer": "B"
    },
    {
        "question_text": "A pull request is used for:",
        "option_a": "Code review before merging",
        "option_b": "Deleting files",
        "option_c": "Changing repo name",
        "option_d": "Making videos",
        "correct_answer": "A"
    },
    {
        "question_text": "Branches in Git are used for:",
        "option_a": "Dividing code versions",
        "option_b": "Storing videos",
        "option_c": "Creating designs",
        "option_d": "Taking screenshots",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command pushes code?",
        "option_a": "git send",
        "option_b": "git push",
        "option_c": "git update",
        "option_d": "git deploy",
        "correct_answer": "B"
    }
],

273: [
    {
        "question_text": "DevOps combines:",
        "option_a": "Development and Operations",
        "option_b": "Design and Testing",
        "option_c": "Hardware and Software",
        "option_d": "UI and UX",
        "correct_answer": "A"
    },
    {
        "question_text": "CI/CD stands for:",
        "option_a": "Code Integration / Code Deployment",
        "option_b": "Continuous Integration / Continuous Delivery",
        "option_c": "Central Input / Central Data",
        "option_d": "Container Image / Code Debugging",
        "correct_answer": "B"
    },
    {
        "question_text": "Which tool is used for CI/CD?",
        "option_a": "Jenkins",
        "option_b": "Excel",
        "option_c": "Figma",
        "option_d": "Photoshop",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker is used for:",
        "option_a": "Containerization",
        "option_b": "3D rendering",
        "option_c": "Hosting videos",
        "option_d": "Making music",
        "correct_answer": "A"
    },
    {
        "question_text": "Infrastructure as Code (IaC) uses tools like:",
        "option_a": "Terraform",
        "option_b": "After Effects",
        "option_c": "Power BI",
        "option_d": "Photoshop",
        "correct_answer": "A"
    },
    {
        "question_text": "Monitoring tools include:",
        "option_a": "Adobe XD",
        "option_b": "Prometheus",
        "option_c": "Canva",
        "option_d": "Word",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is a configuration management tool?",
        "option_a": "Ansible",
        "option_b": "VS Code",
        "option_c": "Android Studio",
        "option_d": "Figma",
        "correct_answer": "A"
    },
    {
        "question_text": "Kubernetes is used to:",
        "option_a": "Build dashboards",
        "option_b": "Orchestrate containers",
        "option_c": "Edit videos",
        "option_d": "Create web pages",
        "correct_answer": "B"
    },
    {
        "question_text": "Version control in DevOps helps with:",
        "option_a": "Tracking code changes",
        "option_b": "Playing games",
        "option_c": "Sending emails",
        "option_d": "Graphic design",
        "correct_answer": "A"
    },
    {
        "question_text": "Which of these supports automated deployments?",
        "option_a": "CI/CD pipeline",
        "option_b": "MS Word",
        "option_c": "Paint",
        "option_d": "Calculator",
        "correct_answer": "A"
    }
],

272: [
    {
        "question_text": "Kubernetes is mainly used for:",
        "option_a": "Video editing",
        "option_b": "Container orchestration",
        "option_c": "Photo editing",
        "option_d": "Graphics design",
        "correct_answer": "B"
    },
    {
        "question_text": "A Kubernetes Pod contains:",
        "option_a": "One or more containers",
        "option_b": "Only images",
        "option_c": "Only logs",
        "option_d": "Only artifacts",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command checks cluster info?",
        "option_a": "kubectl info",
        "option_b": "kubectl cluster-info",
        "option_c": "kubectl data",
        "option_d": "kubectl view",
        "correct_answer": "B"
    },
    {
        "question_text": "K8s stands for:",
        "option_a": "Kernel 8",
        "option_b": "Kubernetes",
        "option_c": "Key builder",
        "option_d": "Kilo bytes",
        "correct_answer": "B"
    },
    {
        "question_text": "Which component schedules pods?",
        "option_a": "Scheduler",
        "option_b": "Controller",
        "option_c": "ReplicaSet",
        "option_d": "ConfigMap",
        "correct_answer": "A"
    },
    {
        "question_text": "ConfigMap stores:",
        "option_a": "Large video files",
        "option_b": "Key-value config data",
        "option_c": "Databases",
        "option_d": "Passwords only",
        "correct_answer": "B"
    },
    {
        "question_text": "Kubernetes service exposes:",
        "option_a": "Phones",
        "option_b": "Pods to network",
        "option_c": "Physical servers",
        "option_d": "USB devices",
        "correct_answer": "B"
    },
    {
        "question_text": "kubectl delete pod deletes:",
        "option_a": "A video",
        "option_b": "A running pod",
        "option_c": "A database",
        "option_d": "CSS file",
        "correct_answer": "B"
    },
    {
        "question_text": "ReplicaSets ensure:",
        "option_a": "UI design",
        "option_b": "Desired number of pod replicas",
        "option_c": "Video resolution",
        "option_d": "Music playback",
        "correct_answer": "B"
    },
    {
        "question_text": "Kubernetes nodes are:",
        "option_a": "Databases",
        "option_b": "Worker machines",
        "option_c": "Images",
        "option_d": "Requests",
        "correct_answer": "B"
    }
],

271: [
    {
        "question_text": "Docker is used for:",
        "option_a": "Containerization",
        "option_b": "Image editing",
        "option_c": "Audio recording",
        "option_d": "Animations",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker images are:",
        "option_a": "Running programs",
        "option_b": "Templates used to create containers",
        "option_c": "Databases",
        "option_d": "Videos",
        "correct_answer": "B"
    },
    {
        "question_text": "Which command starts a container?",
        "option_a": "docker run",
        "option_b": "docker play",
        "option_c": "docker begin",
        "option_d": "docker new",
        "correct_answer": "A"
    },
    {
        "question_text": "Dockerfile is used to:",
        "option_a": "Store logs",
        "option_b": "Build images",
        "option_c": "Delete code",
        "option_d": "Upload videos",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is a container registry?",
        "option_a": "VS Code",
        "option_b": "Docker Hub",
        "option_c": "Instagram",
        "option_d": "Netflix",
        "correct_answer": "B"
    },
    {
        "question_text": "docker ps shows:",
        "option_a": "Running containers",
        "option_b": "Apps list",
        "option_c": "3D files",
        "option_d": "Songs",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command stops a container?",
        "option_a": "docker stop",
        "option_b": "docker end",
        "option_c": "docker halt",
        "option_d": "docker kill",
        "correct_answer": "A"
    },
    {
        "question_text": "Volumes in Docker store:",
        "option_a": "Persistent data",
        "option_b": "Icons",
        "option_c": "Videos",
        "option_d": "Themes",
        "correct_answer": "A"
    },
    {
        "question_text": "Containers are:",
        "option_a": "Lightweight isolated environments",
        "option_b": "Heavy VMs",
        "option_c": "Databases",
        "option_d": "Music files",
        "correct_answer": "A"
    },
    {
        "question_text": "docker build creates:",
        "option_a": "A folder",
        "option_b": "An image",
        "option_c": "A Python project",
        "option_d": "A video",
        "correct_answer": "B"
    }
],
270: [
    {
        "question_text": "Microsoft Azure is a:",
        "option_a": "Database",
        "option_b": "Cloud computing platform",
        "option_c": "Programming language",
        "option_d": "Game engine",
        "correct_answer": "B"
    },
    {
        "question_text": "Azure VM stands for:",
        "option_a": "Virtual Machine",
        "option_b": "Video Manager",
        "option_c": "Value Mode",
        "option_d": "Virtual Map",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Storage is used for:",
        "option_a": "Static files and data",
        "option_b": "UI design",
        "option_c": "Email writing",
        "option_d": "Game development",
        "correct_answer": "A"
    },
    {
        "question_text": "AAD in Azure stands for:",
        "option_a": "Azure Application Deployment",
        "option_b": "Azure Active Directory",
        "option_c": "Account Access Data",
        "option_d": "Admin Access Domain",
        "correct_answer": "B"
    },
    {
        "question_text": "Which service is used for serverless computing?",
        "option_a": "Azure Functions",
        "option_b": "Azure Compute",
        "option_c": "Azure Mail",
        "option_d": "Azure WebView",
        "correct_answer": "A"
    },
    {
        "question_text": "Which Azure service hosts web apps?",
        "option_a": "App Service",
        "option_b": "Photo Service",
        "option_c": "Design Studio",
        "option_d": "DB Connect",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Blob Storage stores:",
        "option_a": "Binary large objects",
        "option_b": "UI wireframes",
        "option_c": "Emails",
        "option_d": "3D models",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure CLI is used for:",
        "option_a": "Command-line management",
        "option_b": "Drawing pictures",
        "option_c": "Photo editing",
        "option_d": "Cloud gaming",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Region refers to:",
        "option_a": "Data center location",
        "option_b": "Color theme",
        "option_c": "CSS layout",
        "option_d": "API error page",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Monitor tracks:",
        "option_a": "Health of cloud resources",
        "option_b": "Mobile notifications",
        "option_c": "Video ads",
        "option_d": "Facebook likes",
        "correct_answer": "A"
    }
],
269: [
    {
        "question_text": "AWS stands for:",
        "option_a": "Amazon Web Services",
        "option_b": "Azure Web System",
        "option_c": "Advanced Web Server",
        "option_d": "Application Web Service",
        "correct_answer": "A"
    },
    {
        "question_text": "Which AWS service is used for object storage?",
        "option_a": "EC2",
        "option_b": "Lambda",
        "option_c": "S3",
        "option_d": "RDS",
        "correct_answer": "C"
    },
    {
        "question_text": "EC2 provides:",
        "option_a": "Virtual servers",
        "option_b": "Container orchestration",
        "option_c": "Database backups",
        "option_d": "Email services",
        "correct_answer": "A"
    },
    {
        "question_text": "IAM in AWS is used for:",
        "option_a": "Billing",
        "option_b": "Identity and Access Management",
        "option_c": "Image processing",
        "option_d": "AI training",
        "correct_answer": "B"
    },
    {
        "question_text": "AWS Lambda is used for:",
        "option_a": "Serverless computing",
        "option_b": "Hosting websites",
        "option_c": "Mobile development",
        "option_d": "Image editing",
        "correct_answer": "A"
    },
    {
        "question_text": "RDS is a:",
        "option_a": "Relational Database Service",
        "option_b": "Remote Deployment System",
        "option_c": "Runtime Delivery Server",
        "option_d": "Resource Data Software",
        "correct_answer": "A"
    },
    {
        "question_text": "CloudFront is a:",
        "option_a": "Firewall",
        "option_b": "CDN",
        "option_c": "Database engine",
        "option_d": "Monitoring tool",
        "correct_answer": "B"
    },
    {
        "question_text": "Which service launches containers?",
        "option_a": "ECS",
        "option_b": "S3",
        "option_c": "IAM",
        "option_d": "SNS",
        "correct_answer": "A"
    },
    {
        "question_text": "SQS is a service for:",
        "option_a": "Queues",
        "option_b": "Security",
        "option_c": "Images",
        "option_d": "Emails",
        "correct_answer": "A"
    },
    {
        "question_text": "AWS region refers to:",
        "option_a": "Data center location",
        "option_b": "Color theme",
        "option_c": "Cloud storage limit",
        "option_d": "IAM user",
        "correct_answer": "A"
    }
],

268: [
    {
        "question_text": "An operating system acts as a:",
        "option_a": "Web browser",
        "option_b": "Interface between hardware and user",
        "option_c": "Cloud server",
        "option_d": "Database engine",
        "correct_answer": "B"
    },
    {
        "question_text": "A process is:",
        "option_a": "A running program",
        "option_b": "A storage device",
        "option_c": "A network packet",
        "option_d": "A code comment",
        "correct_answer": "A"
    },
    {
        "question_text": "Deadlock involves:",
        "option_a": "Memory fragmentation",
        "option_b": "Processes waiting indefinitely",
        "option_c": "High CPU usage",
        "option_d": "File corruption",
        "correct_answer": "B"
    },
    {
        "question_text": "Round Robin is a:",
        "option_a": "Memory algorithm",
        "option_b": "Scheduling algorithm",
        "option_c": "Disk optimization method",
        "option_d": "Network model",
        "correct_answer": "B"
    },
    {
        "question_text": "Thrashing occurs when:",
        "option_a": "RAM is underused",
        "option_b": "System spends too much time swapping",
        "option_c": "CPU overheats",
        "option_d": "Network drops",
        "correct_answer": "B"
    },
    {
        "question_text": "Virtual memory uses:",
        "option_a": "Cache memory",
        "option_b": "Secondary storage",
        "option_c": "CPU register",
        "option_d": "USB",
        "correct_answer": "B"
    },
    {
        "question_text": "Mutex ensures:",
        "option_a": "Parallel execution",
        "option_b": "Mutual exclusion",
        "option_c": "Infinite loops",
        "option_d": "File locking",
        "correct_answer": "B"
    },
    {
        "question_text": "Kernel mode allows:",
        "option_a": "Limited access",
        "option_b": "Full system access",
        "option_c": "No access",
        "option_d": "Frontend control",
        "correct_answer": "B"
    },
    {
        "question_text": "Which is NOT an OS?",
        "option_a": "Windows",
        "option_b": "Linux",
        "option_c": "Python",
        "option_d": "MacOS",
        "correct_answer": "C"
    },
    {
        "question_text": "Paging helps with:",
        "option_a": "Reducing code",
        "option_b": "Memory management",
        "option_c": "Multiprocessing",
        "option_d": "Gaming",
        "correct_answer": "B"
    }
],

267: [
    {
        "question_text": "Computer networks allow:",
        "option_a": "Sharing resources",
        "option_b": "Cooking food",
        "option_c": "Editing images",
        "option_d": "Watching movies",
        "correct_answer": "A"
    },
    {
        "question_text": "TCP stands for:",
        "option_a": "Transmission Control Protocol",
        "option_b": "Transfer Central Program",
        "option_c": "Technical Communication Process",
        "option_d": "Time Control Packet",
        "correct_answer": "A"
    },
    {
        "question_text": "IP address identifies:",
        "option_a": "A network cable",
        "option_b": "A device on a network",
        "option_c": "A database",
        "option_d": "A username",
        "correct_answer": "B"
    },
    {
        "question_text": "HTTP is used for:",
        "option_a": "Image editing",
        "option_b": "Web communication",
        "option_c": "Video playback",
        "option_d": "File compression",
        "correct_answer": "B"
    },
    {
        "question_text": "Routers operate at:",
        "option_a": "Network layer",
        "option_b": "Physical layer",
        "option_c": "Data link layer",
        "option_d": "Application layer",
        "correct_answer": "A"
    },
    {
        "question_text": "Ping checks:",
        "option_a": "Memory",
        "option_b": "Network connectivity",
        "option_c": "Disk usage",
        "option_d": "CPU performance",
        "correct_answer": "B"
    },
    {
        "question_text": "DNS translates:",
        "option_a": "Audio files",
        "option_b": "Domain names to IPs",
        "option_c": "Images to vectors",
        "option_d": "PDFs to text",
        "correct_answer": "B"
    },
    {
        "question_text": "LAN stands for:",
        "option_a": "Local Area Network",
        "option_b": "Large Access Node",
        "option_c": "Local Antenna Net",
        "option_d": "Long Area Network",
        "correct_answer": "A"
    },
    {
        "question_text": "Firewall protects against:",
        "option_a": "Viruses",
        "option_b": "Unauthorized access",
        "option_c": "Electric shock",
        "option_d": "Overheating",
        "correct_answer": "B"
    },
    {
        "question_text": "Which cable is fastest?",
        "option_a": "Copper",
        "option_b": "Fiber optic",
        "option_c": "Coaxial",
        "option_d": "USB",
        "correct_answer": "B"
    }
],

266: [
    {
        "question_text": "Ethical hacking is used for:",
        "option_a": "Illegal access",
        "option_b": "Testing security",
        "option_c": "Gaming",
        "option_d": "Website design",
        "correct_answer": "B"
    },
    {
        "question_text": "The phase of gathering information is called:",
        "option_a": "Enumeration",
        "option_b": "Scanning",
        "option_c": "Reconnaissance",
        "option_d": "Exploitation",
        "correct_answer": "C"
    },
    {
        "question_text": "Which tool scans network vulnerabilities?",
        "option_a": "Nmap",
        "option_b": "Photoshop",
        "option_c": "Premiere",
        "option_d": "Illustrator",
        "correct_answer": "A"
    },
    {
        "question_text": "Brute-force attack tries:",
        "option_a": "Guessing passwords",
        "option_b": "Breaking hardware",
        "option_c": "Deleting files",
        "option_d": "Video editing",
        "correct_answer": "A"
    },
    {
        "question_text": "VPN provides:",
        "option_a": "Anonymous secure connection",
        "option_b": "Cooking recipes",
        "option_c": "Game hacks",
        "option_d": "Email drafts",
        "correct_answer": "A"
    },
    {
        "question_text": "Phishing is:",
        "option_a": "Fake email attack",
        "option_b": "Wireless hacking",
        "option_c": "Server backup",
        "option_d": "Cloud pricing",
        "correct_answer": "A"
    },
    {
        "question_text": "Firewalls protect:",
        "option_a": "Computers from threats",
        "option_b": "Clothes from fire",
        "option_c": "Fans from dust",
        "option_d": "Phones from heat",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL injection targets:",
        "option_a": "Databases",
        "option_b": "Images",
        "option_c": "3D models",
        "option_d": "Audio files",
        "correct_answer": "A"
    },
    {
        "question_text": "Wireshark captures:",
        "option_a": "Network packets",
        "option_b": "Photos",
        "option_c": "Videos",
        "option_d": "Radio signals",
        "correct_answer": "A"
    },
    {
        "question_text": "Two-factor authentication adds:",
        "option_a": "Extra security layer",
        "option_b": "Camera feature",
        "option_c": "Music feature",
        "option_d": "Storage space",
        "correct_answer": "A"
    }
],

265: [
    {
        "question_text": "Cybersecurity protects:",
        "option_a": "Clothes",
        "option_b": "Digital systems",
        "option_c": "Food",
        "option_d": "Furniture",
        "correct_answer": "B"
    },
    {
        "question_text": "Malware includes:",
        "option_a": "Virus",
        "option_b": "Worm",
        "option_c": "Trojan",
        "option_d": "All of these",
        "correct_answer": "D"
    },
    {
        "question_text": "Encryption converts:",
        "option_a": "Plain text to unreadable text",
        "option_b": "Text to image",
        "option_c": "Image to audio",
        "option_d": "Audio to video",
        "correct_answer": "A"
    },
    {
        "question_text": "Firewall filters:",
        "option_a": "Network traffic",
        "option_b": "Emails",
        "option_c": "Power",
        "option_d": "Noise",
        "correct_answer": "A"
    },
    {
        "question_text": "A strong password contains:",
        "option_a": "Only letters",
        "option_b": "Mixed characters",
        "option_c": "Only numbers",
        "option_d": "Only symbols",
        "correct_answer": "B"
    },
    {
        "question_text": "Ransomware:",
        "option_a": "Demands money",
        "option_b": "Plays music",
        "option_c": "Shows ads",
        "option_d": "Fixes phones",
        "correct_answer": "A"
    },
    {
        "question_text": "VPN protects:",
        "option_a": "Online privacy",
        "option_b": "Car engine",
        "option_c": "Camera lens",
        "option_d": "Printer",
        "correct_answer": "A"
    },
    {
        "question_text": "DoS attack overloads:",
        "option_a": "Servers",
        "option_b": "Speakers",
        "option_c": "Lights",
        "option_d": "Keyboards",
        "correct_answer": "A"
    },
    {
        "question_text": "Antivirus software:",
        "option_a": "Detects malware",
        "option_b": "Edits images",
        "option_c": "Makes diagrams",
        "option_d": "Creates slides",
        "correct_answer": "A"
    },
    {
        "question_text": "Personal data protection is part of:",
        "option_a": "Cybersecurity",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Sports",
        "correct_answer": "A"
    }
],

264: [
    {
        "question_text": "Prompt engineering is used for:",
        "option_a": "Training large language models",
        "option_b": "Writing instructions for AI",
        "option_c": "Editing images",
        "option_d": "Controlling hardware",
        "correct_answer": "B"
    },
    {
        "question_text": "A prompt must be:",
        "option_a": "Clear and structured",
        "option_b": "Long and complex",
        "option_c": "Confusing",
        "option_d": "Short with no context",
        "correct_answer": "A"
    },
    {
        "question_text": "Role prompting means:",
        "option_a": "Giving AI a role",
        "option_b": "Adding colors",
        "option_c": "Optimizing RAM",
        "option_d": "Changing password",
        "correct_answer": "A"
    },
    {
        "question_text": "Zero-shot prompting means:",
        "option_a": "AI solves without examples",
        "option_b": "AI needs 10 examples",
        "option_c": "AI refuses output",
        "option_d": "AI writes code only",
        "correct_answer": "A"
    },
    {
        "question_text": "Few-shot prompting means:",
        "option_a": "Giving sample inputs/outputs",
        "option_b": "Giving no data",
        "option_c": "Giving passwords",
        "option_d": "Giving URLs",
        "correct_answer": "A"
    },
    {
        "question_text": "Temperature controls:",
        "option_a": "Randomness",
        "option_b": "Brightness",
        "option_c": "Audio",
        "option_d": "Storage",
        "correct_answer": "A"
    },
    {
        "question_text": "Chain-of-thought is used for:",
        "option_a": "Step-by-step reasoning",
        "option_b": "Random answers",
        "option_c": "Image filters",
        "option_d": "Network logs",
        "correct_answer": "A"
    },
    {
        "question_text": "Prompt context gives:",
        "option_a": "Relevant background info",
        "option_b": "Unrelated files",
        "option_c": "Music",
        "option_d": "Brightness",
        "correct_answer": "A"
    },
    {
        "question_text": "LLM stands for:",
        "option_a": "Large Language Model",
        "option_b": "Long Learning Module",
        "option_c": "Logical Language Maker",
        "option_d": "Large Level Machine",
        "correct_answer": "A"
    },
    {
        "question_text": "Prompt evaluation checks:",
        "option_a": "Quality of outputs",
        "option_b": "Printer ink",
        "option_c": "Color saturation",
        "option_d": "Noise level",
        "correct_answer": "A"
    }
],

263: [
    {
        "question_text": "NLP stands for:",
        "option_a": "Natural Language Processing",
        "option_b": "Network Line Protocol",
        "option_c": "Node Language Program",
        "option_d": "New Learning Process",
        "correct_answer": "A"
    },
    {
        "question_text": "Tokenization splits text into:",
        "option_a": "Images",
        "option_b": "Small units",
        "option_c": "Videos",
        "option_d": "Maps",
        "correct_answer": "B"
    },
    {
        "question_text": "Stemming reduces words to:",
        "option_a": "Longest form",
        "option_b": "Root form",
        "option_c": "Random form",
        "option_d": "Opposite form",
        "correct_answer": "B"
    },
    {
        "question_text": "Sentiment analysis detects:",
        "option_a": "Color",
        "option_b": "Emotion",
        "option_c": "Speed",
        "option_d": "Size",
        "correct_answer": "B"
    },
    {
        "question_text": "Which model is transformer-based?",
        "option_a": "GPT",
        "option_b": "SVM",
        "option_c": "KNN",
        "option_d": "Naive Bayes",
        "correct_answer": "A"
    },
    {
        "question_text": "Stopwords are:",
        "option_a": "Common words ignored",
        "option_b": "HTML tags",
        "option_c": "Large images",
        "option_d": "Audio clips",
        "correct_answer": "A"
    },
    {
        "question_text": "NER extracts:",
        "option_a": "Entities like names",
        "option_b": "Videos",
        "option_c": "UI designs",
        "option_d": "Passwords",
        "correct_answer": "A"
    },
    {
        "question_text": "Embeddings represent words as:",
        "option_a": "Vectors",
        "option_b": "Colors",
        "option_c": "HTML",
        "option_d": "CSS",
        "correct_answer": "A"
    },
    {
        "question_text": "BLEU score evaluates:",
        "option_a": "Translation quality",
        "option_b": "CPU usage",
        "option_c": "Internet speed",
        "option_d": "Color depth",
        "correct_answer": "A"
    },
    {
        "question_text": "Text classification assigns:",
        "option_a": "Labels to text",
        "option_b": "Music to audio",
        "option_c": "Colors to images",
        "option_d": "Routes to servers",
        "correct_answer": "A"
    }
],

262: [
    {
        "question_text": "AI stands for:",
        "option_a": "Artificial Intelligence",
        "option_b": "Advanced Internet",
        "option_c": "Artificial Input",
        "option_d": "Automated Interface",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is a type of AI?",
        "option_a": "Narrow AI",
        "option_b": "Cosmic AI",
        "option_c": "Space AI",
        "option_d": "Water AI",
        "correct_answer": "A"
    },
    {
        "question_text": "Search algorithms are used for:",
        "option_a": "Finding solutions",
        "option_b": "Editing photos",
        "option_c": "Making movies",
        "option_d": "Playing music",
        "correct_answer": "A"
    },
    {
        "question_text": "Agents operate in:",
        "option_a": "Environments",
        "option_b": "Browsers",
        "option_c": "Games only",
        "option_d": "Files",
        "correct_answer": "A"
    },
    {
        "question_text": "Heuristics help AI by:",
        "option_a": "Speeding up decisions",
        "option_b": "Playing videos",
        "option_c": "Changing icons",
        "option_d": "Saving documents",
        "correct_answer": "A"
    },
    {
        "question_text": "ML is a subset of:",
        "option_a": "AI",
        "option_b": "Physics",
        "option_c": "Biology",
        "option_d": "History",
        "correct_answer": "A"
    },
    {
        "question_text": "Knowledge representation stores:",
        "option_a": "Structured knowledge",
        "option_b": "Books",
        "option_c": "Albums",
        "option_d": "Chats",
        "correct_answer": "A"
    },
    {
        "question_text": "Turing test checks:",
        "option_a": "Machine intelligence",
        "option_b": "Memory size",
        "option_c": "Network cables",
        "option_d": "System speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Neural networks contain:",
        "option_a": "Layers of nodes",
        "option_b": "Only one layer",
        "option_c": "Music files",
        "option_d": "HTML tables",
        "correct_answer": "A"
    },
    {
        "question_text": "AI applications include:",
        "option_a": "Speech recognition",
        "option_b": "Cooking",
        "option_c": "Swimming",
        "option_d": "Painting walls",
        "correct_answer": "A"
    }
],

261: [
    {
        "question_text": "Competitive programming focuses on:",
        "option_a": "Fast problem solving",
        "option_b": "Cooking recipes",
        "option_c": "Color grading",
        "option_d": "Painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Time complexity measures:",
        "option_a": "Execution time",
        "option_b": "Image resolution",
        "option_c": "Sound quality",
        "option_d": "Network bandwidth",
        "correct_answer": "A"
    },
    {
        "question_text": "Binary search works on:",
        "option_a": "Sorted arrays",
        "option_b": "Random lists",
        "option_c": "Unsorted graphs",
        "option_d": "Heat maps",
        "correct_answer": "A"
    },
    {
        "question_text": "Two-pointer technique is used for:",
        "option_a": "Array problems",
        "option_b": "Audio mixing",
        "option_c": "UI prototyping",
        "option_d": "File archiving",
        "correct_answer": "A"
    },
    {
        "question_text": "DP stands for:",
        "option_a": "Dynamic Programming",
        "option_b": "Data Processing",
        "option_c": "Direct Protocol",
        "option_d": "Display Picture",
        "correct_answer": "A"
    },
    {
        "question_text": "Greedy algorithms:",
        "option_a": "Choose locally optimal solution",
        "option_b": "Choose random solution",
        "option_c": "Choose worst solution",
        "option_d": "Avoid optimization",
        "correct_answer": "A"
    },
    {
        "question_text": "Graphs consist of:",
        "option_a": "Nodes and edges",
        "option_b": "Songs and beats",
        "option_c": "Colors and shades",
        "option_d": "Wires and lamps",
        "correct_answer": "A"
    },
    {
        "question_text": "Recursion means:",
        "option_a": "Function calling itself",
        "option_b": "Repeating loops",
        "option_c": "Restarting device",
        "option_d": "Copying files",
        "correct_answer": "A"
    },
    {
        "question_text": "Modulo operations help with:",
        "option_a": "Large number handling",
        "option_b": "Video editing",
        "option_c": "Image lighting",
        "option_d": "Color grading",
        "correct_answer": "A"
    },
    {
        "question_text": "Competitive programmers use:",
        "option_a": "C++/Python",
        "option_b": "MS Paint",
        "option_c": "Google Slides",
        "option_d": "Photo editors",
        "correct_answer": "A"
    }
],
260: [
    {
        "question_text": "DSA in Java includes:",
        "option_a": "Trees, graphs, arrays",
        "option_b": "Waterfalls",
        "option_c": "Mountains",
        "option_d": "Music",
        "correct_answer": "A"
    },
    {
        "question_text": "Java Collections include:",
        "option_a": "ArrayList",
        "option_b": "HashMap",
        "option_c": "LinkedList",
        "option_d": "All of these",
        "correct_answer": "D"
    },
    {
        "question_text": "Binary tree has:",
        "option_a": "0–2 children",
        "option_b": "10 children",
        "option_c": "No children",
        "option_d": "Infinite children",
        "correct_answer": "A"
    },
    {
        "question_text": "HashMap stores:",
        "option_a": "Key-value pairs",
        "option_b": "Random strings",
        "option_c": "Videos",
        "option_d": "Colors",
        "correct_answer": "A"
    },
    {
        "question_text": "DFS stands for:",
        "option_a": "Depth First Search",
        "option_b": "Deep Fun Search",
        "option_c": "Data File Storage",
        "option_d": "Direct Fast Speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Queue follows:",
        "option_a": "LIFO",
        "option_b": "FIFO",
        "option_c": "Binary",
        "option_d": "Hashing",
        "correct_answer": "B"
    },
    {
        "question_text": "Stack follows:",
        "option_a": "FIFO",
        "option_b": "LIFO",
        "option_c": "Graph structure",
        "option_d": "Tree traversal",
        "correct_answer": "B"
    },
    {
        "question_text": "Searching in array has complexity:",
        "option_a": "O(n)",
        "option_b": "O(1)",
        "option_c": "O(log n)",
        "option_d": "O(n log n)",
        "correct_answer": "A"
    },
    {
        "question_text": "Binary search works only on:",
        "option_a": "Sorted data",
        "option_b": "Images",
        "option_c": "Audio files",
        "option_d": "Videos",
        "correct_answer": "A"
    },
    {
        "question_text": "Graphs are represented using:",
        "option_a": "Adjacency list",
        "option_b": "Adjacency matrix",
        "option_c": "Both A and B",
        "option_d": "None",
        "correct_answer": "C"
    }
],
259: [
    {
        "question_text": "Machine Learning focuses on:",
        "option_a": "Making machines learn from data",
        "option_b": "Making mobile apps",
        "option_c": "Editing videos",
        "option_d": "Building networks",
        "correct_answer": "A"
    },
    {
        "question_text": "Supervised learning uses:",
        "option_a": "Labeled data",
        "option_b": "Unlabeled data",
        "option_c": "Random data",
        "option_d": "No data",
        "correct_answer": "A"
    },
    {
        "question_text": "Unsupervised learning uses:",
        "option_a": "Labeled data",
        "option_b": "Unlabeled data",
        "option_c": "Videos",
        "option_d": "Music",
        "correct_answer": "B"
    },
    {
        "question_text": "Which algorithm is supervised?",
        "option_a": "Linear Regression",
        "option_b": "K-Means",
        "option_c": "Autoencoder",
        "option_d": "PCA",
        "correct_answer": "A"
    },
    {
        "question_text": "K-Means is used for:",
        "option_a": "Clustering",
        "option_b": "Classification",
        "option_c": "Audio processing",
        "option_d": "File compression",
        "correct_answer": "A"
    },
    {
        "question_text": "Overfitting means:",
        "option_a": "Model memorizes training data",
        "option_b": "Model predicts well",
        "option_c": "Model runs fast",
        "option_d": "Model uses GPU",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is a loss function?",
        "option_a": "MSE",
        "option_b": "RGB",
        "option_c": "HTML",
        "option_d": "PNG",
        "correct_answer": "A"
    },
    {
        "question_text": "Feature engineering means:",
        "option_a": "Creating useful input features",
        "option_b": "Adding colors",
        "option_c": "Downloading files",
        "option_d": "Editing images",
        "correct_answer": "A"
    },
    {
        "question_text": "Which library is used for ML?",
        "option_a": "Scikit-learn",
        "option_b": "Figma",
        "option_c": "Word",
        "option_d": "Excel",
        "correct_answer": "A"
    },
    {
        "question_text": "Train-test split is used for:",
        "option_a": "Evaluating models",
        "option_b": "Splitting videos",
        "option_c": "Batch cooking",
        "option_d": "Color grading",
        "correct_answer": "A"
    }
],

258: [
    {
        "question_text": "Deep learning uses:",
        "option_a": "Neural networks",
        "option_b": "Manual rules",
        "option_c": "Excel sheets",
        "option_d": "Paint files",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is a deep learning framework?",
        "option_a": "TensorFlow",
        "option_b": "QGIS",
        "option_c": "MS Paint",
        "option_d": "React",
        "correct_answer": "A"
    },
    {
        "question_text": "CNNs are mainly used for:",
        "option_a": "Image processing",
        "option_b": "Audio mixing",
        "option_c": "Web design",
        "option_d": "Database backups",
        "correct_answer": "A"
    },
    {
        "question_text": "RNNs are good at:",
        "option_a": "Sequential data",
        "option_b": "3D graphics",
        "option_c": "Video compression",
        "option_d": "Color grading",
        "correct_answer": "A"
    },
    {
        "question_text": "Backpropagation is used for:",
        "option_a": "Training neural networks",
        "option_b": "Deleting files",
        "option_c": "Optimizing CSS",
        "option_d": "Sending emails",
        "correct_answer": "A"
    },
    {
        "question_text": "Dropout reduces:",
        "option_a": "Overfitting",
        "option_b": "Color saturation",
        "option_c": "File size",
        "option_d": "Brightness",
        "correct_answer": "A"
    },
    {
        "question_text": "Activation functions introduce:",
        "option_a": "Non-linearity",
        "option_b": "Brightness",
        "option_c": "Color filters",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "GPU is important for deep learning because:",
        "option_a": "Parallel computation",
        "option_b": "Better audio",
        "option_c": "Better UI",
        "option_d": "Better fonts",
        "correct_answer": "A"
    },
    {
        "question_text": "Softmax is used for:",
        "option_a": "Multi-class classification",
        "option_b": "Storing games",
        "option_c": "Editing text",
        "option_d": "Image resizing",
        "correct_answer": "A"
    },
    {
        "question_text": "Epoch refers to:",
        "option_a": "One full training cycle",
        "option_b": "One minute",
        "option_c": "One image",
        "option_d": "One filter",
        "correct_answer": "A"
    }
],

257: [
    {
        "question_text": "Data Science combines:",
        "option_a": "Math, statistics, programming",
        "option_b": "Cooking and dancing",
        "option_c": "Drawing and singing",
        "option_d": "Running and jumping",
        "correct_answer": "A"
    },
    {
        "question_text": "EDA stands for:",
        "option_a": "Exploratory Data Analysis",
        "option_b": "Experimental Data Algorithm",
        "option_c": "Extended Data Analytics",
        "option_d": "Extra Data Access",
        "correct_answer": "A"
    },
    {
        "question_text": "Which library is used for visualization?",
        "option_a": "Matplotlib",
        "option_b": "Notepad",
        "option_c": "Chrome",
        "option_d": "Edge",
        "correct_answer": "A"
    },
    {
        "question_text": "CSV stands for:",
        "option_a": "Comma Separated Values",
        "option_b": "Color Saturation Value",
        "option_c": "Central Script Volume",
        "option_d": "Common Style Variable",
        "correct_answer": "A"
    },
    {
        "question_text": "Data cleaning means:",
        "option_a": "Removing noise & fixing issues",
        "option_b": "Deleting everything",
        "option_c": "Color correction",
        "option_d": "Game updates",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tool is used for notebooks?",
        "option_a": "Jupyter",
        "option_b": "Lightroom",
        "option_c": "Blender",
        "option_d": "Figma",
        "correct_answer": "A"
    },
    {
        "question_text": "Outliers affect:",
        "option_a": "Model accuracy",
        "option_b": "Screen brightness",
        "option_c": "Game speed",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "Correlation shows:",
        "option_a": "Relationship between variables",
        "option_b": "Image contrast",
        "option_c": "Memory usage",
        "option_d": "Traffic speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Pandas is used for:",
        "option_a": "Data manipulation",
        "option_b": "Image editing",
        "option_c": "Sound mixing",
        "option_d": "Video trimming",
        "correct_answer": "A"
    },
    {
        "question_text": "Model evaluation checks:",
        "option_a": "How well model performs",
        "option_b": "CPU temperature",
        "option_c": "Camera quality",
        "option_d": "Keyboard layout",
        "correct_answer": "A"
    }
],

256: [
    {
        "question_text": "Excel is used for:",
        "option_a": "Data analysis",
        "option_b": "Singing",
        "option_c": "Cooking",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Pivot tables summarize:",
        "option_a": "Large data",
        "option_b": "Images",
        "option_c": "Videos",
        "option_d": "Audio",
        "correct_answer": "A"
    },
    {
        "question_text": "Which formula adds numbers?",
        "option_a": "=ADD()",
        "option_b": "=SUM()",
        "option_c": "=COUNT()",
        "option_d": "=AVG()",
        "correct_answer": "B"
    },
    {
        "question_text": "Charts visualize:",
        "option_a": "Data",
        "option_b": "Games",
        "option_c": "Music",
        "option_d": "Apps",
        "correct_answer": "A"
    },
    {
        "question_text": "Conditional formatting highlights:",
        "option_a": "Cells based on rules",
        "option_b": "Videos",
        "option_c": "Photos",
        "option_d": "Games",
        "correct_answer": "A"
    },
    {
        "question_text": "VLOOKUP retrieves data from:",
        "option_a": "Table",
        "option_b": "Browser",
        "option_c": "Camera",
        "option_d": "WiFi",
        "correct_answer": "A"
    },
    {
        "question_text": "Filter is used to:",
        "option_a": "Show selective rows",
        "option_b": "Record audio",
        "option_c": "Download files",
        "option_d": "Play video",
        "correct_answer": "A"
    },
    {
        "question_text": "Which file extension is Excel?",
        "option_a": ".xlsx",
        "option_b": ".txt",
        "option_c": ".mp3",
        "option_d": ".pdf",
        "correct_answer": "A"
    },
    {
        "question_text": "Which function counts numbers?",
        "option_a": "=SUM()",
        "option_b": "=COUNT()",
        "option_c": "=FIND()",
        "option_d": "=CHECK()",
        "correct_answer": "B"
    },
    {
        "question_text": "Freeze Panes keeps:",
        "option_a": "Headers visible",
        "option_b": "Videos paused",
        "option_c": "CPU cool",
        "option_d": "Battery full",
        "correct_answer": "A"
    }
],

255: [
    {
        "question_text": "Statistics deals with:",
        "option_a": "Data collection and analysis",
        "option_b": "Painting",
        "option_c": "Yoga",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Mean is:",
        "option_a": "Average",
        "option_b": "Difference",
        "option_c": "Maximum",
        "option_d": "Minimum",
        "correct_answer": "A"
    },
    {
        "question_text": "Median is:",
        "option_a": "Middle value",
        "option_b": "Largest number",
        "option_c": "Smallest number",
        "option_d": "Sum of numbers",
        "correct_answer": "A"
    },
    {
        "question_text": "Mode is:",
        "option_a": "Most frequent value",
        "option_b": "Least common value",
        "option_c": "Random value",
        "option_d": "Negative value",
        "correct_answer": "A"
    },
    {
        "question_text": "Probability measures:",
        "option_a": "Likelihood",
        "option_b": "Brightness",
        "option_c": "Height",
        "option_d": "Weight",
        "correct_answer": "A"
    },
    {
        "question_text": "Standard deviation shows:",
        "option_a": "Spread of data",
        "option_b": "Color shade",
        "option_c": "Audio quality",
        "option_d": "Temperature",
        "correct_answer": "A"
    },
    {
        "question_text": "Variance is:",
        "option_a": "Squared deviation",
        "option_b": "Height",
        "option_c": "Weight",
        "option_d": "Time",
        "correct_answer": "A"
    },
    {
        "question_text": "Sampling means:",
        "option_a": "Selecting a subset",
        "option_b": "Deleting everything",
        "option_c": "Adding noise",
        "option_d": "Color grading",
        "correct_answer": "A"
    },
    {
        "question_text": "Histogram visualizes:",
        "option_a": "Frequency distribution",
        "option_b": "Audio waves",
        "option_c": "Network packets",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Correlation identifies:",
        "option_a": "Relationships",
        "option_b": "File size",
        "option_c": "Color tone",
        "option_d": "CPU clock",
        "correct_answer": "A"
    }
],

254: [
    {
        "question_text": "Cloud computing provides:",
        "option_a": "On-demand computing resources",
        "option_b": "Movies",
        "option_c": "Car wash",
        "option_d": "Electricity",
        "correct_answer": "A"
    },
    {
        "question_text": "IaaS stands for:",
        "option_a": "Infrastructure as a Service",
        "option_b": "Internet as a System",
        "option_c": "Info as a Software",
        "option_d": "Interface as a Service",
        "correct_answer": "A"
    },
    {
        "question_text": "SaaS stands for:",
        "option_a": "Software as a Service",
        "option_b": "Server as a System",
        "option_c": "Storage at Scale",
        "option_d": "System as a Software",
        "correct_answer": "A"
    },
    {
        "question_text": "PaaS provides:",
        "option_a": "Platform for development",
        "option_b": "Physical servers",
        "option_c": "Refrigerators",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud enables:",
        "option_a": "Scalability",
        "option_b": "Door locks",
        "option_c": "Noise cancellation",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "Public cloud is:",
        "option_a": "Shared environment",
        "option_b": "Private for one company",
        "option_c": "Offline only",
        "option_d": "Special-purpose",
        "correct_answer": "A"
    },
    {
        "question_text": "Hybrid cloud combines:",
        "option_a": "Public + Private cloud",
        "option_b": "Phone + Laptop",
        "option_c": "TV + Radio",
        "option_d": "Book + Pen",
        "correct_answer": "A"
    },
    {
        "question_text": "Which company provides cloud?",
        "option_a": "AWS",
        "option_b": "Google Cloud",
        "option_c": "Azure",
        "option_d": "All of these",
        "correct_answer": "D"
    },
    {
        "question_text": "Serverless computing uses:",
        "option_a": "Functions",
        "option_b": "CD players",
        "option_c": "Toys",
        "option_d": "Brushes",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud storage stores:",
        "option_a": "Files online",
        "option_b": "Air",
        "option_c": "Shapes",
        "option_d": "Oil",
        "correct_answer": "A"
    }
],

253: [
    {
        "question_text": "SQL stands for:",
        "option_a": "Structured Query Language",
        "option_b": "Sequence Query Logic",
        "option_c": "Standard Quick Language",
        "option_d": "Style Query Level",
        "correct_answer": "A"
    },
    {
        "question_text": "Which command retrieves data?",
        "option_a": "SELECT",
        "option_b": "DELETE",
        "option_c": "DROP",
        "option_d": "INSERT",
        "correct_answer": "A"
    },
    {
        "question_text": "Which keyword filters rows?",
        "option_a": "WHERE",
        "option_b": "WHAT",
        "option_c": "FILTER",
        "option_d": "CHOOSE",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN combines:",
        "option_a": "Tables",
        "option_b": "Images",
        "option_c": "Audio",
        "option_d": "Videos",
        "correct_answer": "A"
    },
    {
        "question_text": "COUNT() returns:",
        "option_a": "Number of rows",
        "option_b": "Colors",
        "option_c": "Password",
        "option_d": "Browser version",
        "correct_answer": "A"
    },
    {
        "question_text": "PRIMARY KEY ensures:",
        "option_a": "Uniqueness",
        "option_b": "Brightness",
        "option_c": "Volume",
        "option_d": "Temperature",
        "correct_answer": "A"
    },
    {
        "question_text": "ORDER BY sorts:",
        "option_a": "Result set",
        "option_b": "Photos",
        "option_c": "Videos",
        "option_d": "Audios",
        "correct_answer": "A"
    },
    {
        "question_text": "UPDATE modifies:",
        "option_a": "Existing rows",
        "option_b": "Colors",
        "option_c": "Music",
        "option_d": "Shapes",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE removes:",
        "option_a": "Rows",
        "option_b": "Monitors",
        "option_c": "Cameras",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "DDL stands for:",
        "option_a": "Data Definition Language",
        "option_b": "Data Drawing Level",
        "option_c": "Device Driver List",
        "option_d": "Double Data Linear",
        "correct_answer": "A"
    }
],

252: [
    {
        "question_text": "Python is:",
        "option_a": "A programming language",
        "option_b": "A video player",
        "option_c": "A speaker",
        "option_d": "A game",
        "correct_answer": "A"
    },
    {
        "question_text": "Which data type is mutable?",
        "option_a": "List",
        "option_b": "Tuple",
        "option_c": "String",
        "option_d": "Integer",
        "correct_answer": "A"
    },
    {
        "question_text": "Which keyword defines a function?",
        "option_a": "func",
        "option_b": "def",
        "option_c": "fn",
        "option_d": "function",
        "correct_answer": "B"
    },
    {
        "question_text": "Which operator is used for exponent?",
        "option_a": "^",
        "option_b": "**",
        "option_c": "exp",
        "option_d": "//",
        "correct_answer": "B"
    },
    {
        "question_text": "Dictionaries store:",
        "option_a": "Key-value pairs",
        "option_b": "Images",
        "option_c": "Audio",
        "option_d": "Passwords",
        "correct_answer": "A"
    },
    {
        "question_text": "Which library is for data analysis?",
        "option_a": "Pandas",
        "option_b": "Blender",
        "option_c": "Unity",
        "option_d": "Figma",
        "correct_answer": "A"
    },
    {
        "question_text": "Which loop repeats until condition fails?",
        "option_a": "while",
        "option_b": "stop",
        "option_c": "exit",
        "option_d": "repeat",
        "correct_answer": "A"
    },
    {
        "question_text": "Which function reads input?",
        "option_a": "type()",
        "option_b": "input()",
        "option_c": "read()",
        "option_d": "scan()",
        "correct_answer": "B"
    },
    {
        "question_text": "Which converts string to integer?",
        "option_a": "int()",
        "option_b": "str()",
        "option_c": "float()",
        "option_d": "chr()",
        "correct_answer": "A"
    },
    {
        "question_text": "Which statement handles errors?",
        "option_a": "try/except",
        "option_b": "if/else",
        "option_c": "for",
        "option_d": "switch",
        "correct_answer": "A"
    }
],

251: [
    {
        "question_text": "JavaScript is:",
        "option_a": "A scripting language",
        "option_b": "A phone",
        "option_c": "A TV",
        "option_d": "A sofa",
        "correct_answer": "A"
    },
    {
        "question_text": "Which keyword declares a variable?",
        "option_a": "var",
        "option_b": "make",
        "option_c": "new",
        "option_d": "let",
        "correct_answer": "A"
    },
    {
        "question_text": "Which operator compares value & type?",
        "option_a": "==",
        "option_b": "=",
        "option_c": "===",
        "option_d": "=!",
        "correct_answer": "C"
    },
    {
        "question_text": "Arrays in JS are:",
        "option_a": "Objects",
        "option_b": "Strings",
        "option_c": "Numbers",
        "option_d": "Booleans",
        "correct_answer": "A"
    },
    {
        "question_text": "Which function prints output?",
        "option_a": "console.log()",
        "option_b": "print()",
        "option_c": "log.print()",
        "option_d": "cout",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is NOT a JS framework?",
        "option_a": "React",
        "option_b": "Vue",
        "option_c": "Angular",
        "option_d": "Photoshop",
        "correct_answer": "D"
    },
    {
        "question_text": "JSON stands for:",
        "option_a": "JavaScript Object Notation",
        "option_b": "Java Secure Object Network",
        "option_c": "Joint Service Oriented Network",
        "option_d": "Java Syntax Object Node",
        "correct_answer": "A"
    },
    {
        "question_text": "DOM stands for:",
        "option_a": "Document Object Model",
        "option_b": "Data Object Module",
        "option_c": "Digital Output Model",
        "option_d": "Dynamic Object Mapper",
        "correct_answer": "A"
    },
    {
        "question_text": "Which event runs on button click?",
        "option_a": "onclick",
        "option_b": "onpress",
        "option_c": "onhover",
        "option_d": "onrun",
        "correct_answer": "A"
    },
    {
        "question_text": "JavaScript runs in:",
        "option_a": "Browser",
        "option_b": "Washing machine",
        "option_c": "TV",
        "option_d": "Fridge",
        "correct_answer": "A"
    }
],

250: [
    {
        "question_text": "HTML stands for:",
        "option_a": "Hyper Text Markup Language",
        "option_b": "High Tool Markup Language",
        "option_c": "Hyperlink Text Memory Language",
        "option_d": "Home Tool Model Language",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS styles:",
        "option_a": "Web pages",
        "option_b": "Cars",
        "option_c": "Phones",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tag creates a hyperlink?",
        "option_a": "<a>",
        "option_b": "<link>",
        "option_c": "<goto>",
        "option_d": "<url>",
        "correct_answer": "A"
    },
    {
        "question_text": "Which property changes background color?",
        "option_a": "background-color",
        "option_b": "bg",
        "option_c": "color",
        "option_d": "paint",
        "correct_answer": "A"
    },
    {
        "question_text": "Which is NOT a CSS unit?",
        "option_a": "px",
        "option_b": "cm",
        "option_c": "kg",
        "option_d": "rem",
        "correct_answer": "C"
    },
    {
        "question_text": "Flexbox aligns items:",
        "option_a": "Horizontally/Vertically",
        "option_b": "Only vertically",
        "option_c": "Only horizontally",
        "option_d": "Diagonal only",
        "correct_answer": "A"
    },
    {
        "question_text": "HTML page starts with:",
        "option_a": "<!DOCTYPE html>",
        "option_b": "<html-start>",
        "option_c": "<body>",
        "option_d": "<layout>",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tag displays images?",
        "option_a": "<img>",
        "option_b": "<pic>",
        "option_c": "<photo>",
        "option_d": "<image>",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS is:",
        "option_a": "Cascading Style Sheets",
        "option_b": "Central Style System",
        "option_c": "Creative Style Script",
        "option_d": "Color Style Service",
        "correct_answer": "A"
    },
    {
        "question_text": "Which tag contains metadata?",
        "option_a": "<head>",
        "option_b": "<meta>",
        "option_c": "<body>",
        "option_d": "<title>",
        "correct_answer": "A"
    }
],
249: [
    {
        "question_text": "Next.js is mainly used for:",
        "option_a": "Server-side rendering",
        "option_b": "Car washing",
        "option_c": "Bike servicing",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js is built on top of:",
        "option_a": "Python",
        "option_b": "React",
        "option_c": "HTML only",
        "option_d": "C++",
        "correct_answer": "B"
    },
    {
        "question_text": "Next.js supports:",
        "option_a": "Static site generation",
        "option_b": "Photo editing",
        "option_c": "Car gaming",
        "option_d": "Wallpaper design",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js routing is:",
        "option_a": "File-based",
        "option_b": "Bike-based",
        "option_c": "Cloud-based only",
        "option_d": "GPS-based",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js improves SEO using:",
        "option_a": "Server-side rendering",
        "option_b": "Music streaming",
        "option_c": "Heat controls",
        "option_d": "Plastic covers",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js pages folder is:",
        "option_a": "/api",
        "option_b": "/pages",
        "option_c": "/root",
        "option_d": "/dev",
        "correct_answer": "B"
    },
    {
        "question_text": "Next.js allows:",
        "option_a": "Full-stack development",
        "option_b": "Bike assembly",
        "option_c": "Engine tuning",
        "option_d": "Shoe polishing",
        "correct_answer": "A"
    },
    {
        "question_text": "API routes in Next.js are under:",
        "option_a": "/server",
        "option_b": "/api",
        "option_c": "/public",
        "option_d": "/config",
        "correct_answer": "B"
    },
    {
        "question_text": "Next.js apps run using:",
        "option_a": "Node.js",
        "option_b": "Battery cells",
        "option_c": "Petrol",
        "option_d": "Air pressure",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js is written in:",
        "option_a": "JavaScript",
        "option_b": "Rubber",
        "option_c": "Stone",
        "option_d": "Metal",
        "correct_answer": "A"
    }
],

248: [
    {
        "question_text": "React Router is used to:",
        "option_a": "Handle navigation",
        "option_b": "Pump fuel",
        "option_c": "Clean dishes",
        "option_d": "Dry clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router routing is:",
        "option_a": "Client-side",
        "option_b": "Server hardware",
        "option_c": "Satellite based",
        "option_d": "Mechanical",
        "correct_answer": "A"
    },
    {
        "question_text": "To navigate, React Router uses:",
        "option_a": "<Link>",
        "option_b": "<Road>",
        "option_c": "<Gate>",
        "option_d": "<Block>",
        "correct_answer": "A"
    },
    {
        "question_text": "Dynamic URL data is read using:",
        "option_a": "useParams",
        "option_b": "useWater",
        "option_c": "useScreen",
        "option_d": "useLight",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router supports:",
        "option_a": "Nested routes",
        "option_b": "Nested wires",
        "option_c": "Nested fans",
        "option_d": "Nested bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Protected routes restrict:",
        "option_a": "Unauthorized access",
        "option_b": "Rainfall",
        "option_c": "Sunlight",
        "option_d": "Wind",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router works with:",
        "option_a": "React apps",
        "option_b": "Excel sheets",
        "option_c": "TV screens",
        "option_d": "Headphones",
        "correct_answer": "A"
    },
    {
        "question_text": "Route definitions use:",
        "option_a": "<Route>",
        "option_b": "<Button>",
        "option_c": "<TV>",
        "option_d": "<Stick>",
        "correct_answer": "A"
    },
    {
        "question_text": "Old <Switch> is replaced by:",
        "option_a": "Routes",
        "option_b": "Blocks",
        "option_c": "Chips",
        "option_d": "Wires",
        "correct_answer": "A"
    },
    {
        "question_text": "Routing improves:",
        "option_a": "User navigation",
        "option_b": "Fuel economy",
        "option_c": "Laptop heat",
        "option_d": "Room lighting",
        "correct_answer": "A"
    }
],

247: [
    {
        "question_text": "React is mainly used for:",
        "option_a": "Building UI",
        "option_b": "Cooking",
        "option_c": "Travelling",
        "option_d": "Cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "React uses:",
        "option_a": "JavaScript",
        "option_b": "Steel",
        "option_c": "Wood",
        "option_d": "Plastic",
        "correct_answer": "A"
    },
    {
        "question_text": "React manages UI using:",
        "option_a": "Components",
        "option_b": "Engines",
        "option_c": "Screws",
        "option_d": "Drivers",
        "correct_answer": "A"
    },
    {
        "question_text": "React DOM updates using:",
        "option_a": "Virtual DOM",
        "option_b": "Virtual AC",
        "option_c": "Virtual camera",
        "option_d": "Virtual shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "React hooks start with:",
        "option_a": "use",
        "option_b": "go",
        "option_c": "on",
        "option_d": "at",
        "correct_answer": "A"
    },
    {
        "question_text": "Props in React are:",
        "option_a": "Inputs",
        "option_b": "Bags",
        "option_c": "Fans",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "State stores:",
        "option_a": "Component data",
        "option_b": "Milk",
        "option_c": "Air",
        "option_d": "Oil",
        "correct_answer": "A"
    },
    {
        "question_text": "React was developed by:",
        "option_a": "Facebook",
        "option_b": "Amazon",
        "option_c": "Samsung",
        "option_d": "Adobe",
        "correct_answer": "A"
    },
    {
        "question_text": "React renders in:",
        "option_a": "Browser",
        "option_b": "Freezer",
        "option_c": "Garden",
        "option_d": "Car",
        "correct_answer": "A"
    },
    {
        "question_text": "JSX allows writing:",
        "option_a": "HTML in JS",
        "option_b": "CSS in stone",
        "option_c": "Wood in metal",
        "option_d": "Air in water",
        "correct_answer": "A"
    }
],

246: [
    {
        "question_text": "MongoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "Camera",
        "option_c": "Speaker",
        "option_d": "Gamepad",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores data as:",
        "option_a": "Documents",
        "option_b": "Papers",
        "option_c": "Leaves",
        "option_d": "Cards",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB uses:",
        "option_a": "Collections",
        "option_b": "Buckets",
        "option_c": "Boxes",
        "option_d": "Shelves",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores:",
        "option_a": "JSON-like data",
        "option_b": "Metal rods",
        "option_c": "Shoes",
        "option_d": "Watches",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is good for:",
        "option_a": "Large unstructured data",
        "option_b": "Large swimming pools",
        "option_c": "Large farms",
        "option_d": "Large bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "The MongoDB query language is:",
        "option_a": "MQL",
        "option_b": "SQL",
        "option_c": "HTML",
        "option_d": "CSS",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB server runs on:",
        "option_a": "mongod",
        "option_b": "mongoa",
        "option_c": "mongoc",
        "option_d": "mongof",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB Compass is:",
        "option_a": "GUI tool",
        "option_b": "Knife",
        "option_c": "Fan",
        "option_d": "Bag",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is used with:",
        "option_a": "Node.js",
        "option_b": "Printer",
        "option_c": "Television",
        "option_d": "Speaker",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is:",
        "option_a": "Schema-less",
        "option_b": "Weight-less",
        "option_c": "Cost-less",
        "option_d": "Color-less",
        "correct_answer": "A"
    }
],
245: [
    {
        "question_text": "MySQL is a:",
        "option_a": "Relational database",
        "option_b": "Drawing tool",
        "option_c": "Camera",
        "option_d": "Telephone",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL uses:",
        "option_a": "Tables",
        "option_b": "Folders",
        "option_c": "Drawers",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "To retrieve data, MySQL uses:",
        "option_a": "SELECT",
        "option_b": "OPEN",
        "option_c": "VIEW",
        "option_d": "FIND",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary key ensures:",
        "option_a": "Uniqueness",
        "option_b": "Coloring",
        "option_c": "Printing",
        "option_d": "Lighting",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL Workbench is a:",
        "option_a": "GUI tool",
        "option_b": "Hammer",
        "option_c": "Screwdriver",
        "option_d": "Wrench",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL uses:",
        "option_a": "SQL queries",
        "option_b": "Excel formulas",
        "option_c": "Videos",
        "option_d": "Music files",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL is commonly used in:",
        "option_a": "Web apps",
        "option_b": "Swimming pools",
        "option_c": "Car engines",
        "option_d": "Shoemaking",
        "correct_answer": "A"
    },
    {
        "question_text": "To update values, MySQL uses:",
        "option_a": "UPDATE",
        "option_b": "CHANGE",
        "option_c": "FIX",
        "option_d": "REPAIR",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL stores data in:",
        "option_a": "Rows and columns",
        "option_b": "Wires and cables",
        "option_c": "Colors and shades",
        "option_d": "Wheels and tires",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL supports:",
        "option_a": "Joins",
        "option_b": "Welding",
        "option_c": "Painting",
        "option_d": "Farming",
        "correct_answer": "A"
    }
],

244: [
    {
        "question_text": "PostgreSQL is known for being:",
        "option_a": "Highly reliable",
        "option_b": "A camera",
        "option_c": "A bicycle",
        "option_d": "A shoe",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL supports:",
        "option_a": "Advanced indexing",
        "option_b": "Food heating",
        "option_c": "Room cleaning",
        "option_d": "Car washing",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL uses:",
        "option_a": "Tables",
        "option_b": "Plants",
        "option_c": "Paints",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL is a:",
        "option_a": "Relational DBMS",
        "option_b": "Garden tool",
        "option_c": "Drinking bottle",
        "option_d": "Helmet",
        "correct_answer": "A"
    },
    {
        "question_text": "To insert data, we use:",
        "option_a": "INSERT",
        "option_b": "ENTER",
        "option_c": "PLACE",
        "option_d": "MAKE",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL supports:",
        "option_a": "JSON data",
        "option_b": "Pen colors",
        "option_c": "Shoe sizes",
        "option_d": "Road signs",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL is often used in:",
        "option_a": "Enterprise apps",
        "option_b": "Street shops",
        "option_c": "Swimming",
        "option_d": "Driving schools",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres admin tool is:",
        "option_a": "pgAdmin",
        "option_b": "pgDrive",
        "option_c": "pgTree",
        "option_d": "pgLamp",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL is:",
        "option_a": "Open source",
        "option_b": "Heavy metal",
        "option_c": "A medicine",
        "option_d": "A perfume",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL queries use:",
        "option_a": "SQL",
        "option_b": "XML",
        "option_c": "CSS",
        "option_d": "JSX",
        "correct_answer": "A"
    }
],

243: [
    {
        "question_text": "FastAPI is used to build:",
        "option_a": "APIs",
        "option_b": "Shoes",
        "option_c": "Cars",
        "option_d": "Carpets",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is written in:",
        "option_a": "Python",
        "option_b": "Cement",
        "option_c": "Plastic",
        "option_d": "Rubber",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is known for being:",
        "option_a": "Fast",
        "option_b": "Slow",
        "option_c": "Heavy",
        "option_d": "Fragile",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI auto-generates:",
        "option_a": "Documentation",
        "option_b": "Music",
        "option_c": "Furniture",
        "option_d": "Ropes",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI uses:",
        "option_a": "Pydantic",
        "option_b": "Wood",
        "option_c": "Pipes",
        "option_d": "Wheels",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI works with:",
        "option_a": "Async code",
        "option_b": "Water pumps",
        "option_c": "Engines",
        "option_d": "Solar panels",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI runs on:",
        "option_a": "Uvicorn",
        "option_b": "Oven",
        "option_c": "Fan",
        "option_d": "Speaker",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is commonly used for:",
        "option_a": "Backend APIs",
        "option_b": "Cutting vegetables",
        "option_c": "Bike polishing",
        "option_d": "Room decoration",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI supports:",
        "option_a": "Validation",
        "option_b": "Painting",
        "option_c": "Boiling",
        "option_d": "Washing",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is:",
        "option_a": "Open source",
        "option_b": "Expensive metal",
        "option_c": "Sweet food",
        "option_d": "Soft cloth",
        "correct_answer": "A"
    }
],

242: [
    {
        "question_text": "DRF is used for building:",
        "option_a": "APIs",
        "option_b": "Shoes",
        "option_c": "Blocks",
        "option_d": "Wires",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF is built on:",
        "option_a": "Django",
        "option_b": "React",
        "option_c": "Vue",
        "option_d": "Flask",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF uses:",
        "option_a": "Serializers",
        "option_b": "Plugs",
        "option_c": "Stickers",
        "option_d": "Pipes",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF supports:",
        "option_a": "Auth",
        "option_b": "Jumping",
        "option_c": "Hiking",
        "option_d": "Running",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF helps create:",
        "option_a": "REST APIs",
        "option_b": "Chairs",
        "option_c": "Phone cases",
        "option_d": "Walls",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF views are:",
        "option_a": "Class based",
        "option_b": "Plastic based",
        "option_c": "Water based",
        "option_d": "Stone based",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF provides:",
        "option_a": "Pagination",
        "option_b": "Decoration",
        "option_c": "Navigation",
        "option_d": "Excavation",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF is popular for:",
        "option_a": "Backend APIs",
        "option_b": "Dancing",
        "option_c": "Acting",
        "option_d": "Sewing",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF supports:",
        "option_a": "Permissions",
        "option_b": "Permissions",
        "option_c": "Walking",
        "option_d": "Talking",
        "correct_answer": "A"
    },
    {
        "question_text": "DRF is:",
        "option_a": "Open source",
        "option_b": "Sugar free",
        "option_c": "Heavy metal",
        "option_d": "Toy material",
        "correct_answer": "A"
    }
],

241: [
    {
        "question_text": "Django is a:",
        "option_a": "Web framework",
        "option_b": "Painting brush",
        "option_c": "Car engine",
        "option_d": "Speaker",
        "correct_answer": "A"
    },
    {
        "question_text": "Django uses:",
        "option_a": "Python",
        "option_b": "Rubber",
        "option_c": "Plastic",
        "option_d": "Steel",
        "correct_answer": "A"
    },
    {
        "question_text": "Django follows:",
        "option_a": "MVT pattern",
        "option_b": "ABC pattern",
        "option_c": "XYZ pattern",
        "option_d": "SSS pattern",
        "correct_answer": "A"
    },
    {
        "question_text": "Django ORM helps work with:",
        "option_a": "Databases",
        "option_b": "Mountains",
        "option_c": "Water tanks",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Django templates handle:",
        "option_a": "Frontend",
        "option_b": "Driving",
        "option_c": "Cleaning",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "Django admin is:",
        "option_a": "Auto generated",
        "option_b": "Hand-made",
        "option_c": "Metal built",
        "option_d": "Cloth based",
        "correct_answer": "A"
    },
    {
        "question_text": "Django executes code via:",
        "option_a": "Views",
        "option_b": "Wheels",
        "option_c": "Switches",
        "option_d": "Knives",
        "correct_answer": "A"
    },
    {
        "question_text": "Django URLs map to:",
        "option_a": "Views",
        "option_b": "Lights",
        "option_c": "Speakers",
        "option_d": "Air",
        "correct_answer": "A"
    },
    {
        "question_text": "Django apps are:",
        "option_a": "Modular",
        "option_b": "Edible",
        "option_c": "Breakable",
        "option_d": "Flammable",
        "correct_answer": "A"
    },
    {
        "question_text": "Django is:",
        "option_a": "Open source",
        "option_b": "Fireproof",
        "option_c": "Heatproof",
        "option_d": "Waterproof",
        "correct_answer": "A"
    }
],
240: [
    {
        "question_text": "Flask is mainly used for:",
        "option_a": "Building web applications",
        "option_b": "Editing videos",
        "option_c": "Designing logos",
        "option_d": "Typing documents",
        "correct_answer": "A"
    },
    {
        "question_text": "Flask is written in:",
        "option_a": "C",
        "option_b": "Python",
        "option_c": "Java",
        "option_d": "HTML",
        "correct_answer": "B"
    },
    {
        "question_text": "Flask is a:",
        "option_a": "Database",
        "option_b": "Web framework",
        "option_c": "Game engine",
        "option_d": "Cloud service",
        "correct_answer": "B"
    },
    {
        "question_text": "Flask routes are used to:",
        "option_a": "Store files",
        "option_b": "Define webpage paths",
        "option_c": "Edit images",
        "option_d": "Play music",
        "correct_answer": "B"
    },
    {
        "question_text": "Flask templates are written in:",
        "option_a": "Excel",
        "option_b": "HTML",
        "option_c": "Python",
        "option_d": "Java",
        "correct_answer": "B"
    },
    {
        "question_text": "Flask uses this file for starting the server:",
        "option_a": "run.py",
        "option_b": "main.java",
        "option_c": "index.cpp",
        "option_d": "server.php",
        "correct_answer": "A"
    },
    {
        "question_text": "Flask is known for being:",
        "option_a": "Heavy",
        "option_b": "Slow",
        "option_c": "Lightweight",
        "option_d": "A compiler",
        "correct_answer": "C"
    },
    {
        "question_text": "Flask can connect to:",
        "option_a": "Only MongoDB",
        "option_b": "Only Excel",
        "option_c": "Many databases",
        "option_d": "Only Word files",
        "correct_answer": "C"
    },
    {
        "question_text": "Flask debug mode:",
        "option_a": "Fixes code",
        "option_b": "Restarts server automatically",
        "option_c": "Plays songs",
        "option_d": "Cleans RAM",
        "correct_answer": "B"
    },
    {
        "question_text": "Flask applications usually start with:",
        "option_a": "app = Flask(__name__)",
        "option_b": "function main()",
        "option_c": "public static void main",
        "option_d": "SELECT * FROM users",
        "correct_answer": "A"
    }
],
239: [
    {
        "question_text": "Decorators in Python are used to:",
        "option_a": "Modify functions",
        "option_b": "Play videos",
        "option_c": "Design posters",
        "option_d": "Draw shapes",
        "correct_answer": "A"
    },
    {
        "question_text": "Generators help in:",
        "option_a": "Reducing memory usage",
        "option_b": "Editing PDFs",
        "option_c": "Storing photos",
        "option_d": "Changing screen brightness",
        "correct_answer": "A"
    },
    {
        "question_text": "A lambda function is:",
        "option_a": "A small anonymous function",
        "option_b": "A big database",
        "option_c": "A cloud server",
        "option_d": "An IDE",
        "correct_answer": "A"
    },
    {
        "question_text": "Python’s async is used for:",
        "option_a": "Parallel cooking",
        "option_b": "Asynchronous programming",
        "option_c": "Fixing hardware",
        "option_d": "Cleaning RAM",
        "correct_answer": "B"
    },
    {
        "question_text": "List comprehension creates:",
        "option_a": "New lists quickly",
        "option_b": "New servers",
        "option_c": "New emails",
        "option_d": "New fonts",
        "correct_answer": "A"
    },
    {
        "question_text": "Exception handling uses:",
        "option_a": "try-except",
        "option_b": "if-else",
        "option_c": "for-while",
        "option_d": "switch-case",
        "correct_answer": "A"
    },
    {
        "question_text": "Python’s OOP includes:",
        "option_a": "Classes & objects",
        "option_b": "Cars & bikes",
        "option_c": "Tables & chairs",
        "option_d": "Rain & wind",
        "correct_answer": "A"
    },
    {
        "question_text": "Modules in Python are:",
        "option_a": "Libraries",
        "option_b": "Snacks",
        "option_c": "Vehicles",
        "option_d": "Apps",
        "correct_answer": "A"
    },
    {
        "question_text": "Virtual environment helps to:",
        "option_a": "Manage packages",
        "option_b": "Wash clothes",
        "option_c": "Ride bikes",
        "option_d": "Fix fans",
        "correct_answer": "A"
    },
    {
        "question_text": "PEP8 is a:",
        "option_a": "Style guide",
        "option_b": "Game",
        "option_c": "OS",
        "option_d": "Database",
        "correct_answer": "A"
    }
],
238: [
    {
        "question_text": "Python is mainly used for:",
        "option_a": "Programming",
        "option_b": "Driving cars",
        "option_c": "Washing clothes",
        "option_d": "Cleaning floors",
        "correct_answer": "A"
    },
    {
        "question_text": "Python files end with:",
        "option_a": ".exe",
        "option_b": ".py",
        "option_c": ".jpg",
        "option_d": ".pdf",
        "correct_answer": "B"
    },
    {
        "question_text": "Variables in Python store:",
        "option_a": "Data",
        "option_b": "Music",
        "option_c": "Furniture",
        "option_d": "Vehicles",
        "correct_answer": "A"
    },
    {
        "question_text": "A loop is used to:",
        "option_a": "Repeat tasks",
        "option_b": "Cook food",
        "option_c": "Paint walls",
        "option_d": "Drive a bus",
        "correct_answer": "A"
    },
    {
        "question_text": "Input() function takes:",
        "option_a": "User input",
        "option_b": "Shoes",
        "option_c": "Air",
        "option_d": "Water",
        "correct_answer": "A"
    },
    {
        "question_text": "Print() is used to:",
        "option_a": "Show output",
        "option_b": "Wash dishes",
        "option_c": "Drive trains",
        "option_d": "Make coffee",
        "correct_answer": "A"
    },
    {
        "question_text": "Lists are used to store:",
        "option_a": "Multiple values",
        "option_b": "Only pictures",
        "option_c": "Only songs",
        "option_d": "Only cars",
        "correct_answer": "A"
    },
    {
        "question_text": "A function is defined using:",
        "option_a": "func",
        "option_b": "define",
        "option_c": "def",
        "option_d": "function",
        "correct_answer": "C"
    },
    {
        "question_text": "Comments in Python start with:",
        "option_a": "#",
        "option_b": "@",
        "option_c": "%",
        "option_d": "&",
        "correct_answer": "A"
    },
    {
        "question_text": "Python was created by:",
        "option_a": "Ada Lovelace",
        "option_b": "Mark Zuckerberg",
        "option_c": "Guido van Rossum",
        "option_d": "Elon Musk",
        "correct_answer": "C"
    }
],
237: [
    {
        "question_text": "Django is mainly used for:",
        "option_a": "Web development",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Django uses which pattern?",
        "option_a": "MVP",
        "option_b": "MVC-like (MTV)",
        "option_c": "FIFO",
        "option_d": "LIFO",
        "correct_answer": "B"
    },
    {
        "question_text": "Django models represent:",
        "option_a": "Database tables",
        "option_b": "Road maps",
        "option_c": "Songs",
        "option_d": "Movies",
        "correct_answer": "A"
    },
    {
        "question_text": "Django templates are used for:",
        "option_a": "Frontend pages",
        "option_b": "Cooking recipes",
        "option_c": "Car servicing",
        "option_d": "Hair styling",
        "correct_answer": "A"
    },
    {
        "question_text": "manage.py is used to:",
        "option_a": "Start Django commands",
        "option_b": "Start a car",
        "option_c": "Play music",
        "option_d": "Clean RAM",
        "correct_answer": "A"
    },
    {
        "question_text": "Django ORM helps in:",
        "option_a": "Database operations",
        "option_b": "Washing clothes",
        "option_c": "Buying things",
        "option_d": "Fixing fans",
        "correct_answer": "A"
    },
    {
        "question_text": "urls.py stores:",
        "option_a": "Routes",
        "option_b": "Fruits",
        "option_c": "Vehicles",
        "option_d": "Songs",
        "correct_answer": "A"
    },
    {
        "question_text": "Django admin is used for:",
        "option_a": "Managing data",
        "option_b": "Editing photos",
        "option_c": "Sending emails",
        "option_d": "Cleaning files",
        "correct_answer": "A"
    },
    {
        "question_text": "settings.py contains:",
        "option_a": "Project configuration",
        "option_b": "Game levels",
        "option_c": "Car parts",
        "option_d": "Shopping lists",
        "correct_answer": "A"
    },
    {
        "question_text": "Django views handle:",
        "option_a": "Business logic",
        "option_b": "Hair cutting",
        "option_c": "Room painting",
        "option_d": "Train driving",
        "correct_answer": "A"
    }
],
236: [
    {
        "question_text": "FastAPI is known for being:",
        "option_a": "Fast and async",
        "option_b": "Slow",
        "option_c": "A game engine",
        "option_d": "A painting tool",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is used for:",
        "option_a": "Building APIs",
        "option_b": "Building chairs",
        "option_c": "Cooking food",
        "option_d": "Growing plants",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is written in:",
        "option_a": "Python",
        "option_b": "C",
        "option_c": "Java",
        "option_d": "Kotlin",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI auto-generates:",
        "option_a": "API documentation",
        "option_b": "Music playlists",
        "option_c": "Paintings",
        "option_d": "Videos",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI runs on:",
        "option_a": "Uvicorn",
        "option_b": "WhatsApp",
        "option_c": "Google Photos",
        "option_d": "MS Word",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI uses what format for data?",
        "option_a": "JSON",
        "option_b": "MP3",
        "option_c": "JPG",
        "option_d": "PDF",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI supports:",
        "option_a": "Async operations",
        "option_b": "Bike racing",
        "option_c": "Photo editing",
        "option_d": "Gaming",
        "correct_answer": "A"
    },
    {
        "question_text": "Path parameters are written using:",
        "option_a": "{} brackets",
        "option_b": "[] brackets",
        "option_c": "() brackets",
        "option_d": "<> arrows",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI is suitable for:",
        "option_a": "High-performance APIs",
        "option_b": "Writing books",
        "option_c": "Making tea",
        "option_d": "Sewing clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "FastAPI depends heavily on:",
        "option_a": "Pydantic",
        "option_b": "Photoshop",
        "option_c": "Netflix",
        "option_d": "YouTube",
        "correct_answer": "A"
    }
],
233: [
    {
        "question_text": "MongoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "Web browser",
        "option_c": "Printer",
        "option_d": "Video editor",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores data in:",
        "option_a": "Documents",
        "option_b": "Tables",
        "option_c": "Folders",
        "option_d": "Slides",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB documents use:",
        "option_a": "JSON-like format",
        "option_b": "MP3 format",
        "option_c": "PNG format",
        "option_d": "ZIP format",
        "correct_answer": "A"
    },
    {
        "question_text": "A collection is a group of:",
        "option_a": "Documents",
        "option_b": "Shoes",
        "option_c": "Cars",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is:",
        "option_a": "Schema-less",
        "option_b": "Weightless",
        "option_c": "Colorless",
        "option_d": "Soundless",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB Compass is a:",
        "option_a": "GUI tool",
        "option_b": "Painter tool",
        "option_c": "Cooking tool",
        "option_d": "Music tool",
        "correct_answer": "A"
    },
    {
        "question_text": "find() is used to:",
        "option_a": "Retrieve documents",
        "option_b": "Find shoes",
        "option_c": "Find pets",
        "option_d": "Find hotels",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is good for:",
        "option_a": "Large datasets",
        "option_b": "Haircuts",
        "option_c": "Painting walls",
        "option_d": "Truck driving",
        "correct_answer": "A"
    },
    {
        "question_text": "insertOne adds:",
        "option_a": "One document",
        "option_b": "One car",
        "option_c": "One shirt",
        "option_d": "One plate",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB runs on:",
        "option_a": "Local or cloud",
        "option_b": "TV",
        "option_c": "Washing machine",
        "option_d": "Microwave",
        "correct_answer": "A"
    }
],
234: [
    {
        "question_text": "MySQL is commonly used for:",
        "option_a": "Storing data",
        "option_b": "Cooking food",
        "option_c": "Sewing clothes",
        "option_d": "Driving buses",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL uses:",
        "option_a": "SQL",
        "option_b": "HTML",
        "option_c": "CSS",
        "option_d": "Photoshop",
        "correct_answer": "A"
    },
    {
        "question_text": "A query is used to:",
        "option_a": "Retrieve data",
        "option_b": "Clean shoes",
        "option_c": "Lift weights",
        "option_d": "Make tea",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL Workbench is a:",
        "option_a": "Database tool",
        "option_b": "Game console",
        "option_c": "Camera lens",
        "option_d": "Kitchen tool",
        "correct_answer": "A"
    },
    {
        "question_text": "A table stores data in:",
        "option_a": "Rows and columns",
        "option_b": "Boxes",
        "option_c": "Folders",
        "option_d": "Drawers",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN is used to:",
        "option_a": "Combine tables",
        "option_b": "Join roads",
        "option_c": "Join chairs",
        "option_d": "Join trains",
        "correct_answer": "A"
    },
    {
        "question_text": "A primary key should be:",
        "option_a": "Unique",
        "option_b": "Yellow",
        "option_c": "Loud",
        "option_d": "Heavy",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL is:",
        "option_a": "Open-source",
        "option_b": "A fruit",
        "option_c": "A shoe brand",
        "option_d": "A country",
        "correct_answer": "A"
    },
    {
        "question_text": "INSERT command adds:",
        "option_a": "New data",
        "option_b": "New cars",
        "option_c": "New clothes",
        "option_d": "New perfumes",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE command removes:",
        "option_a": "Data",
        "option_b": "Buses",
        "option_c": "Tables",
        "option_d": "Sweets",
        "correct_answer": "A"
    }
],
232: [
    {
        "question_text": "React is mainly used for:",
        "option_a": "Building user interfaces",
        "option_b": "Painting walls",
        "option_c": "Cooking food",
        "option_d": "Driving vehicles",
        "correct_answer": "A"
    },
    {
        "question_text": "React uses a:",
        "option_a": "Virtual DOM",
        "option_b": "Bike engine",
        "option_c": "Car battery",
        "option_d": "TV remote",
        "correct_answer": "A"
    },
    {
        "question_text": "React is developed by:",
        "option_a": "Facebook",
        "option_b": "Apple",
        "option_c": "Sony",
        "option_d": "Tesla",
        "correct_answer": "A"
    },
    {
        "question_text": "JSX allows writing:",
        "option_a": "HTML in JavaScript",
        "option_b": "Python in CSS",
        "option_c": "SQL in HTML",
        "option_d": "Java in PNG",
        "correct_answer": "A"
    },
    {
        "question_text": "useState is used for:",
        "option_a": "State management",
        "option_b": "Image editing",
        "option_c": "Audio control",
        "option_d": "Video playback",
        "correct_answer": "A"
    },
    {
        "question_text": "Components in React are:",
        "option_a": "Reusable",
        "option_b": "Edible",
        "option_c": "Breakable",
        "option_d": "Invisible",
        "correct_answer": "A"
    },
    {
        "question_text": "Props are:",
        "option_a": "Inputs to components",
        "option_b": "Shoes",
        "option_c": "Bags",
        "option_d": "Cars",
        "correct_answer": "A"
    },
    {
        "question_text": "React apps run in:",
        "option_a": "Browsers",
        "option_b": "Air conditioners",
        "option_c": "Washing machines",
        "option_d": "Refrigerators",
        "correct_answer": "A"
    },
    {
        "question_text": "React uses what language?",
        "option_a": "JavaScript",
        "option_b": "Ruby",
        "option_c": "Pascal",
        "option_d": "Cobalt",
        "correct_answer": "A"
    },
    {
        "question_text": "React is used for:",
        "option_a": "Frontend development",
        "option_b": "Road construction",
        "option_c": "Furniture building",
        "option_d": "Weather prediction",
        "correct_answer": "A"
    }
],
231: [
    {
        "question_text": "React Router helps in:",
        "option_a": "Navigation",
        "option_b": "Hair cutting",
        "option_c": "Cooking",
        "option_d": "Sports training",
        "correct_answer": "A"
    },
    {
        "question_text": "Routes are defined using:",
        "option_a": "<Route>",
        "option_b": "<Head>",
        "option_c": "<Body>",
        "option_d": "<Html>",
        "correct_answer": "A"
    },
    {
        "question_text": "Navigation uses:",
        "option_a": "<Link>",
        "option_b": "<Img>",
        "option_c": "<Span>",
        "option_d": "<Bold>",
        "correct_answer": "A"
    },
    {
        "question_text": "useParams is used to read:",
        "option_a": "URL parameters",
        "option_b": "Images",
        "option_c": "Music",
        "option_d": "Fonts",
        "correct_answer": "A"
    },
    {
        "question_text": "Nested routes allow:",
        "option_a": "Sub-routing",
        "option_b": "Sub-cooking",
        "option_c": "Sub-driving",
        "option_d": "Sub-sleeping",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router works in:",
        "option_a": "SPA apps",
        "option_b": "Mobile only",
        "option_c": "TV apps",
        "option_d": "Robots",
        "correct_answer": "A"
    },
    {
        "question_text": "Protected routes block:",
        "option_a": "Unauthorized access",
        "option_b": "Cars",
        "option_c": "Bikes",
        "option_d": "Boats",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router DOM is used for:",
        "option_a": "Web apps",
        "option_b": "Shoes",
        "option_c": "Paintings",
        "option_d": "Farming",
        "correct_answer": "A"
    },
    {
        "question_text": "Routes must be wrapped in:",
        "option_a": "<Routes>",
        "option_b": "<List>",
        "option_c": "<Box>",
        "option_d": "<Row>",
        "correct_answer": "A"
    },
    {
        "question_text": "useNavigate helps in:",
        "option_a": "Redirecting",
        "option_b": "Eating",
        "option_c": "Running",
        "option_d": "Sleeping",
        "correct_answer": "A"
    }
],
230: [
    {
        "question_text": "Next.js is used for:",
        "option_a": "React-based web apps",
        "option_b": "Phone repair",
        "option_c": "Drawing",
        "option_d": "Baking",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js supports:",
        "option_a": "Server-side rendering",
        "option_b": "Bike racing",
        "option_c": "Pet training",
        "option_d": "Car cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "Pages are stored in:",
        "option_a": "/pages",
        "option_b": "/root",
        "option_c": "/bin",
        "option_d": "/data",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js improves:",
        "option_a": "SEO",
        "option_b": "Shoe quality",
        "option_c": "Sleeping",
        "option_d": "Clothes drying",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js is built on:",
        "option_a": "React",
        "option_b": "Django",
        "option_c": "Java",
        "option_d": "C++",
        "correct_answer": "A"
    },
    {
        "question_text": "API routes are in:",
        "option_a": "/pages/api",
        "option_b": "/pages/cpu",
        "option_c": "/pages/tv",
        "option_d": "/pages/car",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js supports:",
        "option_a": "Static generation",
        "option_b": "Electric charging",
        "option_c": "Food packaging",
        "option_d": "Cloth washing",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js apps are:",
        "option_a": "Full-stack capable",
        "option_b": "Invisible",
        "option_c": "Underwater only",
        "option_d": "Car-compatible",
        "correct_answer": "A"
    },
    {
        "question_text": "next/head is used for:",
        "option_a": "Meta tags",
        "option_b": "Shoes",
        "option_c": "Buses",
        "option_d": "Animals",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js uses:",
        "option_a": "Node.js",
        "option_b": "Wind",
        "option_c": "Sand",
        "option_d": "Oil",
        "correct_answer": "A"
    }
],
229: [
    {
        "question_text": "Tailwind CSS is a:",
        "option_a": "Utility-first CSS framework",
        "option_b": "Database",
        "option_c": "Game engine",
        "option_d": "Music player",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind works by using:",
        "option_a": "Utility classes",
        "option_b": "Audio files",
        "option_c": "Video clips",
        "option_d": "Keyboard drivers",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind helps in:",
        "option_a": "Fast styling",
        "option_b": "Car painting",
        "option_c": "Food delivery",
        "option_d": "Shoe polishing",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind uses:",
        "option_a": "Class names",
        "option_b": "Python code",
        "option_c": "SQL commands",
        "option_d": "C++ headers",
        "correct_answer": "A"
    },
    {
        "question_text": "The default config file is:",
        "option_a": "tailwind.config.js",
        "option_b": "tailwind.json",
        "option_c": "style.css",
        "option_d": "config.txt",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind can be used with:",
        "option_a": "React",
        "option_b": "MS Paint",
        "option_c": "CorelDRAW",
        "option_d": "GarageBand",
        "correct_answer": "A"
    },
    {
        "question_text": "Hover styles are added using:",
        "option_a": "hover:",
        "option_b": "touch:",
        "option_c": "press:",
        "option_d": "run:",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind helps reduce:",
        "option_a": "Writing custom CSS",
        "option_b": "Washing clothes",
        "option_c": "Cooking time",
        "option_d": "Fuel usage",
        "correct_answer": "A"
    },
    {
        "question_text": "Responsive design uses:",
        "option_a": "sm:, md:, lg:",
        "option_b": "rt:, pl:, mn:",
        "option_c": "re:, tw:, fr:",
        "option_d": "sp:, cl:, pr:",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind builds the CSS using:",
        "option_a": "PostCSS",
        "option_b": "Photoshop",
        "option_c": "Premiere Pro",
        "option_d": "AutoCAD",
        "correct_answer": "A"
    }
],
228: [
    {
        "question_text": "Node.js is used for:",
        "option_a": "Backend development",
        "option_b": "Cooking",
        "option_c": "Painting",
        "option_d": "Cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "Node runs on:",
        "option_a": "JavaScript",
        "option_b": "Python",
        "option_c": "C",
        "option_d": "Java",
        "correct_answer": "A"
    },
    {
        "question_text": "Node uses:",
        "option_a": "npm",
        "option_b": "pip",
        "option_c": "composer",
        "option_d": "gradle",
        "correct_answer": "A"
    },
    {
        "question_text": "Express.js is a:",
        "option_a": "Node framework",
        "option_b": "Bike model",
        "option_c": "Phone brand",
        "option_d": "Camera type",
        "correct_answer": "A"
    },
    {
        "question_text": "Node is:",
        "option_a": "Asynchronous",
        "option_b": "Powder",
        "option_c": "Liquid",
        "option_d": "Solid",
        "correct_answer": "A"
    },
    {
        "question_text": "Node handles:",
        "option_a": "APIs",
        "option_b": "Wallpaper",
        "option_c": "Photos",
        "option_d": "Bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "package.json stores:",
        "option_a": "Dependencies",
        "option_b": "Songs",
        "option_c": "Movies",
        "option_d": "Photos",
        "correct_answer": "A"
    },
    {
        "question_text": "Node is ideal for:",
        "option_a": "Real-time apps",
        "option_b": "Farming",
        "option_c": "Cycling",
        "option_d": "Swimming",
        "correct_answer": "A"
    },
    {
        "question_text": "Node applications run on:",
        "option_a": "Chrome V8 engine",
        "option_b": "Steam engine",
        "option_c": "Electric motors",
        "option_d": "Diesel engines",
        "correct_answer": "A"
    },
    {
        "question_text": "Node can connect to:",
        "option_a": "Databases",
        "option_b": "Shoes",
        "option_c": "Cameras",
        "option_d": "Tables",
        "correct_answer": "A"
    }
],
227: [
    {
        "question_text": "Express.js is used for:",
        "option_a": "API development",
        "option_b": "Gardening",
        "option_c": "Driving",
        "option_d": "Dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Express is built on:",
        "option_a": "Node.js",
        "option_b": "Java",
        "option_c": "C++",
        "option_d": "Rust",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware handles:",
        "option_a": "Requests",
        "option_b": "Laundry",
        "option_c": "Walking",
        "option_d": "Sleeping",
        "correct_answer": "A"
    },
    {
        "question_text": "Routing is done using:",
        "option_a": "app.get()",
        "option_b": "app.jump()",
        "option_c": "app.fly()",
        "option_d": "app.dance()",
        "correct_answer": "A"
    },
    {
        "question_text": "Express can connect to:",
        "option_a": "Databases",
        "option_b": "Plants",
        "option_c": "Shoes",
        "option_d": "Houses",
        "correct_answer": "A"
    },
    {
        "question_text": "Express parses JSON using:",
        "option_a": "express.json()",
        "option_b": "express.give()",
        "option_c": "express.make()",
        "option_d": "express.cut()",
        "correct_answer": "A"
    },
    {
        "question_text": "app.listen is used to:",
        "option_a": "Start server",
        "option_b": "Cook food",
        "option_c": "Clean windows",
        "option_d": "Move bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Express supports:",
        "option_a": "REST APIs",
        "option_b": "Sports",
        "option_c": "Drawing",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "Express uses:",
        "option_a": "npm packages",
        "option_b": "Chocolate",
        "option_c": "Water",
        "option_d": "Glass",
        "correct_answer": "A"
    },
    {
        "question_text": "Express is good for:",
        "option_a": "Building backend services",
        "option_b": "Washing clothes",
        "option_c": "Ironing",
        "option_d": "Driving cars",
        "correct_answer": "A"
    }
],
226: [
    {
        "question_text": "Full stack development includes:",
        "option_a": "Frontend & backend",
        "option_b": "Only cooking",
        "option_c": "Only driving",
        "option_d": "Only painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend mainly uses:",
        "option_a": "HTML, CSS, JS",
        "option_b": "SQL",
        "option_c": "Python only",
        "option_d": "C++",
        "correct_answer": "A"
    },
    {
        "question_text": "Backend handles:",
        "option_a": "Server logic",
        "option_b": "Hair cutting",
        "option_c": "Shopping",
        "option_d": "Painting walls",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs help the frontend:",
        "option_a": "Communicate with backend",
        "option_b": "Cook food",
        "option_c": "Repair bikes",
        "option_d": "Clean houses",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Plants",
        "option_d": "Water",
        "correct_answer": "A"
    },
    {
        "question_text": "Git is used for:",
        "option_a": "Version control",
        "option_b": "Brushing teeth",
        "option_c": "Painting",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "REST APIs use:",
        "option_a": "HTTP",
        "option_b": "Soap",
        "option_c": "Chalk",
        "option_d": "Fuel",
        "correct_answer": "A"
    },
    {
        "question_text": "Full stack developers handle:",
        "option_a": "Entire web apps",
        "option_b": "Road construction",
        "option_c": "Airports",
        "option_d": "Shopping malls",
        "correct_answer": "A"
    },
    {
        "question_text": "Servers run:",
        "option_a": "Backend code",
        "option_b": "Snacks",
        "option_c": "Clothes",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend frameworks include:",
        "option_a": "React",
        "option_b": "Oracle",
        "option_c": "Excel",
        "option_d": "WhatsApp",
        "correct_answer": "A"
    }
],
225: [
    {
        "question_text": "Machine learning trains:",
        "option_a": "Models",
        "option_b": "Shoes",
        "option_c": "Cars",
        "option_d": "Fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Supervised learning uses:",
        "option_a": "Labeled data",
        "option_b": "Paper",
        "option_c": "Water",
        "option_d": "Glass",
        "correct_answer": "A"
    },
    {
        "question_text": "Unsupervised learning finds:",
        "option_a": "Patterns",
        "option_b": "Clothes",
        "option_c": "Fuel",
        "option_d": "Roads",
        "correct_answer": "A"
    },
    {
        "question_text": "Regression predicts:",
        "option_a": "Numbers",
        "option_b": "Fruits",
        "option_c": "Songs",
        "option_d": "Paintings",
        "correct_answer": "A"
    },
    {
        "question_text": "Classification predicts:",
        "option_a": "Categories",
        "option_b": "Animals",
        "option_c": "Cars",
        "option_d": "Bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Training data is used to:",
        "option_a": "Train models",
        "option_b": "Bake cakes",
        "option_c": "Plant trees",
        "option_d": "Build houses",
        "correct_answer": "A"
    },
    {
        "question_text": "Accuracy measures:",
        "option_a": "Correct predictions",
        "option_b": "Height",
        "option_c": "Weight",
        "option_d": "Speed",
        "correct_answer": "A"
    },
    {
        "question_text": "ML uses:",
        "option_a": "Algorithms",
        "option_b": "Shoes",
        "option_c": "Bottles",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Python libraries include:",
        "option_a": "Scikit-learn",
        "option_b": "MS Word",
        "option_c": "Excel",
        "option_d": "Spotify",
        "correct_answer": "A"
    },
    {
        "question_text": "Overfitting happens when model:",
        "option_a": "Learns too much",
        "option_b": "Learns too little",
        "option_c": "Breaks down",
        "option_d": "Sleeps",
        "correct_answer": "A"
    }
],
224: [
    {
        "question_text": "TensorFlow is a:",
        "option_a": "Deep learning framework",
        "option_b": "Photo editor",
        "option_c": "Music app",
        "option_d": "Game",
        "correct_answer": "A"
    },
    {
        "question_text": "Neural networks are inspired by:",
        "option_a": "Human brain",
        "option_b": "Car engine",
        "option_c": "Bike wheel",
        "option_d": "TV screen",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorFlow is developed by:",
        "option_a": "Google",
        "option_b": "Apple",
        "option_c": "Sony",
        "option_d": "IBM",
        "correct_answer": "A"
    },
    {
        "question_text": "Tensors represent:",
        "option_a": "Data in multi-dimensions",
        "option_b": "Shoes",
        "option_c": "Chairs",
        "option_d": "Roads",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorFlow is used for:",
        "option_a": "Training DL models",
        "option_b": "Training cats",
        "option_c": "Training drivers",
        "option_d": "Training singers",
        "correct_answer": "A"
    },
    {
        "question_text": "Activation functions include:",
        "option_a": "ReLU",
        "option_b": "Hello",
        "option_c": "Yellow",
        "option_d": "Mellow",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorFlow models run on:",
        "option_a": "CPU/GPU",
        "option_b": "Bicycle",
        "option_c": "Refrigerator",
        "option_d": "TV",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorFlow uses:",
        "option_a": "Python",
        "option_b": "French",
        "option_c": "Hindi",
        "option_d": "German",
        "correct_answer": "A"
    },
    {
        "question_text": "Model training requires:",
        "option_a": "Dataset",
        "option_b": "Haircut",
        "option_c": "Surgery",
        "option_d": "Snacks",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorBoard helps in:",
        "option_a": "Visualization",
        "option_b": "Decoration",
        "option_c": "Meditation",
        "option_d": "Navigation",
        "correct_answer": "A"
    }
],
223: [
    {
        "question_text": "PyTorch is a:",
        "option_a": "Deep learning library",
        "option_b": "Video game",
        "option_c": "Bike brand",
        "option_d": "Food item",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch is developed by:",
        "option_a": "Facebook (Meta)",
        "option_b": "Google",
        "option_c": "Toyota",
        "option_d": "NASA",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch uses:",
        "option_a": "Tensors",
        "option_b": "Wires",
        "option_c": "Pipes",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch is popular for:",
        "option_a": "Dynamic computation",
        "option_b": "Static images",
        "option_c": "Game controls",
        "option_d": "Car operations",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch models run on:",
        "option_a": "CPU/GPU",
        "option_b": "Car battery",
        "option_c": "Water pump",
        "option_d": "Fan motor",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch helps build:",
        "option_a": "Neural networks",
        "option_b": "Roads",
        "option_c": "Bridges",
        "option_d": "Buildings",
        "correct_answer": "A"
    },
    {
        "question_text": "import torch is used to:",
        "option_a": "Load PyTorch",
        "option_b": "Load Excel",
        "option_c": "Load movies",
        "option_d": "Load games",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch datasets help in:",
        "option_a": "Training models",
        "option_b": "Repairing bikes",
        "option_c": "Cooking food",
        "option_d": "Cleaning tables",
        "correct_answer": "A"
    },
    {
        "question_text": "torchvision is used for:",
        "option_a": "Image data",
        "option_b": "Audio files",
        "option_c": "SMS",
        "option_d": "Calls",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch Lightning is a:",
        "option_a": "Training framework",
        "option_b": "Game engine",
        "option_c": "Paint brand",
        "option_d": "Car model",
        "correct_answer": "A"
    }
],
1: [
    {
        "question_text": "Full stack development includes:",
        "option_a": "Frontend + Backend",
        "option_b": "Only cooking",
        "option_c": "Only driving",
        "option_d": "Only painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend mainly deals with:",
        "option_a": "User interface",
        "option_b": "Road traffic",
        "option_c": "Car engines",
        "option_d": "Laundry",
        "correct_answer": "A"
    },
    {
        "question_text": "Backend handles:",
        "option_a": "Server logic",
        "option_b": "Hair styling",
        "option_c": "Furniture polishing",
        "option_d": "Singing",
        "correct_answer": "A"
    },
    {
        "question_text": "HTML is used for:",
        "option_a": "Structuring web pages",
        "option_b": "Cooking rice",
        "option_c": "Fixing bikes",
        "option_d": "Painting walls",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS is used for:",
        "option_a": "Styling web pages",
        "option_b": "Styling hair",
        "option_c": "Cleaning floors",
        "option_d": "Feeding pets",
        "correct_answer": "A"
    },
    {
        "question_text": "JavaScript helps with:",
        "option_a": "Adding interactivity",
        "option_b": "Mixing colors",
        "option_c": "Driving cars",
        "option_d": "Playing cricket",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Flowers",
        "option_d": "Balloons",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs help systems to:",
        "option_a": "Communicate",
        "option_b": "Dance",
        "option_c": "Fly",
        "option_d": "Sing",
        "correct_answer": "A"
    },
    {
        "question_text": "React, Vue, Angular are:",
        "option_a": "Frontend frameworks",
        "option_b": "Kitchen tools",
        "option_c": "Sports equipment",
        "option_d": "Musical instruments",
        "correct_answer": "A"
    },
    {
        "question_text": "Node.js is used for:",
        "option_a": "Backend development",
        "option_b": "Washing clothes",
        "option_c": "Making juice",
        "option_d": "Decorating rooms",
        "correct_answer": "A"
 }
],
222: [
    {
        "question_text": "NLP stands for:",
        "option_a": "Natural Language Processing",
        "option_b": "Natural Light Power",
        "option_c": "Nano Level Programming",
        "option_d": "New Line Production",
        "correct_answer": "A"
    },
    {
        "question_text": "NLP works mainly with:",
        "option_a": "Text and speech",
        "option_b": "Water and soil",
        "option_c": "Cars and bikes",
        "option_d": "Plants and trees",
        "correct_answer": "A"
    },
    {
        "question_text": "Tokenization breaks text into:",
        "option_a": "Words",
        "option_b": "Shoes",
        "option_c": "Lights",
        "option_d": "Vehicles",
        "correct_answer": "A"
    },
    {
        "question_text": "Sentiment analysis finds:",
        "option_a": "Emotion",
        "option_b": "Weight",
        "option_c": "Height",
        "option_d": "Speed",
        "correct_answer": "A"
    },
    {
        "question_text": "NLP models use:",
        "option_a": "Datasets",
        "option_b": "Bricks",
        "option_c": "Sand",
        "option_d": "Oil",
        "correct_answer": "A"
    },
    {
        "question_text": "Stemming reduces words to:",
        "option_a": "Root form",
        "option_b": "New forms",
        "option_c": "File names",
        "option_d": "Folder names",
        "correct_answer": "A"
    },
    {
        "question_text": "NLP is commonly used in:",
        "option_a": "Chatbots",
        "option_b": "Cars",
        "option_c": "Shoes",
        "option_d": "Furniture",
        "correct_answer": "A"
    },
    {
        "question_text": "Language translation uses:",
        "option_a": "NLP models",
        "option_b": "TV apps",
        "option_c": "Cameras",
        "option_d": "GPS",
        "correct_answer": "A"
    },
    {
        "question_text": "Stopwords are:",
        "option_a": "Common words removed",
        "option_b": "Traffic signals",
        "option_c": "Road bumps",
        "option_d": "Parking stops",
        "correct_answer": "A"
    },
    {
        "question_text": "NER identifies:",
        "option_a": "Named entities",
        "option_b": "Named colors",
        "option_c": "Named vehicles",
        "option_d": "Named roads",
        "correct_answer": "A"
    }
],
221: [
    {
        "question_text": "AI stands for:",
        "option_a": "Artificial Intelligence",
        "option_b": "Automatic Icecream",
        "option_c": "Audio Input",
        "option_d": "Air Injection",
        "correct_answer": "A"
    },
    {
        "question_text": "AI systems learn using:",
        "option_a": "Data",
        "option_b": "Rocks",
        "option_c": "Plants",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "AI is used in:",
        "option_a": "Voice assistants",
        "option_b": "Toothpaste",
        "option_c": "Chalk pieces",
        "option_d": "Water bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "AI aims to mimic:",
        "option_a": "Human intelligence",
        "option_b": "Animal fur",
        "option_c": "Car design",
        "option_d": "Table shape",
        "correct_answer": "A"
    },
    {
        "question_text": "AI helps in:",
        "option_a": "Prediction",
        "option_b": "Car washing",
        "option_c": "Sweeping",
        "option_d": "Driving cycles",
        "correct_answer": "A"
    },
    {
        "question_text": "AI uses:",
        "option_a": "Algorithms",
        "option_b": "Balloons",
        "option_c": "Ribbons",
        "option_d": "Bricks",
        "correct_answer": "A"
    },
    {
        "question_text": "AI is applied in:",
        "option_a": "Healthcare",
        "option_b": "Cinemas",
        "option_c": "Clothing stores",
        "option_d": "Tea shops",
        "correct_answer": "A"
    },
    {
        "question_text": "Machine learning is a subset of:",
        "option_a": "AI",
        "option_b": "History",
        "option_c": "Geography",
        "option_d": "Physics",
        "correct_answer": "A"
    },
    {
        "question_text": "AI models need:",
        "option_a": "Training",
        "option_b": "Washing",
        "option_c": "Freezing",
        "option_d": "Burning",
        "correct_answer": "A"
    },
    {
        "question_text": "AI improves with more:",
        "option_a": "Data",
        "option_b": "Salt",
        "option_c": "Air",
        "option_d": "Shoes",
        "correct_answer": "A"
    }
],
220: [
    {
        "question_text": "Competitive programming improves:",
        "option_a": "Problem solving",
        "option_b": "Singing",
        "option_c": "Driving",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "CP problems are solved using:",
        "option_a": "Algorithms",
        "option_b": "Paint brushes",
        "option_c": "Bikes",
        "option_d": "Hammers",
        "correct_answer": "A"
    },
    {
        "question_text": "CP platforms include:",
        "option_a": "Codeforces",
        "option_b": "Instagram",
        "option_c": "Spotify",
        "option_d": "Hotstar",
        "correct_answer": "A"
    },
    {
        "question_text": "Time complexity measures:",
        "option_a": "Performance",
        "option_b": "Color",
        "option_c": "Weight",
        "option_d": "Shape",
        "correct_answer": "A"
    },
    {
        "question_text": "Sorting is a common:",
        "option_a": "Algorithm topic",
        "option_b": "Dessert",
        "option_c": "Car part",
        "option_d": "Sport",
        "correct_answer": "A"
    },
    {
        "question_text": "Greedy algorithms choose:",
        "option_a": "Best immediate option",
        "option_b": "Random numbers",
        "option_c": "Shoes",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "DP stands for:",
        "option_a": "Dynamic Programming",
        "option_b": "Double Pizza",
        "option_c": "Door Panel",
        "option_d": "Dark Power",
        "correct_answer": "A"
    },
    {
        "question_text": "Most CP programs run in:",
        "option_a": "C++",
        "option_b": "MS Word",
        "option_c": "Photoshop",
        "option_d": "Excel",
        "correct_answer": "A"
    },
    {
        "question_text": "CP helps prepare for:",
        "option_a": "Interviews",
        "option_b": "Birthday parties",
        "option_c": "Painting competitions",
        "option_d": "Cricket matches",
        "correct_answer": "A"
    },
    {
        "question_text": "CP contests require:",
        "option_a": "Speed and accuracy",
        "option_b": "Running",
        "option_c": "Swimming",
        "option_d": "Driving",
        "correct_answer": "A"
    }
],
219: [
    {
        "question_text": "DSA stands for:",
        "option_a": "Data Structures & Algorithms",
        "option_b": "Drive Slow Always",
        "option_c": "Dance Song Album",
        "option_d": "Deep Space Area",
        "correct_answer": "A"
    },
    {
        "question_text": "Stacks follow:",
        "option_a": "LIFO",
        "option_b": "FIFO",
        "option_c": "LILO",
        "option_d": "Random",
        "correct_answer": "A"
    },
    {
        "question_text": "Queues follow:",
        "option_a": "FIFO",
        "option_b": "LIFO",
        "option_c": "Random",
        "option_d": "Circular",
        "correct_answer": "A"
    },
    {
        "question_text": "Binary search works on:",
        "option_a": "Sorted arrays",
        "option_b": "Uncooked rice",
        "option_c": "Paintings",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Trees contain:",
        "option_a": "Nodes",
        "option_b": "Shoes",
        "option_c": "Tracks",
        "option_d": "Nails",
        "correct_answer": "A"
    },
    {
        "question_text": "Graphs store:",
        "option_a": "Connections",
        "option_b": "Clothes",
        "option_c": "Water",
        "option_d": "Fuel",
        "correct_answer": "A"
    },
    {
        "question_text": "Algorithms help improve:",
        "option_a": "Efficiency",
        "option_b": "Taste",
        "option_c": "Smell",
        "option_d": "Height",
        "correct_answer": "A"
    },
    {
        "question_text": "Java uses:",
        "option_a": "Classes",
        "option_b": "Desks",
        "option_c": "Tables",
        "option_d": "Walls",
        "correct_answer": "A"
    },
    {
        "question_text": "Recursion solves problems by:",
        "option_a": "Calling itself",
        "option_b": "Calling police",
        "option_c": "Calling drivers",
        "option_d": "Calling teachers",
        "correct_answer": "A"
    },
    {
        "question_text": "Time complexity describes:",
        "option_a": "Running time",
        "option_b": "Color coding",
        "option_c": "Music time",
        "option_d": "Height gain",
        "correct_answer": "A"
    }
],
213: [
    {
        "question_text": "AWS stands for:",
        "option_a": "Amazon Web Services",
        "option_b": "Advanced Water System",
        "option_c": "Automatic Web Software",
        "option_d": "Alpha Wireless Server",
        "correct_answer": "A"
    },
    {
        "question_text": "S3 is used for:",
        "option_a": "Object storage",
        "option_b": "Cooking food",
        "option_c": "Running games",
        "option_d": "Watching movies",
        "correct_answer": "A"
    },
    {
        "question_text": "EC2 provides:",
        "option_a": "Virtual servers",
        "option_b": "Car engines",
        "option_c": "Mobile apps",
        "option_d": "Paint colors",
        "correct_answer": "A"
    },
    {
        "question_text": "IAM manages:",
        "option_a": "Users & permissions",
        "option_b": "Shoes",
        "option_c": "Desks",
        "option_d": "Shops",
        "correct_answer": "A"
    },
    {
        "question_text": "RDS is a:",
        "option_a": "Database service",
        "option_b": "Delivery truck",
        "option_c": "Mobile phone",
        "option_d": "Laptop brand",
        "correct_answer": "A"
    },
    {
        "question_text": "CloudFront is a:",
        "option_a": "CDN",
        "option_b": "Restaurant",
        "option_c": "Laptop",
        "option_d": "Speaker",
        "correct_answer": "A"
    },
    {
        "question_text": "Lambda is used for:",
        "option_a": "Serverless functions",
        "option_b": "Music editing",
        "option_c": "Game creation",
        "option_d": "Bike repair",
        "correct_answer": "A"
    },
    {
        "question_text": "VPC stands for:",
        "option_a": "Virtual Private Cloud",
        "option_b": "Video Processor Card",
        "option_c": "Virtual PC",
        "option_d": "Voice Processing Channel",
        "correct_answer": "A"
    },
    {
        "question_text": "AWS charges based on:",
        "option_a": "Usage",
        "option_b": "Age",
        "option_c": "Name",
        "option_d": "Color",
        "correct_answer": "A"
    },
    {
        "question_text": "AWS region means:",
        "option_a": "Geographical location",
        "option_b": "Car parking zone",
        "option_c": "Building block",
        "option_d": "File size",
        "correct_answer": "A"
    }
],
212: [
    {
        "question_text": "Azure is a:",
        "option_a": "Cloud platform",
        "option_b": "Bike model",
        "option_c": "Medicine",
        "option_d": "Furniture",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure VMs provide:",
        "option_a": "Virtual machines",
        "option_b": "Water machines",
        "option_c": "Coffee machines",
        "option_d": "Ticket machines",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Storage stores:",
        "option_a": "Files and data",
        "option_b": "Shoes",
        "option_c": "Clothes",
        "option_d": "Milk",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure AD manages:",
        "option_a": "Identity & access",
        "option_b": "Audio devices",
        "option_c": "Agriculture",
        "option_d": "Air cooling",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure SQL is a:",
        "option_a": "Database",
        "option_b": "Pen",
        "option_c": "Car",
        "option_d": "TV",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Functions provide:",
        "option_a": "Serverless compute",
        "option_b": "Music playlists",
        "option_c": "Camera filters",
        "option_d": "Web ads",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure App Service hosts:",
        "option_a": "Web apps",
        "option_b": "Shoes",
        "option_c": "Games",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure regions are:",
        "option_a": "Data center locations",
        "option_b": "Game levels",
        "option_c": "File names",
        "option_d": "Room sizes",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Monitor tracks:",
        "option_a": "Performance",
        "option_b": "Temperature of tea",
        "option_c": "Color of sky",
        "option_d": "Length of wire",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure bills based on:",
        "option_a": "Usage",
        "option_b": "Weather",
        "option_c": "Clothes",
        "option_d": "Street",
        "correct_answer": "A"
    }
],
211: [
    {
        "question_text": "A network connects:",
        "option_a": "Devices",
        "option_b": "Vegetables",
        "option_c": "Clothes",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "LAN stands for:",
        "option_a": "Local Area Network",
        "option_b": "Large Apple Net",
        "option_c": "Low Angle Node",
        "option_d": "Long Area Number",
        "correct_answer": "A"
    },
    {
        "question_text": "IP address identifies:",
        "option_a": "A device",
        "option_b": "A fruit",
        "option_c": "A building",
        "option_d": "A vehicle",
        "correct_answer": "A"
    },
    {
        "question_text": "HTTP is used for:",
        "option_a": "Web communication",
        "option_b": "Cooking meals",
        "option_c": "Charging phones",
        "option_d": "Playing games",
        "correct_answer": "A"
    },
    {
        "question_text": "DNS resolves:",
        "option_a": "Domain names",
        "option_b": "Car names",
        "option_c": "School names",
        "option_d": "Street names",
        "correct_answer": "A"
    },
    {
        "question_text": "Router forwards:",
        "option_a": "Network packets",
        "option_b": "TV channels",
        "option_c": "Music notes",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "TCP ensures:",
        "option_a": "Reliable communication",
        "option_b": "Fast cooking",
        "option_c": "Cloth cleaning",
        "option_d": "Floor wiping",
        "correct_answer": "A"
    },
    {
        "question_text": "UDP is:",
        "option_a": "Connectionless",
        "option_b": "Colorless",
        "option_c": "Weightless",
        "option_d": "Timeless",
        "correct_answer": "A"
    },
    {
        "question_text": "Firewall provides:",
        "option_a": "Network security",
        "option_b": "Room cleaning",
        "option_c": "Bike repair",
        "option_d": "Water pumping",
        "correct_answer": "A"
    },
    {
        "question_text": "Switch connects:",
        "option_a": "Multiple devices",
        "option_b": "Shoes",
        "option_c": "Rooms",
        "option_d": "Cars",
        "correct_answer": "A"
    }
],
210: [
    {
        "question_text": "An operating system manages:",
        "option_a": "Hardware & software",
        "option_b": "Vegetables",
        "option_c": "Furniture",
        "option_d": "Sports",
        "correct_answer": "A"
    },
    {
        "question_text": "The kernel is the:",
        "option_a": "Core of OS",
        "option_b": "Core of fruit",
        "option_c": "Core of car",
        "option_d": "Core of pen",
        "correct_answer": "A"
    },
    {
        "question_text": "RAM stores:",
        "option_a": "Temporary data",
        "option_b": "Shoes",
        "option_c": "Paint",
        "option_d": "Milk",
        "correct_answer": "A"
    },
    {
        "question_text": "A process is a:",
        "option_a": "Program in execution",
        "option_b": "Running shoe",
        "option_c": "Car engine",
        "option_d": "Keyboard",
        "correct_answer": "A"
    },
    {
        "question_text": "OS handles:",
        "option_a": "Memory management",
        "option_b": "Kitchen management",
        "option_c": "Garden management",
        "option_d": "Mall management",
        "correct_answer": "A"
    },
    {
        "question_text": "Scheduling decides:",
        "option_a": "Which process runs",
        "option_b": "Which shoe fits",
        "option_c": "Which bike moves",
        "option_d": "Which door opens",
        "correct_answer": "A"
    },
    {
        "question_text": "Deadlock occurs when:",
        "option_a": "Processes wait forever",
        "option_b": "People walk fast",
        "option_c": "Birds fly",
        "option_d": "Cars move",
        "correct_answer": "A"
    },
    {
        "question_text": "Linux is a:",
        "option_a": "Operating system",
        "option_b": "Shoe brand",
        "option_c": "Pen brand",
        "option_d": "Drink brand",
        "correct_answer": "A"
    },
    {
        "question_text": "OS controls:",
        "option_a": "Input/Output",
        "option_b": "Temperature",
        "option_c": "Rain",
        "option_d": "Wind",
        "correct_answer": "A"
    },
    {
        "question_text": "File system stores:",
        "option_a": "Files",
        "option_b": "Bikes",
        "option_c": "Games",
        "option_d": "Animals",
        "correct_answer": "A"
    }
],
209: [
    {
        "question_text": "Cloud computing delivers:",
        "option_a": "Services over the internet",
        "option_b": "Shoes",
        "option_c": "Water",
        "option_d": "Furniture",
        "correct_answer": "A"
    },
    {
        "question_text": "IaaS provides:",
        "option_a": "Infrastructure",
        "option_b": "Ice cream",
        "option_c": "Insects",
        "option_d": "Ink",
        "correct_answer": "A"
    },
    {
        "question_text": "SaaS provides:",
        "option_a": "Software",
        "option_b": "Salt",
        "option_c": "Sand",
        "option_d": "Soap",
        "correct_answer": "A"
    },
    {
        "question_text": "PaaS provides:",
        "option_a": "Platform",
        "option_b": "Pencil",
        "option_c": "Pillow",
        "option_d": "Paper",
        "correct_answer": "A"
    },
    {
        "question_text": "Major cloud provider:",
        "option_a": "AWS",
        "option_b": "Adobe",
        "option_c": "Pepsi",
        "option_d": "Honda",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud allows:",
        "option_a": "Scalability",
        "option_b": "Walking",
        "option_c": "Cooking",
        "option_d": "Washing",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud stores data in:",
        "option_a": "Remote servers",
        "option_b": "Shoes",
        "option_c": "Drawers",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Virtualization enables:",
        "option_a": "Multiple VMs",
        "option_b": "Multiple bikes",
        "option_c": "Multiple books",
        "option_d": "Multiple trees",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud apps run:",
        "option_a": "Online",
        "option_b": "Underwater",
        "option_c": "In air",
        "option_d": "Inside books",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud backups help in:",
        "option_a": "Data recovery",
        "option_b": "Cooking chapati",
        "option_c": "Fixing bikes",
        "option_d": "Repairing phones",
        "correct_answer": "A"
    }
],
208: [
    {
        "question_text": "CPU stands for:",
        "option_a": "Central Processing Unit",
        "option_b": "Cold Power Unit",
        "option_c": "Car Parking Unit",
        "option_d": "Coffee Processing Unit",
        "correct_answer": "A"
    },
    {
        "question_text": "ALU performs:",
        "option_a": "Arithmetic operations",
        "option_b": "Painting",
        "option_c": "Singing",
        "option_d": "Dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Registers store:",
        "option_a": "Temporary data",
        "option_b": "Clothes",
        "option_c": "Shoes",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Cache memory is:",
        "option_a": "Fast memory",
        "option_b": "Cold memory",
        "option_c": "Wet memory",
        "option_d": "Tall memory",
        "correct_answer": "A"
    },
    {
        "question_text": "Von Neumann model uses:",
        "option_a": "Single memory",
        "option_b": "Seven memories",
        "option_c": "Three memories",
        "option_d": "Four memories",
        "correct_answer": "A"
    },
    {
        "question_text": "Clock speed measures:",
        "option_a": "CPU speed",
        "option_b": "Bike speed",
        "option_c": "Running speed",
        "option_d": "Car speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Instruction cycle contains:",
        "option_a": "Fetch & execute",
        "option_b": "Cook & eat",
        "option_c": "Walk & run",
        "option_d": "Sit & stand",
        "correct_answer": "A"
    },
    {
        "question_text": "RAM is:",
        "option_a": "Volatile",
        "option_b": "Edible",
        "option_c": "Liquid",
        "option_d": "Invisible",
        "correct_answer": "A"
    },
    {
        "question_text": "GPU is used for:",
        "option_a": "Graphics",
        "option_b": "Buses",
        "option_c": "Shoes",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "ROM stores:",
        "option_a": "Permanent data",
        "option_b": "Fresh food",
        "option_c": "Old clothes",
        "option_d": "Sports items",
        "correct_answer": "A"
    }
],
207: [
    {
        "question_text": "Software engineering focuses on:",
        "option_a": "Building software",
        "option_b": "Building roads",
        "option_c": "Building tables",
        "option_d": "Building gardens",
        "correct_answer": "A"
    },
    {
        "question_text": "SDLC stands for:",
        "option_a": "Software Development Life Cycle",
        "option_b": "Soft Drink Large Cup",
        "option_c": "Small Data Logic Circuit",
        "option_d": "Safe Driving Lane Code",
        "correct_answer": "A"
    },
    {
        "question_text": "Testing ensures:",
        "option_a": "Quality",
        "option_b": "Rain",
        "option_c": "Wind",
        "option_d": "Storm",
        "correct_answer": "A"
    },
    {
        "question_text": "Agile is a:",
        "option_a": "Development methodology",
        "option_b": "Fruit",
        "option_c": "Metal",
        "option_d": "Animal",
        "correct_answer": "A"
    },
    {
        "question_text": "Requirement gathering is a:",
        "option_a": "SDLC phase",
        "option_b": "Sports event",
        "option_c": "Shopping method",
        "option_d": "Cooking style",
        "correct_answer": "A"
    },
    {
        "question_text": "Bug means:",
        "option_a": "Error in code",
        "option_b": "Fly",
        "option_c": "Mosquito",
        "option_d": "Fish",
        "correct_answer": "A"
    },
    {
        "question_text": "Documentation helps:",
        "option_a": "Understanding system",
        "option_b": "Driving cars",
        "option_c": "Cleaning floors",
        "option_d": "Washing clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Prototype is a:",
        "option_a": "Model",
        "option_b": "Meal",
        "option_c": "Toy",
        "option_d": "Chair",
        "correct_answer": "A"
    },
    {
        "question_text": "Version control manages:",
        "option_a": "Code changes",
        "option_b": "Bike changes",
        "option_c": "Dress changes",
        "option_d": "Room changes",
        "correct_answer": "A"
    },
    {
        "question_text": "Maintenance fixes:",
        "option_a": "Errors",
        "option_b": "Pillows",
        "option_c": "Dress buttons",
        "option_d": "Shoes",
        "correct_answer": "A"
    }
],
206: [
    {
        "question_text": "System design focuses on:",
        "option_a": "Designing scalable systems",
        "option_b": "Designing clothes",
        "option_c": "Designing cups",
        "option_d": "Designing chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Load balancing distributes:",
        "option_a": "Traffic",
        "option_b": "Food",
        "option_c": "Shoes",
        "option_d": "Pens",
        "correct_answer": "A"
    },
    {
        "question_text": "Caching improves:",
        "option_a": "Speed",
        "option_b": "Color",
        "option_c": "Taste",
        "option_d": "Weight",
        "correct_answer": "A"
    },
    {
        "question_text": "Database sharding splits:",
        "option_a": "Data",
        "option_b": "Dinner",
        "option_c": "Water",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "System reliability ensures:",
        "option_a": "Uptime",
        "option_b": "Sunshine",
        "option_c": "Rain",
        "option_d": "Wind",
        "correct_answer": "A"
    },
    {
        "question_text": "CDN delivers:",
        "option_a": "Static content",
        "option_b": "Fresh air",
        "option_c": "Vehicles",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Microservices are:",
        "option_a": "Independent services",
        "option_b": "Independent tables",
        "option_c": "Independent cars",
        "option_d": "Independent shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "API gateway manages:",
        "option_a": "API requests",
        "option_b": "Bike requests",
        "option_c": "Food requests",
        "option_d": "Train requests",
        "correct_answer": "A"
    },
    {
        "question_text": "A monolith is:",
        "option_a": "Single large application",
        "option_b": "Single large car",
        "option_c": "Single large shoe",
        "option_d": "Single large book",
        "correct_answer": "A"
    },
    {
        "question_text": "High availability means:",
        "option_a": "System always works",
        "option_b": "Lights always ON",
        "option_c": "Phones always charged",
        "option_d": "Shoes always clean",
        "correct_answer": "A"
    }
],
205: [
    {
        "question_text": "DBMS stands for:",
        "option_a": "Database Management System",
        "option_b": "Data Bike Motor Speed",
        "option_c": "Dry Bread Milk Sandwich",
        "option_d": "Desk Book Mobile Storage",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL is used for:",
        "option_a": "Querying data",
        "option_b": "Cooking",
        "option_c": "Painting",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "A table contains:",
        "option_a": "Rows & columns",
        "option_b": "Wheels",
        "option_c": "Doors",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary key is:",
        "option_a": "Unique identifier",
        "option_b": "Unique shoe",
        "option_c": "Unique fruit",
        "option_d": "Unique drink",
        "correct_answer": "A"
    },
    {
        "question_text": "Joins combine:",
        "option_a": "Tables",
        "option_b": "Chairs",
        "option_c": "Shoes",
        "option_d": "Cars",
        "correct_answer": "A"
    },
    {
        "question_text": "Database stores:",
        "option_a": "Data",
        "option_b": "Sand",
        "option_c": "Water",
        "option_d": "Dust",
        "correct_answer": "A"
    },
    {
        "question_text": "Index improves:",
        "option_a": "Speed",
        "option_b": "Taste",
        "option_c": "Color",
        "option_d": "Smell",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign key links:",
        "option_a": "Tables",
        "option_b": "Shoes",
        "option_c": "Papers",
        "option_d": "Rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Normalization reduces:",
        "option_a": "Redundancy",
        "option_b": "Electricity",
        "option_c": "Sound",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "DDL stands for:",
        "option_a": "Data Definition Language",
        "option_b": "Dry Delicious Lemonade",
        "option_c": "Dark Dancing Light",
        "option_d": "Digital Driving License",
        "correct_answer": "A"
    }
],
204: [
    {
        "question_text": "Data structures store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Pens",
        "option_d": "Bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Stack follows:",
        "option_a": "LIFO",
        "option_b": "FIFO",
        "option_c": "Random",
        "option_d": "Circular",
        "correct_answer": "A"
    },
    {
        "question_text": "Queue follows:",
        "option_a": "FIFO",
        "option_b": "LIFO",
        "option_c": "Reverse",
        "option_d": "Random",
        "correct_answer": "A"
    },
    {
        "question_text": "Arrays store data in:",
        "option_a": "Contiguous memory",
        "option_b": "Pockets",
        "option_c": "Drawers",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Linked list contains:",
        "option_a": "Nodes",
        "option_b": "Stones",
        "option_c": "Papers",
        "option_d": "Cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Trees are:",
        "option_a": "Hierarchical",
        "option_b": "Flat",
        "option_c": "Round",
        "option_d": "Square",
        "correct_answer": "A"
    },
    {
        "question_text": "Graphs connect:",
        "option_a": "Vertices",
        "option_b": "Shoes",
        "option_c": "Clothes",
        "option_d": "Rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Searching finds:",
        "option_a": "Element",
        "option_b": "Water",
        "option_c": "Air",
        "option_d": "Paint",
        "correct_answer": "A"
    },
    {
        "question_text": "Sorting arranges:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Bikes",
        "option_d": "Rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Hashing stores data by:",
        "option_a": "Key",
        "option_b": "Color",
        "option_c": "Taste",
        "option_d": "Size",
        "correct_answer": "A"
    }
],
201: [
    {
        "question_text": "An algorithm is a:",
        "option_a": "Step-by-step process",
        "option_b": "Step-by-step dance",
        "option_c": "Random guess",
        "option_d": "Magic trick",
        "correct_answer": "A"
    },
    {
        "question_text": "Searching algorithms find:",
        "option_a": "Elements",
        "option_b": "Shoes",
        "option_c": "Clothes",
        "option_d": "Animals",
        "correct_answer": "A"
    },
    {
        "question_text": "Sorting arranges:",
        "option_a": "Data",
        "option_b": "Vegetables",
        "option_c": "Bikes",
        "option_d": "Rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Binary search works on:",
        "option_a": "Sorted data",
        "option_b": "Painted walls",
        "option_c": "Broken tables",
        "option_d": "Wet floors",
        "correct_answer": "A"
    },
    {
        "question_text": "Time complexity measures:",
        "option_a": "Efficiency",
        "option_b": "Height",
        "option_c": "Weight",
        "option_d": "Taste",
        "correct_answer": "A"
    },
    {
        "question_text": "Merge sort uses:",
        "option_a": "Divide & conquer",
        "option_b": "Divide & eat",
        "option_c": "Divide & paint",
        "option_d": "Divide & run",
        "correct_answer": "A"
    },
    {
        "question_text": "A graph represents:",
        "option_a": "Connections",
        "option_b": "Clothes",
        "option_c": "Shoes",
        "option_d": "Boxes",
        "correct_answer": "A"
    },
    {
        "question_text": "Recursion is a function that:",
        "option_a": "Calls itself",
        "option_b": "Calls friends",
        "option_c": "Calls strangers",
        "option_d": "Calls numbers",
        "correct_answer": "A"
    },
    {
        "question_text": "Greedy algorithms choose:",
        "option_a": "Best immediate choice",
        "option_b": "Worst choice",
        "option_c": "Random choice",
        "option_d": "No choice",
        "correct_answer": "A"
    },
    {
        "question_text": "Graph traversal includes:",
        "option_a": "BFS & DFS",
        "option_b": "Up & Down",
        "option_c": "Left & Right",
        "option_d": "In & Out",
        "correct_answer": "A"
    }
],

200: [
    {
        "question_text": "Data science uses:",
        "option_a": "Data",
        "option_b": "Chairs",
        "option_c": "Shoes",
        "option_d": "Air",
        "correct_answer": "A"
    },
    {
        "question_text": "Python libraries include:",
        "option_a": "Pandas",
        "option_b": "Spotify",
        "option_c": "Instagram",
        "option_d": "Bluetooth",
        "correct_answer": "A"
    },
    {
        "question_text": "Matplotlib is used for:",
        "option_a": "Visualization",
        "option_b": "Cooking",
        "option_c": "Cleaning",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Data cleaning removes:",
        "option_a": "Errors",
        "option_b": "Shoes",
        "option_c": "Cars",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "CSV files store:",
        "option_a": "Data",
        "option_b": "Water",
        "option_c": "Paint",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Machine learning is part of:",
        "option_a": "Data science",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Singing",
        "correct_answer": "A"
    },
    {
        "question_text": "NumPy arrays are:",
        "option_a": "Numeric data structures",
        "option_b": "Shoes",
        "option_c": "Tables",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "EDA helps in:",
        "option_a": "Understanding data",
        "option_b": "Understanding music",
        "option_c": "Understanding pets",
        "option_d": "Understanding roads",
        "correct_answer": "A"
    },
    {
        "question_text": "Predictive models make:",
        "option_a": "Predictions",
        "option_b": "Food",
        "option_c": "Movies",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Python is popular due to:",
        "option_a": "Simplicity",
        "option_b": "Taste",
        "option_c": "Smell",
        "option_d": "Color",
        "correct_answer": "A"
    }
],
199: [
    {
        "question_text": "AI helps computers:",
        "option_a": "Think",
        "option_b": "Eat",
        "option_c": "Walk",
        "option_d": "Sleep",
        "correct_answer": "A"
    },
    {
        "question_text": "AI applications include:",
        "option_a": "Chatbots",
        "option_b": "Fruit shops",
        "option_c": "Laundry",
        "option_d": "Gardening",
        "correct_answer": "A"
    },
    {
        "question_text": "AI uses:",
        "option_a": "Algorithms",
        "option_b": "Chalks",
        "option_c": "Shoes",
        "option_d": "Glass",
        "correct_answer": "A"
    },
    {
        "question_text": "AI models improve with:",
        "option_a": "More data",
        "option_b": "More noise",
        "option_c": "More dust",
        "option_d": "More stones",
        "correct_answer": "A"
    },
    {
        "question_text": "AI predicts:",
        "option_a": "Outcomes",
        "option_b": "Sunrise",
        "option_c": "Rain timing",
        "option_d": "Earth shape",
        "correct_answer": "A"
    },
    {
        "question_text": "AI is a part of:",
        "option_a": "Computer science",
        "option_b": "Arts",
        "option_c": "Medicine",
        "option_d": "Cooking",
        "correct_answer": "A"
    },
    {
        "question_text": "AI helps in:",
        "option_a": "Automation",
        "option_b": "Decoration",
        "option_c": "Relaxation",
        "option_d": "Celebration",
        "correct_answer": "A"
    },
    {
        "question_text": "AI powers apps like:",
        "option_a": "Google Assistant",
        "option_b": "Camera flashlight",
        "option_c": "Power bank",
        "option_d": "Oil filter",
        "correct_answer": "A"
    },
    {
        "question_text": "AI can recognize:",
        "option_a": "Speech",
        "option_b": "Taste",
        "option_c": "Smell",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "AI is used in:",
        "option_a": "Healthcare",
        "option_b": "Paperwork",
        "option_c": "Mailboxes",
        "option_d": "Toy shops",
        "correct_answer": "A"
    }
],
198: [
    {
        "question_text": "Big data refers to:",
        "option_a": "Large datasets",
        "option_b": "Large shoes",
        "option_c": "Large fruits",
        "option_d": "Large pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Hadoop is used for:",
        "option_a": "Big data processing",
        "option_b": "Cooking",
        "option_c": "Painting",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "MapReduce performs:",
        "option_a": "Parallel processing",
        "option_b": "Parallel cooking",
        "option_c": "Parallel running",
        "option_d": "Parallel dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Spark is a:",
        "option_a": "Data engine",
        "option_b": "Car engine",
        "option_c": "Bike engine",
        "option_d": "Fan engine",
        "correct_answer": "A"
    },
    {
        "question_text": "Big data is described by:",
        "option_a": "Volume, Velocity, Variety",
        "option_b": "Height, Width, Weight",
        "option_c": "Taste, Colour, Smell",
        "option_d": "Hot, Cold, Warm",
        "correct_answer": "A"
    },
    {
        "question_text": "Big data stores:",
        "option_a": "Huge information",
        "option_b": "Huge shoes",
        "option_c": "Huge cars",
        "option_d": "Huge pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "HDFS is a:",
        "option_a": "File system",
        "option_b": "Phone",
        "option_c": "Bag",
        "option_d": "Chair",
        "correct_answer": "A"
    },
    {
        "question_text": "Data lakes store:",
        "option_a": "Raw data",
        "option_b": "Raw vegetables",
        "option_c": "Raw stones",
        "option_d": "Raw wood",
        "correct_answer": "A"
    },
    {
        "question_text": "Big data helps in:",
        "option_a": "Analytics",
        "option_b": "Cycling",
        "option_c": "Swimming",
        "option_d": "Painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Cluster means:",
        "option_a": "Group of servers",
        "option_b": "Group of chairs",
        "option_c": "Group of shirts",
        "option_d": "Group of cups",
        "correct_answer": "A"
    }
],
197: [
    {
        "question_text": "PostgreSQL is a:",
        "option_a": "Relational database",
        "option_b": "Shoe brand",
        "option_c": "Phone charger",
        "option_d": "Cooking stove",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres uses:",
        "option_a": "SQL",
        "option_b": "HTML",
        "option_c": "Photoshop",
        "option_d": "Excel formulas",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary keys must be:",
        "option_a": "Unique",
        "option_b": "Blue",
        "option_c": "Heavy",
        "option_d": "Round",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN combines:",
        "option_a": "Tables",
        "option_b": "Shoes",
        "option_c": "Boxes",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres supports:",
        "option_a": "JSON data",
        "option_b": "JPG images",
        "option_c": "MP3 songs",
        "option_d": "PNG editing",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes improve:",
        "option_a": "Query speed",
        "option_b": "Color quality",
        "option_c": "Sound quality",
        "option_d": "Bike mileage",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres stores data in:",
        "option_a": "Tables",
        "option_b": "Tanks",
        "option_c": "Trucks",
        "option_d": "Trees",
        "correct_answer": "A"
    },
    {
        "question_text": "ACID ensures:",
        "option_a": "Database reliability",
        "option_b": "Food freshness",
        "option_c": "Room lighting",
        "option_d": "Battery backup",
        "correct_answer": "A"
    },
    {
        "question_text": "Constraints protect:",
        "option_a": "Data integrity",
        "option_b": "Skin",
        "option_c": "Shoes",
        "option_d": "Clothing",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign key links:",
        "option_a": "Two tables",
        "option_b": "Two chairs",
        "option_c": "Two phones",
        "option_d": "Two bikes",
        "correct_answer": "A"
    }
],
196: [
    {
        "question_text": "SQL is used to:",
        "option_a": "Query data",
        "option_b": "Cook food",
        "option_c": "Fly drones",
        "option_d": "Paint walls",
        "correct_answer": "A"
    },
    {
        "question_text": "SELECT keyword retrieves:",
        "option_a": "Data",
        "option_b": "Water",
        "option_c": "Shoes",
        "option_d": "Tables",
        "correct_answer": "A"
    },
    {
        "question_text": "WHERE is used to:",
        "option_a": "Filter data",
        "option_b": "Filter tea",
        "option_c": "Filter air",
        "option_d": "Filter water",
        "correct_answer": "A"
    },
    {
        "question_text": "ORDER BY sorts:",
        "option_a": "Results",
        "option_b": "Clothes",
        "option_c": "Sheets",
        "option_d": "Plates",
        "correct_answer": "A"
    },
    {
        "question_text": "INSERT adds:",
        "option_a": "New records",
        "option_b": "New shoes",
        "option_c": "New phones",
        "option_d": "New lamps",
        "correct_answer": "A"
    },
    {
        "question_text": "UPDATE modifies:",
        "option_a": "Records",
        "option_b": "T-shirts",
        "option_c": "Notebooks",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE removes:",
        "option_a": "Records",
        "option_b": "Bikes",
        "option_c": "Vegetables",
        "option_d": "Games",
        "correct_answer": "A"
    },
    {
        "question_text": "GROUP BY groups:",
        "option_a": "Data",
        "option_b": "Chairs",
        "option_c": "Pillows",
        "option_d": "Doors",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN connects:",
        "option_a": "Tables",
        "option_b": "Cars",
        "option_c": "Bags",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL constraints ensure:",
        "option_a": "Data accuracy",
        "option_b": "Food freshness",
        "option_c": "Air purity",
        "option_d": "Light brightness",
        "correct_answer": "A"
    }
],
195: [
    {
        "question_text": "Power BI is used for:",
        "option_a": "Data visualization",
        "option_b": "Drawing cartoons",
        "option_c": "Cooking",
        "option_d": "Sewing",
        "correct_answer": "A"
    },
    {
        "question_text": "Dashboards show:",
        "option_a": "Insights",
        "option_b": "Shoes",
        "option_c": "Rooms",
        "option_d": "Clouds",
        "correct_answer": "A"
    },
    {
        "question_text": "Power Query helps in:",
        "option_a": "Data cleaning",
        "option_b": "Shoe polishing",
        "option_c": "Car washing",
        "option_d": "Room painting",
        "correct_answer": "A"
    },
    {
        "question_text": "DAX is used for:",
        "option_a": "Calculations",
        "option_b": "Decoration",
        "option_c": "Driving",
        "option_d": "Singing",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI connects to:",
        "option_a": "Databases",
        "option_b": "Speakers",
        "option_c": "Watches",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Reports contain:",
        "option_a": "Visuals",
        "option_b": "Pillows",
        "option_c": "Lamps",
        "option_d": "Fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI can import:",
        "option_a": "CSV files",
        "option_b": "Chocolates",
        "option_c": "Shoes",
        "option_d": "Phones",
        "correct_answer": "A"
    },
    {
        "question_text": "Filters help in:",
        "option_a": "Focusing data",
        "option_b": "Focusing sound",
        "option_c": "Focusing light",
        "option_d": "Focusing cars",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI Service is:",
        "option_a": "Cloud platform",
        "option_b": "Shoe rack",
        "option_c": "Water tank",
        "option_d": "Car garage",
        "correct_answer": "A"
    },
    {
        "question_text": "Mobile view optimizes:",
        "option_a": "Reports",
        "option_b": "Movies",
        "option_c": "Games",
        "option_d": "Shoes",
        "correct_answer": "A"
    }
],
194: [
    {
        "question_text": "Tableau is a:",
        "option_a": "Data visualization tool",
        "option_b": "Bike tool",
        "option_c": "Room heater",
        "option_d": "Cup holder",
        "correct_answer": "A"
    },
    {
        "question_text": "Dashboards contain:",
        "option_a": "Charts",
        "option_b": "Shoes",
        "option_c": "Buses",
        "option_d": "Fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Tableau connects to:",
        "option_a": "Databases",
        "option_b": "Televisions",
        "option_c": "Doors",
        "option_d": "Toys",
        "correct_answer": "A"
    },
    {
        "question_text": "Filters help in:",
        "option_a": "Refining data",
        "option_b": "Refining oil",
        "option_c": "Refining wood",
        "option_d": "Refining glass",
        "correct_answer": "A"
    },
    {
        "question_text": "Calculated fields perform:",
        "option_a": "Custom calculations",
        "option_b": "Custom tailoring",
        "option_c": "Custom design",
        "option_d": "Custom repair",
        "correct_answer": "A"
    },
    {
        "question_text": "Story points create:",
        "option_a": "Presentations",
        "option_b": "Movies",
        "option_c": "Games",
        "option_d": "Songs",
        "correct_answer": "A"
    },
    {
        "question_text": "Tableau Public is:",
        "option_a": "Free platform",
        "option_b": "Free pizza",
        "option_c": "Free bike",
        "option_d": "Free shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Workbooks store:",
        "option_a": "Visuals",
        "option_b": "Fruits",
        "option_c": "Shoes",
        "option_d": "Glasses",
        "correct_answer": "A"
    },
    {
        "question_text": "Tableau extracts:",
        "option_a": "Store data",
        "option_b": "Store clothes",
        "option_c": "Store water",
        "option_d": "Store bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Maps are used for:",
        "option_a": "Geographical data",
        "option_b": "Musical data",
        "option_c": "Chemical data",
        "option_d": "Sports data",
        "correct_answer": "A"
    }
],
193: [
    {
        "question_text": "MongoDB stores data in:",
        "option_a": "Documents",
        "option_b": "Folders",
        "option_c": "Shoes",
        "option_d": "Cabinets",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB uses:",
        "option_a": "JSON-like data",
        "option_b": "SQL tables",
        "option_c": "Images",
        "option_d": "Videos",
        "correct_answer": "A"
    },
    {
        "question_text": "A collection contains:",
        "option_a": "Documents",
        "option_b": "Pencils",
        "option_c": "Phones",
        "option_d": "Keys",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "Music player",
        "option_c": "Web browser",
        "option_d": "Paint tool",
        "correct_answer": "A"
    },
    {
        "question_text": "find() is used to:",
        "option_a": "Retrieve data",
        "option_b": "Retrieve bikes",
        "option_c": "Retrieve cups",
        "option_d": "Retrieve chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "insertOne() adds:",
        "option_a": "A document",
        "option_b": "A painting",
        "option_c": "A carpet",
        "option_d": "A shirt",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB Compass is a:",
        "option_a": "GUI tool",
        "option_b": "Game",
        "option_c": "Bag",
        "option_d": "Fan",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is ideal for:",
        "option_a": "Flexible data",
        "option_b": "Frozen food",
        "option_c": "Hard metals",
        "option_d": "Heavy tools",
        "correct_answer": "A"
    },
    {
        "question_text": "ObjectID is a:",
        "option_a": "Unique identifier",
        "option_b": "Unique shoe",
        "option_c": "Unique box",
        "option_d": "Unique bottle",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB cluster improves:",
        "option_a": "Scaling",
        "option_b": "Tasting",
        "option_c": "Smelling",
        "option_d": "Sleeping",
        "correct_answer": "A"
    }
],
192: [
    {
        "question_text": "MySQL is a:",
        "option_a": "Relational database",
        "option_b": "Room heater",
        "option_c": "Paint brand",
        "option_d": "Milk product",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL uses:",
        "option_a": "Tables",
        "option_b": "Trees",
        "option_c": "Shoes",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "SELECT returns:",
        "option_a": "Data",
        "option_b": "Water",
        "option_c": "Air",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "WHERE filters:",
        "option_a": "Rows",
        "option_b": "Shoes",
        "option_c": "Walls",
        "option_d": "Posts",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL Workbench is a:",
        "option_a": "GUI tool",
        "option_b": "Cooking pan",
        "option_c": "TV remote",
        "option_d": "Electric heater",
        "correct_answer": "A"
    },
    {
        "question_text": "INSERT adds new:",
        "option_a": "Rows",
        "option_b": "Fans",
        "option_c": "Phones",
        "option_d": "Cups",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN merges:",
        "option_a": "Tables",
        "option_b": "Shoes",
        "option_c": "Belts",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL is:",
        "option_a": "Open-source",
        "option_b": "Hot sauce",
        "option_c": "Cold drink",
        "option_d": "Plastic",
        "correct_answer": "A"
    },
    {
        "question_text": "A query is a:",
        "option_a": "Request for data",
        "option_b": "Request for money",
        "option_c": "Request for food",
        "option_d": "Request for clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Normalization improves:",
        "option_a": "Database design",
        "option_b": "Painting design",
        "option_c": "Shoe design",
        "option_d": "Dress design",
        "correct_answer": "A"
    }
],
191: [
    {
        "question_text": "MongoDB stores data as:",
        "option_a": "Documents",
        "option_b": "Tables",
        "option_c": "Folders",
        "option_d": "Photos",
        "correct_answer": "A"
    },
    {
        "question_text": "The BSON format is:",
        "option_a": "Binary JSON",
        "option_b": "Image format",
        "option_c": "Audio format",
        "option_d": "Video format",
        "correct_answer": "A"
    },
    {
        "question_text": "A collection contains:",
        "option_a": "Multiple documents",
        "option_b": "Multiple tires",
        "option_c": "Multiple bags",
        "option_d": "Multiple tables",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is best for:",
        "option_a": "Unstructured data",
        "option_b": "Road construction",
        "option_c": "Sports training",
        "option_d": "Cooking classes",
        "correct_answer": "A"
    },
    {
        "question_text": "ObjectId is used as:",
        "option_a": "Unique identifier",
        "option_b": "Color code",
        "option_c": "Music key",
        "option_d": "Discount code",
        "correct_answer": "A"
    },
    {
        "question_text": "The command find() is used to:",
        "option_a": "Retrieve data",
        "option_b": "Remove data",
        "option_c": "Print photos",
        "option_d": "Open folders",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB Atlas is:",
        "option_a": "Cloud database service",
        "option_b": "Food delivery app",
        "option_c": "Smartphone",
        "option_d": "Video editing tool",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexing improves:",
        "option_a": "Query performance",
        "option_b": "Battery life",
        "option_c": "Photo clarity",
        "option_d": "Speaker volume",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB uses which query language?",
        "option_a": "Mongo query syntax",
        "option_b": "SQL",
        "option_c": "C#",
        "option_d": "Go",
        "correct_answer": "A"
    },
    {
        "question_text": "Aggregation is used for:",
        "option_a": "Data analysis",
        "option_b": "Music mixing",
        "option_c": "Movie editing",
        "option_d": "Road construction",
        "correct_answer": "A"
    }
],
190: [
    {
        "question_text": "MySQL is a:",
        "option_a": "Relational database",
        "option_b": "Photo editor",
        "option_c": "Cloud provider",
        "option_d": "Game engine",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL uses:",
        "option_a": "Tables",
        "option_b": "Folders",
        "option_c": "Shoes",
        "option_d": "Pipes",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary keys must be:",
        "option_a": "Unique",
        "option_b": "Tall",
        "option_c": "Brown",
        "option_d": "Circular",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN combines:",
        "option_a": "Two tables",
        "option_b": "Two shoes",
        "option_c": "Two cars",
        "option_d": "Two bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign key connects:",
        "option_a": "Tables",
        "option_b": "Fans",
        "option_c": "Markers",
        "option_d": "Switches",
        "correct_answer": "A"
    },
    {
        "question_text": "Normalization avoids:",
        "option_a": "Data duplication",
        "option_b": "Cold weather",
        "option_c": "Food spoilage",
        "option_d": "Battery drain",
        "correct_answer": "A"
    },
    {
        "question_text": "MySQL Workbench is:",
        "option_a": "GUI tool",
        "option_b": "Game",
        "option_c": "Car tool",
        "option_d": "TV remote",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes help in:",
        "option_a": "Fast searching",
        "option_b": "Fast running",
        "option_c": "Fast cooking",
        "option_d": "Fast printing",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL stands for:",
        "option_a": "Structured Query Language",
        "option_b": "Simple Quick Language",
        "option_c": "System Query Loop",
        "option_d": "Standard Quality Logic",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE command removes:",
        "option_a": "Records",
        "option_b": "Shoes",
        "option_c": "Phones",
        "option_d": "Caps",
        "correct_answer": "A"
    }
],
189: [
    {
        "question_text": "PostgreSQL is known for:",
        "option_a": "Advanced features",
        "option_b": "Bike riding",
        "option_c": "Cloud raining",
        "option_d": "Photo editing",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres supports:",
        "option_a": "JSON data",
        "option_b": "Video files",
        "option_c": "MP3 audio",
        "option_d": "PNG icons",
        "correct_answer": "A"
    },
    {
        "question_text": "ACID ensures:",
        "option_a": "Transaction reliability",
        "option_b": "Food temperature",
        "option_c": "Room decoration",
        "option_d": "Phone charging",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign keys connect:",
        "option_a": "Two tables",
        "option_b": "Two windows",
        "option_c": "Two shirts",
        "option_d": "Two fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Views store:",
        "option_a": "Saved queries",
        "option_b": "Saved photos",
        "option_c": "Saved songs",
        "option_d": "Saved shorts",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes improve:",
        "option_a": "Query speed",
        "option_b": "Walking speed",
        "option_c": "Wind speed",
        "option_d": "Bike speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres uses:",
        "option_a": "SQL",
        "option_b": "HTML",
        "option_c": "CSS",
        "option_d": "XML",
        "correct_answer": "A"
    },
    {
        "question_text": "A table row is a:",
        "option_a": "Record",
        "option_b": "Notebook",
        "option_c": "Lamp",
        "option_d": "Door",
        "correct_answer": "A"
    },
    {
        "question_text": "A schema is a:",
        "option_a": "Database structure",
        "option_b": "Kitchen structure",
        "option_c": "Gate structure",
        "option_d": "Room structure",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN merges:",
        "option_a": "Multiple tables",
        "option_b": "Multiple bags",
        "option_c": "Multiple shoes",
        "option_d": "Multiple caps",
        "correct_answer": "A"
    }
],
188: [
    {
        "question_text": "React is a:",
        "option_a": "JavaScript library",
        "option_b": "Bike brand",
        "option_c": "Phone cover",
        "option_d": "TV remote",
        "correct_answer": "A"
    },
    {
        "question_text": "React uses:",
        "option_a": "Components",
        "option_b": "Spices",
        "option_c": "Chairs",
        "option_d": "Bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "JSX allows mixing:",
        "option_a": "HTML + JS",
        "option_b": "Rice + Water",
        "option_c": "Oil + Paint",
        "option_d": "Shoes + Socks",
        "correct_answer": "A"
    },
    {
        "question_text": "State stores:",
        "option_a": "Component data",
        "option_b": "Food",
        "option_c": "Songs",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "useState is a:",
        "option_a": "Hook",
        "option_b": "Drink",
        "option_c": "Fan",
        "option_d": "Switch",
        "correct_answer": "A"
    },
    {
        "question_text": "Props are:",
        "option_a": "Inputs to components",
        "option_b": "Inputs to cars",
        "option_c": "Inputs to rooms",
        "option_d": "Inputs to bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Virtual DOM improves:",
        "option_a": "Performance",
        "option_b": "Cooking",
        "option_c": "Cleaning",
        "option_d": "Lighting",
        "correct_answer": "A"
    },
    {
        "question_text": "React apps are built with:",
        "option_a": "Components",
        "option_b": "Trees",
        "option_c": "Belts",
        "option_d": "Caps",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router enables:",
        "option_a": "Navigation",
        "option_b": "Painting",
        "option_c": "Driving",
        "option_d": "Shopping",
        "correct_answer": "A"
    },
    {
        "question_text": "React is developed by:",
        "option_a": "Facebook",
        "option_b": "Netflix",
        "option_c": "Amazon",
        "option_d": "Google",
        "correct_answer": "A"
    }
],
187: [
    {
        "question_text": "React Router is used for:",
        "option_a": "Navigation",
        "option_b": "Decoration",
        "option_c": "Communication",
        "option_d": "Calculation",
        "correct_answer": "A"
    },
    {
        "question_text": "A route defines:",
        "option_a": "A path in the app",
        "option_b": "A path in forest",
        "option_c": "A path on roof",
        "option_d": "A path in airport",
        "correct_answer": "A"
    },
    {
        "question_text": "BrowserRouter handles:",
        "option_a": "URL routing",
        "option_b": "TV channels",
        "option_c": "Fan speed",
        "option_d": "Room lights",
        "correct_answer": "A"
    },
    {
        "question_text": "useNavigate helps to:",
        "option_a": "Redirect pages",
        "option_b": "Redirect cars",
        "option_c": "Redirect water",
        "option_d": "Redirect air",
        "correct_answer": "A"
    },
    {
        "question_text": "Link component creates:",
        "option_a": "Clickable links",
        "option_b": "Clickable bottles",
        "option_c": "Clickable caps",
        "option_d": "Clickable shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Dynamic routes contain:",
        "option_a": "Parameters",
        "option_b": "Salt",
        "option_c": "Sugar",
        "option_d": "Stones",
        "correct_answer": "A"
    },
    {
        "question_text": "Nested routes allow:",
        "option_a": "Child components",
        "option_b": "Child chairs",
        "option_c": "Child tables",
        "option_d": "Child phones",
        "correct_answer": "A"
    },
    {
        "question_text": "useParams retrieves:",
        "option_a": "Route parameters",
        "option_b": "Food ingredients",
        "option_c": "Phone contacts",
        "option_d": "Game scores",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router supports:",
        "option_a": "SPA navigation",
        "option_b": "Bike navigation",
        "option_c": "Ship navigation",
        "option_d": "Plane navigation",
        "correct_answer": "A"
    },
    {
        "question_text": "Navigate replaces:",
        "option_a": "Window.location",
        "option_b": "Window curtain",
        "option_c": "Window lock",
        "option_d": "Window glass",
        "correct_answer": "A"
    }
],
186: [
    {
        "question_text": "Next.js is built on:",
        "option_a": "React",
        "option_b": "Angular",
        "option_c": "Vue",
        "option_d": "Svelte",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js supports:",
        "option_a": "Server-side rendering",
        "option_b": "Stone carving",
        "option_c": "Road building",
        "option_d": "Furniture polishing",
        "correct_answer": "A"
    },
    {
        "question_text": "Pages in Next.js are stored inside:",
        "option_a": "pages folder",
        "option_b": "public folder",
        "option_c": "images folder",
        "option_d": "videos folder",
        "correct_answer": "A"
    },
    {
        "question_text": "API routes start with:",
        "option_a": "/api",
        "option_b": "/food",
        "option_c": "/shoes",
        "option_d": "/bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Static generation builds pages at:",
        "option_a": "Build time",
        "option_b": "Lunch time",
        "option_c": "Tea time",
        "option_d": "Night time",
        "correct_answer": "A"
    },
    {
        "question_text": "Dynamic routes use:",
        "option_a": "Square brackets",
        "option_b": "Round bottles",
        "option_c": "Flat boxes",
        "option_d": "Blue lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js is ideal for:",
        "option_a": "SEO",
        "option_b": "Car repair",
        "option_c": "Bike washing",
        "option_d": "Painting walls",
        "correct_answer": "A"
    },
    {
        "question_text": "next/image handles:",
        "option_a": "Optimized images",
        "option_b": "Optimized rice",
        "option_c": "Optimized chairs",
        "option_d": "Optimized pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware runs:",
        "option_a": "Before request",
        "option_b": "Before lunch",
        "option_c": "Before exams",
        "option_d": "Before movies",
        "correct_answer": "A"
    },
    {
        "question_text": "Next.js exports apps as:",
        "option_a": "Static sites",
        "option_b": "Static bags",
        "option_c": "Static shirts",
        "option_d": "Static toys",
        "correct_answer": "A"
    }
],
185: [
    {
        "question_text": "Tailwind CSS is a:",
        "option_a": "Utility-first framework",
        "option_b": "Biscuit brand",
        "option_c": "Milk brand",
        "option_d": "Car brand",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind uses:",
        "option_a": "Classes",
        "option_b": "Buttons",
        "option_c": "Pipes",
        "option_d": "Switches",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind helps design:",
        "option_a": "UI quickly",
        "option_b": "Shoes quickly",
        "option_c": "Roads quickly",
        "option_d": "Rooms quickly",
        "correct_answer": "A"
    },
    {
        "question_text": "Responsive classes use:",
        "option_a": "sm, md, lg",
        "option_b": "xl, xxl, xxxl shirts",
        "option_c": "hot, warm, cold",
        "option_d": "slow, medium, fast",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind works with:",
        "option_a": "React",
        "option_b": "Photoshop",
        "option_c": "Excel",
        "option_d": "VS Code themes",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind CLI builds:",
        "option_a": "CSS files",
        "option_b": "Water bottles",
        "option_c": "Chairs",
        "option_d": "Mobile phones",
        "correct_answer": "A"
    },
    {
        "question_text": "Colors in Tailwind use:",
        "option_a": "color-name/shade",
        "option_b": "RGB only",
        "option_c": "Food colors",
        "option_d": "Car colors",
        "correct_answer": "A"
    },
    {
        "question_text": "Tailwind replaces:",
        "option_a": "Writing custom CSS",
        "option_b": "Writing books",
        "option_c": "Writing songs",
        "option_d": "Writing exams",
        "correct_answer": "A"
    },
    {
        "question_text": "Opacity classes control:",
        "option_a": "Transparency",
        "option_b": "Temperature",
        "option_c": "Taste",
        "option_d": "Volume",
        "correct_answer": "A"
    },
    {
        "question_text": "Spacing uses:",
        "option_a": "m- p- classes",
        "option_b": "kg- g- classes",
        "option_c": "km- cm- classes",
        "option_d": "l- ml- classes",
        "correct_answer": "A"
    }
],
184: [
    {
        "question_text": "JavaScript is:",
        "option_a": "A programming language",
        "option_b": "A food item",
        "option_c": "A painting style",
        "option_d": "A shoe brand",
        "correct_answer": "A"
    },
    {
        "question_text": "JS runs in:",
        "option_a": "Browser",
        "option_b": "Television",
        "option_c": "Refrigerator",
        "option_d": "Water tank",
        "correct_answer": "A"
    },
    {
        "question_text": "Variables store:",
        "option_a": "Values",
        "option_b": "Vegetables",
        "option_c": "Vehicles",
        "option_d": "Valves",
        "correct_answer": "A"
    },
    {
        "question_text": "Functions are:",
        "option_a": "Reusable code blocks",
        "option_b": "Reusable bottles",
        "option_c": "Reusable bags",
        "option_d": "Reusable lamps",
        "correct_answer": "A"
    },
    {
        "question_text": "Arrays store:",
        "option_a": "Multiple values",
        "option_b": "Multiple fans",
        "option_c": "Multiple chairs",
        "option_d": "Multiple shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Objects store:",
        "option_a": "Key-value pairs",
        "option_b": "Key-box pairs",
        "option_c": "Key-shoe pairs",
        "option_d": "Key-paper pairs",
        "correct_answer": "A"
    },
    {
        "question_text": "JS DOM manipulates:",
        "option_a": "HTML elements",
        "option_b": "Phones",
        "option_c": "Shoes",
        "option_d": "Speakers",
        "correct_answer": "A"
    },
    {
        "question_text": "Promises handle:",
        "option_a": "Async operations",
        "option_b": "Weddings",
        "option_c": "Meetings",
        "option_d": "Parties",
        "correct_answer": "A"
    },
    {
        "question_text": "console.log() prints:",
        "option_a": "Output",
        "option_b": "Books",
        "option_c": "Backpacks",
        "option_d": "Plants",
        "correct_answer": "A"
    },
    {
        "question_text": "JS is used for:",
        "option_a": "Web interactivity",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Running",
        "correct_answer": "A"
    }
],
183: [
    {
        "question_text": "TypeScript is:",
        "option_a": "A superset of JavaScript",
        "option_b": "A biscuit brand",
        "option_c": "A smartphone",
        "option_d": "A clothing style",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript adds:",
        "option_a": "Types",
        "option_b": "Water",
        "option_c": "Music",
        "option_d": "Smoke",
        "correct_answer": "A"
    },
    {
        "question_text": "The file extension is:",
        "option_a": ".ts",
        "option_b": ".txt",
        "option_c": ".mp3",
        "option_d": ".exe",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript helps catch:",
        "option_a": "Errors early",
        "option_b": "Fish early",
        "option_c": "Trains early",
        "option_d": "Buses early",
        "correct_answer": "A"
    },
    {
        "question_text": "Interfaces define:",
        "option_a": "Object shapes",
        "option_b": "Road shapes",
        "option_c": "Cloud shapes",
        "option_d": "Room shapes",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript compiles to:",
        "option_a": "JavaScript",
        "option_b": "Python",
        "option_c": "C++",
        "option_d": "Rust",
        "correct_answer": "A"
    },
    {
        "question_text": "Enums represent:",
        "option_a": "Constant values",
        "option_b": "Kitchen items",
        "option_c": "Bike parts",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "Optional chaining uses:",
        "option_a": "?.",
        "option_b": "+=",
        "option_c": "//",
        "option_d": "::",
        "correct_answer": "A"
    },
    {
        "question_text": "Type inference automatically:",
        "option_a": "Assigns types",
        "option_b": "Assigns drinks",
        "option_c": "Assigns shirts",
        "option_d": "Assigns fans",
        "correct_answer": "A"
    },
    {
        "question_text": "TS is used in:",
        "option_a": "Large apps",
        "option_b": "Large parties",
        "option_c": "Large malls",
        "option_d": "Large farms",
        "correct_answer": "A"
    }
],
182: [
    {
        "question_text": "Node.js runs on:",
        "option_a": "JavaScript",
        "option_b": "Java",
        "option_c": "Python",
        "option_d": "Rust",
        "correct_answer": "A"
    },
    {
        "question_text": "Node.js executes:",
        "option_a": "Server-side code",
        "option_b": "Laundry",
        "option_c": "Car servicing",
        "option_d": "Painting",
        "correct_answer": "A"
    },
    {
        "question_text": "npm manages:",
        "option_a": "Packages",
        "option_b": "Shoes",
        "option_c": "Bags",
        "option_d": "Phones",
        "correct_answer": "A"
    },
    {
        "question_text": "Express.js is a:",
        "option_a": "Backend framework",
        "option_b": "Shoe brand",
        "option_c": "Phone charger",
        "option_d": "Milk product",
        "correct_answer": "A"
    },
    {
        "question_text": "Node.js handles:",
        "option_a": "Async tasks",
        "option_b": "Haircuts",
        "option_c": "Driving",
        "option_d": "Cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "API stands for:",
        "option_a": "Application Programming Interface",
        "option_b": "Apple Pineapple Ice-cream",
        "option_c": "Automatic Power Input",
        "option_d": "Analog Power Indicator",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware processes:",
        "option_a": "Requests",
        "option_b": "Boxes",
        "option_c": "Tables",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Node uses:",
        "option_a": "Event loop",
        "option_b": "Water loop",
        "option_c": "Light loop",
        "option_d": "Fan loop",
        "correct_answer": "A"
    },
    {
        "question_text": "JSON is used for:",
        "option_a": "Data transfer",
        "option_b": "Water transfer",
        "option_c": "Air transfer",
        "option_d": "Heat transfer",
        "correct_answer": "A"
    },
    {
        "question_text": "Node.js is good for:",
        "option_a": "Real-time apps",
        "option_b": "Real-time cooking",
        "option_c": "Real-time painting",
        "option_d": "Real-time cleaning",
        "correct_answer": "A"
    }
],
181: [
    {
        "question_text": "Express.js is a:",
        "option_a": "Backend framework",
        "option_b": "Bike model",
        "option_c": "Camera lens",
        "option_d": "Toy brand",
        "correct_answer": "A"
    },
    {
        "question_text": "Express apps run on:",
        "option_a": "Node.js",
        "option_b": "Python",
        "option_c": "Java",
        "option_d": "C++",
        "correct_answer": "A"
    },
    {
        "question_text": "Routes define:",
        "option_a": "API endpoints",
        "option_b": "House plan",
        "option_c": "Garden shape",
        "option_d": "Shirt size",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware handles:",
        "option_a": "Requests",
        "option_b": "Shoes",
        "option_c": "Plates",
        "option_d": "Caps",
        "correct_answer": "A"
    },
    {
        "question_text": "req.body holds:",
        "option_a": "Incoming data",
        "option_b": "Shoelaces",
        "option_c": "Fruits",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Express uses:",
        "option_a": "JavaScript",
        "option_b": "Chocolate",
        "option_c": "Spices",
        "option_d": "Paper",
        "correct_answer": "A"
    },
    {
        "question_text": "REST APIs communicate via:",
        "option_a": "HTTP",
        "option_b": "Bluetooth",
        "option_c": "Infrared",
        "option_d": "Electricity",
        "correct_answer": "A"
    },
    {
        "question_text": "JSON is used for:",
        "option_a": "Data exchange",
        "option_b": "Music exchange",
        "option_c": "Food exchange",
        "option_d": "Clothes exchange",
        "correct_answer": "A"
    },
    {
        "question_text": "Express supports:",
        "option_a": "Middleware chaining",
        "option_b": "Song chaining",
        "option_c": "Chair chaining",
        "option_d": "Shoe chaining",
        "correct_answer": "A"
    },
    {
        "question_text": "res.send() sends:",
        "option_a": "Response",
        "option_b": "Shoes",
        "option_c": "Hats",
        "option_d": "Clocks",
        "correct_answer": "A"
    }
],
180: [
    {
        "question_text": "Full stack includes:",
        "option_a": "Frontend + Backend",
        "option_b": "Rice + Water",
        "option_c": "Bike + Helmet",
        "option_d": "Shirt + Pant",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend handles:",
        "option_a": "UI",
        "option_b": "Weather",
        "option_c": "Cooking",
        "option_d": "Car servicing",
        "correct_answer": "A"
    },
    {
        "question_text": "Backend handles:",
        "option_a": "Server logic",
        "option_b": "Shoes",
        "option_c": "Glass",
        "option_d": "Paint",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Bags",
        "option_c": "Phones",
        "option_d": "Flour",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs allow:",
        "option_a": "Communication",
        "option_b": "Decoration",
        "option_c": "Navigation",
        "option_d": "Rotation",
        "correct_answer": "A"
    },
    {
        "question_text": "HTML builds:",
        "option_a": "Structure",
        "option_b": "Food",
        "option_c": "Light",
        "option_d": "Sound",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS styles:",
        "option_a": "Webpages",
        "option_b": "Bags",
        "option_c": "Cars",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "JavaScript makes pages:",
        "option_a": "Interactive",
        "option_b": "Cold",
        "option_c": "Dark",
        "option_d": "Silent",
        "correct_answer": "A"
    },
    {
        "question_text": "Frameworks help in:",
        "option_a": "Faster development",
        "option_b": "Faster cooking",
        "option_c": "Faster running",
        "option_d": "Faster painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Full stack dev handles:",
        "option_a": "End-to-end development",
        "option_b": "End-to-end cleaning",
        "option_c": "End-to-end shopping",
        "option_d": "End-to-end walking",
        "correct_answer": "A"
    }
],
179: [
    {
        "question_text": "Machine learning teaches machines:",
        "option_a": "To learn from data",
        "option_b": "To cook food",
        "option_c": "To climb trees",
        "option_d": "To clean rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Supervised learning uses:",
        "option_a": "Labeled data",
        "option_b": "Heavy data",
        "option_c": "Cold data",
        "option_d": "Dark data",
        "correct_answer": "A"
    },
    {
        "question_text": "Regression predicts:",
        "option_a": "Numbers",
        "option_b": "Textures",
        "option_c": "Smells",
        "option_d": "Flavors",
        "correct_answer": "A"
    },
    {
        "question_text": "Classification predicts:",
        "option_a": "Categories",
        "option_b": "Rooms",
        "option_c": "Fruits",
        "option_d": "Cloths",
        "correct_answer": "A"
    },
    {
        "question_text": "Model training requires:",
        "option_a": "Data",
        "option_b": "Paint",
        "option_c": "Wires",
        "option_d": "Batteries",
        "correct_answer": "A"
    },
    {
        "question_text": "Testing checks:",
        "option_a": "Model accuracy",
        "option_b": "Food taste",
        "option_c": "Traffic speed",
        "option_d": "Rainfall",
        "correct_answer": "A"
    },
    {
        "question_text": "Neural networks mimic:",
        "option_a": "Human brain",
        "option_b": "Bird wings",
        "option_c": "Car engine",
        "option_d": "Cloud shapes",
        "correct_answer": "A"
    },
    {
        "question_text": "ML is used in:",
        "option_a": "Recommendations",
        "option_b": "Cooking",
        "option_c": "Painting",
        "option_d": "Driving bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Training data improves:",
        "option_a": "Model performance",
        "option_b": "Bike performance",
        "option_c": "Fan performance",
        "option_d": "Light performance",
        "correct_answer": "A"
    },
    {
        "question_text": "Python is popular for ML because:",
        "option_a": "Easy libraries",
        "option_b": "Easy flavors",
        "option_c": "Easy pillows",
        "option_d": "Easy bags",
        "correct_answer": "A"
    }
],
178: [
    {
        "question_text": "TensorFlow is a:",
        "option_a": "Deep learning framework",
        "option_b": "Game engine",
        "option_c": "Furniture store",
        "option_d": "Shoe brand",
        "correct_answer": "A"
    },
    {
        "question_text": "A tensor is:",
        "option_a": "Multi-dimensional data",
        "option_b": "Multi-dimensional shoes",
        "option_c": "Multi-dimensional bags",
        "option_d": "Multi-dimensional fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Neural networks contain:",
        "option_a": "Layers",
        "option_b": "Ropes",
        "option_c": "Chairs",
        "option_d": "Tables",
        "correct_answer": "A"
    },
    {
        "question_text": "Activation functions introduce:",
        "option_a": "Non-linearity",
        "option_b": "Spiciness",
        "option_c": "Coldness",
        "option_d": "Sharpness",
        "correct_answer": "A"
    },
    {
        "question_text": "Training improves:",
        "option_a": "Model accuracy",
        "option_b": "Shoe accuracy",
        "option_c": "Door accuracy",
        "option_d": "Fan accuracy",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorFlow is developed by:",
        "option_a": "Google",
        "option_b": "Samsung",
        "option_c": "Honda",
        "option_d": "Sony",
        "correct_answer": "A"
    },
    {
        "question_text": "CNNs are good for:",
        "option_a": "Image tasks",
        "option_b": "Laundry tasks",
        "option_c": "Cooking tasks",
        "option_d": "Washing tasks",
        "correct_answer": "A"
    },
    {
        "question_text": "RNNs are good for:",
        "option_a": "Sequence data",
        "option_b": "Glass data",
        "option_c": "Metal data",
        "option_d": "Ink data",
        "correct_answer": "A"
    },
    {
        "question_text": "TensorBoard visualizes:",
        "option_a": "Training metrics",
        "option_b": "Rain metrics",
        "option_c": "Wind metrics",
        "option_d": "Light metrics",
        "correct_answer": "A"
    },
    {
        "question_text": "Deep learning requires:",
        "option_a": "Large datasets",
        "option_b": "Large bags",
        "option_c": "Large pillows",
        "option_d": "Large rooms",
        "correct_answer": "A"
    }
],
177: [
    {
        "question_text": "PyTorch is a:",
        "option_a": "Deep learning framework",
        "option_b": "Shoe brand",
        "option_c": "Painting tool",
        "option_d": "Game console",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch uses:",
        "option_a": "Tensors",
        "option_b": "Legos",
        "option_c": "Nuts",
        "option_d": "Cables",
        "correct_answer": "A"
    },
    {
        "question_text": "Autograd handles:",
        "option_a": "Automatic gradients",
        "option_b": "Automatic cooking",
        "option_c": "Automatic parking",
        "option_d": "Automatic messaging",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch is developed by:",
        "option_a": "Meta",
        "option_b": "Apple",
        "option_c": "Sony",
        "option_d": "Honda",
        "correct_answer": "A"
    },
    {
        "question_text": "A neural network has:",
        "option_a": "Layers",
        "option_b": "Leaves",
        "option_c": "Branches",
        "option_d": "Wheels",
        "correct_answer": "A"
    },
    {
        "question_text": "Torchvision is used for:",
        "option_a": "Images",
        "option_b": "Water",
        "option_c": "Music",
        "option_d": "Paint",
        "correct_answer": "A"
    },
    {
        "question_text": "Training requires:",
        "option_a": "Data",
        "option_b": "Juice",
        "option_c": "Fuel",
        "option_d": "Air",
        "correct_answer": "A"
    },
    {
        "question_text": "Optimizers update:",
        "option_a": "Model weights",
        "option_b": "Bike tires",
        "option_c": "Phone covers",
        "option_d": "Shoe polish",
        "correct_answer": "A"
    },
    {
        "question_text": "RNNs are good for:",
        "option_a": "Sequences",
        "option_b": "Furniture",
        "option_c": "Paint",
        "option_d": "Glass",
        "correct_answer": "A"
    },
    {
        "question_text": "PyTorch supports:",
        "option_a": "Dynamic computation",
        "option_b": "Dynamic rainfall",
        "option_c": "Dynamic dancing",
        "option_d": "Dynamic cooking",
        "correct_answer": "A"
    }
],
176: [
    {
        "question_text": "DSA helps in:",
        "option_a": "Efficient coding",
        "option_b": "Efficient cooking",
        "option_c": "Efficient painting",
        "option_d": "Efficient sleeping",
        "correct_answer": "A"
    },
    {
        "question_text": "Python lists represent:",
        "option_a": "Arrays",
        "option_b": "Stairs",
        "option_c": "Chairs",
        "option_d": "Doors",
        "correct_answer": "A"
    },
    {
        "question_text": "A stack follows:",
        "option_a": "LIFO",
        "option_b": "FIFO",
        "option_c": "Circular",
        "option_d": "Random",
        "correct_answer": "A"
    },
    {
        "question_text": "A queue follows:",
        "option_a": "FIFO",
        "option_b": "LIFO",
        "option_c": "Reverse",
        "option_d": "Loop",
        "correct_answer": "A"
    },
    {
        "question_text": "A tree is:",
        "option_a": "Hierarchical",
        "option_b": "Flat",
        "option_c": "Round",
        "option_d": "Square",
        "correct_answer": "A"
    },
    {
        "question_text": "Graphs contain:",
        "option_a": "Nodes & edges",
        "option_b": "Doors & windows",
        "option_c": "Cups & plates",
        "option_d": "Fans & lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Searching finds:",
        "option_a": "An element",
        "option_b": "A friend",
        "option_c": "A tree",
        "option_d": "A shoe",
        "correct_answer": "A"
    },
    {
        "question_text": "Sorting arranges:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Pens",
        "option_d": "Boxes",
        "correct_answer": "A"
    },
    {
        "question_text": "Hashing uses:",
        "option_a": "Keys",
        "option_b": "Bags",
        "option_c": "Sticks",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Recursion means:",
        "option_a": "Function calling itself",
        "option_b": "Fan rotating itself",
        "option_c": "Tree watering itself",
        "option_d": "Car repairing itself",
        "correct_answer": "A"
    }
],
175: [
    {
        "question_text": "OOP stands for:",
        "option_a": "Object Oriented Programming",
        "option_b": "Orange Onion Pizza",
        "option_c": "Open Office Printer",
        "option_d": "Old Olympic Parade",
        "correct_answer": "A"
    },
    {
        "question_text": "A class defines:",
        "option_a": "Blueprint",
        "option_b": "Mountain",
        "option_c": "Car model",
        "option_d": "Tree shape",
        "correct_answer": "A"
    },
    {
        "question_text": "Objects are:",
        "option_a": "Instances of class",
        "option_b": "Instances of shoes",
        "option_c": "Instances of fruits",
        "option_d": "Instances of rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Constructor initializes:",
        "option_a": "Object",
        "option_b": "Table",
        "option_c": "Bike",
        "option_d": "Light",
        "correct_answer": "A"
    },
    {
        "question_text": "STL stands for:",
        "option_a": "Standard Template Library",
        "option_b": "Standard Tea Leaves",
        "option_c": "Standard Train Line",
        "option_d": "Standard Toy Lab",
        "correct_answer": "A"
    },
    {
        "question_text": "Vector is a:",
        "option_a": "Dynamic array",
        "option_b": "Dynamic bus",
        "option_c": "Dynamic tree",
        "option_d": "Dynamic bottle",
        "correct_answer": "A"
    },
    {
        "question_text": "Polymorphism allows:",
        "option_a": "Many forms",
        "option_b": "Many chairs",
        "option_c": "Many walls",
        "option_d": "Many clouds",
        "correct_answer": "A"
    },
    {
        "question_text": "Inheritance allows:",
        "option_a": "Reuse of code",
        "option_b": "Reuse of shoes",
        "option_c": "Reuse of clothes",
        "option_d": "Reuse of books",
        "correct_answer": "A"
    },
    {
        "question_text": "Encapsulation means:",
        "option_a": "Data hiding",
        "option_b": "Light hiding",
        "option_c": "Food hiding",
        "option_d": "Chair hiding",
        "correct_answer": "A"
    },
    {
        "question_text": "STL includes:",
        "option_a": "Algorithms & containers",
        "option_b": "Songs & videos",
        "option_c": "Shoes & socks",
        "option_d": "Brushes & paints",
        "correct_answer": "A"
    }
],
174: [
    {
        "question_text": "Spring Boot is used for:",
        "option_a": "Building Java backend apps",
        "option_b": "Cooking food",
        "option_c": "Repairing bikes",
        "option_d": "Editing videos",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot reduces:",
        "option_a": "Configuration effort",
        "option_b": "Electricity bill",
        "option_c": "Bike mileage",
        "option_d": "Room temperature",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot uses:",
        "option_a": "Annotations",
        "option_b": "Pencils",
        "option_c": "Stickers",
        "option_d": "Ribbons",
        "correct_answer": "A"
    },
    {
        "question_text": "REST APIs are built using:",
        "option_a": "@RestController",
        "option_b": "@Tree",
        "option_c": "@Photo",
        "option_d": "@Car",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot runs on:",
        "option_a": "Java",
        "option_b": "Clothes",
        "option_c": "Music",
        "option_d": "Appliances",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot supports:",
        "option_a": "Auto-configuration",
        "option_b": "Auto-painting",
        "option_c": "Auto-driving",
        "option_d": "Auto-sweeping",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot applications start with:",
        "option_a": "main()",
        "option_b": "open()",
        "option_c": "run()",
        "option_d": "cook()",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot uses:",
        "option_a": "Embedded servers",
        "option_b": "Embedded shoes",
        "option_c": "Embedded bottles",
        "option_d": "Embedded lamps",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot makes apps:",
        "option_a": "Production-ready",
        "option_b": "Water-ready",
        "option_c": "Music-ready",
        "option_d": "Food-ready",
        "correct_answer": "A"
    },
    {
        "question_text": "Spring Boot uses:",
        "option_a": "Dependencies",
        "option_b": "Fruits",
        "option_c": "Paint",
        "option_d": "Pillows",
        "correct_answer": "A"
    }
],
173: [
    {
        "question_text": "Laravel is a:",
        "option_a": "PHP framework",
        "option_b": "Car engine",
        "option_c": "Mobile OS",
        "option_d": "Headphone",
        "correct_answer": "A"
    },
    {
        "question_text": "Laravel uses:",
        "option_a": "Blade templates",
        "option_b": "Blade fans",
        "option_c": "Blade knives",
        "option_d": "Blade wheels",
        "correct_answer": "A"
    },
    {
        "question_text": "Routes define:",
        "option_a": "URL paths",
        "option_b": "Bus paths",
        "option_c": "River paths",
        "option_d": "Walking paths",
        "correct_answer": "A"
    },
    {
        "question_text": "Laravel follows:",
        "option_a": "MVC pattern",
        "option_b": "ABC pattern",
        "option_c": "XYZ pattern",
        "option_d": "MNO pattern",
        "correct_answer": "A"
    },
    {
        "question_text": "Migrations manage:",
        "option_a": "Database changes",
        "option_b": "Hair changes",
        "option_c": "Weather changes",
        "option_d": "Cloth changes",
        "correct_answer": "A"
    },
    {
        "question_text": "Eloquent ORM handles:",
        "option_a": "Database queries",
        "option_b": "Painting walls",
        "option_c": "Washing clothes",
        "option_d": "Driving cars",
        "correct_answer": "A"
    },
    {
        "question_text": "Controllers handle:",
        "option_a": "Logic",
        "option_b": "Cooking",
        "option_c": "Dancing",
        "option_d": "Singing",
        "correct_answer": "A"
    },
    {
        "question_text": "Laravel uses:",
        "option_a": "Composer",
        "option_b": "Decomposer",
        "option_c": "Recomposer",
        "option_d": "Comfy chair",
        "correct_answer": "A"
    },
    {
        "question_text": "Middleware filters:",
        "option_a": "Requests",
        "option_b": "Water",
        "option_c": "Air",
        "option_d": "Food",
        "correct_answer": "A"
    },
    {
        "question_text": "Laravel supports:",
        "option_a": "Authentication",
        "option_b": "Accommodation",
        "option_c": "Decoration",
        "option_d": "Celebration",
        "correct_answer": "A"
    }
],
172: [
    {
        "question_text": "Blockchain stores data in:",
        "option_a": "Blocks",
        "option_b": "Bats",
        "option_c": "Keys",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Blockchain is:",
        "option_a": "Decentralized",
        "option_b": "Centralized",
        "option_c": "Digital-only",
        "option_d": "Offline-only",
        "correct_answer": "A"
    },
    {
        "question_text": "Bitcoin uses:",
        "option_a": "Blockchain",
        "option_b": "Stone chain",
        "option_c": "Tree chain",
        "option_d": "Air chain",
        "correct_answer": "A"
    },
    {
        "question_text": "Blocks contain:",
        "option_a": "Transactions",
        "option_b": "Furniture",
        "option_c": "Food",
        "option_d": "Songs",
        "correct_answer": "A"
    },
    {
        "question_text": "A ledger is:",
        "option_a": "A record",
        "option_b": "A sofa",
        "option_c": "A bag",
        "option_d": "A charger",
        "correct_answer": "A"
    },
    {
        "question_text": "Nodes maintain:",
        "option_a": "Network",
        "option_b": "Kitchen",
        "option_c": "Bathroom",
        "option_d": "Garden",
        "correct_answer": "A"
    },
    {
        "question_text": "Hashing ensures:",
        "option_a": "Security",
        "option_b": "Electricity",
        "option_c": "Water",
        "option_d": "Air",
        "correct_answer": "A"
    },
    {
        "question_text": "Mining validates:",
        "option_a": "Transactions",
        "option_b": "Clothes",
        "option_c": "Shoes",
        "option_d": "Tables",
        "correct_answer": "A"
    },
    {
        "question_text": "Smart contracts run on:",
        "option_a": "Blockchain",
        "option_b": "Notebooks",
        "option_c": "Files",
        "option_d": "Clouds",
        "correct_answer": "A"
    },
    {
        "question_text": "Blockchain prevents:",
        "option_a": "Tampering",
        "option_b": "Sleeping",
        "option_c": "Eating",
        "option_d": "Walking",
        "correct_answer": "A"
    }
],
171: [
    {
        "question_text": "Unity is used for:",
        "option_a": "Game development",
        "option_b": "Car washing",
        "option_c": "Room painting",
        "option_d": "Bike repairing",
        "correct_answer": "A"
    },
    {
        "question_text": "Unity supports:",
        "option_a": "2D & 3D games",
        "option_b": "2D & 3D cooking",
        "option_c": "2D & 3D washing",
        "option_d": "2D & 3D shopping",
        "correct_answer": "A"
    },
    {
        "question_text": "Unity uses:",
        "option_a": "C#",
        "option_b": "Python",
        "option_c": "Java",
        "option_d": "C",
        "correct_answer": "A"
    },
    {
        "question_text": "The Unity Editor helps build:",
        "option_a": "Scenes",
        "option_b": "Tables",
        "option_c": "Pillows",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "GameObjects represent:",
        "option_a": "Items in a scene",
        "option_b": "Food items",
        "option_c": "Clothing items",
        "option_d": "Kitchen items",
        "correct_answer": "A"
    },
    {
        "question_text": "Assets include:",
        "option_a": "Models & textures",
        "option_b": "Books & pens",
        "option_c": "Shoes & socks",
        "option_d": "Cars & trucks",
        "correct_answer": "A"
    },
    {
        "question_text": "Prefabs are:",
        "option_a": "Reusable objects",
        "option_b": "Reusable notebooks",
        "option_c": "Reusable clothes",
        "option_d": "Reusable plates",
        "correct_answer": "A"
    },
    {
        "question_text": "Colliders detect:",
        "option_a": "Collision",
        "option_b": "Noise",
        "option_c": "Heat",
        "option_d": "Light",
        "correct_answer": "A"
    },
    {
        "question_text": "Unity builds games for:",
        "option_a": "Multiple platforms",
        "option_b": "Multiple kitchens",
        "option_c": "Multiple malls",
        "option_d": "Multiple bedrooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Animations make scenes:",
        "option_a": "Dynamic",
        "option_b": "Static",
        "option_c": "Dirty",
        "option_d": "Frozen",
        "correct_answer": "A"
    }
],
170: [
    {
        "question_text": "Unreal Engine is used for:",
        "option_a": "High-end game development",
        "option_b": "Ironing clothes",
        "option_c": "Boiling water",
        "option_d": "Filling bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal uses:",
        "option_a": "Blueprints",
        "option_b": "Pinkprints",
        "option_c": "Greenprints",
        "option_d": "Woodprints",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal provides:",
        "option_a": "Realistic graphics",
        "option_b": "Realistic tea",
        "option_c": "Realistic pillows",
        "option_d": "Realistic shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "C++ is commonly used with:",
        "option_a": "Unreal Engine",
        "option_b": "Comic books",
        "option_c": "Coffee shops",
        "option_d": "TV brands",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal Editor helps build:",
        "option_a": "Levels",
        "option_b": "Beds",
        "option_c": "Cars",
        "option_d": "Phones",
        "correct_answer": "A"
    },
    {
        "question_text": "Physics engine handles:",
        "option_a": "Real-world behavior",
        "option_b": "Cloud behavior",
        "option_c": "Fruit behavior",
        "option_d": "Shoe behavior",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal supports:",
        "option_a": "Cinematic rendering",
        "option_b": "Cinematic cooking",
        "option_c": "Cinematic cleaning",
        "option_d": "Cinematic sleeping",
        "correct_answer": "A"
    },
    {
        "question_text": "Blueprints allow:",
        "option_a": "Visual scripting",
        "option_b": "Visual eating",
        "option_c": "Visual drinking",
        "option_d": "Visual ironing",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal builds for:",
        "option_a": "Games & simulations",
        "option_b": "Shopping marts",
        "option_c": "Car garages",
        "option_d": "Airports",
        "correct_answer": "A"
    },
    {
        "question_text": "Unreal Engine excels in:",
        "option_a": "Graphics quality",
        "option_b": "Food quality",
        "option_c": "Shoe quality",
        "option_d": "Paper quality",
        "correct_answer": "A"
    }
],
169: [
    {
        "question_text": "Godot is:",
        "option_a": "A game engine",
        "option_b": "A washing machine",
        "option_c": "A torch",
        "option_d": "A mobile phone",
        "correct_answer": "A"
    },
    {
        "question_text": "Godot uses:",
        "option_a": "GDScript",
        "option_b": "GDWater",
        "option_c": "GDFire",
        "option_d": "GDTrees",
        "correct_answer": "A"
    },
    {
        "question_text": "Godot supports:",
        "option_a": "2D & 3D games",
        "option_b": "2D & 3D snacks",
        "option_c": "2D & 3D clothes",
        "option_d": "2D & 3D phones",
        "correct_answer": "A"
    },
    {
        "question_text": "Scenes contain:",
        "option_a": "Nodes",
        "option_b": "Pillows",
        "option_c": "Tables",
        "option_d": "Plates",
        "correct_answer": "A"
    },
    {
        "question_text": "Animations add:",
        "option_a": "Movement",
        "option_b": "Food",
        "option_c": "Noise",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "Godot is known for:",
        "option_a": "Lightweight design",
        "option_b": "Heavy weight lifting",
        "option_c": "Heavy rain",
        "option_d": "Heavy bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Signals support:",
        "option_a": "Communication",
        "option_b": "Decoration",
        "option_c": "Fluctuation",
        "option_d": "Evaporation",
        "correct_answer": "A"
    },
    {
        "question_text": "Godot is:",
        "option_a": "Open-source",
        "option_b": "Closed-source",
        "option_c": "Paid-only",
        "option_d": "Subscription-only",
        "correct_answer": "A"
    },
    {
        "question_text": "Scripts control:",
        "option_a": "Behavior",
        "option_b": "Flavor",
        "option_c": "Color",
        "option_d": "Noise",
        "correct_answer": "A"
    },
    {
        "question_text": "Godot exports to:",
        "option_a": "Many platforms",
        "option_b": "Many gardens",
        "option_c": "Many rivers",
        "option_d": "Many trees",
        "correct_answer": "A"
    }
],
168: [
    {
        "question_text": "Python is used for:",
        "option_a": "General-purpose programming",
        "option_b": "Washing clothes",
        "option_c": "Building drones",
        "option_d": "Cleaning windows",
        "correct_answer": "A"
    },
    {
        "question_text": "Python syntax is:",
        "option_a": "Easy to learn",
        "option_b": "Hard to paint",
        "option_c": "Hard to cook",
        "option_d": "Hard to drive",
        "correct_answer": "A"
    },
    {
        "question_text": "Variables store:",
        "option_a": "Values",
        "option_b": "Shoes",
        "option_c": "Books",
        "option_d": "Rain",
        "correct_answer": "A"
    },
    {
        "question_text": "Lists store:",
        "option_a": "Multiple items",
        "option_b": "Multiple lamps",
        "option_c": "Multiple caps",
        "option_d": "Multiple spoons",
        "correct_answer": "A"
    },
    {
        "question_text": "Functions are defined with:",
        "option_a": "def",
        "option_b": "fun",
        "option_c": "make",
        "option_d": "init",
        "correct_answer": "A"
    },
    {
        "question_text": "Input is taken using:",
        "option_a": "input()",
        "option_b": "take()",
        "option_c": "collect()",
        "option_d": "grab()",
        "correct_answer": "A"
    },
    {
        "question_text": "Loops help in:",
        "option_a": "Repeating tasks",
        "option_b": "Repeating songs",
        "option_c": "Repeating fights",
        "option_d": "Repeating rain",
        "correct_answer": "A"
    },
    {
        "question_text": "Comments start with:",
        "option_a": "#",
        "option_b": "@",
        "option_c": "&",
        "option_d": "%",
        "correct_answer": "A"
    },
    {
        "question_text": "Dictionaries store:",
        "option_a": "Key-value pairs",
        "option_b": "Key-shoes",
        "option_c": "Key-books",
        "option_d": "Key-trees",
        "correct_answer": "A"
    },
    {
        "question_text": "Python is known for:",
        "option_a": "Simplicity",
        "option_b": "Spiciness",
        "option_c": "Loudness",
        "option_d": "Heaviness",
        "correct_answer": "A"
    }
],
167: [
    {
        "question_text": "Django is a:",
        "option_a": "Python web framework",
        "option_b": "Bike brand",
        "option_c": "Coffee brand",
        "option_d": "Phone brand",
        "correct_answer": "A"
    },
    {
        "question_text": "Django follows:",
        "option_a": "MVT pattern",
        "option_b": "ABC pattern",
        "option_c": "XYZ pattern",
        "option_d": "AAA pattern",
        "correct_answer": "A"
    },
    {
        "question_text": "Models represent:",
        "option_a": "Database tables",
        "option_b": "Table fans",
        "option_c": "Table lamps",
        "option_d": "Table cloths",
        "correct_answer": "A"
    },
    {
        "question_text": "Views contain:",
        "option_a": "Business logic",
        "option_b": "Garden plants",
        "option_c": "Room paint",
        "option_d": "Car seats",
        "correct_answer": "A"
    },
    {
        "question_text": "URLs route to:",
        "option_a": "Views",
        "option_b": "Buildings",
        "option_c": "Banks",
        "option_d": "Hotels",
        "correct_answer": "A"
    },
    {
        "question_text": "Templates contain:",
        "option_a": "HTML",
        "option_b": "Wood",
        "option_c": "Glass",
        "option_d": "Stone",
        "correct_answer": "A"
    },
    {
        "question_text": "Django admin manages:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Pens",
        "option_d": "Trees",
        "correct_answer": "A"
    },
    {
        "question_text": "ORM stands for:",
        "option_a": "Object Relational Mapping",
        "option_b": "Object Road Mapping",
        "option_c": "Open Road Machine",
        "option_d": "Online Reading Material",
        "correct_answer": "A"
    },
    {
        "question_text": "Django is:",
        "option_a": "Secure",
        "option_b": "Weak",
        "option_c": "Slow",
        "option_d": "Broken",
        "correct_answer": "A"
    },
    {
        "question_text": "Django apps are:",
        "option_a": "Modular",
        "option_b": "Metal",
        "option_c": "Liquid",
        "option_d": "Wooden",
        "correct_answer": "A"
    }
],
166: [
    {
        "question_text": "React is used for:",
        "option_a": "Building UI",
        "option_b": "Building doors",
        "option_c": "Building pipes",
        "option_d": "Building scooters",
        "correct_answer": "A"
    },
    {
        "question_text": "Hooks allow:",
        "option_a": "Functional components to use state",
        "option_b": "Bikes to use petrol",
        "option_c": "Cars to use fans",
        "option_d": "Shoes to use laces",
        "correct_answer": "A"
    },
    {
        "question_text": "Redux manages:",
        "option_a": "Global state",
        "option_b": "Global traffic",
        "option_c": "Global heat",
        "option_d": "Global food",
        "correct_answer": "A"
    },
    {
        "question_text": "Memoization helps:",
        "option_a": "Performance",
        "option_b": "Cooking",
        "option_c": "Washing",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Props are:",
        "option_a": "Inputs",
        "option_b": "Outputs",
        "option_c": "Clothes",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Context API avoids:",
        "option_a": "Prop drilling",
        "option_b": "Food drilling",
        "option_c": "Road drilling",
        "option_d": "Water drilling",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router manages:",
        "option_a": "Navigation",
        "option_b": "Decoration",
        "option_c": "Construction",
        "option_d": "Electricity",
        "correct_answer": "A"
    },
    {
        "question_text": "useEffect handles:",
        "option_a": "Side effects",
        "option_b": "Side dishes",
        "option_c": "Side mirrors",
        "option_d": "Side stands",
        "correct_answer": "A"
    },
    {
        "question_text": "JSX combines:",
        "option_a": "JS & HTML",
        "option_b": "Soap & water",
        "option_c": "Milk & tea",
        "option_d": "Ink & paper",
        "correct_answer": "A"
    },
    {
        "question_text": "Virtual DOM improves:",
        "option_a": "Speed",
        "option_b": "Taste",
        "option_c": "Color",
        "option_d": "Sound",
        "correct_answer": "A"
    }
],
165: [
    {
        "question_text": "JavaScript is used for:",
        "option_a": "Web interactivity",
        "option_b": "Drying clothes",
        "option_c": "Boiling water",
        "option_d": "Fixing bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "JS runs in:",
        "option_a": "Browsers",
        "option_b": "Refrigerators",
        "option_c": "Washing machines",
        "option_d": "Headphones",
        "correct_answer": "A"
    },
    {
        "question_text": "Objects represent:",
        "option_a": "Key-value data",
        "option_b": "Key-door data",
        "option_c": "Key-shirt data",
        "option_d": "Key-pillow data",
        "correct_answer": "A"
    },
    {
        "question_text": "The DOM allows:",
        "option_a": "HTML manipulation",
        "option_b": "Shoe polishing",
        "option_c": "Tree planting",
        "option_d": "Pet training",
        "correct_answer": "A"
    },
    {
        "question_text": "Promises handle:",
        "option_a": "Asynchronous operations",
        "option_b": "Dinner operations",
        "option_c": "Room operations",
        "option_d": "Garden operations",
        "correct_answer": "A"
    },
    {
        "question_text": "Functions allow:",
        "option_a": "Reusable code",
        "option_b": "Reusable shirts",
        "option_c": "Reusable bottles",
        "option_d": "Reusable pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Arrow functions are:",
        "option_a": "Shorter syntax",
        "option_b": "Longer syntax",
        "option_c": "Broken syntax",
        "option_d": "Heavy syntax",
        "correct_answer": "A"
    },
    {
        "question_text": "Event listeners detect:",
        "option_a": "User actions",
        "option_b": "Dog actions",
        "option_c": "Weather actions",
        "option_d": "Bird actions",
        "correct_answer": "A"
    },
    {
        "question_text": "JS arrays store:",
        "option_a": "Multiple values",
        "option_b": "Multiple batteries",
        "option_c": "Multiple hats",
        "option_d": "Multiple cups",
        "correct_answer": "A"
    },
    {
        "question_text": "JSON stands for:",
        "option_a": "JavaScript Object Notation",
        "option_b": "JavaScript Orange Nut",
        "option_c": "JavaScript Onion Note",
        "option_d": "JavaScript Oven Name",
        "correct_answer": "A"
    }
],
164: [
    {
        "question_text": "TypeScript is:",
        "option_a": "A typed superset of JavaScript",
        "option_b": "A fruit juice",
        "option_c": "A cooking method",
        "option_d": "A shoe polish",
        "correct_answer": "A"
    },
    {
        "question_text": "TS files end with:",
        "option_a": ".ts",
        "option_b": ".txt",
        "option_c": ".exe",
        "option_d": ".pdf",
        "correct_answer": "A"
    },
    {
        "question_text": "Interfaces define:",
        "option_a": "Object structure",
        "option_b": "Tower structure",
        "option_c": "Tree structure",
        "option_d": "Shoe structure",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript improves:",
        "option_a": "Code safety",
        "option_b": "Room safety",
        "option_c": "Car safety",
        "option_d": "Water safety",
        "correct_answer": "A"
    },
    {
        "question_text": "Enums represent:",
        "option_a": "Fixed values",
        "option_b": "Fixed plates",
        "option_c": "Fixed boxes",
        "option_d": "Fixed caps",
        "correct_answer": "A"
    },
    {
        "question_text": "Generics help with:",
        "option_a": "Reusable types",
        "option_b": "Reusable fans",
        "option_c": "Reusable bags",
        "option_d": "Reusable jars",
        "correct_answer": "A"
    },
    {
        "question_text": "TS compiles to:",
        "option_a": "JavaScript",
        "option_b": "Ruby",
        "option_c": "PHP",
        "option_d": "Swift",
        "correct_answer": "A"
    },
    {
        "question_text": "Type inference means TS:",
        "option_a": "Guesses the type",
        "option_b": "Guesses the weather",
        "option_c": "Guesses the food",
        "option_d": "Guesses the clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "TS reduces:",
        "option_a": "Runtime errors",
        "option_b": "Power errors",
        "option_c": "Water errors",
        "option_d": "Sound errors",
        "correct_answer": "A"
    },
    {
        "question_text": "TS is widely used in:",
        "option_a": "Large projects",
        "option_b": "Large kitchens",
        "option_c": "Large malls",
        "option_d": "Large parks",
        "correct_answer": "A"
    }
],
163: [
    {
        "question_text": "Full stack includes:",
        "option_a": "Frontend + Backend",
        "option_b": "Shirt + Pant",
        "option_c": "Bike + Helmet",
        "option_d": "Tea + Biscuit",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend handles:",
        "option_a": "UI",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Planting",
        "correct_answer": "A"
    },
    {
        "question_text": "Backend handles:",
        "option_a": "Server logic",
        "option_b": "Room logic",
        "option_c": "Shoe logic",
        "option_d": "Bag logic",
        "correct_answer": "A"
    },
    {
        "question_text": "HTML builds:",
        "option_a": "Structure",
        "option_b": "Water",
        "option_c": "Plastic",
        "option_d": "Metal",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS styles:",
        "option_a": "Webpages",
        "option_b": "Wood",
        "option_c": "Glass",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "JavaScript adds:",
        "option_a": "Interactivity",
        "option_b": "Sugar",
        "option_c": "Salt",
        "option_d": "Air",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs help with:",
        "option_a": "Communication",
        "option_b": "Calculation",
        "option_c": "Decoration",
        "option_d": "Circulation",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Paint",
        "option_d": "Boxes",
        "correct_answer": "A"
    },
    {
        "question_text": "Frameworks help:",
        "option_a": "Speed up development",
        "option_b": "Speed up cooking",
        "option_c": "Speed up walking",
        "option_d": "Speed up running",
        "correct_answer": "A"
    },
    {
        "question_text": "Full stack dev handles:",
        "option_a": "End-to-end development",
        "option_b": "End-to-end cooking",
        "option_c": "End-to-end laundry",
        "option_d": "End-to-end shopping",
        "correct_answer": "A"
    }
],
162: [
    {
        "question_text": "SQL stands for:",
        "option_a": "Structured Query Language",
        "option_b": "Simple Quick Language",
        "option_c": "System Query Logic",
        "option_d": "Strong Query Launcher",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL is used for:",
        "option_a": "Database management",
        "option_b": "Cooking vegetables",
        "option_c": "Painting walls",
        "option_d": "Training dogs",
        "correct_answer": "A"
    },
    {
        "question_text": "SELECT is used to:",
        "option_a": "Fetch data",
        "option_b": "Fetch chairs",
        "option_c": "Fetch shoes",
        "option_d": "Fetch bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "INSERT adds:",
        "option_a": "New data",
        "option_b": "New pillows",
        "option_c": "New cups",
        "option_d": "New bulbs",
        "correct_answer": "A"
    },
    {
        "question_text": "UPDATE modifies:",
        "option_a": "Existing data",
        "option_b": "Existing shoes",
        "option_c": "Existing tables",
        "option_d": "Existing bags",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE removes:",
        "option_a": "Records",
        "option_b": "Clouds",
        "option_c": "Papers",
        "option_d": "Birds",
        "correct_answer": "A"
    },
    {
        "question_text": "WHERE filters:",
        "option_a": "Rows",
        "option_b": "Air",
        "option_c": "Water",
        "option_d": "Sound",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary key uniquely identifies:",
        "option_a": "A record",
        "option_b": "A tree",
        "option_c": "A shoe",
        "option_d": "A road",
        "correct_answer": "A"
    },
    {
        "question_text": "Tables store:",
        "option_a": "Structured data",
        "option_b": "Structured chairs",
        "option_c": "Structured bricks",
        "option_d": "Structured fans",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL is used in:",
        "option_a": "Most applications",
        "option_b": "Most kitchens",
        "option_c": "Most gardens",
        "option_d": "Most gyms",
        "correct_answer": "A"
    }
],
161: [
    {
        "question_text": "JOIN combines:",
        "option_a": "Data from multiple tables",
        "option_b": "Shoes from multiple shops",
        "option_c": "Foods from multiple hotels",
        "option_d": "Cars from multiple garages",
        "correct_answer": "A"
    },
    {
        "question_text": "INDEX improves:",
        "option_a": "Query speed",
        "option_b": "Bike speed",
        "option_c": "Fan speed",
        "option_d": "Car speed",
        "correct_answer": "A"
    },
    {
        "question_text": "GROUP BY is used for:",
        "option_a": "Aggregation",
        "option_b": "Navigation",
        "option_c": "Decoration",
        "option_d": "Celebration",
        "correct_answer": "A"
    },
    {
        "question_text": "HAVING filters:",
        "option_a": "Groups",
        "option_b": "Rooms",
        "option_c": "Shoes",
        "option_d": "Trees",
        "correct_answer": "A"
    },
    {
        "question_text": "A subquery is:",
        "option_a": "A query inside another query",
        "option_b": "A bottle inside another bottle",
        "option_c": "A table inside another table",
        "option_d": "A phone inside another phone",
        "correct_answer": "A"
    },
    {
        "question_text": "ACID ensures:",
        "option_a": "Transaction reliability",
        "option_b": "Water reliability",
        "option_c": "Fan reliability",
        "option_d": "Door reliability",
        "correct_answer": "A"
    },
    {
        "question_text": "Views store:",
        "option_a": "Virtual tables",
        "option_b": "Virtual shoes",
        "option_c": "Virtual fans",
        "option_d": "Virtual cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Triggers run:",
        "option_a": "Automatically",
        "option_b": "Manually",
        "option_c": "Slowly",
        "option_d": "Rarely",
        "correct_answer": "A"
    },
    {
        "question_text": "Normalization avoids:",
        "option_a": "Data duplication",
        "option_b": "Cloth duplication",
        "option_c": "Bag duplication",
        "option_d": "Plate duplication",
        "correct_answer": "A"
    },
    {
        "question_text": "Stored procedures:",
        "option_a": "Reuse logic",
        "option_b": "Reuse bottles",
        "option_c": "Reuse shirts",
        "option_d": "Reuse papers",
        "correct_answer": "A"
    }
],
160: [
    {
        "question_text": "PostgreSQL is a:",
        "option_a": "Relational database",
        "option_b": "Fish tank",
        "option_c": "Coffee grinder",
        "option_d": "TV brand",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres supports:",
        "option_a": "JSON data",
        "option_b": "Hot tea",
        "option_c": "Cold air",
        "option_d": "Balloons",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL is known for:",
        "option_a": "Reliability",
        "option_b": "Spiciness",
        "option_c": "Softness",
        "option_d": "Brightness",
        "correct_answer": "A"
    },
    {
        "question_text": "Schemas help in:",
        "option_a": "Organizing tables",
        "option_b": "Organizing shirts",
        "option_c": "Organizing caps",
        "option_d": "Organizing bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Extensions add:",
        "option_a": "Extra features",
        "option_b": "Extra sugar",
        "option_c": "Extra leaves",
        "option_d": "Extra soil",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign keys maintain:",
        "option_a": "Relationships",
        "option_b": "Temperatures",
        "option_c": "Weights",
        "option_d": "Distances",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes speed up:",
        "option_a": "Queries",
        "option_b": "Walking",
        "option_c": "Sleeping",
        "option_d": "Eating",
        "correct_answer": "A"
    },
    {
        "question_text": "Postgres CLI command is:",
        "option_a": "psql",
        "option_b": "pgopen",
        "option_c": "runpg",
        "option_d": "sqlpg",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL supports:",
        "option_a": "Triggers",
        "option_b": "Umbrellas",
        "option_c": "Microwaves",
        "option_d": "Clippers",
        "correct_answer": "A"
    },
    {
        "question_text": "CTEs start with:",
        "option_a": "WITH",
        "option_b": "SET",
        "option_c": "FROM",
        "option_d": "SHOW",
        "correct_answer": "A"
    }
],
159: [
    {
        "question_text": "MongoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "Bike battery",
        "option_c": "Room heater",
        "option_d": "Gaming mouse",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores data as:",
        "option_a": "Documents",
        "option_b": "Plates",
        "option_c": "Shoes",
        "option_d": "Fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB uses:",
        "option_a": "Collections",
        "option_b": "Refrigerators",
        "option_c": "Pillows",
        "option_d": "Cars",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores data in:",
        "option_a": "JSON-like format",
        "option_b": "Plastic format",
        "option_c": "Metal format",
        "option_d": "Paper format",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB scales:",
        "option_a": "Horizontally",
        "option_b": "Vertically",
        "option_c": "Downwards",
        "option_d": "Sideways",
        "correct_answer": "A"
    },
    {
        "question_text": "Mongo shell command is:",
        "option_a": "mongo",
        "option_b": "dbshell",
        "option_c": "mongorun",
        "option_d": "startmongo",
        "correct_answer": "A"
    },
    {
        "question_text": "Documents contain:",
        "option_a": "Key-value pairs",
        "option_b": "Knife-spoon pairs",
        "option_c": "Chair-table pairs",
        "option_d": "Fan-light pairs",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is good for:",
        "option_a": "Unstructured data",
        "option_b": "Cold data",
        "option_c": "Hot data",
        "option_d": "Bright data",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB supports:",
        "option_a": "Sharding",
        "option_b": "Sharpening",
        "option_c": "Shaping",
        "option_d": "Shocking",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes improve:",
        "option_a": "Query performance",
        "option_b": "Room performance",
        "option_c": "Bike performance",
        "option_d": "Shoe performance",
        "correct_answer": "A"
    }
],
158: [
    {
        "question_text": "Docker is used for:",
        "option_a": "Containerization",
        "option_b": "Decoration",
        "option_c": "Navigation",
        "option_d": "Celebration",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker images are:",
        "option_a": "Blueprints for containers",
        "option_b": "Blueprints for houses",
        "option_c": "Blueprints for cars",
        "option_d": "Blueprints for shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker containers run:",
        "option_a": "Applications",
        "option_b": "Cars",
        "option_c": "Fans",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Dockerfile defines:",
        "option_a": "Image instructions",
        "option_b": "Recipe instructions",
        "option_c": "Dance instructions",
        "option_d": "Driving instructions",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker Hub stores:",
        "option_a": "Public images",
        "option_b": "Public clothes",
        "option_c": "Public toys",
        "option_d": "Public bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker uses:",
        "option_a": "Containers",
        "option_b": "Buses",
        "option_c": "Bags",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Volume stores:",
        "option_a": "Persistent data",
        "option_b": "Persistent books",
        "option_c": "Persistent caps",
        "option_d": "Persistent shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "docker ps lists:",
        "option_a": "Running containers",
        "option_b": "Running shoes",
        "option_c": "Running children",
        "option_d": "Running engines",
        "correct_answer": "A"
    },
    {
        "question_text": "docker build creates:",
        "option_a": "Images",
        "option_b": "Tables",
        "option_c": "Bikes",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Docker compose manages:",
        "option_a": "Multiple containers",
        "option_b": "Multiple candles",
        "option_c": "Multiple bottles",
        "option_d": "Multiple shirts",
        "correct_answer": "A"
    }
],
157: [
    {
        "question_text": "Kubernetes manages:",
        "option_a": "Containers",
        "option_b": "Cars",
        "option_c": "Rooms",
        "option_d": "Trees",
        "correct_answer": "A"
    },
    {
        "question_text": "A pod contains:",
        "option_a": "One or more containers",
        "option_b": "One or more chairs",
        "option_c": "One or more shirts",
        "option_d": "One or more bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Kubernetes is also called:",
        "option_a": "K8s",
        "option_b": "K88",
        "option_c": "K22",
        "option_d": "K2X",
        "correct_answer": "A"
    },
    {
        "question_text": "Service exposes:",
        "option_a": "Pods",
        "option_b": "Cars",
        "option_c": "Walls",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Deployment manages:",
        "option_a": "Replica sets",
        "option_b": "Replica fans",
        "option_c": "Replica cars",
        "option_d": "Replica shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "kubectl is used for:",
        "option_a": "Cluster control",
        "option_b": "Home control",
        "option_c": "Bike control",
        "option_d": "TV control",
        "correct_answer": "A"
    },
    {
        "question_text": "ConfigMap stores:",
        "option_a": "Configuration data",
        "option_b": "Cloth data",
        "option_c": "Shoe data",
        "option_d": "Food data",
        "correct_answer": "A"
    },
    {
        "question_text": "Node runs:",
        "option_a": "Worker processes",
        "option_b": "Worker robots",
        "option_c": "Worker toys",
        "option_d": "Worker bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Kubernetes ensures:",
        "option_a": "Auto-scaling",
        "option_b": "Auto-cleaning",
        "option_c": "Auto-running",
        "option_d": "Auto-packing",
        "correct_answer": "A"
    },
    {
        "question_text": "Persistent Volume stores:",
        "option_a": "Data permanently",
        "option_b": "Shoes permanently",
        "option_c": "Bags permanently",
        "option_d": "Chairs permanently",
        "correct_answer": "A"
    }
],
156: [
    {
        "question_text": "Big Data deals with:",
        "option_a": "Large datasets",
        "option_b": "Large buckets",
        "option_c": "Large boxes",
        "option_d": "Large shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Hadoop is a:",
        "option_a": "Big data framework",
        "option_b": "Water bottle",
        "option_c": "Music speaker",
        "option_d": "Kitchen tool",
        "correct_answer": "A"
    },
    {
        "question_text": "HDFS stores:",
        "option_a": "Distributed files",
        "option_b": "Distributed clothes",
        "option_c": "Distributed bottles",
        "option_d": "Distributed chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Spark is used for:",
        "option_a": "Fast data processing",
        "option_b": "Fast eating",
        "option_c": "Fast running",
        "option_d": "Fast drawing",
        "correct_answer": "A"
    },
    {
        "question_text": "Big data volume refers to:",
        "option_a": "Data size",
        "option_b": "Sound size",
        "option_c": "Bottle size",
        "option_d": "Shoe size",
        "correct_answer": "A"
    },
    {
        "question_text": "Velocity refers to:",
        "option_a": "Data speed",
        "option_b": "Wind speed",
        "option_c": "Water speed",
        "option_d": "Bike speed",
        "correct_answer": "A"
    },
    {
        "question_text": "Variety refers to:",
        "option_a": "Different data types",
        "option_b": "Different bikes",
        "option_c": "Different shirts",
        "option_d": "Different soaps",
        "correct_answer": "A"
    },
    {
        "question_text": "MapReduce performs:",
        "option_a": "Parallel processing",
        "option_b": "Parallel cooking",
        "option_c": "Parallel cycling",
        "option_d": "Parallel driving",
        "correct_answer": "A"
    },
    {
        "question_text": "NoSQL is used for:",
        "option_a": "Unstructured data",
        "option_b": "Structured clothes",
        "option_c": "Structured fruits",
        "option_d": "Structured toys",
        "correct_answer": "A"
    },
    {
        "question_text": "Kafka handles:",
        "option_a": "Real-time data streams",
        "option_b": "Real-time rain",
        "option_c": "Real-time cooking",
        "option_d": "Real-time parking",
        "correct_answer": "A"
    }
],
155: [
    {
        "question_text": "Advanced Big Data focuses on:",
        "option_a": "Real-time analytics",
        "option_b": "Real-time cooking",
        "option_c": "Real-time painting",
        "option_d": "Real-time shopping",
        "correct_answer": "A"
    },
    {
        "question_text": "Spark Streaming processes:",
        "option_a": "Live data",
        "option_b": "Live fish",
        "option_c": "Live music",
        "option_d": "Live birds",
        "correct_answer": "A"
    },
    {
        "question_text": "Kafka is used for:",
        "option_a": "Message streaming",
        "option_b": "Message singing",
        "option_c": "Message printing",
        "option_d": "Message packing",
        "correct_answer": "A"
    },
    {
        "question_text": "Flink supports:",
        "option_a": "Real-time computation",
        "option_b": "Real-time dancing",
        "option_c": "Real-time watering",
        "option_d": "Real-time cycling",
        "correct_answer": "A"
    },
    {
        "question_text": "Hadoop YARN manages:",
        "option_a": "Cluster resources",
        "option_b": "Classroom resources",
        "option_c": "Garden resources",
        "option_d": "Kitchen resources",
        "correct_answer": "A"
    },
    {
        "question_text": "Airflow is used for:",
        "option_a": "Workflow scheduling",
        "option_b": "Room cooling",
        "option_c": "Food heating",
        "option_d": "Car washing",
        "correct_answer": "A"
    },
    {
        "question_text": "Delta Lake provides:",
        "option_a": "Data reliability",
        "option_b": "Water reliability",
        "option_c": "Fan reliability",
        "option_d": "Plant reliability",
        "correct_answer": "A"
    },
    {
        "question_text": "HBase stores:",
        "option_a": "Wide-column data",
        "option_b": "Wide-column clothes",
        "option_c": "Wide-column papers",
        "option_d": "Wide-column toys",
        "correct_answer": "A"
    },
    {
        "question_text": "Data pipelines move:",
        "option_a": "Data between systems",
        "option_b": "Food between kitchens",
        "option_c": "Air between rooms",
        "option_d": "Water between tanks",
        "correct_answer": "A"
    },
    {
        "question_text": "Big data security protects:",
        "option_a": "Sensitive information",
        "option_b": "Sensitive pillows",
        "option_c": "Sensitive shoes",
        "option_d": "Sensitive chairs",
        "correct_answer": "A"
    }
],
154: [
    {
        "question_text": "DSA stands for:",
        "option_a": "Data Structures & Algorithms",
        "option_b": "Data Shoes & Accessories",
        "option_c": "Daily Snacks & Appetizers",
        "option_d": "Drawing Shapes & Art",
        "correct_answer": "A"
    },
    {
        "question_text": "Array stores:",
        "option_a": "Elements in order",
        "option_b": "Elements in circles",
        "option_c": "Elements in bottles",
        "option_d": "Elements in pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Stack follows:",
        "option_a": "LIFO",
        "option_b": "FIFO",
        "option_c": "MOMO",
        "option_d": "DODO",
        "correct_answer": "A"
    },
    {
        "question_text": "Queue follows:",
        "option_a": "FIFO",
        "option_b": "LIFO",
        "option_c": "RIFO",
        "option_d": "TIFO",
        "correct_answer": "A"
    },
    {
        "question_text": "Linked list contains:",
        "option_a": "Nodes",
        "option_b": "Doors",
        "option_c": "Chairs",
        "option_d": "Fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Tree is:",
        "option_a": "Hierarchical structure",
        "option_b": "Flat structure",
        "option_c": "Circular structure",
        "option_d": "Random structure",
        "correct_answer": "A"
    },
    {
        "question_text": "Graph contains:",
        "option_a": "Vertices & edges",
        "option_b": "Shoes & socks",
        "option_c": "Bags & belts",
        "option_d": "Pens & books",
        "correct_answer": "A"
    },
    {
        "question_text": "Binary search works on:",
        "option_a": "Sorted data",
        "option_b": "Random water",
        "option_c": "Sorted fruits",
        "option_d": "Sorted shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Recursion calls:",
        "option_a": "Function itself",
        "option_b": "Parents",
        "option_c": "Neighbours",
        "option_d": "Friends",
        "correct_answer": "A"
    },
    {
        "question_text": "Time complexity measures:",
        "option_a": "Performance",
        "option_b": "Temperature",
        "option_c": "Sound",
        "option_d": "Pressure",
        "correct_answer": "A"
    }
],
153: [
    {
        "question_text": "Dynamic programming optimizes:",
        "option_a": "Overlapping subproblems",
        "option_b": "Overlapping chairs",
        "option_c": "Overlapping pillows",
        "option_d": "Overlapping cars",
        "correct_answer": "A"
    },
    {
        "question_text": "Greedy algorithms make:",
        "option_a": "Local optimum choices",
        "option_b": "Local food choices",
        "option_c": "Local cloth choices",
        "option_d": "Local drink choices",
        "correct_answer": "A"
    },
    {
        "question_text": "Graph algorithms include:",
        "option_a": "Dijkstra",
        "option_b": "Discord",
        "option_c": "Dinosaur",
        "option_d": "Dome",
        "correct_answer": "A"
    },
    {
        "question_text": "Trie stores:",
        "option_a": "Strings efficiently",
        "option_b": "Clothes efficiently",
        "option_c": "Shoes efficiently",
        "option_d": "Fans efficiently",
        "correct_answer": "A"
    },
    {
        "question_text": "Heap is used for:",
        "option_a": "Priority queue",
        "option_b": "Priority shoes",
        "option_c": "Priority bikes",
        "option_d": "Priority shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Topological sort applies to:",
        "option_a": "DAGs",
        "option_b": "MAGs",
        "option_c": "BAGs",
        "option_d": "RAGs",
        "correct_answer": "A"
    },
    {
        "question_text": "Segment tree is used for:",
        "option_a": "Range queries",
        "option_b": "Range washing",
        "option_c": "Range cooking",
        "option_d": "Range painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Backtracking explores:",
        "option_a": "All possibilities",
        "option_b": "All fruits",
        "option_c": "All clothes",
        "option_d": "All cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Hashing maps:",
        "option_a": "Keys to values",
        "option_b": "Keys to bottles",
        "option_c": "Keys to bikes",
        "option_d": "Keys to caps",
        "correct_answer": "A"
    },
    {
        "question_text": "DP table stores:",
        "option_a": "Subproblem results",
        "option_b": "Subproblem shoes",
        "option_c": "Subproblem papers",
        "option_d": "Subproblem shirts",
        "correct_answer": "A"
    }
],
152: [
    {
        "question_text": "An operating system manages:",
        "option_a": "Hardware and software resources",
        "option_b": "Food and drinks",
        "option_c": "Shoes and bags",
        "option_d": "Wires and pipes",
        "correct_answer": "A"
    },
    {
        "question_text": "A process is:",
        "option_a": "A running program",
        "option_b": "A running bicycle",
        "option_c": "A running shirt",
        "option_d": "A running motor",
        "correct_answer": "A"
    },
    {
        "question_text": "Multitasking allows:",
        "option_a": "Multiple programs to run",
        "option_b": "Multiple bags to run",
        "option_c": "Multiple boxes to run",
        "option_d": "Multiple plates to run",
        "correct_answer": "A"
    },
    {
        "question_text": "Threads are:",
        "option_a": "Lightweight processes",
        "option_b": "Lightweight bottles",
        "option_c": "Lightweight chairs",
        "option_d": "Lightweight books",
        "correct_answer": "A"
    },
    {
        "question_text": "Deadlock occurs when:",
        "option_a": "Processes wait forever",
        "option_b": "People wait forever",
        "option_c": "Cars wait forever",
        "option_d": "Fans wait forever",
        "correct_answer": "A"
    },
    {
        "question_text": "Memory management allocates:",
        "option_a": "RAM",
        "option_b": "Shoes",
        "option_c": "Plates",
        "option_d": "Cups",
        "correct_answer": "A"
    },
    {
        "question_text": "File system stores:",
        "option_a": "Files and directories",
        "option_b": "Clothes and shoes",
        "option_c": "Pens and books",
        "option_d": "Beds and pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Scheduling selects:",
        "option_a": "Next process to run",
        "option_b": "Next shirt to buy",
        "option_c": "Next fruit to cut",
        "option_d": "Next cup to fill",
        "correct_answer": "A"
    },
    {
        "question_text": "OS acts as a:",
        "option_a": "Resource manager",
        "option_b": "Room manager",
        "option_c": "Cloth manager",
        "option_d": "Fan manager",
        "correct_answer": "A"
    },
    {
        "question_text": "Kernel is the:",
        "option_a": "Core of OS",
        "option_b": "Core of fruit",
        "option_c": "Core of pencil",
        "option_d": "Core of plate",
        "correct_answer": "A"
    }
],
151: [
    {
        "question_text": "Virtual memory allows:",
        "option_a": "More memory than RAM",
        "option_b": "More cars than roads",
        "option_c": "More books than shelves",
        "option_d": "More chairs than rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "Mutex prevents:",
        "option_a": "Race conditions",
        "option_b": "Car races",
        "option_c": "Fish races",
        "option_d": "Wind races",
        "correct_answer": "A"
    },
    {
        "question_text": "Page replacement decides:",
        "option_a": "Which page to swap",
        "option_b": "Which fruit to swap",
        "option_c": "Which bag to swap",
        "option_d": "Which cup to swap",
        "correct_answer": "A"
    },
    {
        "question_text": "Thrashing reduces:",
        "option_a": "Performance",
        "option_b": "Temperature",
        "option_c": "Brightness",
        "option_d": "Wind",
        "correct_answer": "A"
    },
    {
        "question_text": "Kernel mode allows:",
        "option_a": "Privileged instructions",
        "option_b": "Privileged cooking",
        "option_c": "Privileged painting",
        "option_d": "Privileged dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Monolithic kernel:",
        "option_a": "Contains all services",
        "option_b": "Contains all fruits",
        "option_c": "Contains all bottles",
        "option_d": "Contains all shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Microkernel:",
        "option_a": "Keeps minimal services",
        "option_b": "Keeps minimal books",
        "option_c": "Keeps minimal shoes",
        "option_d": "Keeps minimal lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Process synchronization ensures:",
        "option_a": "Correct execution",
        "option_b": "Correct driving",
        "option_c": "Correct singing",
        "option_d": "Correct washing",
        "correct_answer": "A"
    },
    {
        "question_text": "DMA improves:",
        "option_a": "Data transfer",
        "option_b": "Water transfer",
        "option_c": "Heat transfer",
        "option_d": "Air transfer",
        "correct_answer": "A"
    },
    {
        "question_text": "I/O scheduling improves:",
        "option_a": "Disk performance",
        "option_b": "Room performance",
        "option_c": "Bike performance",
        "option_d": "Fan performance",
        "correct_answer": "A"
    }
],
150: [
    {
        "question_text": "CPU stands for:",
                         "option_a": "Central Processing Unit",
        "option_b": "Central Parking Unit",
        "option_c": "Central Painting Unit",
        "option_d": "Central Playing Unit",
        "correct_answer": "A"
    },
    {
        "question_text": "ALU performs:",
        "option_a": "Arithmetic and logic operations",
        "option_b": "Arithmetic and cooking",
        "option_c": "Arithmetic and jumping",
        "option_d": "Arithmetic and dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Cache stores:",
        "option_a": "Frequently used data",
        "option_b": "Frequently used shirts",
        "option_c": "Frequently used bottles",
        "option_d": "Frequently used fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "Registers are:",
        "option_a": "Small fast storage",
        "option_b": "Small fast bikes",
        "option_c": "Small fast plates",
        "option_d": "Small fast shirts",
        "correct_answer": "A"
    },
    {
        "question_text": "Pipelining improves:",
        "option_a": "Instruction throughput",
        "option_b": "Car throughput",
        "option_c": "Shoe throughput",
        "option_d": "Fan throughput",
        "correct_answer": "A"
    },
    {
        "question_text": "Clock speed measures:",
        "option_a": "Cycles per second",
        "option_b": "Steps per second",
        "option_c": "Cars per second",
        "option_d": "Lights per second",
        "correct_answer": "A"
    },
    {
        "question_text": "Instruction set defines:",
        "option_a": "CPU commands",
        "option_b": "TV commands",
        "option_c": "Fan commands",
        "option_d": "Light commands",
        "correct_answer": "A"
    },
    {
        "question_text": "Control unit manages:",
        "option_a": "Instruction execution",
        "option_b": "Room cleaning",
        "option_c": "Garden planting",
        "option_d": "Water filling",
        "correct_answer": "A"
    },
    {
        "question_text": "RISC architecture focuses on:",
        "option_a": "Simple instructions",
        "option_b": "Simple shoes",
        "option_c": "Simple fruits",
        "option_d": "Simple caps",
        "correct_answer": "A"
    },
    {
        "question_text": "Memory bus transfers:",
        "option_a": "Data between CPU & RAM",
        "option_b": "Data between rooms",
        "option_c": "Data between cups",
        "option_d": "Data between plates",
        "correct_answer": "A"
    }
],
149: [
    {
        "question_text": "Software Engineering focuses on:",
        "option_a": "Systematic development",
        "option_b": "Random painting",
        "option_c": "Random cooking",
        "option_d": "Random shopping",
        "correct_answer": "A"
    },
    {
        "question_text": "SDLC describes:",
        "option_a": "Project stages",
        "option_b": "Sports stages",
        "option_c": "Shoe stages",
        "option_d": "Food stages",
        "correct_answer": "A"
    },
    {
        "question_text": "Agile emphasizes:",
        "option_a": "Flexibility",
        "option_b": "Electricity",
        "option_c": "Humidity",
        "option_d": "Activity",
        "correct_answer": "A"
    },
    {
        "question_text": "Waterfall model is:",
        "option_a": "Sequential",
        "option_b": "Circular",
        "option_c": "Random",
        "option_d": "Reverse",
        "correct_answer": "A"
    },
    {
        "question_text": "Testing ensures:",
        "option_a": "Quality",
        "option_b": "Brightness",
        "option_c": "Softness",
        "option_d": "Hardness",
        "correct_answer": "A"
    },
    {
        "question_text": "Documentation helps:",
        "option_a": "Understanding the system",
        "option_b": "Understanding cooking",
        "option_c": "Understanding shoes",
        "option_d": "Understanding chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Version control tracks:",
        "option_a": "Code changes",
        "option_b": "Room changes",
        "option_c": "Hair changes",
        "option_d": "Weather changes",
        "correct_answer": "A"
    },
    {
        "question_text": "UML diagrams represent:",
        "option_a": "System structure",
        "option_b": "Garden structure",
        "option_c": "House structure",
        "option_d": "Bag structure",
        "correct_answer": "A"
    },
    {
        "question_text": "SRS stands for:",
        "option_a": "Software Requirements Specification",
        "option_b": "Software Repair Shop",
        "option_c": "Standard Radio System",
        "option_d": "Simple Repair Service",
        "correct_answer": "A"
    },
    {
        "question_text": "Software maintenance includes:",
        "option_a": "Fixing bugs",
        "option_b": "Fixing bikes",
        "option_c": "Fixing rooms",
        "option_d": "Fixing plates",
        "correct_answer": "A"
    }
],
148: [
    {
        "question_text": "An OS manages:",
        "option_a": "System resources",
        "option_b": "Street resources",
        "option_c": "Garden resources",
        "option_d": "Kitchen resources",
        "correct_answer": "A"
    },
    {
        "question_text": "CPU scheduling selects:",
        "option_a": "Processes",
        "option_b": "Bottles",
        "option_c": "Plants",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "RAM stores:",
        "option_a": "Temporary data",
        "option_b": "Temporary shoes",
        "option_c": "Temporary bricks",
        "option_d": "Temporary chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Files are stored in:",
        "option_a": "File system",
        "option_b": "Shoe rack",
        "option_c": "Plant pot",
        "option_d": "Fridge",
        "correct_answer": "A"
    },
    {
        "question_text": "Deadlock causes:",
        "option_a": "Process waiting forever",
        "option_b": "People waiting forever",
        "option_c": "Dogs waiting forever",
        "option_d": "Cars waiting forever",
        "correct_answer": "A"
    },
    {
        "question_text": "Kernel manages:",
        "option_a": "Core tasks",
        "option_b": "Core apples",
        "option_c": "Core tables",
        "option_d": "Core beds",
        "correct_answer": "A"
    },
    {
        "question_text": "Multitasking allows:",
        "option_a": "Multiple programs",
        "option_b": "Multiple shirts",
        "option_c": "Multiple caps",
        "option_d": "Multiple bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "ROM stores:",
        "option_a": "Permanent data",
        "option_b": "Permanent bikes",
        "option_c": "Permanent fruits",
        "option_d": "Permanent chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Virtual memory uses:",
        "option_a": "Hard disk",
        "option_b": "Car battery",
        "option_c": "Water tank",
        "option_d": "Painting board",
        "correct_answer": "A"
    },
    {
        "question_text": "Paging divides memory into:",
        "option_a": "Blocks",
        "option_b": "Bottles",
        "option_c": "Books",
        "option_d": "Beds",
        "correct_answer": "A"
    }
],
147: [
    {
        "question_text": "A network connects:",
        "option_a": "Devices",
        "option_b": "Shoes",
        "option_c": "Tables",
        "option_d": "Plants",
        "correct_answer": "A"
    },
    {
        "question_text": "IP stands for:",
        "option_a": "Internet Protocol",
        "option_b": "Indian Police",
        "option_c": "Iron Pipe",
        "option_d": "Image Print",
        "correct_answer": "A"
    },
    {
        "question_text": "LAN covers:",
        "option_a": "Small area",
        "option_b": "Huge area",
        "option_c": "Mountains",
        "option_d": "Countries",
        "correct_answer": "A"
    },
    {
        "question_text": "Packet switching sends:",
        "option_a": "Data in small chunks",
        "option_b": "Data in big buckets",
        "option_c": "Data in long sticks",
        "option_d": "Data in pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Router forwards:",
        "option_a": "Packets",
        "option_b": "Shoes",
        "option_c": "Plates",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "HTTP is used for:",
        "option_a": "Web communication",
        "option_b": "Cooking communication",
        "option_c": "Shoe communication",
        "option_d": "Room communication",
        "correct_answer": "A"
    },
    {
        "question_text": "DNS resolves:",
        "option_a": "Domain names",
        "option_b": "Baby names",
        "option_c": "Car names",
        "option_d": "Plant names",
        "correct_answer": "A"
    },
    {
        "question_text": "TCP ensures:",
        "option_a": "Reliable transmission",
        "option_b": "Fast cooking",
        "option_c": "Strong shoes",
        "option_d": "Heavy chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Firewall provides:",
        "option_a": "Security",
        "option_b": "Electricity",
        "option_c": "Water",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "MAC address identifies:",
        "option_a": "Hardware device",
        "option_b": "Hair dryer",
        "option_c": "Hand bag",
        "option_d": "Helmet",
        "correct_answer": "A"
    }
],
146: [
    {
        "question_text": "Cloud computing provides:",
        "option_a": "On-demand resources",
        "option_b": "On-demand food",
        "option_c": "On-demand shoes",
        "option_d": "On-demand rooms",
        "correct_answer": "A"
    },
    {
        "question_text": "IaaS offers:",
        "option_a": "Infrastructure",
        "option_b": "Ice cream",
        "option_c": "Ink bottles",
        "option_d": "Iron tools",
        "correct_answer": "A"
    },
    {
        "question_text": "PaaS provides:",
        "option_a": "Platform",
        "option_b": "Plants",
        "option_c": "Plates",
        "option_d": "Pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "SaaS delivers:",
        "option_a": "Software",
        "option_b": "Snacks",
        "option_c": "Sweets",
        "option_d": "Seats",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud is:",
        "option_a": "Scalable",
        "option_b": "Pourable",
        "option_c": "Shakeable",
        "option_d": "Breakable",
        "correct_answer": "A"
    },
    {
        "question_text": "AWS stands for:",
        "option_a": "Amazon Web Services",
        "option_b": "American Water Supply",
        "option_c": "Asian Weather System",
        "option_d": "Automatic Watch System",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure is by:",
        "option_a": "Microsoft",
        "option_b": "Google",
        "option_c": "Apple",
        "option_d": "Samsung",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud storage stores:",
        "option_a": "Data online",
        "option_b": "Water online",
        "option_c": "Books online",
        "option_d": "Shoes online",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud functions run:",
        "option_a": "Code on demand",
        "option_b": "Food on demand",
        "option_c": "Paint on demand",
        "option_d": "Shoes on demand",
        "correct_answer": "A"
    },
    {
        "question_text": "Cloud security protects:",
        "option_a": "Data",
        "option_b": "Clothes",
        "option_c": "Bikes",
        "option_d": "Tables",
        "correct_answer": "A"
    }
],

        145: [
    {
        "question_text": "AWS EC2 provides:",
        "option_a": "Virtual servers",
        "option_b": "Virtual shirts",
        "option_c": "Virtual pillows",
        "option_d": "Virtual trucks",
        "correct_answer": "A"
    },
    {
        "question_text": "S3 is used for:",
        "option_a": "Object storage",
        "option_b": "Object cooking",
        "option_c": "Object painting",
        "option_d": "Object washing",
        "correct_answer": "A"
    },
    {
        "question_text": "Lambda runs code:",
        "option_a": "Without servers",
        "option_b": "Without water",
        "option_c": "Without air",
        "option_d": "Without chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "CloudWatch monitors:",
        "option_a": "AWS resources",
        "option_b": "TV channels",
        "option_c": "Room fans",
        "option_d": "Kitchen ovens",
        "correct_answer": "A"
    },
    {
        "question_text": "CloudTrail records:",
        "option_a": "API activity",
        "option_b": "School activity",
        "option_c": "Gym activity",
        "option_d": "Garden activity",
        "correct_answer": "A"
    },
    {
        "question_text": "AWS VPC provides:",
        "option_a": "Network isolation",
        "option_b": "Room isolation",
        "option_c": "Plant isolation",
        "option_d": "Bike isolation",
        "correct_answer": "A"
    },
    {
        "question_text": "IAM manages:",
        "option_a": "Users & roles",
        "option_b": "Shoes & socks",
        "option_c": "Bowls & spoons",
        "option_d": "Beds & tables",
        "correct_answer": "A"
    },
    {
        "question_text": "RDS handles:",
        "option_a": "Relational databases",
        "option_b": "Relational bags",
        "option_c": "Relational chairs",
        "option_d": "Relational toys",
        "correct_answer": "A"
    },
    {
        "question_text": "SNS sends:",
        "option_a": "Notifications",
        "option_b": "Shoes",
        "option_c": "Books",
        "option_d": "Balloons",
        "correct_answer": "A"
    },
    {
        "question_text": "SQS is a:",
        "option_a": "Message queue",
        "option_b": "Message plate",
        "option_c": "Message pipe",
        "option_d": "Message light",
        "correct_answer": "A"
    }
],
        144: [
    {
        "question_text": "Azure is a:",
        "option_a": "Cloud platform",
        "option_b": "Milk platform",
        "option_c": "Paint platform",
        "option_d": "Shoe platform",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure VM provides:",
        "option_a": "Virtual machines",
        "option_b": "Virtual fridges",
        "option_c": "Virtual bags",
        "option_d": "Virtual lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Blob stores:",
        "option_a": "Objects",
        "option_b": "Fruits",
        "option_c": "Shirts",
        "option_d": "Bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Functions run:",
        "option_a": "Serverless code",
        "option_b": "Serverless bikes",
        "option_c": "Serverless fans",
        "option_d": "Serverless cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Active Directory manages:",
        "option_a": "Identities",
        "option_b": "Vegetables",
        "option_c": "Chairs",
        "option_d": "Stones",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure SQL is a:",
        "option_a": "Managed database",
        "option_b": "Managed room",
        "option_c": "Managed car",
        "option_d": "Managed fan",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Monitor tracks:",
        "option_a": "Performance metrics",
        "option_b": "Cooking metrics",
        "option_c": "Driving metrics",
        "option_d": "Walking metrics",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Kubernetes Service manages:",
        "option_a": "Containers",
        "option_b": "Refrigerators",
        "option_c": "Ceilings",
        "option_d": "Mirrors",
        "correct_answer": "A"
    },
    {
        "question_text": "Scale sets allow:",
        "option_a": "Auto-scaling",
        "option_b": "Auto-cleaning",
        "option_c": "Auto-cooking",
        "option_d": "Auto-driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure logic apps create:",
        "option_a": "Workflows",
        "option_b": "Shoes",
        "option_c": "Fans",
        "option_d": "Lights",
        "correct_answer": "A"
    }
],
144: [
    {
        "question_text": "Azure is a:",
        "option_a": "Cloud platform",
        "option_b": "Milk platform",
        "option_c": "Paint platform",
        "option_d": "Shoe platform",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure VM provides:",
        "option_a": "Virtual machines",
        "option_b": "Virtual fridges",
        "option_c": "Virtual bags",
        "option_d": "Virtual lights",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Blob stores:",
        "option_a": "Objects",
        "option_b": "Fruits",
        "option_c": "Shirts",
        "option_d": "Bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Functions run:",
        "option_a": "Serverless code",
        "option_b": "Serverless bikes",
        "option_c": "Serverless fans",
        "option_d": "Serverless cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Active Directory manages:",
        "option_a": "Identities",
        "option_b": "Vegetables",
        "option_c": "Chairs",
        "option_d": "Stones",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure SQL is a:",
        "option_a": "Managed database",
        "option_b": "Managed room",
        "option_c": "Managed car",
        "option_d": "Managed fan",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Monitor tracks:",
        "option_a": "Performance metrics",
        "option_b": "Cooking metrics",
        "option_c": "Driving metrics",
        "option_d": "Walking metrics",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure Kubernetes Service manages:",
        "option_a": "Containers",
        "option_b": "Refrigerators",
        "option_c": "Ceilings",
        "option_d": "Mirrors",
        "correct_answer": "A"
    },
    {
        "question_text": "Scale sets allow:",
        "option_a": "Auto-scaling",
        "option_b": "Auto-cleaning",
        "option_c": "Auto-cooking",
        "option_d": "Auto-driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Azure logic apps create:",
        "option_a": "Workflows",
        "option_b": "Shoes",
        "option_c": "Fans",
        "option_d": "Lights",
        "correct_answer": "A"
    }
],

        143: [
    {
        "question_text": "AWS provides:",
        "option_a": "Cloud services",
        "option_b": "Shoe services",
        "option_c": "Water services",
        "option_d": "Furniture services",
        "correct_answer": "A"
    },
    {
        "question_text": "EC2 is used for:",
        "option_a": "Virtual servers",
        "option_b": "Virtual pillows",
        "option_c": "Virtual belts",
        "option_d": "Virtual tanks",
        "correct_answer": "A"
    },
    {
        "question_text": "S3 stores:",
        "option_a": "Objects",
        "option_b": "Books",
        "option_c": "Plants",
        "option_d": "Tools",
        "correct_answer": "A"
    },
    {
        "question_text": "CloudFront delivers:",
        "option_a": "Content fast",
        "option_b": "Food fast",
        "option_c": "Shoes fast",
        "option_d": "Bikes fast",
        "correct_answer": "A"
    },
    {
        "question_text": "IAM controls:",
        "option_a": "Access",
        "option_b": "Temperature",
        "option_c": "Colour",
        "option_d": "Size",
        "correct_answer": "A"
    },
    {
        "question_text": "RDS manages:",
        "option_a": "Databases",
        "option_b": "Dustbins",
        "option_c": "Doormats",
        "option_d": "Drawers",
        "correct_answer": "A"
    },
    {
        "question_text": "VPC provides:",
        "option_a": "Network isolation",
        "option_b": "Kitchen isolation",
        "option_c": "Garden isolation",
        "option_d": "Garage isolation",
        "correct_answer": "A"
    },
    {
        "question_text": "Lambda executes code:",
        "option_a": "On demand",
        "option_b": "On wheels",
        "option_c": "On paper",
        "option_d": "On plates",
        "correct_answer": "A"
    },
    {
        "question_text": "SNS sends:",
        "option_a": "Notifications",
        "option_b": "Menus",
        "option_c": "Shoes",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "DynamoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "SQL bottle",
        "option_c": "SQL fan",
        "option_d": "SQL coat",
        "correct_answer": "A"
    }
],
142: [
    {
        "question_text": "AI stands for:",
        "option_a": "Artificial Intelligence",
        "option_b": "Automatic Iron",
        "option_c": "Autumn Icecream",
        "option_d": "Automatic Ink",
        "correct_answer": "A"
    },
    {
        "question_text": "AI systems learn from:",
        "option_a": "Data",
        "option_b": "Water",
        "option_c": "Shoes",
        "option_d": "Furniture",
        "correct_answer": "A"
    },
    {
        "question_text": "Machine learning is a part of:",
        "option_a": "AI",
        "option_b": "Cooking",
        "option_c": "Painting",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Neural networks mimic:",
        "option_a": "Human brain",
        "option_b": "Human hair",
        "option_c": "Human shoes",
        "option_d": "Human clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "AI applications include:",
        "option_a": "Chatbots",
        "option_b": "Chairs",
        "option_c": "Cups",
        "option_d": "Carpets",
        "correct_answer": "A"
    },
    {
        "question_text": "AI improves:",
        "option_a": "Automation",
        "option_b": "Decoration",
        "option_c": "Illustration",
        "option_d": "Pollination",
        "correct_answer": "A"
    },
    {
        "question_text": "AI is used in:",
        "option_a": "Healthcare",
        "option_b": "Plant care",
        "option_c": "Shoe care",
        "option_d": "Pet care",
        "correct_answer": "A"
    },
    {
        "question_text": "AI models require:",
        "option_a": "Training",
        "option_b": "Washing",
        "option_c": "Singing",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "AI predictions are based on:",
        "option_a": "Patterns",
        "option_b": "Rivers",
        "option_c": "Shoes",
        "option_d": "Rain",
        "correct_answer": "A"
    },
    {
        "question_text": "AI helps in:",
        "option_a": "Decision making",
        "option_b": "Cloth making",
        "option_c": "Fan making",
        "option_d": "Door making",
        "correct_answer": "A"
    }
],
141: [
    {
        "question_text": "Data Science involves:",
        "option_a": "Analyzing data",
        "option_b": "Analyzing clothes",
        "option_c": "Analyzing chairs",
        "option_d": "Analyzing fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "Pandas is used for:",
        "option_a": "Data manipulation",
        "option_b": "Food manipulation",
        "option_c": "Hair manipulation",
        "option_d": "Paper manipulation",
        "correct_answer": "A"
    },
    {
        "question_text": "NumPy is used for:",
        "option_a": "Numerical computation",
        "option_b": "Numerical cooking",
        "option_c": "Numerical climbing",
        "option_d": "Numerical painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Matplotlib helps with:",
        "option_a": "Data visualization",
        "option_b": "Room decoration",
        "option_c": "Table polishing",
        "option_d": "Glass coloring",
        "correct_answer": "A"
    },
    {
        "question_text": "A dataset contains:",
        "option_a": "Rows and columns",
        "option_b": "Shoes and socks",
        "option_c": "Beds and pillows",
        "option_d": "Cars and bikes",
        "correct_answer": "A"
    },
    {
        "question_text": "Machine learning models need:",
        "option_a": "Training data",
        "option_b": "Training biscuits",
        "option_c": "Training shoes",
        "option_d": "Training caps",
        "correct_answer": "A"
    },
    {
        "question_text": "Data cleaning removes:",
        "option_a": "Errors",
        "option_b": "Clothes",
        "option_c": "Boxes",
        "option_d": "Hats",
        "correct_answer": "A"
    },
    {
        "question_text": "CSV stands for:",
        "option_a": "Comma Separated Values",
        "option_b": "Common Shoe Variety",
        "option_c": "Car Speed Value",
        "option_d": "Cold Soup Value",
        "correct_answer": "A"
    },
    {
        "question_text": "Python is popular in Data Science because it is:",
        "option_a": "Simple",
        "option_b": "Heavy",
        "option_c": "Noisy",
        "option_d": "Expensive",
        "correct_answer": "A"
    },
    {
        "question_text": "EDA stands for:",
        "option_a": "Exploratory Data Analysis",
        "option_b": "Exhaust Dust Analysis",
        "option_c": "Extra Data Access",
        "option_d": "Electrical Data Area",
        "correct_answer": "A"
    }
],
140: [
    {
        "question_text": "Machine Learning allows machines to:",
        "option_a": "Learn from data",
        "option_b": "Learn from cooking",
        "option_c": "Learn from pillows",
        "option_d": "Learn from shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Supervised learning uses:",
        "option_a": "Labeled data",
        "option_b": "Labeled bags",
        "option_c": "Labeled shirts",
        "option_d": "Labeled books",
        "correct_answer": "A"
    },
    {
        "question_text": "Unsupervised learning finds:",
        "option_a": "Patterns",
        "option_b": "Paintings",
        "option_c": "Photos",
        "option_d": "Plants",
        "correct_answer": "A"
    },
    {
        "question_text": "Regression predicts:",
        "option_a": "Continuous values",
        "option_b": "Continuous wind",
        "option_c": "Continuous rain",
        "option_d": "Continuous food",
        "correct_answer": "A"
    },
    {
        "question_text": "Classification predicts:",
        "option_a": "Categories",
        "option_b": "Furniture",
        "option_c": "Vehicles",
        "option_d": "Animals",
        "correct_answer": "A"
    },
    {
        "question_text": "Overfitting happens when model:",
        "option_a": "Learns noise",
        "option_b": "Learns music",
        "option_c": "Learns cooking",
        "option_d": "Learns dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "Feature scaling helps:",
        "option_a": "Normalize data",
        "option_b": "Normalize shoes",
        "option_c": "Normalize plants",
        "option_d": "Normalize fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Deep learning uses:",
        "option_a": "Neural networks",
        "option_b": "Iron networks",
        "option_c": "Tree networks",
        "option_d": "Cable networks",
        "correct_answer": "A"
    },
    {
        "question_text": "ML models are evaluated using:",
        "option_a": "Metrics",
        "option_b": "Sticks",
        "option_c": "Pens",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Training set is used to:",
        "option_a": "Train the model",
        "option_b": "Train the dog",
        "option_c": "Train the fan",
        "option_d": "Train the shoes",
        "correct_answer": "A"
    }
],
139: [
    {
        "question_text": "MongoDB is a:",
        "option_a": "NoSQL database",
        "option_b": "Bike",
        "option_c": "Shoe",
        "option_d": "Car",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB stores data in:",
        "option_a": "Documents",
        "option_b": "Bottles",
        "option_c": "Shoeboxes",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "The default data format of MongoDB:",
        "option_a": "JSON-like format",
        "option_b": "Wood format",
        "option_c": "Metal format",
        "option_d": "Paper format",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB collections contain:",
        "option_a": "Documents",
        "option_b": "Movies",
        "option_c": "Plants",
        "option_d": "Pictures",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is best for:",
        "option_a": "Flexible schema",
        "option_b": "Flexible clothes",
        "option_c": "Flexible chairs",
        "option_d": "Flexible fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB Atlas is a:",
        "option_a": "Cloud database service",
        "option_b": "Cloud shoe service",
        "option_c": "Cloud food service",
        "option_d": "Cloud painting service",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB uses:",
        "option_a": "BSON",
        "option_b": "SOAP",
        "option_c": "MILK",
        "option_d": "WOOD",
        "correct_answer": "A"
    },
    {
        "question_text": "To insert data in MongoDB we use:",
        "option_a": "insertOne",
        "option_b": "insertShoe",
        "option_c": "insertCar",
        "option_d": "insertLamp",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is:",
        "option_a": "Document-oriented",
        "option_b": "Shoe-oriented",
        "option_c": "Chair-oriented",
        "option_d": "Bike-oriented",
        "correct_answer": "A"
    },
    {
        "question_text": "MongoDB is known for:",
        "option_a": "High scalability",
        "option_b": "High cooking",
        "option_c": "High jumping",
        "option_d": "High dancing",
        "correct_answer": "A"
    }
],
138: [
    {
        "question_text": "PostgreSQL is a:",
        "option_a": "Relational database",
        "option_b": "Water tank",
        "option_c": "Shoe rack",
        "option_d": "Cloth bag",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL supports:",
        "option_a": "ACID compliance",
        "option_b": "ACID washing",
        "option_c": "ACID spraying",
        "option_d": "ACID packaging",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL uses:",
        "option_a": "SQL",
        "option_b": "MILK",
        "option_c": "WOOD",
        "option_d": "GAS",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes improve:",
        "option_a": "Query speed",
        "option_b": "Bike speed",
        "option_c": "Fan speed",
        "option_d": "Car mileage",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL supports:",
        "option_a": "JSON data",
        "option_b": "Shoe data",
        "option_c": "Chair data",
        "option_d": "Fruit data",
        "correct_answer": "A"
    },
    {
        "question_text": "Backup in PostgreSQL can be done using:",
        "option_a": "pg_dump",
        "option_b": "pg_shoe",
        "option_c": "pg_car",
        "option_d": "pg_bottle",
        "correct_answer": "A"
    },
    {
        "question_text": "A table contains:",
        "option_a": "Rows",
        "option_b": "Ropes",
        "option_c": "Rocks",
        "option_d": "Rains",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary key ensures:",
        "option_a": "Uniqueness",
        "option_b": "Happiness",
        "option_c": "Brightness",
        "option_d": "Softness",
        "correct_answer": "A"
    },
    {
        "question_text": "Foreign key creates:",
        "option_a": "Relationships",
        "option_b": "Rainfall",
        "option_c": "Sunlight",
        "option_d": "Waves",
        "correct_answer": "A"
    },
    {
        "question_text": "PostgreSQL is known for:",
        "option_a": "Reliability",
        "option_b": "Fragility",
        "option_c": "Softness",
        "option_d": "Fogginess",
        "correct_answer": "A"
    }
],
137: [
    {
        "question_text": "SQL is used for:",
        "option_a": "Managing databases",
        "option_b": "Managing shoes",
        "option_c": "Managing bags",
        "option_d": "Managing pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "A JOIN combines:",
        "option_a": "Multiple tables",
        "option_b": "Multiple shoes",
        "option_c": "Multiple hats",
        "option_d": "Multiple socks",
        "correct_answer": "A"
    },
    {
        "question_text": "Indexes improve:",
        "option_a": "Query performance",
        "option_b": "Fan performance",
        "option_c": "Shoe performance",
        "option_d": "Room performance",
        "correct_answer": "A"
    },
    {
        "question_text": "GROUP BY is used for:",
        "option_a": "Grouping rows",
        "option_b": "Grouping shirts",
        "option_c": "Grouping bottles",
        "option_d": "Grouping cars",
        "correct_answer": "A"
    },
    {
        "question_text": "ORDER BY sorts:",
        "option_a": "Query results",
        "option_b": "Furniture",
        "option_c": "Plants",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Subqueries are:",
        "option_a": "Queries inside queries",
        "option_b": "Shoes inside boxes",
        "option_c": "Cars inside garages",
        "option_d": "Pens inside bags",
        "correct_answer": "A"
    },
    {
        "question_text": "UNION combines:",
        "option_a": "Two result sets",
        "option_b": "Two fruits",
        "option_c": "Two chairs",
        "option_d": "Two pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "HAVING is used with:",
        "option_a": "Aggregate functions",
        "option_b": "Hair functions",
        "option_c": "Heat functions",
        "option_d": "Hand functions",
        "correct_answer": "A"
    },
    {
        "question_text": "Stored procedures contain:",
        "option_a": "Reusable SQL code",
        "option_b": "Reusable shoes",
        "option_c": "Reusable chairs",
        "option_d": "Reusable bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "SQL injection is a:",
        "option_a": "Security threat",
        "option_b": "Food item",
        "option_c": "Sports event",
        "option_d": "Festival",
        "correct_answer": "A"
    }
],
136: [
    {
        "question_text": "SQL stands for:",
        "option_a": "Structured Query Language",
        "option_b": "Strong Quality Light",
        "option_c": "Small Quick List",
        "option_d": "Soft Quiet Lamp",
        "correct_answer": "A"
    },
    {
        "question_text": "A table contains:",
        "option_a": "Rows and columns",
        "option_b": "Shoes and socks",
        "option_c": "Bags and books",
        "option_d": "Fans and lights",
        "correct_answer": "A"
    },
    {
        "question_text": "SELECT is used to:",
        "option_a": "Retrieve data",
        "option_b": "Retrieve clothes",
        "option_c": "Retrieve toys",
        "option_d": "Retrieve fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "INSERT adds:",
        "option_a": "New records",
        "option_b": "New pillows",
        "option_c": "New shoes",
        "option_d": "New bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "DELETE removes:",
        "option_a": "Records",
        "option_b": "Cars",
        "option_c": "Papers",
        "option_d": "Hats",
        "correct_answer": "A"
    },
    {
        "question_text": "UPDATE changes:",
        "option_a": "Existing data",
        "option_b": "Existing walls",
        "option_c": "Existing shoes",
        "option_d": "Existing plants",
        "correct_answer": "A"
    },
    {
        "question_text": "WHERE filters:",
        "option_a": "Rows",
        "option_b": "Rooms",
        "option_c": "Ropes",
        "option_d": "Rains",
        "correct_answer": "A"
    },
    {
        "question_text": "A database stores:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Chairs",
        "option_d": "Bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Primary key is:",
        "option_a": "Unique identifier",
        "option_b": "Unique shirt",
        "option_c": "Unique pillow",
        "option_d": "Unique bag",
        "correct_answer": "A"
    },
    {
        "question_text": "JOIN is used to:",
        "option_a": "Combine tables",
        "option_b": "Combine shoes",
        "option_c": "Combine hats",
        "option_d": "Combine fruits",
        "correct_answer": "A"
    }
],
135: [
    {
        "question_text": "Full stack development involves:",
        "option_a": "Frontend and backend",
        "option_b": "Shoes and socks",
        "option_c": "Plants and pots",
        "option_d": "Books and bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Frontend handles:",
        "option_a": "User interface",
        "option_b": "Room interface",
        "option_c": "Car interface",
        "option_d": "Bike interface",
        "correct_answer": "A"
    },
    {
        "question_text": "Backend handles:",
        "option_a": "Server logic",
        "option_b": "Shoe logic",
        "option_c": "Fan logic",
        "option_d": "Light logic",
        "correct_answer": "A"
    },
    {
        "question_text": "React is used for:",
        "option_a": "Building UIs",
        "option_b": "Building chairs",
        "option_c": "Building roads",
        "option_d": "Building fans",
        "correct_answer": "A"
    },
    {
        "question_text": "Node.js helps with:",
        "option_a": "Backend development",
        "option_b": "Tree cutting",
        "option_c": "Painting walls",
        "option_d": "Cooking food",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs help in:",
        "option_a": "Communication between systems",
        "option_b": "Communication between birds",
        "option_c": "Communication between chairs",
        "option_d": "Communication between cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Phones",
        "option_d": "Cups",
        "correct_answer": "A"
    },
    {
        "question_text": "HTML is used for:",
        "option_a": "Structure",
        "option_b": "Sound",
        "option_c": "Smell",
        "option_d": "Taste",
        "correct_answer": "A"
    },
    {
        "question_text": "CSS is used for:",
        "option_a": "Styling",
        "option_b": "Cooking",
        "option_c": "Driving",
        "option_d": "Washing",
        "correct_answer": "A"
    },
    {
        "question_text": "JavaScript adds:",
        "option_a": "Interactivity",
        "option_b": "Electricity",
        "option_c": "Humidity",
        "option_d": "Dust",
        "correct_answer": "A"
    }
],
134: [
    {
        "question_text": "TypeScript is a superset of:",
        "option_a": "JavaScript",
        "option_b": "Milk",
        "option_c": "Water",
        "option_d": "Oil",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript adds:",
        "option_a": "Types",
        "option_b": "Shoes",
        "option_c": "Bags",
        "option_d": "Plants",
        "correct_answer": "A"
    },
    {
        "question_text": "Interfaces define:",
        "option_a": "Object structure",
        "option_b": "Room structure",
        "option_c": "Chair structure",
        "option_d": "Car structure",
        "correct_answer": "A"
    },
    {
        "question_text": "Enums are used for:",
        "option_a": "Constants",
        "option_b": "Clothes",
        "option_c": "Fans",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript reduces:",
        "option_a": "Errors",
        "option_b": "Shoes",
        "option_c": "Cars",
        "option_d": "Noise",
        "correct_answer": "A"
    },
    {
        "question_text": "TS files end with:",
        "option_a": ".ts",
        "option_b": ".mp3",
        "option_c": ".jpg",
        "option_d": ".exe",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript is:",
        "option_a": "Strongly typed",
        "option_b": "Strongly cooked",
        "option_c": "Strongly painted",
        "option_d": "Strongly washed",
        "correct_answer": "A"
    },
    {
        "question_text": "Type checking happens:",
        "option_a": "At compile time",
        "option_b": "At bedtime",
        "option_c": "At lunchtime",
        "option_d": "At movie time",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript compiler converts TS to:",
        "option_a": "JavaScript",
        "option_b": "Juice",
        "option_c": "Jam",
        "option_d": "Jackets",
        "correct_answer": "A"
    },
    {
        "question_text": "TypeScript improves:",
        "option_a": "Code readability",
        "option_b": "Room readability",
        "option_c": "Chair readability",
        "option_d": "Car readability",
        "correct_answer": "A"
    }
],
133: [
    {
        "question_text": "JavaScript is used for:",
        "option_a": "Web interactivity",
        "option_b": "Washing dishes",
        "option_c": "Driving cars",
        "option_d": "Cooking food",
        "correct_answer": "A"
    },
    {
        "question_text": "JS runs in:",
        "option_a": "Browser",
        "option_b": "Refrigerator",
        "option_c": "Fan",
        "option_d": "Car",
        "correct_answer": "A"
    },
    {
        "question_text": "Variables store:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Plants",
        "option_d": "Books",
        "correct_answer": "A"
    },
    {
        "question_text": "Functions are:",
        "option_a": "Reusable blocks",
        "option_b": "Reusable bottles",
        "option_c": "Reusable shirts",
        "option_d": "Reusable hats",
        "correct_answer": "A"
    },
    {
        "question_text": "DOM is:",
        "option_a": "Document Object Model",
        "option_b": "Dish Object Model",
        "option_c": "Door Object Model",
        "option_d": "Desk Object Model",
        "correct_answer": "A"
    },
    {
        "question_text": "React uses:",
        "option_a": "JSX",
        "option_b": "XOX",
        "option_c": "SMS",
        "option_d": "PNG",
        "correct_answer": "A"
    },
    {
        "question_text": "Promises handle:",
        "option_a": "Async operations",
        "option_b": "Async cooking",
        "option_c": "Async driving",
        "option_d": "Async painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Events capture:",
        "option_a": "User actions",
        "option_b": "Rain actions",
        "option_c": "Wind actions",
        "option_d": "Fan actions",
        "correct_answer": "A"
    },
    {
        "question_text": "Arrays store:",
        "option_a": "Multiple values",
        "option_b": "Multiple shoes",
        "option_c": "Multiple hats",
        "option_d": "Multiple plants",
        "correct_answer": "A"
    },
    {
        "question_text": "Objects store:",
        "option_a": "Key-value pairs",
        "option_b": "Shirt-value pairs",
        "option_c": "Fan-value pairs",
        "option_d": "Lamp-value pairs",
        "correct_answer": "A"
    }
],
132: [
    {
        "question_text": "React uses:",
        "option_a": "Components",
        "option_b": "Chairs",
        "option_c": "Shoes",
        "option_d": "Tables",
        "correct_answer": "A"
    },
    {
        "question_text": "Redux manages:",
        "option_a": "State",
        "option_b": "Water",
        "option_c": "Plants",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Hooks help in:",
        "option_a": "Using state in functions",
        "option_b": "Using shoes in bags",
        "option_c": "Using fruits in water",
        "option_d": "Using chairs on fans",
        "correct_answer": "A"
    },
    {
        "question_text": "React Router handles:",
        "option_a": "Navigation",
        "option_b": "Decoration",
        "option_c": "Foundation",
        "option_d": "Illumination",
                   "correct_answer": "A"
    },
    {
        "question_text": "Context API avoids:",
        "option_a": "Prop drilling",
        "option_b": "Road drilling",
        "option_c": "Well drilling",
        "option_d": "Wall drilling",
        "correct_answer": "A"
    },
    {
        "question_text": "JSX looks like:",
        "option_a": "HTML",
        "option_b": "Metal",
        "option_c": "Glass",
        "option_d": "Rubber",
        "correct_answer": "A"
    },
    {
        "question_text": "Memoization helps:",
        "option_a": "Improve performance",
        "option_b": "Improve dressing",
        "option_c": "Improve cleaning",
        "option_d": "Improve dancing",
        "correct_answer": "A"
    },
    {
        "question_text": "React is:",
        "option_a": "Declarative",
        "option_b": "Explosive",
        "option_c": "Radioactive",
        "option_d": "Compulsive",
        "correct_answer": "A"
    },
    {
        "question_text": "Keys help with:",
        "option_a": "Identifying list items",
        "option_b": "Identifying shoes",
        "option_c": "Identifying fruits",
        "option_d": "Identifying pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "useEffect runs:",
        "option_a": "Side effects",
        "option_b": "Side snacks",
        "option_c": "Side paintings",
        "option_d": "Side pillows",
        "correct_answer": "A"
    }
],
131: [
    {
        "question_text": "Django is a:",
        "option_a": "Web framework",
        "option_b": "Picture frame",
        "option_c": "Bike frame",
        "option_d": "Metal frame",
        "correct_answer": "A"
    },
    {
        "question_text": "Django uses:",
        "option_a": "MVT architecture",
        "option_b": "TV architecture",
        "option_c": "AC architecture",
        "option_d": "Fan architecture",
        "correct_answer": "A"
    },
    {
        "question_text": "Models define:",
        "option_a": "Database structure",
        "option_b": "Room structure",
        "option_c": "Shoe structure",
        "option_d": "Bike structure",
        "correct_answer": "A"
    },
    {
        "question_text": "Views contain:",
        "option_a": "Logic",
        "option_b": "Traffic",
        "option_c": "Music",
        "option_d": "Plastic",
        "correct_answer": "A"
    },
    {
        "question_text": "Templates handle:",
        "option_a": "UI",
        "option_b": "Tea",
        "option_c": "Ink",
        "option_d": "Oil",
        "correct_answer": "A"
    },
    {
        "question_text": "ORM helps in:",
        "option_a": "Database queries",
        "option_b": "Garden queries",
        "option_c": "Room queries",
        "option_d": "Fan queries",
        "correct_answer": "A"
    },
    {
        "question_text": "Django admin manages:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Chairs",
        "option_d": "Pens",
        "correct_answer": "A"
    },
    {
        "question_text": "URLs map to:",
        "option_a": "Views",
        "option_b": "Rooms",
        "option_c": "Bags",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Static files include:",
        "option_a": "CSS & JS",
        "option_b": "Cars & bikes",
        "option_c": "Pens & bags",
        "option_d": "Fans & bulbs",
        "correct_answer": "A"
    },
    {
        "question_text": "Migrations update:",
        "option_a": "Database schema",
        "option_b": "Shoe colors",
        "option_c": "Car windows",
        "option_d": "Wall paint",
        "correct_answer": "A"
    }
],
130: [
    {
        "question_text": "Python is:",
        "option_a": "Easy to learn",
        "option_b": "Hard to drink",
        "option_c": "Soft to sit",
        "option_d": "Cold to touch",
        "correct_answer": "A"
    },
    {
        "question_text": "A variable stores:",
        "option_a": "Data",
        "option_b": "Shoes",
        "option_c": "Clothes",
        "option_d": "Glass",
        "correct_answer": "A"
    },
    {
        "question_text": "print() is used to:",
        "option_a": "Show output",
        "option_b": "Show shoes",
        "option_c": "Show bags",
        "option_d": "Show wires",
        "correct_answer": "A"
    },
    {
        "question_text": "A list is:",
        "option_a": "A collection",
        "option_b": "A machine",
        "option_c": "A fan",
        "option_d": "A fruit",
        "correct_answer": "A"
    },
    {
        "question_text": "Loops help:",
        "option_a": "Repeat tasks",
        "option_b": "Repeat songs",
        "option_c": "Repeat clothes",
        "option_d": "Repeat cups",
        "correct_answer": "A"
    },
    {
        "question_text": "if-else is used for:",
        "option_a": "Decision making",
        "option_b": "Color making",
        "option_c": "Shoe making",
        "option_d": "Fan making",
        "correct_answer": "A"
    },
    {
        "question_text": "Functions are:",
        "option_a": "Reusable code",
        "option_b": "Reusable bags",
        "option_c": "Reusable chairs",
        "option_d": "Reusable socks",
        "correct_answer": "A"
    },
    {
        "question_text": "Comments start with:",
        "option_a": "#",
        "option_b": "@",
        "option_c": "%",
        "option_d": "$",
        "correct_answer": "A"
    },
    {
        "question_text": "Python was created by:",
        "option_a": "Guido van Rossum",
        "option_b": "Elon Musk",
        "option_c": "Bill Gates",
        "option_d": "Steve Jobs",
        "correct_answer": "A"
    },
    {
        "question_text": "Python is:",
        "option_a": "High-level",
        "option_b": "Low-sugar",
        "option_c": "High-fan",
        "option_d": "Low-floor",
        "correct_answer": "A"
    }
],
126: [
    {
        "question_text": "System design focuses on:",
        "option_a": "High-level architecture",
        "option_b": "High-level cooking",
        "option_c": "High-level washing",
        "option_d": "High-level driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Load balancing distributes:",
        "option_a": "Traffic",
        "option_b": "Shoes",
        "option_c": "Plants",
        "option_d": "Plates",
        "correct_answer": "A"
    },
    {
        "question_text": "Caching improves:",
        "option_a": "Speed",
        "option_b": "Height",
        "option_c": "Brightness",
        "option_d": "Softness",
        "correct_answer": "A"
    },
    {
        "question_text": "Databases store:",
        "option_a": "Data",
        "option_b": "Chairs",
        "option_c": "Bikes",
        "option_d": "Caps",
        "correct_answer": "A"
    },
    {
        "question_text": "Horizontal scaling adds:",
        "option_a": "More servers",
        "option_b": "More shirts",
        "option_c": "More fans",
        "option_d": "More bottles",
        "correct_answer": "A"
    },
    {
        "question_text": "APIs enable:",
        "option_a": "Communication",
        "option_b": "Decoration",
        "option_c": "Navigation",
        "option_d": "Calibration",
        "correct_answer": "A"
    },
    {
        "question_text": "Microservices split:",
        "option_a": "Applications",
        "option_b": "Shoes",
        "option_c": "Plants",
        "option_d": "Doors",
        "correct_answer": "A"
    },
    {
        "question_text": "CDNs deliver:",
        "option_a": "Content",
        "option_b": "Curtains",
        "option_c": "Cars",
        "option_d": "Chairs",
        "correct_answer": "A"
    },
    {
        "question_text": "Logging helps track:",
        "option_a": "System activity",
        "option_b": "Rain activity",
        "option_c": "Wind activity",
        "option_d": "Fan activity",
        "correct_answer": "A"
    },
    {
        "question_text": "Monitoring detects:",
        "option_a": "Issues",
        "option_b": "Pillows",
        "option_c": "Shoes",
        "option_d": "Plants",
        "correct_answer": "A"
    }
],
119: [
    {
        "question_text": "Agile focuses on:",
        "option_a": "Iterative development",
        "option_b": "One-time cooking",
        "option_c": "Fast driving",
        "option_d": "Deep painting",
        "correct_answer": "A"
    },
    {
        "question_text": "Scrum is a type of:",
        "option_a": "Agile framework",
        "option_b": "Chair framework",
        "option_c": "Fan framework",
        "option_d": "Bike framework",
        "correct_answer": "A"
    },
    {
        "question_text": "Daily standup helps in:",
        "option_a": "Team communication",
        "option_b": "Team dancing",
        "option_c": "Team swimming",
        "option_d": "Team cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "Sprints deliver:",
        "option_a": "Working features",
        "option_b": "Working shoes",
        "option_c": "Working fruits",
        "option_d": "Working pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "Product backlog contains:",
        "option_a": "Requirements",
        "option_b": "Snacks",
        "option_c": "Clothes",
        "option_d": "Tools",
        "correct_answer": "A"
    },
    {
        "question_text": "Scrum Master ensures:",
        "option_a": "Process flow",
        "option_b": "Wind flow",
        "option_c": "Water flow",
        "option_d": "Air flow",
        "correct_answer": "A"
    },
    {
        "question_text": "Retrospectives help in:",
        "option_a": "Improvement",
        "option_b": "Decoration",
        "option_c": "Navigation",
        "option_d": "Conversation",
        "correct_answer": "A"
    },
    {
        "question_text": "Kanban visualizes:",
        "option_a": "Workflow",
        "option_b": "Rainflow",
        "option_c": "Hairflow",
        "option_d": "Bikeflow",
        "correct_answer": "A"
    },
    {
        "question_text": "Agile prefers:",
        "option_a": "Flexibility",
        "option_b": "Humidity",
        "option_c": "Electricity",
        "option_d": "Velocity",
        "correct_answer": "A"
    },
    {
        "question_text": "User stories describe:",
        "option_a": "User requirements",
        "option_b": "User clothes",
        "option_c": "User shoes",
        "option_d": "User fruits",
        "correct_answer": "A"
    }
],
118: [
    {
        "question_text": "API stands for:",
        "option_a": "Application Programming Interface",
        "option_b": "Apple Pie Ingredient",
        "option_c": "Air Pressure Index",
        "option_d": "Audio Power Input",
        "correct_answer": "A"
    },
    {
        "question_text": "API testing ensures:",
        "option_a": "Functionality",
        "option_b": "Fashion",
        "option_c": "Friction",
        "option_d": "Flavor",
        "correct_answer": "A"
    },
    {
        "question_text": "Postman is used for:",
        "option_a": "API testing",
        "option_b": "Shoe polishing",
        "option_c": "Garden watering",
        "option_d": "Room cooling",
        "correct_answer": "A"
    },
    {
        "question_text": "Status code 200 means:",
        "option_a": "Success",
        "option_b": "Failure",
        "option_c": "Rain",
        "option_d": "Snow",
        "correct_answer": "A"
    },
    {
        "question_text": "Status code 404 means:",
        "option_a": "Not found",
        "option_b": "Found shoes",
        "option_c": "Found bikes",
        "option_d": "Found plants",
        "correct_answer": "A"
    },
    {
        "question_text": "Authentication verifies:",
        "option_a": "User identity",
        "option_b": "User height",
        "option_c": "User color",
        "option_d": "User weight",
        "correct_answer": "A"
    },
    {
        "question_text": "A GET request:",
        "option_a": "Fetches data",
        "option_b": "Deletes data",
        "option_c": "Paints data",
        "option_d": "Washes data",
        "correct_answer": "A"
    },
    {
        "question_text": "A POST request:",
        "option_a": "Creates data",
        "option_b": "Cleans data",
        "option_c": "Dries data",
        "option_d": "Moves data",
        "correct_answer": "A"
    },
    {
        "question_text": "Swagger is used for:",
        "option_a": "API documentation",
        "option_b": "Car polishing",
        "option_c": "Fan cleaning",
        "option_d": "Window fixing",
        "correct_answer": "A"
    },
    {
        "question_text": "JSON is:",
        "option_a": "Data format",
        "option_b": "Music format",
        "option_c": "Fuel type",
        "option_d": "Paint type",
        "correct_answer": "A"
    }
],
117: [
    {
        "question_text": "Unit tests test:",
        "option_a": "Small code blocks",
        "option_b": "Small shoes",
        "option_c": "Small rooms",
        "option_d": "Small trees",
        "correct_answer": "A"
    },
    {
        "question_text": "unittest is a:",
        "option_a": "Python testing framework",
        "option_b": "Python washing machine",
        "option_c": "Python painting kit",
        "option_d": "Python driving tool",
        "correct_answer": "A"
    },
    {
        "question_text": "assertEqual checks:",
        "option_a": "Equality",
        "option_b": "Speed",
        "option_c": "Color",
        "option_d": "Weight",
        "correct_answer": "A"
    },
    {
        "question_text": "Test cases are written in:",
        "option_a": "Classes",
        "option_b": "Cars",
        "option_c": "Shoes",
        "option_d": "Beds",
        "correct_answer": "A"
    },
    {
        "question_text": "Mocks simulate:",
        "option_a": "External systems",
        "option_b": "External plants",
        "option_c": "External shoes",
        "option_d": "External pillows",
        "correct_answer": "A"
    },
    {
        "question_text": "pytest is:",
        "option_a": "A testing tool",
        "option_b": "A cooking tool",
        "option_c": "A driving tool",
        "option_d": "A cleaning tool",
        "correct_answer": "A"
    },
    {
        "question_text": "setUp runs:",
        "option_a": "Before tests",
        "option_b": "After lunch",
        "option_c": "After sleep",
        "option_d": "Before movies",
        "correct_answer": "A"
    },
    {
        "question_text": "tearDown runs:",
        "option_a": "After tests",
        "option_b": "After swimming",
        "option_c": "After painting",
        "option_d": "After shopping",
        "correct_answer": "A"
    },
    {
        "question_text": "Tests improve:",
        "option_a": "Code quality",
        "option_b": "Room quality",
        "option_c": "Shoe quality",
        "option_d": "Water quality",
        "correct_answer": "A"
    },
    {
        "question_text": "CI tools run tests:",
        "option_a": "Automatically",
        "option_b": "Manually",
        "option_c": "Slowly",
        "option_d": "Randomly",
        "correct_answer": "A"
    }
],
116: [
    {
        "question_text": "Software testing ensures:",
        "option_a": "Quality",
        "option_b": "Quantity",
        "option_c": "Velocity",
        "option_d": "Humidity",
        "correct_answer": "A"
    },
    {
        "question_text": "Manual testing is done:",
        "option_a": "By humans",
        "option_b": "By robots",
        "option_c": "By cars",
        "option_d": "By birds",
        "correct_answer": "A"
    },
    {
        "question_text": "Automation testing is done using:",
        "option_a": "Tools",
        "option_b": "Shoes",
        "option_c": "Pillows",
        "option_d": "Mirrors",
        "correct_answer": "A"
    },
    {
        "question_text": "Bug is a:",
        "option_a": "Defect",
        "option_b": "Design",
        "option_c": "Decision",
        "option_d": "Decoration",
        "correct_answer": "A"
    },
    {
        "question_text": "Test cases describe:",
        "option_a": "Steps to test",
        "option_b": "Steps to cook",
        "option_c": "Steps to walk",
        "option_d": "Steps to dance",
        "correct_answer": "A"
    },
    {
        "question_text": "Regression testing checks:",
        "option_a": "Existing features",
        "option_b": "Existing shoes",
        "option_c": "Existing chairs",
        "option_d": "Existing bags",
        "correct_answer": "A"
    },
    {
        "question_text": "Performance testing measures:",
        "option_a": "Speed",
        "option_b": "Height",
        "option_c": "Width",
        "option_d": "Weight",
        "correct_answer": "A"
    },
    {
        "question_text": "Load testing checks:",
        "option_a": "High user traffic",
        "option_b": "High water flow",
        "option_c": "High wind flow",
        "option_d": "High bird flow",
        "correct_answer": "A"
    },
    {
        "question_text": "Selenium is a:",
        "option_a": "Automation tool",
        "option_b": "Baking tool",
        "option_c": "Painting tool",
        "option_d": "Driving tool",
        "correct_answer": "A"
    },
    {
        "question_text": "Testing improves:",
        "option_a": "Reliability",
        "option_b": "Electricity",
        "option_c": "Humidity",
        "option_d": "Lighting",
        "correct_answer": "A"
    }
],
115: [
    {
        "question_text": "Linux is a:",
        "option_a": "Operating system",
        "option_b": "Gaming system",
        "option_c": "Sleeping system",
        "option_d": "Cooling system",
        "correct_answer": "A"
    },
    {
        "question_text": "The Linux terminal is used for:",
        "option_a": "Commands",
        "option_b": "Paintings",
        "option_c": "Photos",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "The root user has:",
        "option_a": "Full permissions",
        "option_b": "Half permissions",
        "option_c": "No permissions",
        "option_d": "Light permissions",
        "correct_answer": "A"
    },
    {
        "question_text": "mkdir creates:",
        "option_a": "Directories",
        "option_b": "Cars",
        "option_c": "Plants",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "ls lists:",
        "option_a": "Files",
        "option_b": "Chairs",
        "option_c": "Fans",
        "option_d": "Lights",
        "correct_answer": "A"
    },
    {
        "question_text": "cd changes:",
        "option_a": "Directory",
        "option_b": "Weather",
        "option_c": "Color",
        "option_d": "Height",
        "correct_answer": "A"
    },
    {
        "question_text": "pwd prints:",
        "option_a": "Current path",
        "option_b": "Current noise",
        "option_c": "Current smell",
        "option_d": "Current taste",
        "correct_answer": "A"
    },
    {
        "question_text": "rm deletes:",
        "option_a": "Files",
        "option_b": "Fruits",
        "option_c": "Shoes",
        "option_d": "Fans",
        "correct_answer": "A"
    },
    {
        "question_text": "chmod changes:",
        "option_a": "Permissions",
        "option_b": "Weather",
        "option_c": "Distance",
        "option_d": "Volume",
        "correct_answer": "A"
    },
    {
        "question_text": "Linux is known for:",
        "option_a": "Security",
        "option_b": "Humidity",
        "option_c": "Wind",
        "option_d": "Dust",
        "correct_answer": "A"
    }
],
114: [
    {
        "question_text": "Git is used for:",
        "option_a": "Version control",
        "option_b": "Temperature control",
        "option_c": "Volume control",
        "option_d": "Speed control",
        "correct_answer": "A"
    },
    {
        "question_text": "A repository stores:",
        "option_a": "Code",
        "option_b": "Cakes",
        "option_c": "Cars",
        "option_d": "Clothes",
        "correct_answer": "A"
    },
    {
        "question_text": "git clone copies:",
        "option_a": "A repository",
        "option_b": "A refrigerator",
        "option_c": "A pillow",
        "option_d": "A shoe",
        "correct_answer": "A"
    },
    {
        "question_text": "git commit saves:",
        "option_a": "Changes",
        "option_b": "Songs",
        "option_c": "Photos",
        "option_d": "Shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "git push uploads:",
        "option_a": "Local commits",
        "option_b": "Local chairs",
        "option_c": "Local plants",
        "option_d": "Local fruits",
        "correct_answer": "A"
    },
    {
        "question_text": "Branches help in:",
        "option_a": "Parallel development",
        "option_b": "Parallel swimming",
        "option_c": "Parallel cooking",
        "option_d": "Parallel sleeping",
        "correct_answer": "A"
    },
    {
        "question_text": "Pull request is used for:",
        "option_a": "Code review",
        "option_b": "Food review",
        "option_c": "Hotel review",
        "option_d": "Book review",
        "correct_answer": "A"
    },
    {
        "question_text": "GitHub is a:",
        "option_a": "Code hosting platform",
        "option_b": "Food hosting platform",
        "option_c": "Game hosting platform",
        "option_d": "Bike hosting platform",
        "correct_answer": "A"
    },
    {
        "question_text": "git merge combines:",
        "option_a": "Branches",
        "option_b": "Vegetables",
        "option_c": "Shoes",
        "option_d": "Plants",
        "correct_answer": "A"
    },
    {
        "question_text": "git status shows:",
        "option_a": "Repo status",
        "option_b": "Weather status",
        "option_c": "Light status",
        "option_d": "Fan status",
        "correct_answer": "A"
    }
],
113: [
    {
        "question_text": "Power BI is used for:",
        "option_a": "Data visualization",
        "option_b": "Room decoration",
        "option_c": "Shoe polishing",
        "option_d": "Plant watering",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI dashboards display:",
        "option_a": "Insights",
        "option_b": "Music",
        "option_c": "Perfume",
        "option_d": "Heat",
        "correct_answer": "A"
    },
    {
        "question_text": "DAX is used for:",
        "option_a": "Calculations",
        "option_b": "Cooking",
        "option_c": "Dancing",
        "option_d": "Driving",
        "correct_answer": "A"
    },
    {
        "question_text": "Power Query helps in:",
        "option_a": "Data cleaning",
        "option_b": "Cloth cleaning",
        "option_c": "Shoe cleaning",
        "option_d": "Room cleaning",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI can connect to:",
        "option_a": "Multiple data sources",
        "option_b": "Multiple shoes",
        "option_c": "Multiple fans",
        "option_d": "Multiple cups",
        "correct_answer": "A"
    },
    {
        "question_text": "Reports allow:",
        "option_a": "Detailed analysis",
        "option_b": "Detailed cooking",
        "option_c": "Detailed ironing",
        "option_d": "Detailed washing",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI service is:",
        "option_a": "Cloud-based",
        "option_b": "Shoe-based",
        "option_c": "Plant-based",
        "option_d": "Wood-based",
        "correct_answer": "A"
    },
    {
        "question_text": "Data models define:",
        "option_a": "Relationships",
        "option_b": "Friendships",
        "option_c": "Partnerships",
        "option_d": "Memberships",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI supports:",
        "option_a": "Interactive visuals",
        "option_b": "Interactive music",
        "option_c": "Interactive pillows",
        "option_d": "Interactive shoes",
        "correct_answer": "A"
    },
    {
        "question_text": "Power BI is widely used in:",
        "option_a": "Business analytics",
        "option_b": "Bike analytics",
        "option_c": "Plant analytics",
        "option_d": "Fan analytics",
        "correct_answer": "A"
    }
],

        
        
        }
        for course_id, questions in DATA.items():
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Course {course_id} not found"))
                continue

            for q in questions:
                Question.objects.create(course=course, **q)

            self.stdout.write(self.style.SUCCESS(f"Inserted {len(questions)} questions into course {course_id}"))
