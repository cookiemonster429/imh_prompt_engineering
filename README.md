# README: Text Extraction, Categorization, and Questionnaire Pipeline

This project provides a comprehensive pipeline for processing and analyzing patient triage forms. The pipeline involves text extraction, categorization based on predefined fields, conversion of qualitative data to quantitative codes, and further analysis through the completion of questionnaires that assess social support and other psychological factors. The following steps explain the entire process:

### 1. **Extract Text from Triage Forms**

- **Input**: Folder containing `.docx` triage forms.
- **Process**: Iterate through each `.docx` file, extracting the relevant sections of text between specified markers (e.g., ‘Additional information’ to ‘Follow-Up Plan’).
- **Output**: Save the extracted text as individual `.txt` files or in-memory data structures.
- Please run 'python text_extraction.py' with the relevant input and output folders

### 2. **Format Text with Appropriate Columns**

- **Input**: Extracted text from triage forms + raw docx (attached into chatgpt as docx file)
- **Process**: Create a json structure with predefined columns such as "Age", "Ethnicity", "Diagnosis", etc. Each triage form fills the relevant fields in the CSV format. Handle potential variations in the structure of the triage forms (e.g., missing fields)
- **Tools**: Chatgpt
- **Output**: A structured CSV file containing formatted data from multiple triage forms, and possibly a csv if required (state: ‘Please save this json output as a csv as well’ )

**Prompt:**
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

