from collections import Counter
word_set = """ Technical Management - Data for Learning and Thought Leadership
•	Lead the implementation of a strategy for imPact (Pact’s instance of DHIS2) design, usage and data for decision making
•	Support Pact leadership to resource and utilize imPact, ensuring imPact meets organizational and strategic needs including that of data analytics
•	Create and maintain standard operating procedures for database configuration, user management, data access, dashboard management, and data usage and promote organization-wide knowledge of these SOPs and monitor adherence
•	Provide regular updates on progress of system implementation and support senior leadership in leveraging imPact as part of Pact’s strategic priority 2: re-imagine impact delivery and strategic priority 3: influence markets. Document and share learnings from data systems implementation process.
•	Build a culture of data usage by socializing imPact within the organization, providing appropriate updates and resources to users throughout the organization
•	Assist Pact to roll out the use of innovative and complimentary technologies such as GIS, mobile data collection and techniques for visualizing data to improve MERL practice as part of Pact’s strategic priority 2: re-imagine impact delivery
•	Ensure Pact projects have the necessary information to make informed decisions about use of appropriate M&E technology.
•	Manage data warehousing within the Organization
Development and Maintenance of Information Systems
•	Lead the roll out of imPact to manage, analyze and report on Pact’s overall results and effectiveness
•	Ensure imPact administration needs are met: server functionality, bug fixes, user access and security, configuration modifications, bulk data upload, analytics.
•	Lead configuration for DHIS2 instances of simple project sites to meet project needs, ensuring standard system architecture, maintaining user access and groups, assisting in training and capacity building of country level staff.
•	Delegate tasks and supervise quality of Global imPact team (dispersed talent) as needed.
•	Quality assurance of imPact database including ensuring that inbuilt quality controls, data aggregation scripts, linkages between sites etc. are functioning properly
•	Analyze systems performance, identify challenges, troubleshoot and produce regular system performance reports
•	Continuously review and analyze data for quality standards and highlight any issues arising to the Country MEL and Results and Measurements team for action
User Training and Provision of Technical Assistance
•	Provide technical assistance and advice to country offices in planning for and managing their transition to and proper usage of imPact and data for learning
•	Design and deliver trainings on data entry, data analysis, visualization and interpretation, system administration, database configuration
•	Participate in academic and professional conferences to publicize Pact’s imPact experience, data use and learning
•	Serve as a thought leader and internal resource on data system implementation and appropriate usage
Basic Requirements
•	Bachelor’s Degree in Health Informatics, Computer Science, Computer Engineering, Data Science or related fields and nine (9) years’ experience or a Master’s Degree Health Informatics, Computer Science, Computer Engineering, Data Science or related fields and seven (7) years of experience. Experience will include working with international development programs and MERL systems, with at least two (2) years in a low-resource setting
•	Demonstrated expertise in DHIS2 and cloud-based data management, at least five (5) years of experience in system roll-out, configuration and usage
•	Proven ability to strategize, train and socialize on uptake of a new system
•	Demonstrated knowledge and experience in international health, livelihoods and economic opportunities, capacity development, and/or governance
•	Strong working knowledge of MERL principles, including qualitative and quantitative data collection and analysis, tracking outcome indicators, and design of program evaluations using mixed methods
•	Ability to link MERL and technology skills and knowledge to leverage the power of a new system
•	Strong data mining, analytics, and visualization skills using STATA, PowerBI ; with experience with programming language(s) (R, Python, SPSS modeler) is a plus
•	A strong understanding and working knowledge of database design and conceptualization
•	Strong facilitation, teaching and coaching skills
•	Ability to work independently, be accountable for a new system, and to perform and prioritize multiple tasks
•	Ability to establish and sustain interpersonal and professional relationships with Pact staff, donor organizations, and peer organizations
•	Experience doing M&E for USAID, DFID, and other bilateral donors and/or foundations
Preferred Qualifications
•	Experience in data analytics and synthesizing disparate datasets for predictive analytics and improving organizational and programmatic efficiencies
•	Fluency in relevant languages (for example, French)
•	Experience with qualitative analysis software, GIS systems, and/or data visualization software (NVivo, ArcGIS, Power BI, Tableau, etc.)
•	Experience developing web-based and mobile applications, web-oriented programming language (e.g. Java, Java Script), and Unix/Linux system management
•	Working knowledge of database management systems SQL server or MySQL is a plus
  """
word_list = word_set.split()

# Get the count of each word.
word_count = Counter(word_list)

# Use most_common() method from Counter subclass
print(word_count.most_common(100))