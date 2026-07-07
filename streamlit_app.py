import streamlit as st
import pandas as pd
import joblib
# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Customer Churn Prediction System",
    page_icon="📊",
    layout="wide"
)
# ==========================================
# Load Trained Model
# ==========================================

model = joblib.load("models/customer_churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
# ==========================================
# Sidebar
# ==========================================

# ==========================================
# Sidebar
# ==========================================

st.sidebar.image("assets/cu_logo.png", width=150)

st.sidebar.markdown("## Customer Churn")
st.sidebar.caption("MCA Major Project • 2026")

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📈 Data Analysis",
        "🤖 Predict Churn",
        "ℹ️ About Project"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Developed by\n\n**Priyanshu Chand**"
)

# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    # Logo
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image(
            "assets/cu_logo.png",
            width='content'
        )

    # Title
    st.markdown(
        """
        <div style="text-align:center;">

        <h1>Customer Churn Prediction System</h1>

        <h3 style="color:#C00000;">
        Chandigarh University
        </h3>

        <h4 style="color:gray;">
        MCA Major Project • 2026
        </h4>

        <p style="font-size:18px;">
        <b>Developed by:</b> Priyanshu Chand
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.write(
        """
        This dashboard analyzes customer churn patterns and predicts
        whether a customer is likely to leave the company using
        Machine Learning techniques.
        """
    )

    # KPI Cards

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Total Customers", "7,043")

    with c2:
        st.metric("📉 Churn Rate", "26.5%")

    with c3:
        st.metric("🤖 Best Model", "Logistic Regression")

    with c4:
        st.metric("🎯 Accuracy", "80.34%")

    st.divider()

    st.success(
        "✅ Logistic Regression achieved the highest accuracy (80.34%) and was selected as the final prediction model."
    )

    st.divider()

    st.subheader("📊 Model Performance")

    comparison = pd.DataFrame({
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "Accuracy": [
            80.34,
            78.50,
            79.49
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )


    # Two Columns

    left, right = st.columns(2)

    with left:

        st.subheader("🎯 Project Objectives")

        st.markdown("""
- Analyze customer churn patterns.
- Perform exploratory data analysis.
- Train multiple machine learning models.
- Compare model performance.
- Predict customer churn.
""")

    with right:

        st.subheader("📂 Dataset Information")

        st.markdown("""
**Dataset**

IBM Telco Customer Churn Dataset

**Records**

7043

**Features**

20

**Target Variable**

Customer Churn
""")

    st.divider()

    st.subheader("🛠 Technologies Used")

    a, b, c = st.columns(3)

    with a:
        st.success("Python")
        st.success("Pandas")
        st.success("NumPy")

    with b:
        st.success("Matplotlib")
        st.success("Seaborn")
        st.success("Scikit-Learn")

    with c:
        st.success("Streamlit")
        st.success("Joblib")
        st.success("Jupyter Notebook")

    st.divider()

    st.caption(
    "Developed by Priyanshu Chand • MCA Major Project • Chandigarh University • 2026"
    )
# ==========================================
# DATA ANALYSIS
# ==========================================

elif page == "📈 Data Analysis":

    st.title("📈 Customer Churn Analysis Dashboard")

    st.write(
        "The following visualizations provide insights into customer behavior and factors influencing churn."
    )

    st.divider()

    # -----------------------------
    # Row 1
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Customer Churn Distribution")
        st.image(
            "images/churn_distribution.png",
            use_container_width=True
        )

    with col2:
        st.subheader("Customer Churn by Contract")
        st.image(
            "images/contract_vs_churn.png",
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Row 2
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Internet Service vs Churn")
        st.image(
            "images/internet_service_vs_churn.png",
            use_container_width=True
        )

    with col2:
        st.subheader("Payment Method vs Churn")
        st.image(
            "images/payment_method_vs_churn.png",
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Row 3
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tenure Distribution")
        st.image(
            "images/tenure_distribution.png",
            use_container_width=True
        )

    with col2:
        st.subheader("Monthly Charges vs Churn")
        st.image(
            "images/monthly_charges_vs_churn.png",
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Row 4
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Correlation Heatmap")
        st.image(
            "images/correlation_heatmap.png",
            use_container_width=True
        )

    with col2:
        st.subheader("Feature Importance")
        st.image(
            "images/feature_importance.png",
            use_container_width=True
        )

    st.divider()

    st.caption(
    "Developed by Priyanshu Chand • MCA Major Project • Chandigarh University • 2026"
    )
# ==========================================
# PREDICT CHURN
# ==========================================

elif page == "🤖 Predict Churn":

    st.title("🤖 Customer Churn Prediction")

    st.write(
        "Enter customer information below to predict whether the customer is likely to churn."
    )

    st.divider()

    # -------------------------
    # Customer Information
    # -------------------------

    st.subheader("👤 Customer Information")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            label_encoders["Gender"].classes_
        )

        senior = st.selectbox(
            "Senior Citizen",
            label_encoders["Senior Citizen"].classes_
        )

        partner = st.selectbox(
            "Partner",
            label_encoders["Partner"].classes_
        )

        dependents = st.selectbox(
            "Dependents",
            label_encoders["Dependents"].classes_
        )

    with col2:

        tenure = st.number_input(
            "Tenure (Months)",
            min_value=0,
            max_value=100,
            value=12
        )

        monthly = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            max_value=200.0,
            value=70.0
        )

    st.divider()

    # -------------------------
    # Services
    # -------------------------

    st.subheader("📡 Services")

    col1, col2 = st.columns(2)

    with col1:

        phone = st.selectbox(
            "Phone Service",
            label_encoders["Phone Service"].classes_
        )

        multiple = st.selectbox(
            "Multiple Lines",
            label_encoders["Multiple Lines"].classes_
        )

        internet = st.selectbox(
            "Internet Service",
            label_encoders["Internet Service"].classes_
        )

        security = st.selectbox(
            "Online Security",
            label_encoders["Online Security"].classes_
        )

        backup = st.selectbox(
            "Online Backup",
            label_encoders["Online Backup"].classes_
        )

    with col2:

        protection = st.selectbox(
            "Device Protection",
            label_encoders["Device Protection"].classes_
        )

        support = st.selectbox(
            "Tech Support",
            label_encoders["Tech Support"].classes_
        )

        tv = st.selectbox(
            "Streaming TV",
            label_encoders["Streaming TV"].classes_
        )

        movies = st.selectbox(
            "Streaming Movies",
            label_encoders["Streaming Movies"].classes_
        )

    st.divider()

    # -------------------------
    # Subscription
    # -------------------------

    st.subheader("💳 Subscription")

    col1, col2 = st.columns(2)

    with col1:

        contract = st.selectbox(
            "Contract",
            label_encoders["Contract"].classes_
        )

    with col2:

        paperless = st.selectbox(
            "Paperless Billing",
            label_encoders["Paperless Billing"].classes_
        )

        payment = st.selectbox(
            "Payment Method",
            label_encoders["Payment Method"].classes_
        )

    st.divider()

    # -------------------------
    # Predict Button
    # -------------------------

    predict_button = st.button(
        "🔮 Predict Customer Churn",
        use_container_width=True
    )

    if predict_button:

        # Calculate Total Charges
        total_charges = tenure * monthly

        # Encode categorical variables
        input_data = {
            "Gender": label_encoders["Gender"].transform([gender])[0],
            "Senior Citizen": label_encoders["Senior Citizen"].transform([senior])[0],
            "Partner": label_encoders["Partner"].transform([partner])[0],
            "Dependents": label_encoders["Dependents"].transform([dependents])[0],
            "Tenure Months": tenure,
            "Phone Service": label_encoders["Phone Service"].transform([phone])[0],
            "Multiple Lines": label_encoders["Multiple Lines"].transform([multiple])[0],
            "Internet Service": label_encoders["Internet Service"].transform([internet])[0],
            "Online Security": label_encoders["Online Security"].transform([security])[0],
            "Online Backup": label_encoders["Online Backup"].transform([backup])[0],
            "Device Protection": label_encoders["Device Protection"].transform([protection])[0],
            "Tech Support": label_encoders["Tech Support"].transform([support])[0],
            "Streaming TV": label_encoders["Streaming TV"].transform([tv])[0],
            "Streaming Movies": label_encoders["Streaming Movies"].transform([movies])[0],
            "Contract": label_encoders["Contract"].transform([contract])[0],
            "Paperless Billing": label_encoders["Paperless Billing"].transform([paperless])[0],
            "Payment Method": label_encoders["Payment Method"].transform([payment])[0],
            "Monthly Charges": monthly,
            "Total Charges": total_charges
        }

        # Create DataFrame
        input_df = pd.DataFrame([input_data])

        # Match training feature order
        input_df = input_df[feature_names]

        # Scale only numeric columns
        numeric_columns = [
            "Tenure Months",
            "Monthly Charges",
            "Total Charges"
        ]

        input_df[numeric_columns] = scaler.transform(
            input_df[numeric_columns]
        )

        # Prediction
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        st.divider()

        st.subheader("📊 Prediction Result")

        confidence = max(probability) * 100

        if prediction == 1:

            st.error("## 🔴 High Risk of Customer Churn")

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.progress(float(probability[1]))

            st.markdown("""
        ### Recommendation

        • Contact the customer proactively.

        • Offer promotional discounts.

        • Encourage a longer contract.

        • Improve customer support engagement.
        """)

        else:

            st.success("## 🟢 Customer Likely to Stay")

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.progress(float(probability[0]))

            st.markdown("""
        ### Recommendation

        • Continue providing quality service.

        • Maintain customer engagement.

        • Offer loyalty rewards.

        • Monitor customer satisfaction.
        """)

        st.divider()

        st.write(f"**Stay Probability:** {probability[0]*100:.2f}%")

        st.write(f"**Churn Probability:** {probability[1]*100:.2f}%")

        st.info(
            """
            **Disclaimer**

            This prediction is generated using a machine learning model trained on the IBM Telco Customer Churn dataset.

            The prediction should be used to support business decision-making rather than as the sole basis for customer retention actions.
            """
            )

        result = pd.DataFrame({
        "Prediction": [
            "Likely to Churn" if prediction == 1 else "Likely to Stay"
        ],
        "Confidence (%)": [
            round(confidence,2)
        ],
        "Stay Probability (%)": [
            round(probability[0]*100,2)
        ],
        "Churn Probability (%)": [
            round(probability[1]*100,2)
        ]
    })

        st.download_button(
            "📥 Download Prediction Result",
            result.to_csv(index=False),
            file_name="prediction_result.csv",
            mime="text/csv"
        )

    st.divider()

    st.caption(
    "Developed by Priyanshu Chand • MCA Major Project • Chandigarh University • 2026"
    )
# ==========================================
# ABOUT PROJECT
# ==========================================

elif page == "ℹ️ About Project":

    st.title("ℹ️ About Project")

    st.markdown("""
    ## Customer Churn Prediction System Using Predictive Analytics and Machine Learning

    This project was developed as part of the **Master of Computer Applications (MCA)** program at **Chandigarh University**.

    The objective of the project is to analyze customer behavior, identify churn patterns, and predict whether a customer is likely to leave the company using machine learning techniques.
    """)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👨‍🎓 Student Information")

        st.write("**Student Name:** Priyanshu Chand")
        st.write("**Course:** Master of Computer Applications")
        st.write("**University:** Chandigarh University")
        st.write("**Year:** 2026")

    with col2:

        st.subheader("📂 Dataset")

        st.write("**Dataset:** IBM Telco Customer Churn")
        st.write("**Total Records:** 7043")
        st.write("**Features:** 20")
        st.write("**Target Variable:** Churn Value")

    st.divider()

    st.subheader("🤖 Machine Learning Models")

    st.markdown("""
    - Logistic Regression ✅ (Selected Model)
    - Decision Tree
    - Random Forest
    """)

    st.divider()

    st.subheader("🛠 Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.success("Python")
        st.success("Pandas")
        st.success("NumPy")

    with tech2:
        st.success("Scikit-Learn")
        st.success("Matplotlib")
        st.success("Seaborn")

    with tech3:
        st.success("Streamlit")
        st.success("Joblib")
        st.success("Jupyter Notebook")

    st.divider()

    st.subheader("🎯 Project Outcome")

    st.success(
        "The developed machine learning system achieved an accuracy of 80.34% using Logistic Regression and can assist organizations in identifying customers at risk of churn."
    )

    st.divider()

    st.caption(
    "Developed by Priyanshu Chand • MCA Major Project • Chandigarh University • 2026"
    )
    