```json
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
    "Perpetuating_Factors": "Chronic stress",
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


### 3. **Categorize Based on Guidelines (Qualitative to Quantitative)** (Continued)

- **Input**: Structured CSV containing qualitative data from the forms.
- **Process**: Apply coding rules to convert qualitative data (e.g., symptoms, alcohol consumption, predisposing factors) into quantitative values. Retain fields that are not categorized (e.g., diagnosis, occupation) as original text. Handle exceptions where fields are missing by omitting them from categorization.
- **Tools**: ChatGPT
- **Output**: Updated CSV with coded numeric fields where applicable.

**Prompt:**
I have patient data extracted from triage forms and need to convert the qualitative information into quantitative codes for data analysis. Use the coding schemes provided below. If a field is not available in the form, omit it. Similarly, retain any information that is not coded in the prompt, such as occupation or diagnosis, in its original form.

For age, convert the values into ranges using the specified dictionary. Return numeric codes for the appropriate fields, and retain original values for non-coded fields (e.g., occupation, diagnosis, presenting concerns). No explanation is needed, just return the coded results.

Multi-coded fields: If a field can have multiple valid codes (e.g., Protective Factors), return them as a comma-separated list (e.g., '1,2' for Family support and Personal insight). Only use the combination code (e.g., 4 for Protective Factors) if all the listed subcategories apply; otherwise, list the individual codes.

Coded Values:

- **Age**:  
  0: 0–9  
  1: 10–19  
  2: 20–29  
  3: 30–39  
  4: 40–49  
  5: 50–59  
  6: 60–69  
  7: 70+

- **Symptoms**:  
  0: None  
  1: Present  

- **Ethnicity**:  
  1: Chinese  
  2: Malay  
  3: Indian  
  4: Eurasian  
  5: Others (e.g., Korean, Japanese)

- **Gender**:  
  1: Male  
  0: Female

- **Past Psychiatric History**:  
  0: None  
  1: Present  

- **Past Admissions to IMH**:  
  0: None  
  1: Present  

- **Past Medical History**:  
  0: None  
  1: Present  

- **Family Medical History**:  
  0: None  
  1: Mental Health History (e.g., depression, anxiety)  
  2: Physical Health History (e.g., hypertension, diabetes)  
  3: Both Mental and Physical Health History  

- **Alcohol Consumption**:  
  0: None  
  1: Occasional  
  2: Frequent  
  3: Heavy  

- **Diagnosis (ICD-11)**: Retain original values (e.g., Major Depressive Disorder, GAD, etc.)

- **Occupation**:  
  1: Manual Labour  
  2: Office  
  3: White Collar  
  4: Service  
  5: Other  

- **Living Arrangements**:  
  0: Couple base (with/without children)  
  1: Lone parent (with children)  
  2: Living alone (purely alone)  
  3: Other households with family nucleus (uncle, cousin, etc.)  
  4: Other households without family nucleus (other tenants, etc.)

- **Substance Abuse (Alcohol)**:  
  0: None  
  1: Occasional  
  2: Frequent  
  3: Heavy  

- **Pack Years**:  
  0: None  
  1: Occasional (1–5 pack years)  
  2: Frequent (6–15 pack years)  
  3: Heavy (16+ pack years)  

- **Functional Impairment**:  
  0: None  
  1: Mild  
  2: Moderate  
  3: Severe  

- **Precipitating_Factors**: Retain original values  

- **Perpetuating_Factors**: Retain original values  

- **Protective_Factors**: Retain original values  

- **Predisposing_Factors**: Retain original values  

- **Coping Mechanisms**:  
  0: None  
  1: Healthy (exercise, therapy, etc.)  
  2: Unhealthy (alcohol, smoking, etc.)  
  3: Mixed (both healthy and unhealthy)  

- **Suicidal Ideation**:  
  0: None  
  1: Present (thoughts)  
  2: Attempted (suicide attempt)  

- **Aggression**:  
  0: None  
  1: Verbal aggression  
  2: Physical aggression  
  3: Both  

- **Social History**:  
  0: Stable (no significant issues)  
  1: Conflicts at work or with friends  
  2: Relationship breakdown (e.g., divorce, separation)  
  3: Legal issues or other social stressors


### Step 4: **Categorize 4 P's (Biological, Psychological, Social)**

|  | **Biological** | **Psychological** | **Social** |
| --- | --- | --- | --- |
| **Predisposing** (What is their “setup?” What were they working with initially?) | • What was their temperament at birth?  
• What do we know about their consistent personality characteristics?  
• Is there a family psychiatric history?  
• Are there toxic exposures in utero, birth complications, or developmental disorders?  
• Is there a history of concussions or traumatic brain injuries?  
• Neurodevelopmental history | • What is their attachment style?  
• How did their family act and what is the family structure (i.e. - did the patient model their parent's behaviours, or did they rebel against their parent's behaviours – you either “act like your parents” or “act the opposite of your parents because you don't want to be like them”)?  
• Do they have problems with affect modulation?  
• Do they have a rigid or negative cognitive style?  
• Low self-image/self-esteem? | • Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?  
• Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?  
• Immigration history, marginalization, discrimination, or racism?  
• Exposure to antisocial personality/traits |
| **Precipitating** (What acute events occurred, and how did they affect them?) | • Serious medical illness or injury?  
• Increasing use of alcohol or drugs?  
• Medication non-adherence?  
• Pregnancy or hormonal changes?  
• Sleep deprivation? | Stressor that activate one or more psychological processes:  
• Cognitive: core beliefs and cognitive distortions  
• Dialectical: emotional dysregulation and dysfunction  
• Interpersonal: grief, loss, disagreement, change/transitions  
• Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns (psychic determinism) | • Loss of or separation from close family, partner, or friends  
• Interpersonal trauma  
• Work/academic/financial stressors  
• Recent immigration, loss of home, loss of a supportive service (e.g. - respite services, appropriate school placement)  
• Is the individual's current experience/symptoms similar to a past situation (i.e. - “history repeating itself”)? For example, they might have had a loss, separation etc. in the past |
| **Perpetuating** (What chronic issues are ongoing?) | • Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?  
• Lack of medication optimization (suboptimal doses)  
• Lack of treatment or follow up for mental illness  
• Current substance use?  
• Chronic medical problems, chronic pain, or disability?  
• How is patient responding to hospitalization?  
• What are the degree of the symptoms right now? | One or more perpetuating psychological processes:  
• Cognitive: chronic negative thoughts and reinforcing environment  
• Dialectical: help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance  
• Interpersonal: Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions  
• Psychodynamic: recurring themes throughout one’s life, chronic primitive defenses

• What are their beliefs about self/others/world? What ideas have they internalized?  
• Are there self-destructive coping mechanisms, or traumatic re-enactments?  
• Ongoing poor coping skills, limited or lack of insight?  
• Personality traits (e.g. unable to maintain consistent interpersonal relationships in borderline personality disorder)  
• How is their attachment style playing out in this particular situation? | • Chronic marital/relationship discord, lack of empathy from family/friends, developmentally inappropriate expectations  
• Chronically dangerous or hostile neighbourhood, trans-generational problems of immigration, lack of culturally competent services  
• Ongoing transitions and stressors  
• Poor finances or working long hours  
• Isolation, unsafe environment |
| **Protective** (What factors are supporting their well-being?) | • Good overall health  
• Absence of family psychiatric history  
• What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)?  
• Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?  
• No substance use is a protective factor | • Do they have ability to be reflective or modulate their affect?  
• Do they have ability to mentalize (see other's perspectives)?  
• Do they have a positive sense of self, or adaptive coping mechanisms?  
• Psychologically-minded, reflective, and capacity to change thinking patterns?  
• Have they previously responded well to therapy?  
• Good coping skills, good insight? | • Positive relationships, supportive community, and/or extended family/friends?  
• Religious/spiritual beliefs  
• Good interpersonal supports  
• Financial/disability support  
• Has an outpatient healthcare team: GP, psychiatrist, social, or case worker? |

### Step 5: **Questionnaire for Patient Assessment**

**Multidimensional Scale of Perceived Social Support (MSPSS)**

1. There is a special person who is around when I am in need.  
2. There is a special person with whom I can share my joys and sorrows.  
3. My family really tries to help me.  
4. I get the emotional help and support I need from my family.  
5. I have a special person who is a real source of comfort to me.  
6. My friends really try to help me.  
7. I can count on my friends when things go wrong.  
8. I can talk about my problems with my family.  
9. I have friends with whom I can share my joys and sorrows.  
9. There is a special person in my life who cares about my feelings.  
10. My family is willing to help me make decisions.  
11. I can talk about my problems with my friends.  

Scale Items and Response Options:  
Each item is rated on a 5-point Likert scale:  
0 = Strongly Disagree  
1 = Disagree  
2 = NA # neither agree or disagree  
3 = Agree  
4 = Strongly Agree  

