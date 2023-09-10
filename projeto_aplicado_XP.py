import streamlit as st

def main():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(' ')

    with col2:
        st.image('logo - bing.jpg', width=100)

    with col3:
        st.write(' ')
        
    st.title("Projeto Aplicado - Faculdade XPE")
  
if __name__ == "__main__":
    main()
