from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.college_chatbot
collection = db.qa


# Define sample data representing intents, questions, and responses
sample_data = [
    {
        "intent": "Admissions",
        "questions": [
            "How can I apply for admission?",
            "What is the admission procedure?",
            "When is the application deadline?"
        ],
       "response": "Admissions to DrMCET are based on merit and entrance examination scores. Prospective students can apply online through the college website during the specified application period. Admission requirements vary depending on the program applied for, but typically include academic qualifications, entrance exam scores, and any specific eligibility criteria set by the college or university."
    },
    {
        "intent": "Courses",
        "questions": [
            "What courses are offered in the Computer Science department?",
            "Can you tell me about the courses in the Biology department?"
        ],
       "response": "DrMCET offers a wide range of undergraduate and postgraduate programs in engineering disciplines such as Civil Engineering, Mechanical Engineering, Electrical and Electronics Engineering, Computer Science and Engineering, and Electronics and Communication Engineering. Additionally, the college offers MBA and MCA programs for management and computer applications enthusiasts."
    },
    {
        "intent": "Registrar",
        "questions": [
            "What are the office hours of the registrar?",
            "Where is the registrar's office located?"
        ],
        "response": "The registrar's office is open from 9 AM to 5 PM, Monday to Friday."
    },
    {
        "intent": "Financial Aid",
        "questions": [
            "How can I apply for financial aid?",
            "What types of financial aid are available?",
            "What are the requirements for receiving financial aid?"
        ],
        "response": "To apply for financial aid, you need to fill out the FAFSA form. We offer scholarships, grants, and student loans based on eligibility criteria."
    },
    {
        "intent": "Campus Facilities",
        "questions": [
            "Can you tell me about the campus facilities?",
            "Where can I find the library on campus?",
            "What sports facilities are available?"
        ],
        "response": "Our campus offers state-of-the-art facilities including libraries, sports complexes, gymnasiums, and recreational areas. The library is located in the central campus area near the academic buildings."
    },
    {
        "intent": "Housing",
        "questions": [
            "How can I apply for on-campus housing?",
            "What are the different housing options available?",
            "Are there any housing requirements for freshmen?"
        ],
        "response": "To apply for on-campus housing, you need to fill out a housing application form. We offer various housing options including dormitories, apartments, and themed housing. Freshmen are required to live on campus for their first year."
    },
    {
        "intent": "Admissions Events",
        "questions": [
            "Are there any upcoming admissions events or tours?",
            "Can I schedule a campus visit?",
            "Do you offer virtual tours for prospective students?"
        ],
        "response": "Yes, we regularly host admissions events and campus tours. You can schedule a campus visit through our website. We also offer virtual tours for prospective students who are unable to visit in person."
    },
    {
        "intent": "Academic Advising",
        "questions": [
            "How can I get academic advising?",
            "Who can I talk to about choosing my major?",
            "Are there resources available for academic support?"
        ],
        "response": "We provide academic advising services to all students. You can schedule an appointment with an academic advisor through our student portal. Additionally, we have resources such as tutoring centers and study groups for academic support."
    },
    {
        "intent": "Student Life",
        "questions": [
            "What is student life like on campus?",
            "Are there any student clubs or organizations?",
            "Can you tell me about campus events and activities?"
        ],
        "response": "Student life on campus is vibrant and diverse. We have a wide range of student clubs and organizations covering various interests and hobbies. Additionally, there are frequent campus events including cultural festivals, guest lectures, and sports competitions."
    },
    {
        "intent": "International Students",
        "questions": [
            "What support services are available for international students?",
            "Are there English language proficiency requirements for international students?",
            "Can you provide information on obtaining a student visa?"
        ],
        "response": "We offer support services tailored to the needs of international students, including orientation programs, visa assistance, and English language courses. International students are required to demonstrate English language proficiency through standardized tests such as TOEFL or IELTS. We can provide guidance on obtaining a student visa."
    },
    {
        "intent": "Transfer Students",
        "questions": [
            "What is the process for transferring to your college?",
            "Are there specific requirements for transfer students?",
            "Can I transfer credits from my previous college?"
        ],
        "response": "To transfer to our college, you need to submit a transfer application along with your academic transcripts. We consider various factors including your GPA and course compatibility. You may be able to transfer credits from your previous college, subject to evaluation by our admissions office."
    },    {
        "intent": "Library",
        "questions": [
            "What are the library hours?",
            "Where is the library located?",
            "Can I borrow books from other libraries?"
        ],
        "response": "The library is open from 8 AM to 10 PM on weekdays and from 10 AM to 6 PM on weekends. It is located near the main entrance of the campus. Yes, you can borrow books from other libraries through our interlibrary loan service."
    },
    {
        "intent": "Tuition and Fees",
        "questions": [
            "How much is tuition?",
            "What are the additional fees?",
            "Are there any payment plans available?"
        ],
        "response": "Tuition fees vary depending on the program and residency status. You can find detailed information about tuition and fees on our website. Additional fees may include technology fees, student activity fees, and health insurance. We offer payment plans to help students manage their expenses."
    },
    {
        "intent": "Career Services",
        "questions": [
            "What services does the career center offer?",
            "How can I find internships or job opportunities?",
            "Do you provide resume assistance?"
        ],
        "response": "Our career center offers a range of services including resume building, mock interviews, career counseling, and networking events. We have partnerships with local companies and organizations to help students find internships and job opportunities."
    },
    {
        "intent": "Health Services",
        "questions": [
            "Is there a health center on campus?",
            "What medical services are available?",
            "Do you provide mental health counseling?"
        ],
        "response": "Yes, we have a health center on campus staffed with medical professionals. Services include basic medical care, vaccinations, and health education. We also offer mental health counseling services to support students' well-being."
    },
    {
        "intent": "Transportation",
        "questions": [
            "Is there public transportation available near the campus?",
            "Do you offer shuttle services?",
            "Where can I park my car on campus?"
        ],
        "response": "Public transportation options are available near the campus, including bus routes and train stations. We provide shuttle services to nearby areas and parking lots on campus for students, faculty, and staff. Visitors can use designated parking areas."
    }, 
    {
        "intent": "Greetings",
        "questions": ["Hi", "Hello", "Hey", "Good morning", "Good afternoon", "Good evening"],
        "response": "Hello! How can I assist you today?"
    },
    {
        "intent": "Goodbye",
        "questions": ["Goodbye", "Bye", "See you later", "Farewell"],
        "response": "Goodbye! Have a great day!"
    },
    {
        "intent": "About College",
        "questions": [
            "Can you tell me about the history of the college?",
            "What are the notable achievements of the college?",
            "How is the college ranked nationally?"
        ],
        "response": "Dr. Mahalingam College of Engineering and Technology (DrMCET) is a renowned engineering college located in Pollachi, Tamil Nadu, India. Established in 1998, DrMCET offers undergraduate and postgraduate programs in various engineering disciplines, as well as MBA and MCA programs. The college is affiliated with Anna University, Chennai, and approved by AICTE. DrMCET is committed to providing quality education, fostering research, and promoting innovation."
    },
    {
        "intent": "Faculty",
        "questions": [
            "How qualified are the faculty members?",
            "What research areas do the faculty specialize in?",
            "Are there any award-winning professors?"
        ],
        "response": "Our faculty members are highly qualified, with many holding advanced degrees in their fields. They specialize in various research areas such as [IEEE Conferences]. We have several award-winning professors who have been recognized for their contributions to teaching and research."
    },
    {
        "intent": "Facilities",
        "questions": [
            "What facilities does the college offer?",
            "Are there any laboratories or research centers?",
            "How is the campus infrastructure?"
        ],
        "response":"DrMCET provides modern infrastructure and state-of-the-art facilities to support the academic and extracurricular activities of students. The campus features well-equipped laboratories, spacious classrooms, a central library, computer centers, sports facilities, hostels, cafeteria, and medical facilities. The college also offers transportation services for the convenience of students and staff."
    },
    {
        "intent": "Accreditations",
        "questions": [
            "Is the college accredited?",
            "What accrediting bodies has the college received accreditation from?",
            "How does accreditation benefit students?"
        ],
        "response": "Yes, our college is accredited by ANNA University, ensuring that our programs meet high standards of quality and rigor. Accreditation benefits students by providing assurance of the quality of education they receive, enhancing the credibility of their degrees, and facilitating transferability of credits."
    }

]

# Insert sample data into MongoDB collection
collection.insert_many(sample_data)


# Print success message
print("Sample data inserted successfully.")
db.qa.createIndex({ "questions": "text" })