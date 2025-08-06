import streamlit as st
from backend import back, D2, D3

st.title("📈 Expression Plotter")
st.text("Examples: x**2 + 2*x + 1   or   sin(x)*y")

user = st.text_input("Enter expression:")

if user.strip():
    try:
        variables, expression = back(user)

        if len(variables) == 1:
            x_range = st.slider("Select X range", -10, 10, (-5, 5))
            fig = D2(variables, expression, x_range)
            st.pyplot(fig)

        elif len(variables) == 2:
            x_range = st.slider("X range", -10, 10, (-5, 5))
            y_range = st.slider("Y range", -10, 10, (-5, 5))
            fig = D3(variables, expression, x_range, y_range)
            st.pyplot(fig)

        else:
            st.warning("⚠ This app supports only 1 or 2 variables.")

    except Exception as e:
        st.error(f"❌ Invalid expression: {e}")
else:
    st.info("💡 Please enter a mathematical expression to visualize.")