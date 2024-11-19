import streamlit as st

st.set_page_config(layout="wide")

st.title("About Me - Philippe Paulos")

st.write("""
Hey there! 👋 \n
I'm Philippe Paulos, your friendly neighborhood Data Engineer with over 8 years of experience in turning data into insights. 
Let's dive into my story!
""")

st.header("Who Am I?")
st.write("""
By day, I'm a data wizard 🧙‍♂️ working currently at Total Energies in Paris, where I maintain and evolve data pipelines, develop backend applications, and lead projects on Azure, AWS, and Databricks.
By night, I'm a tech enthusiast passionate about innovation and always eager to tackle new challenges. 🚀
""")

st.header("My Journey")
st.write("""
My adventure in the data world began at BNP in Montreuil, where I helped set up a pilot project for banking data collection. Since then, I've hopped around some big french companies like ENEDIS, SFR, Ingenico, AXA France, and Air Liquide, constantly honing my skills in data engineering, cloud computing, and DevOps.

I've had the chance to work with a plethora of technologies including Spark, Kafka, Hadoop, and various cloud platforms like Azure and AWS. Whether it's developing CI/CD pipelines, orchestrating data workflows with Airflow, or crafting user interfaces with React and Node, I've done it all! 💻
""")

st.header("What I Love")
st.write("""
- **Coding:** Python, Scala, Java, Bash, SQL, JavaScript, you name it! 🐍
- **Cloud:** Azure, AWS, and everything in between. ☁️
- **DevOps:** Docker, Jenkins, GitLab CI, and more. 🔧
- **Frameworks:** Spark, Kafka, FastAPI, and the list goes on. 🚀
- **Data Tech:** Databricks, Snowflake, Hadoop, and more. 📊
- **Data Visualization:** D3.js, Streamlit, Power BI – turning data into stories. 📈
- **ETL:** Talend, Dagster, and other tools to make data flow smoothly. 🔄
- **Web3:** Solidity, Cairo, React, Node – diving into the decentralized web. 🌐

I'm a polyglot who loves languages, both human and programming. I speak English (B2), French (C2), Spanish(C1), Portuguese (C2), and Armenian (A1). 🌍
""")

st.header("Let's Connect!")
st.write("""
I'm always excited to connect with fellow tech enthusiasts, potential collaborators, or anyone who wants to chat about data, tech, or anything in between. Feel free to reach out to me:""")
# Add the LinkedIn logo and link
st.markdown(
    """
- **Email:** philippe.paulos@gmail.com 📧
- **LinkedIn:** [Philippe Paulos](https://www.linkedin.com/in/philippe-p-a42a1487/) 🔗
- **GitHub:** [github.com/philippepaulos](https://github.com/philippepaulos) 🐱
""",
    unsafe_allow_html=True,
)

st.write("""
Thanks for stopping by! I hope you enjoyed getting to know a bit about me. Stay awesome and keep exploring the amazing world of data! 🌟
Feel free to explore my projects and get in touch if you have any questions or opportunities!
""")
