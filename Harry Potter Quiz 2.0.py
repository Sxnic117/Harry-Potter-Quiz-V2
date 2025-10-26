
import streamlit as st

st.title('Harry Potter House Quiz')

with st.form("quiz_form"):
    q1 = st.radio(
        "Q1) Do you like Dawn or Dusk?",
        ("Dawn", "Dusk")
    )

    q2 = st.radio(
        "Q2) When I'm dead, I want people to remember me as:",
        ("The Good", "The Great", "The Wise", "The Bold")
    )

    q3 = st.radio(
        "Q3) Which kind of instrument most pleases your ear?",
        ("The violin", "The trumpet", "The piano", "The drum")
    )

    submitted = st.form_submit_button("Ergebnis anzeigen")

if submitted:
    slytherin = 0
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0

    
    if q1 == "Dawn":
        gryffindor += 1
        ravenclaw += 1
    else:
        hufflepuff += 1
        slytherin += 1

    
    if q2 == "The Good":
        hufflepuff += 2
    elif q2 == "The Great":
        slytherin += 2
    elif q2 == "The Wise":
        ravenclaw += 2
    elif q2 == "The Bold":
        gryffindor += 2

    
    if q3 == "The violin":
        slytherin += 4
    elif q3 == "The trumpet":
        hufflepuff += 4
    elif q3 == "The piano":
        ravenclaw += 4
    elif q3 == "The drum":
        gryffindor += 4

    st.write("Gryffindor:", gryffindor)
    st.write("Slytherin:", slytherin)
    st.write("Ravenclaw:", ravenclaw)
    st.write("Hufflepuff:", hufflepuff)

    
    scores = {
        "Gryffindor": gryffindor,
        "Slytherin": slytherin,
        "Ravenclaw": ravenclaw,
        "Hufflepuff": hufflepuff
    }
    max_score = max(scores.values())
    winners = [name for name, score in scores.items() if score == max_score]

    if len(winners) == 1:
        st.success(f"The Winner is: {winners[0]}!")
    else:
        st.info(f"It's a tie between: {', '.join(winners)}")
