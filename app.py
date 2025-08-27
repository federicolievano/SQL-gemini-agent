import google.generativeai as genai
import pandas as pd
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY
from database import execute_query, get_available_tables, get_table_schema

# Page configuration
st.set_page_config(page_title="SQL Query Assistant", page_icon="🗄️", layout="wide")

# Initialize Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0.1,  # Más determinístico = más rápido
        max_tokens=150,  # Limitar respuesta para mayor velocidad
    )
else:
    st.error("⚠️ Please set your Gemini API key in the config.py file")
    st.stop()

# Header
st.title("🗄️ SQL Query Assistant")
st.markdown(
    "Ask questions in natural language and get SQL results from your MySQL database"
)

# Sidebar for database info
with st.sidebar:
    st.header("📊 Database Information")

    if st.button("🔄 Refresh Database Info"):
        st.rerun()

    # Show available tables
    tables_df = get_available_tables()
    if tables_df is not None:
        st.subheader("Available Tables:")
        for table in tables_df.iloc[:, 0]:
            st.write(f"• {table}")

            # Show table schema on expander
            with st.expander(f"Schema for {table}"):
                schema_df = get_table_schema(table)
                if schema_df is not None:
                    st.dataframe(schema_df, use_container_width=True)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Ask Your Question")

    # Natural language input
    user_question = st.text_area(
        "Describe what you want to know about your data:",
        placeholder="Example: Show me all actors from the film 'Jaws'",
        height=100,
    )

    # Generate SQL button
    if st.button("🔍 Generate SQL Query", type="primary"):
        if user_question:
            with st.spinner("Generating SQL query..."):
                try:
                    # Prompt template for SQL generation - Simplified for speed
                    sql_prompt = PromptTemplate(
                        input_variables=["question"],
                        template="Convert to MySQL SQL for world database: {question}. Return only SQL:",
                    )

                    # Generate SQL with timeout indicator
                    with st.spinner(
                        "🔄 Generating SQL (this may take 10-30 seconds)..."
                    ):
                        sql_query = llm.invoke(
                            sql_prompt.format(question=user_question)
                        )

                    # Clean the response
                    sql_query = sql_query.content.strip()
                    if sql_query.startswith("```sql"):
                        sql_query = sql_query[7:]
                    if sql_query.endswith("```"):
                        sql_query = sql_query[:-3]
                    sql_query = sql_query.strip()

                    st.session_state.sql_query = sql_query
                    st.success("✅ SQL Query generated!")

                except Exception as e:
                    st.error(f"❌ Error generating SQL: {e}")
                    st.info(
                        "💡 Try asking a simpler question or check your internet connection"
                    )

with col2:
    st.subheader("📝 Generated SQL")

    if "sql_query" in st.session_state:
        st.code(st.session_state.sql_query, language="sql")

        # Execute query button
        if st.button("▶️ Execute Query"):
            with st.spinner("Executing query..."):
                try:
                    results_df = execute_query(st.session_state.sql_query)

                    if results_df is not None:
                        st.session_state.results = results_df
                        st.success(f"✅ Query executed! Found {len(results_df)} rows")
                    else:
                        st.error("❌ Error executing query")

                except Exception as e:
                    st.error(f"❌ Error: {e}")

# Display results
if "results" in st.session_state and st.session_state.results is not None:
    st.subheader("📊 Query Results")

    # Show results info
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Total Rows", len(st.session_state.results))
    with col_info2:
        st.metric("Total Columns", len(st.session_state.results.columns))
    with col_info3:
        st.metric(
            "Memory Usage",
            f"{st.session_state.results.memory_usage(deep=True).sum() / 1024:.1f} KB",
        )

    # Display results
    st.dataframe(st.session_state.results, use_container_width=True)

    # Download button
    csv = st.session_state.results.to_csv(index=False)
    st.download_button(
        label="📥 Download Results as CSV",
        data=csv,
        file_name="query_results.csv",
        mime="text/csv",
    )

# Footer
st.markdown("---")
st.markdown("💡 **Tip**: Be specific in your questions for better SQL generation!")
