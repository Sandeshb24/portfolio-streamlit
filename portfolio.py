import streamlit as st
import requests
import time # For simulating delays in animations
from streamlit_lottie import st_lottie
from PIL import Image # For local images, if you use them

# --- CONFIGURATIONS ---
st.set_page_config(page_title="My Animated Portfolio", page_icon=":rocket:", layout="centered")

# --- HELPER FUNCTIONS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to inject custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- LOAD ASSETS (Lottie animations, Images) ---
# You can find Lottie animations at lottiefiles.com
lottie_hello = load_lottieurl("https://lottiefiles.com/animations/robot-developer-1WbL1gNqL2") # Animated greeting
lottie_skills = load_lottieurl("https://lottiefiles.com/animations/skills-development-rO0iJd7wz4") # For skills section
lottie_projects = load_lottieurl("https://lottiefiles.com/animations/coding-work-1j3C9G5fW6") # For projects section
lottie_contact = load_lottieurl("https://lottiefiles.com/animations/email-send-Q3bJ7Qk2eB") # For contact section

# Local Images (uncomment and replace with your image paths)
# img_project1 = Image.open("images/project1.png")
# img_project2 = Image.open("images/project2.png")
# img_profile = Image.open("images/your_profile_picture.jpg") # Optional profile picture

# --- Inject Custom CSS (for subtle hover effects, etc.) ---
# Create a file named 'style.css' in the same directory as your app.py
# and add the CSS code below into it.
local_css("style.css")

