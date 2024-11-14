### 1. **Extract Text from Triage Forms**

- **Input**: Folder containing `.docx` triage forms.
- **Process**: Iterate through each `.docx` file, extracting the relevant sections of text between specified markers (e.g., ‘Additional information’ to ‘Follow-Up Plan’).
- **Output**: Save the extracted text as individual `.txt` files or in-memory data structures.

### 2. **Format Text with Appropriate Columns**

- **Input**: Extracted text from triage forms + raw docx (attached into chatgpt as docx file)
- **Process**: Create a json structure with predefined columns such as "Age", "Ethnicity", "Diagnosis", etc. Each triage form fills the relevant fields in the CSV format. Handle potential variations in the structure of the triage forms (e.g., missing fields)
- **Tools**: Chatgpt
- **Output**: A structured CSV file containing formatted data from multiple triage forms, and possibly a csv if required (state: ‘Please save this json output as a csv as well’ )

```jsx
Prompt:
"I have multiple documents containing patient case details extracted from triage forms, and I need assistance in categorizing the extracted text into specific medical and social categories. Each document includes information on patient demographics, medical history, mental health status, presenting concerns, symptoms, and coping mechanisms.

Please analyze the following sample text and categorize the information into the following fields. If additional categories are relevant, feel free to suggest them based on the content:

Filename: The name of the document.
Age: The age of the patient.
Ethnicity: The patient's ethnicity.
Gender: The patient's gender.
Occupation: The patient’s occupation.
Past_Psychiatric_History: Any history of psychiatric illness.
Past_Admissions_to_IMH: Any past admissions to IMH (Institute of Mental Health).
Past_Medical_History: Previous medical conditions (e.g., Hypertension, Hyperlipidemia).
Family_Medical_History: Family history of mental health or medical conditions.
Diagnosis: The patient's current mental health diagnosis.
Presenting_Concerns: The patient’s concerns at the time of evaluation.
Symptoms: List of symptoms (e.g., lethargy, low mood, insomnia).
Living_Arrangement: The patient's living situation (e.g., with family, alone).
Pack_Years: The smoking history (in pack years).
Alcohol_Consumption: Details about alcohol consumption.
Functional_Impairment: Any reported functional impairment.
Precipitating_Factors: Events or factors that triggered the current crisis.
Protective_Factors: Support systems or personal factors that may prevent deterioration.
Predisposing_Factors: Childhood experiences or past trauma contributing to current issues.
Coping_Mechanisms: How the patient is currently coping (e.g., alcohol use, smoking).
Formulation: A summary of the patient's mental health status based on their history and presenting symptoms.
Social_History: Information about social relationships, conflicts, or recent changes in the patient’s life.
Substance_Use: Details on smoking, alcohol, or other substance use.
Suicidal_Ideation: Any mention of suicidal thoughts or attempts.
Aggression: Any reports of aggression or violent behavior.
Here is a sample patient case for categorization:

Please return a JSON-like structure with the fields populated based on the sample, and add any additional fields you think would be useful in this context. 
If there are no suitable content to fill the header, you may leave it blank

{
    "Filename": "Simulated Triage Form #1.docx",
    "Age": "45",
    "Ethnicity": "Chinese",
    "Gender": "Male",
    "Occupation": "Accountant at PWC",
    "Past_Psychiatric_History": "Nil",
    "Past_Admissions_to_IMH": "Nil",
    "Past_Medical_History": "Hypertension, Hyperlipidemia",
    "Family_Medical_History": "Father with depression",
    "Diagnosis": "Depression",
    "Presenting_Concerns": "Unable to focus at work, missing many days, doesn’t feel like getting up from bed, not enjoying hobbies like fishing or reading",
    "Symptoms": "Lethargy, low mood, insomnia, loss of appetite, irritability for 4 months",
    "Living_Arrangement": "Lives with wife and 2 younger children",
    "Pack_Years": "20 pack years",
    "Alcohol_Consumption": "Heavy drinker (3x bottles of Tiger beer daily)",
    "Functional_Impairment": "Nil",
    "Precipitating_Factors": "Recent lay-off from job at PWC",
    "Perpetuating_Factors": "Chronic stress"
    "Protective_Factors": "Good family support, Insight into own emotions, Open to regular psychotherapy sessions and medication",
    "Predisposing_Factors": "Abuse by father when young, bullying in school, FMHx of father with depression",
    "Coping_Mechanisms": "Increased alcohol consumption (3x bottles of Tiger beer daily), Smoking regularly to relieve stress",
    "Formulation": "Long history of low self-esteem, lack of control over situations, persistent negative ruminations, possible auditory hallucinations to explore further",
    "Social_History": "Conflict with coworkers, trouble concentrating, recent job loss",
    "Substance_Use": {
        "Smoking": "20 pack years, regular smoker to relieve stress",
        "Alcohol": "Heavy drinker, 3x bottles of Tiger beer daily"
    },
    "Suicidal_Ideation": "Threatened to jump down from 16th floor HDB block",
    "Aggression": "Aggressive towards family, threatened wife, shouted vulgarities"
}

### Step 3: 4 P's

|  | **Biological** | **Psychological** | **Social** |
| --- | --- | --- | --- |
| **Predisposing** (What is their “setup?” What were they working with initially?) | • What was their temperament at birth? <br> • What do we know about their consistent personality characteristics? <br> • Is there a family psychiatric history? <br> • Are there toxic exposures in utero, birth complications, or developmental disorders? <br> • Is there a history of concussions or traumatic brain injuries? <br> • Neurodevelopmental history | • What is their attachment style? <br> • How did their family act and what is the family structure (i.e. - did the patient model their parent's behaviours, or did they rebel against their parent's behaviours – you either “act like your parents” or “act the opposite of your parents because you don't want to be like them”)? <br> • Do they have problems with affect modulation? <br> • Do they have a rigid or negative cognitive style? <br> • Low self-image/self-esteem? | • Poverty, low socioeconomic status, teenage parenthood, or poor access to health care? <br> • Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts? <br> • Immigration history, marginalization, discrimination, or racism? <br> • Exposure to antisocial personality/traits |
| **Precipitating** (What acute events occurred, and how did they affect them?) | • Serious medical illness or injury? <br> • Increasing use of alcohol or drugs? <br> • Medication non-adherence? <br> • Pregnancy or hormonal changes? <br> • Sleep deprivation? | Stressor that activate one or more psychological processes: <br> • Cognitive: core beliefs and cognitive distortions <br> • Dialectical: emotional dysregulation and dysfunction <br> • Interpersonal: grief, loss, disagreement, change/transitions <br> • Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns (psychic determinism) | • Loss of or separation from close family, partner, or friends <br> • Interpersonal trauma <br> • Work/academic/financial stressors <br> • Recent immigration, loss of home, loss of a supportive service (e.g. - respite services, appropriate school placement) <br> • Is the individual's current experience/symptoms similar to a past situation (i.e. - “history repeating itself”)? For example, they might have had a loss, separation etc. in the past |
| **Perpetuating** (What chronic issues are ongoing?) | • Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder? <br> • Lack of medication optimization (suboptimal doses) <br> • Lack of treatment or follow up for mental illness <br> • Current substance use? <br> • Chronic medical problems, chronic pain, or disability? <br> • How is patient responding to hospitalization? <br> • What are the degree of the symptoms right now? | One or more perpetuating psychological processes: <br> • Cognitive: chronic negative thoughts and reinforcing environment <br> • Dialectical: help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance <br> • Interpersonal: Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions <br> • Psychodynamic: recurring themes throughout one’s life, chronic primitive defenses <br> • What are their beliefs about self/others/world? What ideas have they internalized? <br> • Are there self-destructive coping mechanisms, or traumatic re-enactments? <br> • Ongoing poor coping skills, limited or lack of insight? <br> • Personality traits (e.g. - unable to maintain consistent interpersonal relationships in borderline personality disorder) <br> • How is their attachment style playing out in this particular situation? | • Chronic marital/relationship discord, lack of empathy from family/friends, developmentally inappropriate expectations <br> • Chronically dangerous or hostile neighbourhood, trans-generational problems of immigration, lack of culturally competent services <br> • Ongoing transitions and stressors <br> • Poor finances or working long hours <br> • Isolation, unsafe environment |
| **Protective** (What factors are supporting their well-being?) | • Good overall health <br> • Absence of family psychiatric history <br> • What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)? <br> • Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities? <br> • No substance use is a protective factor | • Do they have ability to be reflective or modulate their affect? <br> • Do they have ability to mentalize (see other's perspectives)? <br> • Do they have a positive sense of self, or adaptive coping mechanisms? <br> • Psychologically-minded, reflective, and capacity to change thinking patterns? <br> • Have they previously responded well to therapy? <br> • Good coping skills, good insight? | • Positive relationships, supportive community, and/or extended family/friends? <br> • Religious/spiritual beliefs <br> • Good interpersonal supports <br> • Financial/disability support <br> • Has an outpatient healthcare team: GP, psychiatrist, social, or case worker? |
