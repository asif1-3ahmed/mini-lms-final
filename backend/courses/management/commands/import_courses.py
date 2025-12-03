from django.core.management.base import BaseCommand
from courses.models import Course
from django.utils.timezone import now

class Command(BaseCommand):
    help = "Bulk Import 50+ Courses Into Database"

    def handle(self, *args, **kwargs):
        admin_user = 1  # assuming admin user ID = 1 in DB

        courses = [
            ("Python for Beginners", "Learn Python basics, loops, functions", "6 weeks", "Programming"),
            ("Advanced Python", "Deep dive into generators, threading, async", "8 weeks", "Programming"),
            ("Django Basics", "Learn Django backend fundamentals", "5 weeks", "Backend"),
            ("Django REST API", "Build APIs using Django Rest Framework", "6 weeks", "Backend"),
            ("React for Beginners", "Learn React components, props, state", "5 weeks", "Frontend"),
            ("Advanced React", "Hooks, performance optimization", "7 weeks", "Frontend"),
            ("JavaScript Mastery", "Full JS guide from basics to advanced", "4 weeks", "Programming"),
            ("TypeScript Basics", "Learn TS interfaces, types", "3 weeks", "Frontend"),
            ("Full Stack Web Dev", "HTML, CSS, React, Django", "12 weeks", "Web"),
            ("SQL for Beginners", "Database basics, queries", "4 weeks", "Database"),
            ("Advanced SQL", "Joins, indexing, optimization", "6 weeks", "Database"),
            ("PostgreSQL Master", "Everything about PostgreSQL", "8 weeks", "Database"),
            ("MongoDB Basics", "NoSQL fundamentals", "3 weeks", "Database"),
            ("Machine Learning (ML) Intro", "Learn ML fundamentals", "6 weeks", "AI"),
            ("Deep Learning Basics", "Neural networks fundamentals", "8 weeks", "AI"),
            ("Data Science with Python", "Pandas, NumPy, data analysis", "10 weeks", "Data"),
            ("AI for Everyone", "Basic AI concepts", "4 weeks", "AI"),
            ("DevOps Basics", "Deployment, CI/CD fundamentals", "6 weeks", "DevOps"),
            ("AWS Cloud Practitioner", "Basics of AWS services", "6 weeks", "Cloud"),
            ("Advanced AWS", "EC2, Lambda, deployment", "8 weeks", "Cloud"),
            ("Azure Basics", "Intro to Microsoft Azure", "5 weeks", "Cloud"),
            ("Cloud Computing Mastery", "AWS + Azure", "12 weeks", "Cloud"),
            ("Cybersecurity Basics", "Security fundamentals", "6 weeks", "Security"),
            ("Ethical Hacking", "Hacking fundamentals", "8 weeks", "Security"),
            ("Networking Basics", "Computer networks intro", "4 weeks", "Networking"),
            ("Advanced Networking", "Routing, switching", "6 weeks", "Networking"),
            ("Blockchain Intro", "Basics of blockchain", "6 weeks", "Emerging Tech"),
            ("Advanced Blockchain", "Smart contracts, crypto", "10 weeks", "Emerging Tech"),
            ("Solidity Basics", "Intro to smart contract coding", "5 weeks", "Blockchain"),
            ("AR/VR Development", "Augmented reality basics", "8 weeks", "Emerging Tech"),
            ("AR/VR Advanced", "Build AR/VR apps", "12 weeks", "Emerging Tech"),
            ("C Basics", "Intro to C programming", "4 weeks", "Programming"),
            ("C++ Basics", "Intro to CPP", "4 weeks", "Programming"),
            ("Advanced C++", "OOP, STL", "6 weeks", "Programming"),
            ("Java Basics", "Intro to Java programming", "6 weeks", "Programming"),
            ("Advanced Java", "Spring Boot basics", "8 weeks", "Backend"),
            ("Spring Boot Intro", "REST APIs, DB integration", "8 weeks", "Backend"),
            ("Docker Basics", "Containers fundamentals", "3 weeks", "DevOps"),
            ("Kubernetes Basics", "Container orchestration", "5 weeks", "Cloud"),
            ("Big Data Intro", "Hadoop, Spark basics", "8 weeks", "Data"),
            ("Advanced Big Data", "Real-time analytics", "12 weeks", "Data"),
            ("Git & GitHub", "Version control", "2 weeks", "Tools"),
            ("DSA Basics", "Data structures, algorithms", "6 weeks", "CS"),
            ("Advanced DSA", "Solve DSA problems", "10 weeks", "CS"),
            ("Operating System Basics", "OS fundamentals", "4 weeks", "CS"),
            ("Advanced OS", "Processes, threads, memory", "6 weeks", "CS"),
            ("Computer Architecture", "CPU, memory, I/O", "5 weeks", "CS"),
            ("Software Engineering", "SDLC basics", "3 weeks", "CS"),
            ("Agile Methodology", "Agile project basics", "2 weeks", "Management"),
            ("UI/UX Basics", "Design fundamentals", "4 weeks", "Design"),
            ("Figma Mastery", "App prototyping", "5 weeks", "Design"),
            ("Figma for Beginners", "Basics of Figma tool", "3 weeks", "Design"),
            ("Advanced Figma", "Auto layouts, Prototyping", "4 weeks", "Design"),
            ("Photoshop Basics", "Intro to Photoshop", "2 weeks", "Design"),
            ("Canva Design", "Design using Canva", "2 weeks", "Design"),
            ("3D with Blender", "Intro to 3D using Blender", "10 weeks", "Design"),
            ("Unity Game Dev", "Game development with Unity", "10 weeks", "Game"),
            ("Unreal Game Dev", "Intro to Unreal engine", "12 weeks", "Game"),
            ("Game Dev with Godot", "Intro to Godot", "8 weeks", "Game"),
            ("Mobile App Dev", "Flutter basics", "6 weeks", "Mobile"),
            ("Advanced Flutter", "State, APIs Flutter", "10 weeks", "Mobile")
        ]

        for title, description, duration, category in courses:
            if not Course.objects.filter(title=title).exists():
                Course.objects.create(
                    title=title,
                    description=description,
                    duration=duration,
                    category=category,
                    overview="Coming soon",
                    skills=[],
                    modules=[],
                    career_paths=[],
                    roadmap=[],
                    faq=[],
                    created_by_id=admin_user,
                    created_at=now()
                )
                self.stdout.write(self.style.SUCCESS(f"✔ Added: {title}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠ Already exists: {title}"))

        self.stdout.write(self.style.SUCCESS("✅ 50+ Courses Imported Successfully!"))
