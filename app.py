
import os
import pandas as pd
import streamlit as st

from docx import Document

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



import os
import streamlit as st


if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("Please add GOOGLE_API_KEY in Streamlit Secrets")
    st.stop()


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.3
)

template = """

Create a professional business proposal.

Company Profile:

{company}


Client Requirement:

{requirement}


Include:

1. Executive Summary
2. Company Introduction
3. Client Understanding
4. Proposed Solution
5. Scope of Work
6. Deliverables
7. Timeline
8. Technology Stack
9. Pricing
10. Conclusion

"""


prompt = PromptTemplate(
    input_variables=[
        "company",
        "requirement"
    ],
    template=template
)



parser = StrOutputParser()


proposal_chain = (
    prompt 
    | llm
    | parser
)

company_profile = """

ABC Technologies Pvt Ltd.

We provide AI solutions,
Machine Learning applications,
Cloud services and automation.

Our expertise:

- Generative AI
- Data Analytics
- Enterprise Applications
- AI Chatbots

Experience:
5 years

"""

client_requirement = """

Client wants an AI-powered healthcare assistant.

Required features:

- Patient chatbot
- Appointment booking
- Medical FAQ system
- Analytics dashboard
- Cloud deployment

Expected timeline:
5 months

"""

proposal = proposal_chain.invoke(
    {
        "company": company_profile,
        "requirement": client_requirement
    }
)




doc = Document()

doc.add_heading(
    "Business Proposal",
    level=0
)


doc.add_paragraph(proposal)


doc.save(
    "AI_Business_Proposal.docx"
)


doc.save(
    "AI_Business_Proposal.docx"
)
with open("AI_Business_Proposal.docx", "rb") as file:

    st.download_button(
        label="Download Proposal",
        data=file,
        file_name="AI_Business_Proposal.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