# --- HEADER SECTION ---
with st.container():
    col1, col2 = st.columns([2, 1]) # Adjust column width for text and Lottie
    with col1:
        # If you have a profile picture, you can display it here
        # st.image(img_profile, width=150)
        st.subheader("Hi, I am [Your Name] 👋", anchor="home") # Added anchor for navigation
        st.title("A [Your Profession/Role] from India")
        st.write(
            "I am passionate about [Your Passion/Domain, e.g., building data-driven applications, creating engaging web experiences, solving complex problems with code]."
        )
        st.markdown(
            """
            <div class="social-links">
                <a href="https://yourwebsite.com/about" target="_blank" class="hover-grow">Learn More</a> | 
                <a href="https://linkedin.com/in/yourprofile" target="_blank" class="hover-grow">LinkedIn</a> | 
                <a href="https://github.com/yourgithub" target="_blank" class="hover-grow">GitHub</a>
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        if lottie_hello:
            st_lottie(lottie_hello, height=250, key="hello_animation") # Adjusted height for better fit
        else:
            st.info("Lottie 'hello' animation failed to load. Check the URL.")

# --- ABOUT ME SECTION ---
with st.container():
    st.write("---") # Separator
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me", anchor="about") # Added anchor
        st.write("##") # Space
        st.write(
            """
            I am a highly motivated and results-oriented [Your Profession/Role] with X years of experience in [Your Area of Expertise, e.g., Python development, machine learning, web development].
            My journey into technology began when [brief story, e.g., I built my first small app, I got fascinated by data].

            I thrive on turning complex challenges into elegant, efficient, and user-friendly solutions.
            I am always eager to learn new technologies and improve my skills, believing in continuous growth and collaboration.
            """
        )
        # Adding a button that shows a simulated download progress
        if st.button("Download My Resume (Simulated)", key="download_resume"):
            with st.status("Downloading resume...", expanded=True) as status:
                st.write("Initiating download...")
                time.sleep(1)
                st.write("Verifying file integrity...")
                time.sleep(0.5)
                st.write("Almost done...")
                time.sleep(1.5)
                status.update(label="Download Complete!", state="complete", icon="✅")
            st.success("Resume downloaded successfully! (This is a simulation)")
            st.toast("Resume downloaded!", icon="⬇️") # Small toast notification
            # In a real app, you'd trigger a file download here.
            # Example for actual download if you have a file:
            # with open("path/to/your_resume.pdf", "rb") as file:
            #     st.download_button(
            #         label="Click to Download (Actual)",
            #         data=file,
            #         file_name="your_resume.pdf",
            #         mime="application/pdf"
            #     )

    with right_column:
        # Reusing the coding animation or use a different one
        if lottie_skills: # Using skills animation here for diversity
            st_lottie(lottie_skills, height=300, key="about_animation")
        else:
            st.info("Lottie animation failed to load. Check the URL.")

# --- SKILLS SECTION ---
with st.container():
    st.write("---")
    st.header("My Skills", anchor="skills") # Added anchor
    st.write("##")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming Languages")
        st.markdown("""
        - Python (Advanced)
        - SQL
        - JavaScript (Intermediate)
        - R (Basic)
        """)
    with col2:
        st.subheader("Frameworks & Libraries")
        st.markdown("""
        - Streamlit
        - Pandas, NumPy, Scikit-learn
        - TensorFlow / PyTorch
        - Flask / Django (if applicable)
        - React (if applicable)
        """)
    with col3:
        st.subheader("Tools & Platforms")
        st.markdown("""
        - Git, GitHub
        - Docker
        - AWS / GCP / Azure (basic)
        - VS Code
        - Jupyter Notebooks
        """)
    st.write("---")

# --- PROJECTS SECTION ---
with st.container():
    st.header("My Projects", anchor="projects") # Added anchor
    st.write("##")

    # Adding a Lottie animation for projects
    project_lottie_col, project_content_col = st.columns([1, 2])
    with project_lottie_col:
        if lottie_projects:
            st_lottie(lottie_projects, height=200, key="projects_animation")
        else:
            st.info("Lottie projects animation failed to load.")
    with project_content_col:
        st.write("Here are some of the projects I've worked on, showcasing my skills and passion.")

    st.write("---")

    # Project 1 with a simulated animated progress
    st.subheader("1. Interactive Dashboard with Streamlit")
    st.write(
        """
        **Description:** Developed a dynamic dashboard to visualize sales data, allowing users to filter by date range, product category, and region.
        Utilized Pandas for data processing and Plotly for interactive visualizations.
        """
    )
    st.markdown("[View Code >](https://github.com/yourgithub/dashboard-project)"
                " | [Live Demo >](https://yourdashboard.streamlit.app)")

    # Simulate a project loading animation
    if st.button("Simulate Dashboard Load", key="load_dashboard_btn"):
        with st.spinner('Loading dashboard components...'):
            time.sleep(2) # Simulate network delay or complex computation
        st.success('Dashboard components loaded!')
        st.balloons() # Small celebratory animation

    st.write("---")

    st.subheader("2. Machine Learning Model for Customer Churn Prediction")
    st.write(
        """
        **Description:** Built and deployed a customer churn prediction model using scikit-learn.
        Preprocessed customer data, trained a classification model (e.g., RandomForest), and evaluated its performance.
        """
    )
    st.markdown("[View Code >](https://github.com/yourgithub/churn-prediction)"
                " | [Read Blog Post (if any) >](https://yourblog.com/churn-prediction-post)")

    # Example of a dynamic progress bar for a hypothetical model training
    if st.button("Simulate Model Training", key="train_model_btn"):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=f"{progress_text} {percent_complete + 1}%")
        st.success("Model training complete!")
        st.snow() # Another celebratory animation

    st.write("---")

    st.subheader("3. Web Scraping Tool for Research")
    st.write(
        """
        **Description:** Created a Python script using Beautiful Soup and Requests to extract specific data from multiple websites for academic research purposes.
        Included error handling and data storage in CSV format.
        """
    )
    st.markdown("[View Code >](https://github.com/yourgithub/web-scraper)")
    st.write("---")

# --- CONTACT SECTION ---
with st.container():
    st.write("---")
    st.header("Get In Touch!", anchor="contact") # Added anchor
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/your.email@example.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        if lottie_contact:
            st_lottie(lottie_contact, height=300, key="contact_animation")
        else:
            st.info("Lottie contact animation failed to load. Check the URL.")

# --- SIDEBAR NAVIGATION ---
# This uses Streamlit's built-in sidebar.
# For smooth scrolling to sections with 'anchors', we'll use JavaScript
# injected via `st.markdown`.
st.sidebar.title("Navigation")
st.sidebar.markdown("---")

# Define unique IDs for sections to scroll to
# These correspond to the `anchor` attribute we added to st.header/st.subheader
sections = {
    "Home": "home",
    "About Me": "about",
    "Skills": "skills",
    "Projects": "projects",
    "Contact": "contact"
}

for section_name, section_id in sections.items():
    if st.sidebar.button(section_name, key=f"nav_{section_id}"):
        # Inject JavaScript to scroll to the element with the given ID
        st.markdown(
            f"""
            <script>
                document.getElementById("{section_id}").scrollIntoView({{behavior: "smooth", block: "start"}});
            </script>
            """,
            unsafe_allow_html=True
        )

# --- Custom CSS (save this in a file named `style.css` in the same directory) ---
# This CSS will provide subtle hover effects for links and buttons,
# and some basic styling for the form.
st.markdown("""
<style>
/* Basic styling for the contact form */
input[type=text], input[type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    resize: vertical;
    background-color: #f8f8f8; /* Light background */
    color: #333; /* Dark text */
    font-family: 'Roboto', sans-serif; /* Use a common font */
}

button[type=submit] {
    background-color: #4CAF50; /* Green submit button */
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s ease; /* Smooth transition on hover */
}

button[type=submit]:hover {
    background-color: #45a049; /* Darker green on hover */
}

/* Streamlit button specific styling (Applies to all st.button) */
.stButton button {
    background-color: #007bff; /* Blue */
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease; /* Smooth transition and slight scale */
}

.stButton button:hover {
    background-color: #0056b3; /* Darker blue on hover */
    transform: translateY(-2px); /* Slight lift effect */
}

/* Custom class for social links */
.social-links a {
    color: #007bff; /* Blue link color */
    text-decoration: none;
    margin-right: 15px;
    transition: color 0.3s ease, transform 0.2s ease;
    display: inline-block; /* Essential for transform to work */
}

.social-links a:hover {
    color: #0056b3; /* Darker blue on hover */
    transform: scale(1.05); /* Slight grow effect */
}

/* Optional: Add a subtle fade-in animation for containers on load */
/* This is more complex and might require JavaScript observer APIs for true scroll-based animation */
/* For a simple fade-in on app load, you can target .stApp directly, but it applies to everything */
/*
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
.stApp {
    animation: fadeIn 1s ease-in-out;
}
*/

/* Adjust Streamlit's default container padding if needed */
.stApp {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True) # Ensure this is always at the end or in a separate file loaded by local_css()
