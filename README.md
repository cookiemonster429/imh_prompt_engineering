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

```

### Step 3: 4 P's

|  | **Biological** | **Psychological** | **Social** |
| --- | --- | --- | --- |
| **Predisposing** (What is their “setup?” What were they working with initially?) | • What was their temperament at birth? <br> • What do we know about their consistent personality characteristics? <br> • Is there a family psychiatric history? <br> • Are there toxic exposures in utero, birth complications, or developmental disorders? <br> • Is there a history of concussions or traumatic brain injuries? <br> • Neurodevelopmental history | • What is their attachment style? <br> • How did their family act and what is the family structure (i.e. - did the patient model their parent's behaviours, or did they rebel against their parent's behaviours – you either “act like your parents” or “act the opposite of your parents because you don't want to be like them”)? <br> • Do they have problems with affect modulation? <br> • Do they have a rigid or negative cognitive style? <br> • Low self-image/self-esteem? | • Poverty, low socioeconomic status, teenage parenthood, or poor access to health care? <br> • Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts? <br> • Immigration history, marginalization, discrimination, or racism? <br> • Exposure to antisocial personality/traits |
| **Precipitating** (What acute events occurred, and how did they affect them?) | • Serious medical illness or injury? <br> • Increasing use of alcohol or drugs? <br> • Medication non-adherence? <br> • Pregnancy or hormonal changes? <br> • Sleep deprivation? | Stressor that activate one or more psychological processes: <br> • Cognitive: core beliefs and cognitive distortions <br> • Dialectical: emotional dysregulation and dysfunction <br> • Interpersonal: grief, loss, disagreement, change/transitions <br> • Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns (psychic determinism) | • Loss of or separation from close family, partner, or friends <br> • Interpersonal trauma <br> • Work/academic/financial stressors <br> • Recent immigration, loss of home, loss of a supportive service (e.g. - respite services, appropriate school placement) <br> • Is the individual's current experience/symptoms similar to a past situation (i.e. - “history repeating itself”)? For example, they might have had a loss, separation etc. in the past |
| **Perpetuating** (What chronic issues are ongoing?) | • Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder? <br> • Lack of medication optimization (suboptimal doses) <br> • Lack of treatment or follow up for mental illness <br> • Current substance use? <br> • Chronic medical problems, chronic pain, or disability? <br> • How is patient responding to hospitalization? <br> • What are the degree of the symptoms right now? | One or more perpetuating psychological processes: <br> • Cognitive: chronic negative thoughts and reinforcing environment <br> • Dialectical: help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance <br> • Interpersonal: Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions <br> • Psychodynamic: recurring themes throughout one’s life, chronic primitive defenses <br> • What are their beliefs about self/others/world? What ideas have they internalized? <br> • Are there self-destructive coping mechanisms, or traumatic re-enactments? <br> • Ongoing poor coping skills, limited or lack of insight? <br> • Personality traits (e.g. - unable to maintain consistent interpersonal relationships in borderline personality disorder) <br> • How is their attachment style playing out in this particular situation? | • Chronic marital/relationship discord, lack of empathy from family/friends, developmentally inappropriate expectations <br> • Chronically dangerous or hostile neighbourhood, trans-generational problems of immigration, lack of culturally competent services <br> • Ongoing transitions and stressors <br> • Poor finances or working long hours <br> • Isolation, unsafe environment |
| **Protective** (What factors are supporting their well-being?) | • Good overall health <br> • Absence of family psychiatric history <br> • What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)? <br> • Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities? <br> • No substance use is a protective factor | • Do they have ability to be reflective or modulate their affect? <br> • Do they have ability to mentalize (see other's perspectives)? <br> • Do they have a positive sense of self, or adaptive coping mechanisms? <br> • Psychologically-minded, reflective, and capacity to change thinking patterns? <br> • Have they previously responded well to therapy? <br> • Good coping skills, good insight? | • Positive relationships, supportive community, and/or extended family/friends? <br> • Religious/spiritual beliefs <br> • Good interpersonal supports <br> • Financial/disability support <br> • Has an outpatient healthcare team: GP, psychiatrist, social, or case worker? |


Prompt:

```
You are given a patient data structure that contains various coded fields from a triage form. Your task is to analyze the fields related to Precipitating Factors, Perpetuating Factors, Protective Factors, and Predisposing Factors and classify them into biological, psychological, and social categories based on the definitions and examples provided below.

Input Structure:

json
{
    "Filename": "Simulated Triage Form #1.docx",
    "Age": 4,
    "Ethnicity": 1,
    "Gender": 1,
    "Occupation": "Accountant at PWC",
    "Past_Psychiatric_History": 0,
    "Past_Admissions_to_IMH": 0,
    "Past_Medical_History": 1,
    "Family_Medical_History": 1,
    "Diagnosis": "Depression",
    "Presenting_Concerns": "Unable to focus at work, missing many days, doesn’t feel like getting up from bed, not enjoying hobbies like fishing or reading",
    "Symptoms": 1,
    "Living_Arrangement": 0,
    "Pack_Years": 3,
    "Alcohol_Consumption": 3,
    "Functional_Impairment": 0,
    "Precipitating_Factors": "Recent lay-off from long-term job as accountant in PWC (15 years)",
    "Perpetuating_Factors": "Chronic stress",
    "Protective_Factors": "Good family support, Insight into own emotions, Open to regular psychotherapy sessions and medication",
    "Predisposing_Factors": "Abuse by father when young, bullying in school, FMHx of father with depression",
    "Coping_Mechanisms": 2,
    "Formulation": "Long history of low self-esteem issues and is constantly bothered by his lack of meaning and contribution to the world around him. This lack of control over his situation in early childhood has continued throughout adulthood. Possible auditory hallucinations to explore further.",
    "Social_History": 1,
    "Substance_Use": {
        "Smoking": 3,
        "Alcohol": 3
    },
    "Suicidal_Ideation": 1,
    "Aggression": 3
}

Classification Categories, please help to fill it up and state if a trait is present:

{
  "Biological": {
    "Predisposing": [
      "What was their temperament at birth?",
      "What do we know about their consistent personality characteristics?",
      "Is there a family psychiatric history?",
      "Are there toxic exposures in utero, birth complications, or developmental disorders?",
      "Is there a history of concussions or traumatic brain injuries?",
      "Neurodevelopmental history"
    ],
    "Precipitating": [
      "Serious medical illness or injury?",
      "Increasing use of alcohol or drugs?",
      "Medication non-adherence?",
      "Pregnancy or hormonal changes?",
      "Sleep deprivation?"
    ],
    "Perpetuating": [
      "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?",
      "Lack of medication optimization (suboptimal doses)",
      "Lack of treatment or follow up for mental illness",
      "Current substance use?",
      "Chronic medical problems, chronic pain, or disability?",
      "How is patient responding to hospitalization?",
      "What are the degree of the symptoms right now?"
    ],
    "Protective": [
      "Good overall health",
      "Absence of family psychiatric history",
      "What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)?",
      "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?",
      "No substance use is a protective factor"
    ]
  },
  "Psychological": {
    "Predisposing": [
      "What is their attachment style?",
      "How did their family act and what is the family structure?",
      "Do they have problems with affect modulation?",
      "Do they have a rigid or negative cognitive style?",
      "Low self-image/self-esteem?"
    ],
    "Precipitating": [
      "Cognitive: core beliefs and cognitive distortions",
      "Dialectical: emotional dysregulation and dysfunction",
      "Interpersonal: grief, loss, disagreement, change/transitions",
      "Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns"
    ],
    "Perpetuating": [
      "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment",
      "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance",
      "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions",
      "Recurring themes throughout one’s life, chronic primitive defenses",
      "What are their beliefs about self/others/world? What ideas have they internalized?",
      "Are there self-destructive coping mechanisms, or traumatic re-enactments?",
      "Ongoing poor coping skills, limited or lack of insight?",
      "Personality traits that affect relationships (e.g. borderline personality disorder)",
      "How is their attachment style playing out in this particular situation?"
    ],
    "Protective": [
      "Do they have ability to be reflective or modulate their affect?",
      "Do they have ability to mentalize (see other's perspectives)?",
      "Do they have a positive sense of self, or adaptive coping mechanisms?",
      "Psychologically-minded, reflective, and capacity to change thinking patterns?",
      "Have they previously responded well to therapy?",
      "Good coping skills, good insight?"
    ]
  },
  "Social": {
    "Predisposing": [
      "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?",
      "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?",
      "Immigration history, marginalization, discrimination, or racism?",
      "Exposure to antisocial personality/traits"
    ],
    "Precipitating": [
      "Loss of or separation from close family, partner, or friends",
      "Interpersonal trauma",
      "Work/academic/financial stressors",
      "Recent immigration, loss of home, loss of a supportive service",
      "Is the individual's current experience/symptoms similar to a past situation?"
    ],
    "Perpetuating": [
      "Chronic marital/relationship discord, lack of empathy from family/friends",
      "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration",
      "Ongoing transitions and stressors",
      "Poor finances or working long hours",
      "Isolation, unsafe environment"
    ],
    "Protective": [
      "Positive relationships, supportive community, and/or extended family/friends?",
      "Religious/spiritual beliefs",
      "Good interpersonal supports",
      "Financial/disability support",
      "Has an outpatient healthcare team: GP, psychiatrist, social, or case worker?"
    ]
  }
}
```

Sample output:
```
{
  "Biological": {
    "Predisposing": {
      "Questions": [
        "What was their temperament at birth?",
        "What do we know about their consistent personality characteristics?",
        "Is there a family psychiatric history?",
        "Are there toxic exposures in utero, birth complications, or developmental disorders?",
        "Is there a history of concussions or traumatic brain injuries?",
        "Neurodevelopmental history"
      ],
      "Presence": {
        "What was their temperament at birth?": "Cannot be inferred/Not enough info",
        "What do we know about their consistent personality characteristics?": "Cannot be inferred/Not enough info",
        "Is there a family psychiatric history?": "Yes, there is a family history of depression in the father.",
        "Are there toxic exposures in utero, birth complications, or developmental disorders?": "No evidence of such exposures.",
        "Is there a history of concussions or traumatic brain injuries?": "No known history of concussions or traumatic brain injuries.",
        "Neurodevelopmental history": "Cannot be inferred/Not enough info"
      }
    },
    "Precipitating": {
      "Questions": [
        "Serious medical illness or injury?",
        "Increasing use of alcohol or drugs?",
        "Medication non-adherence?",
        "Pregnancy or hormonal changes?",
        "Sleep deprivation?"
      ],
      "Presence": {
        "Serious medical illness or injury?": "No serious medical illness reported.",
        "Increasing use of alcohol or drugs?": "There is increased alcohol consumption; the patient has rated their consumption as high (3).",
        "Medication non-adherence?": "There is no mention of medication non-adherence.",
        "Pregnancy or hormonal changes?": "Not applicable, as the patient is male and no pregnancy-related issues are indicated.",
        "Sleep deprivation?": "Patient reports difficulty getting out of bed, indicating possible sleep issues."
      }
    },
    "Perpetuating": {
      "Questions": [
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?",
        "Lack of medication optimization (suboptimal doses)",
        "Lack of treatment or follow up for mental illness",
        "Current substance use?",
        "Chronic medical problems, chronic pain, or disability?",
        "How is patient responding to hospitalization?",
        "What are the degree of the symptoms right now?"
      ],
      "Presence": {
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?": "No chronic illness reported, but the patient has functional impairment related to depression.",
        "Lack of medication optimization (suboptimal doses)": "There is no current medication optimization mentioned; treatment adherence is unclear.",
        "Lack of treatment or follow up for mental illness": "Yes, the patient has a history of depression but appears to lack ongoing treatment.",
        "Current substance use?": "Yes, the patient reports current substance use, including alcohol and smoking.",
        "Chronic medical problems, chronic pain, or disability?": "No chronic medical problems or disabilities are indicated.",
        "How is patient responding to hospitalization?": "Not applicable; there is no mention of hospitalization.",
        "What are the degree of the symptoms right now?": "The patient experiences significant symptoms including difficulty focusing, lack of motivation, and loss of enjoyment in activities."
      }
    },
    "Protective": {
      "Questions": [
        "Good overall health",
        "Absence of family psychiatric history",
        "What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)?",
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?",
        "No substance use is a protective factor"
      ],
      "Presence": {
        "Good overall health": "Not indicated; patient has some medical history.",
        "Absence of family psychiatric history": "No, there is a family history of psychiatric issues (father with depression).",
        "What is their response to medications?": "The patient is open to psychotherapy and medication, indicating a willingness to engage in treatment.",
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?": "The patient demonstrates insight into their emotions, suggesting some level of resilience.",
        "No substance use is a protective factor": "This is not applicable; the patient has current substance use."
      }
    }
  },
  "Psychological": {
    "Predisposing": {
      "Questions": [
        "What is their attachment style?",
        "How did their family act and what is the family structure?",
        "Do they have problems with affect modulation?",
        "Do they have a rigid or negative cognitive style?",
        "Low self-image/self-esteem?"
      ],
      "Presence": {
        "What is their attachment style?": "Cannot be inferred/Not enough info",
        "How did their family act and what is the family structure?": "The family environment appears to be negative, with reported abuse and bullying affecting development.",
        "Do they have problems with affect modulation?": "Yes, the patient has issues with regulating emotions as evidenced by depressive symptoms.",
        "Do they have a rigid or negative cognitive style?": "Yes, there are indications of a negative cognitive style, as the patient expresses feelings of low self-worth.",
        "Low self-image/self-esteem?": "Yes, the patient exhibits low self-esteem, as noted in their concerns about meaning and contribution to the world."
      }
    },
    "Precipitating": {
      "Questions": [
        "Cognitive: core beliefs and cognitive distortions",
        "Dialectical: emotional dysregulation and dysfunction",
        "Interpersonal: grief, loss, disagreement, change/transitions",
        "Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns"
      ],
      "Presence": {
        "Cognitive: core beliefs and cognitive distortions": "Yes, the patient may hold cognitive distortions related to their self-worth.",
        "Dialectical: emotional dysregulation and dysfunction": "Yes, the patient shows signs of emotional dysregulation, as indicated by depressive symptoms.",
        "Interpersonal: grief, loss, disagreement, change/transitions": "Yes, the recent lay-off signifies an interpersonal and occupational stressor.",
        "Psychodynamic: unconscious conflicts/defenses": "Yes, the formulation suggests potential unresolved conflicts from childhood."
      }
    },
    "Perpetuating": {
      "Questions": [
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment",
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance",
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions",
        "Recurring themes throughout one’s life, chronic primitive defenses",
        "What are their beliefs about self/others/world? What ideas have they internalized?",
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?",
        "Ongoing poor coping skills, limited or lack of insight?",
        "Personality traits that affect relationships (e.g. borderline personality disorder)",
        "How is their attachment style playing out in this particular situation?"
      ],
      "Presence": {
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment": "Yes, chronic negative thoughts about self are present.",
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance": "Yes, there are indications of help-seeking behavior but chronic emotional issues persist.",
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions": "Yes, past bullying and abuse indicate unresolved interpersonal issues.",
        "Recurring themes throughout one’s life, chronic primitive defenses": "Yes, there are recurring themes related to self-worth and control.",
        "What are their beliefs about self/others/world?": "The patient struggles with feelings of meaninglessness and a lack of contribution.",
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?": "Yes, possible auditory hallucinations suggest self-destructive mechanisms.",
        "Ongoing poor coping skills, limited or lack of insight?": "Yes, ongoing coping issues are suggested by their current struggles.",
        "Personality traits that affect relationships": "Cannot be inferred/Not enough info.",
        "How is their attachment style playing out in this particular situation?": "Cannot be inferred/Not enough info."
      }
    }
  },
  "Social": {
    "Predisposing": {
      "Questions": [
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?",
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?",
        "Immigration history, marginalization, discrimination, or racism?",
        "Exposure to antisocial personality/traits"
      ],
      "Presence": {
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?": "Cannot be inferred/Not enough info.",
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?": "Yes, the patient has a history of bullying and abuse.",
        "Immigration history, marginalization, discrimination, or racism?": "Not applicable; no mention of such factors.",
        "Exposure to antisocial personality/traits": "Not applicable; no mention of such factors."
      }
    },
    "Precipitating": {
      "Questions": [
        "Loss of or separation from close family, partner, or friends",
        "Interpersonal trauma",
        "Work/academic/financial stressors",
        "Recent immigration, loss of home, loss of a supportive service",
        "Is the individual's current experience/symptoms similar to a past situation?"
      ],
      "Presence": {
        "Loss of or separation from close family, partner, or friends": "Yes, the recent lay-off signifies a loss of work relationships.",
        "Interpersonal trauma": "Cannot be inferred/Not enough info.",
        "Work/academic/financial stressors": "Yes, the patient is experiencing financial stress due to lay-off.",
        "Recent immigration, loss of home, loss of a supportive service": "Not applicable; no mention of such factors.",
        "Is the individual's current experience/symptoms similar to a past situation?": "Yes, the patient exhibits signs of history repeating itself."
      }
    },
    "Perpetuating": {
      "Questions": [
        "Chronic marital/relationship discord, lack of empathy from family/friends",
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration",
        "Ongoing transitions and stressors",
        "Poor finances or working long hours",
        "Isolation, unsafe environment"
      ],
      "Presence": {
        "Chronic marital/relationship discord, lack of empathy from family/friends": "Cannot be inferred/Not enough info.",
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration": "Not applicable; no mention of such factors.",
        "Ongoing transitions and stressors": "Yes, the patient is facing ongoing stress from recent lay-offs.",
        "Poor finances or working long hours": "Yes, the patient is under financial stress due to unemployment.",
        "Isolation, unsafe environment": "Cannot be inferred/Not enough info."
      }
    }
  }
}
```

Step 2: 
**input :** database of answers (categorised by the headings in the table, ie should have 12 databases of answers), all triage forms
**output :** triage forms with coded categories

Prompt

```
Prompt for Step 2: Categorizing the Data
I have patient data categorized into biological, psychological, and social factors from a triage form. I need to code the qualitative information into quantitative values for data analysis. Use the coding scheme provided below to translate the data. If the field does not apply, omit it. Return a JSON output with numeric codes for the specified categories, and retain other values as provided.

For multi-coded fields, return them as a comma-separated list. No explanation is needed, just return the coded results.

Coding Scheme:
json

Example Input:
json

{
  "Biological": {
    "Predisposing": {
      "Questions": [
        "What was their temperament at birth?",
        "What do we know about their consistent personality characteristics?",
        "Is there a family psychiatric history?",
        "Are there toxic exposures in utero, birth complications, or developmental disorders?",
        "Is there a history of concussions or traumatic brain injuries?",
        "Neurodevelopmental history"
      ],
      "Presence": {
        "What was their temperament at birth?": "Cannot be inferred/Not enough info",
        "What do we know about their consistent personality characteristics?": "Cannot be inferred/Not enough info",
        "Is there a family psychiatric history?": "Yes, there is a family history of depression in the father.",
        "Are there toxic exposures in utero, birth complications, or developmental disorders?": "No evidence of such exposures.",
        "Is there a history of concussions or traumatic brain injuries?": "No known history of concussions or traumatic brain injuries.",
        "Neurodevelopmental history": "Cannot be inferred/Not enough info"
      }
    },
    "Precipitating": {
      "Questions": [
        "Serious medical illness or injury?",
        "Increasing use of alcohol or drugs?",
        "Medication non-adherence?",
        "Pregnancy or hormonal changes?",
        "Sleep deprivation?"
      ],
      "Presence": {
        "Serious medical illness or injury?": "No serious medical illness reported.",
        "Increasing use of alcohol or drugs?": "There is increased alcohol consumption; the patient has rated their consumption as high (3).",
        "Medication non-adherence?": "There is no mention of medication non-adherence.",
        "Pregnancy or hormonal changes?": "Not applicable, as the patient is male and no pregnancy-related issues are indicated.",
        "Sleep deprivation?": "Patient reports difficulty getting out of bed, indicating possible sleep issues."
      }
    },
    "Perpetuating": {
      "Questions": [
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?",
        "Lack of medication optimization (suboptimal doses)",
        "Lack of treatment or follow up for mental illness",
        "Current substance use?",
        "Chronic medical problems, chronic pain, or disability?",
        "How is patient responding to hospitalization?",
        "What are the degree of the symptoms right now?"
      ],
      "Presence": {
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?": "No chronic illness reported, but the patient has functional impairment related to depression.",
        "Lack of medication optimization (suboptimal doses)": "There is no current medication optimization mentioned; treatment adherence is unclear.",
        "Lack of treatment or follow up for mental illness": "Yes, the patient has a history of depression but appears to lack ongoing treatment.",
        "Current substance use?": "Yes, the patient reports current substance use, including alcohol and smoking.",
        "Chronic medical problems, chronic pain, or disability?": "No chronic medical problems or disabilities are indicated.",
        "How is patient responding to hospitalization?": "Not applicable; there is no mention of hospitalization.",
        "What are the degree of the symptoms right now?": "The patient experiences significant symptoms including difficulty focusing, lack of motivation, and loss of enjoyment in activities."
      }
    },
    "Protective": {
      "Questions": [
        "Good overall health",
        "Absence of family psychiatric history",
        "What is their response to medications (good response/no response, did they achieve remission, are they optimized on current medications)?",
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?",
        "No substance use is a protective factor"
      ],
      "Presence": {
        "Good overall health": "Not indicated; patient has some medical history.",
        "Absence of family psychiatric history": "No, there is a family history of psychiatric issues (father with depression).",
        "What is their response to medications?": "The patient is open to psychotherapy and medication, indicating a willingness to engage in treatment.",
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?": "The patient demonstrates insight into their emotions, suggesting some level of resilience.",
        "No substance use is a protective factor": "This is not applicable; the patient has current substance use."
      }
    }
  },
  "Psychological": {
    "Predisposing": {
      "Questions": [
        "What is their attachment style?",
        "How did their family act and what is the family structure?",
        "Do they have problems with affect modulation?",
        "Do they have a rigid or negative cognitive style?",
        "Low self-image/self-esteem?"
      ],
      "Presence": {
        "What is their attachment style?": "Cannot be inferred/Not enough info",
        "How did their family act and what is the family structure?": "The family environment appears to be negative, with reported abuse and bullying affecting development.",
        "Do they have problems with affect modulation?": "Yes, the patient has issues with regulating emotions as evidenced by depressive symptoms.",
        "Do they have a rigid or negative cognitive style?": "Yes, there are indications of a negative cognitive style, as the patient expresses feelings of low self-worth.",
        "Low self-image/self-esteem?": "Yes, the patient exhibits low self-esteem, as noted in their concerns about meaning and contribution to the world."
      }
    },
    "Precipitating": {
      "Questions": [
        "Cognitive: core beliefs and cognitive distortions",
        "Dialectical: emotional dysregulation and dysfunction",
        "Interpersonal: grief, loss, disagreement, change/transitions",
        "Psychodynamic: unconscious conflicts/defenses, and unconscious repetition of early relationship patterns"
      ],
      "Presence": {
        "Cognitive: core beliefs and cognitive distortions": "Yes, the patient may hold cognitive distortions related to their self-worth.",
        "Dialectical: emotional dysregulation and dysfunction": "Yes, the patient shows signs of emotional dysregulation, as indicated by depressive symptoms.",
        "Interpersonal: grief, loss, disagreement, change/transitions": "Yes, the recent lay-off signifies an interpersonal and occupational stressor.",
        "Psychodynamic: unconscious conflicts/defenses": "Yes, the formulation suggests potential unresolved conflicts from childhood."
      }
    },
    "Perpetuating": {
      "Questions": [
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment",
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance",
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions",
        "Recurring themes throughout one’s life, chronic primitive defenses",
        "What are their beliefs about self/others/world? What ideas have they internalized?",
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?",
        "Ongoing poor coping skills, limited or lack of insight?",
        "Personality traits that affect relationships (e.g. borderline personality disorder)",
        "How is their attachment style playing out in this particular situation?"
      ],
      "Presence": {
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment": "Yes, chronic negative thoughts about self are present.",
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance": "Yes, there are indications of help-seeking behavior but chronic emotional issues persist.",
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions": "Yes, past bullying and abuse indicate unresolved interpersonal issues.",
        "Recurring themes throughout one’s life, chronic primitive defenses": "Yes, there are recurring themes related to self-worth and control.",
        "What are their beliefs about self/others/world?": "The patient struggles with feelings of meaninglessness and a lack of contribution.",
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?": "Yes, possible auditory hallucinations suggest self-destructive mechanisms.",
        "Ongoing poor coping skills, limited or lack of insight?": "Yes, ongoing coping issues are suggested by their current struggles.",
        "Personality traits that affect relationships": "Cannot be inferred/Not enough info.",
        "How is their attachment style playing out in this particular situation?": "Cannot be inferred/Not enough info."
      }
    }
  },
  "Social": {
    "Predisposing": {
      "Questions": [
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?",
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?",
        "Immigration history, marginalization, discrimination, or racism?",
        "Exposure to antisocial personality/traits"
      ],
      "Presence": {
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?": "Cannot be inferred/Not enough info.",
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?": "Yes, the patient has a history of bullying and abuse.",
        "Immigration history, marginalization, discrimination, or racism?": "Not applicable; no mention of such factors.",
        "Exposure to antisocial personality/traits": "Not applicable; no mention of such factors."
      }
    },
    "Precipitating": {
      "Questions": [
        "Loss of or separation from close family, partner, or friends",
        "Interpersonal trauma",
        "Work/academic/financial stressors",
        "Recent immigration, loss of home, loss of a supportive service",
        "Is the individual's current experience/symptoms similar to a past situation?"
      ],
      "Presence": {
        "Loss of or separation from close family, partner, or friends": "Yes, the recent lay-off signifies a loss of work relationships.",
        "Interpersonal trauma": "Cannot be inferred/Not enough info.",
        "Work/academic/financial stressors": "Yes, the patient is experiencing financial stress due to lay-off.",
        "Recent immigration, loss of home, loss of a supportive service": "Not applicable; no mention of such factors.",
        "Is the individual's current experience/symptoms similar to a past situation?": "Yes, the patient exhibits signs of history repeating itself."
      }
    },
    "Perpetuating": {
      "Questions": [
        "Chronic marital/relationship discord, lack of empathy from family/friends",
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration",
        "Ongoing transitions and stressors",
        "Poor finances or working long hours",
        "Isolation, unsafe environment"
      ],
      "Presence": {
        "Chronic marital/relationship discord, lack of empathy from family/friends": "Cannot be inferred/Not enough info.",
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration": "Not applicable; no mention of such factors.",
        "Ongoing transitions and stressors": "Yes, the patient is facing ongoing stress from recent lay-offs.",
        "Poor finances or working long hours": "Yes, the patient is under financial stress due to unemployment.",
        "Isolation, unsafe environment": "Cannot be inferred/Not enough info."
      }
    }
  }
}


Output:
Return the input data with the qualitative factors replaced by their corresponding numeric codes based on the coding scheme provided.
```

Sample output:
```
{
  "Biological": {
    "Predisposing": {
      "Presence": {
        "What was their temperament at birth?": "0",  // Cannot be inferred
        "What do we know about their consistent personality characteristics?": "0",  // Cannot be inferred
        "Is there a family psychiatric history?": "1",  // Family history of depression
        "Are there toxic exposures in utero, birth complications, or developmental disorders?": "0",  // No evidence
        "Is there a history of concussions or traumatic brain injuries?": "0",  // No known history
        "Neurodevelopmental history": "0"  // Cannot be inferred
      }
    },
    "Precipitating": {
      "Presence": {
        "Serious medical illness or injury?": "0",  // No serious medical illness
        "Increasing use of alcohol or drugs?": "1",  // Increased alcohol consumption
        "Medication non-adherence?": "0",  // No mention of non-adherence
        "Pregnancy or hormonal changes?": "0",  // Not applicable
        "Sleep deprivation?": "1"  // Possible sleep issues
      }
    },
    "Perpetuating": {
      "Presence": {
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?": "0",  // No chronic illness
        "Lack of medication optimization (suboptimal doses)": "0",  // Not mentioned
        "Lack of treatment or follow up for mental illness": "1",  // Lack of ongoing treatment
        "Current substance use?": "1",  // Reports substance use
        "Chronic medical problems, chronic pain, or disability?": "0",  // No chronic problems indicated
        "How is patient responding to hospitalization?": "0",  // Not applicable
        "What are the degree of the symptoms right now?": "1"  // Significant symptoms present
      }
    },
    "Protective": {
      "Presence": {
        "Good overall health": "0",  // Not indicated
        "Absence of family psychiatric history": "0",  // Family history of psychiatric issues
        "What is their response to medications?": "1",  // Open to treatment
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?": "1",  // Indicates resilience
        "No substance use is a protective factor": "0"  // Substance use present
      }
    }
  },
  "Psychological": {
    "Predisposing": {
      "Presence": {
        "What is their attachment style?": "0",  // Cannot be inferred
        "How did their family act and what is the family structure?": "1",  // Negative family environment
        "Do they have problems with affect modulation?": "1",  // Issues with emotional regulation
        "Do they have a rigid or negative cognitive style?": "1",  // Negative cognitive style indicated
        "Low self-image/self-esteem?": "1"  // Low self-esteem present
      }
    },
    "Precipitating": {
      "Presence": {
        "Cognitive: core beliefs and cognitive distortions": "1",  // Cognitive distortions related to self-worth
        "Dialectical: emotional dysregulation and dysfunction": "1",  // Signs of emotional dysregulation
        "Interpersonal: grief, loss, disagreement, change/transitions": "1",  // Lay-off as stressor
        "Psychodynamic: unconscious conflicts/defenses": "1"  // Suggests unresolved conflicts
      }
    },
    "Perpetuating": {
      "Presence": {
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment": "1",  // Chronic negative thoughts present
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance": "1",  // Help-seeking behavior indicated
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions": "1",  // Indicates unresolved issues
        "Recurring themes throughout one’s life, chronic primitive defenses": "1",  // Recurring themes of self-worth
        "What are their beliefs about self/others/world?": "1",  // Struggles with feelings of meaninglessness
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?": "1",  // Possible auditory hallucinations
        "Ongoing poor coping skills, limited or lack of insight?": "1",  // Ongoing coping issues noted
        "Personality traits that affect relationships": "0",  // Cannot be inferred
        "How is their attachment style playing out in this particular situation?": "0"  // Cannot be inferred
      }
    }
  },
  "Social": {
    "Predisposing": {
      "Presence": {
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?": "0",  // Cannot be inferred
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?": "1",  // History of abuse and bullying
        "Immigration history, marginalization, discrimination, or racism?": "0",  // Not applicable
        "Exposure to antisocial personality/traits": "0"  // Not applicable
      }
    },
    "Precipitating": {
      "Presence": {
        "Loss of or separation from close family, partner, or friends": "1",  // Recent lay-off signifies loss
        "Interpersonal trauma": "0",  // Cannot be inferred
        "Work/academic/financial stressors": "1",  // Financial stress due to lay-off
        "Recent immigration, loss of home, loss of a supportive service": "0",  // Not applicable
        "Is the individual's current experience/symptoms similar to a past situation?": "1"  // Signs of history repeating itself
      }
    },
    "Perpetuating": {
      "Presence": {
        "Chronic marital/relationship discord, lack of empathy from family/friends": "0",  // Cannot be inferred
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration": "0",  // Not applicable
        "Ongoing transitions and stressors": "1",  // Yes, the patient is facing ongoing stress from recent lay-offs.
        "Poor finances or working long hours": "1",  // Yes, the patient is under financial stress due to unemployment.
        "Isolation, unsafe environment": "0"  // Cannot be inferred
      }
    }
  }
}
```

### Step 4: Questionaire

### Questionnaire for Patient Assessment

### 

Integration into Your Pipeline:

1. Use ChatGPT to analyze and score the responses.
2. Integrate these scores back into your patient records and treatment plans.
3. Use the insights from the scores to guide therapeutic interventions and monitor progress over time.

Prompt:
```
Prompt for Populating the Patient Assessment Questionnaire
You are provided with structured patient data extracted from a triage form, along with categorized biological, psychological, and social factors related to the patient's mental health assessment. Your task is to populate a detailed questionnaire designed to assess various factors influencing the patient's mental well-being.

Patient Data:

json
Copy code
{
    "Filename": "Simulated Triage Form #1.docx",
    "Age": 4,
    "Ethnicity": 1,
    "Gender": 1,
    "Occupation": 3,
    "Past_Psychiatric_History": 0,
    "Past_Admissions_to_IMH": 0,
    "Past_Medical_History": 1,
    "Family_Medical_History": 1,
    "Diagnosis": "Depression",
    "Presenting_Concerns": "Unable to focus at work, missing many days, doesn’t feel like getting up from bed, not enjoying hobbies like fishing or reading",
    "Symptoms": 1,
    "Living_Arrangement": 0,
    "Pack_Years": 3,
    "Alcohol_Consumption": 3,
    "Functional_Impairment": 0,
    "Precipitating_Factors": 1,
    "Protective_Factors": 4,
    "Predisposing_Factors": 4,
    "Coping_Mechanisms": 2,
    "Formulation": "Long history of low self-esteem, lack of control over situations, persistent negative ruminations, possible auditory hallucinations to explore further",
    "Social_History": 1,
    "Substance_Use": {
        "Smoking": 3,
        "Alcohol": 3
    },
    "Suicidal_Ideation": 1,
    "Aggression": 1
}
4 P’s Categorization:

json
{
  "Biological": {
    "Predisposing": {
      "Presence": {
        "What was their temperament at birth?": "0",  // Cannot be inferred
        "What do we know about their consistent personality characteristics?": "0",  // Cannot be inferred
        "Is there a family psychiatric history?": "1",  // Family history of depression
        "Are there toxic exposures in utero, birth complications, or developmental disorders?": "0",  // No evidence
        "Is there a history of concussions or traumatic brain injuries?": "0",  // No known history
        "Neurodevelopmental history": "0"  // Cannot be inferred
      }
    },
    "Precipitating": {
      "Presence": {
        "Serious medical illness or injury?": "0",  // No serious medical illness
        "Increasing use of alcohol or drugs?": "1",  // Increased alcohol consumption
        "Medication non-adherence?": "0",  // No mention of non-adherence
        "Pregnancy or hormonal changes?": "0",  // Not applicable
        "Sleep deprivation?": "1"  // Possible sleep issues
      }
    },
    "Perpetuating": {
      "Presence": {
        "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?": "0",  // No chronic illness
        "Lack of medication optimization (suboptimal doses)": "0",  // Not mentioned
        "Lack of treatment or follow up for mental illness": "1",  // Lack of ongoing treatment
        "Current substance use?": "1",  // Reports substance use
        "Chronic medical problems, chronic pain, or disability?": "0",  // No chronic problems indicated
        "How is patient responding to hospitalization?": "0",  // Not applicable
        "What are the degree of the symptoms right now?": "1"  // Significant symptoms present
      }
    },
    "Protective": {
      "Presence": {
        "Good overall health": "0",  // Not indicated
        "Absence of family psychiatric history": "0",  // Family history of psychiatric issues
        "What is their response to medications?": "1",  // Open to treatment
        "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?": "1",  // Indicates resilience
        "No substance use is a protective factor": "0"  // Substance use present
      }
    }
  },
  "Psychological": {
    "Predisposing": {
      "Presence": {
        "What is their attachment style?": "0",  // Cannot be inferred
        "How did their family act and what is the family structure?": "1",  // Negative family environment
        "Do they have problems with affect modulation?": "1",  // Issues with emotional regulation
        "Do they have a rigid or negative cognitive style?": "1",  // Negative cognitive style indicated
        "Low self-image/self-esteem?": "1"  // Low self-esteem present
      }
    },
    "Precipitating": {
      "Presence": {
        "Cognitive: core beliefs and cognitive distortions": "1",  // Cognitive distortions related to self-worth
        "Dialectical: emotional dysregulation and dysfunction": "1",  // Signs of emotional dysregulation
        "Interpersonal: grief, loss, disagreement, change/transitions": "1",  // Lay-off as stressor
        "Psychodynamic: unconscious conflicts/defenses": "1"  // Suggests unresolved conflicts
      }
    },
    "Perpetuating": {
      "Presence": {
        "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment": "1",  // Chronic negative thoughts present
        "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance": "1",  // Help-seeking behavior indicated
        "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions": "1",  // Indicates unresolved issues
        "Recurring themes throughout one’s life, chronic primitive defenses": "1",  // Recurring themes of self-worth
        "What are their beliefs about self/others/world?": "1",  // Struggles with feelings of meaninglessness
        "Are there self-destructive coping mechanisms, or traumatic re-enactments?": "1",  // Possible auditory hallucinations
        "Ongoing poor coping skills, limited or lack of insight?": "1",  // Ongoing coping issues noted
        "Personality traits that affect relationships": "0",  // Cannot be inferred
        "How is their attachment style playing out in this particular situation?": "0"  // Cannot be inferred
      }
    }
  },
  "Social": {
    "Predisposing": {
      "Presence": {
        "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?": "0",  // Cannot be inferred
        "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?": "1",  // History of abuse and bullying
        "Immigration history, marginalization, discrimination, or racism?": "0",  // Not applicable
        "Exposure to antisocial personality/traits": "0"  // Not applicable
      }
    },
    "Precipitating": {
      "Presence": {
        "Loss of or separation from close family, partner, or friends": "1",  // Recent lay-off signifies loss
        "Interpersonal trauma": "0",  // Cannot be inferred
        "Work/academic/financial stressors": "1",  // Financial stress due to lay-off
        "Recent immigration, loss of home, loss of a supportive service": "0",  // Not applicable
        "Is the individual's current experience/symptoms similar to a past situation?": "1"  // Signs of history repeating itself
      }
    },
    "Perpetuating": {
      "Presence": {
        "Chronic marital/relationship discord, lack of empathy from family/friends": "0",  // Cannot be inferred
        "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration": "0",  // Not applicable
        "Ongoing transitions and stressors": "1",  // Yes, the patient is facing ongoing stress from recent lay-offs.
        "Poor finances or working long hours": "1",  // Yes, the patient is under financial stress due to unemployment.
        "Isolation, unsafe environment": "0"  // Cannot be inferred
      }
    }
  }
}


Task: Using the above patient data and categorized 4 P's information, please populate the following questionnaire to the best of your ability.
Do sound off if you are not able to make an intelligent guess due to lack of information.

Multidimensional Scale of Perceived Social Support (MSPSS)

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

Scale Items and Response Options
Each item is rated on a 5-point Likert scale:

0 = Strongly Disagree
1 = Disagree
2 = NA # neither agree or disagree
3 = Agree
4 = Strongly Agree

 0 - NA, 
 provide all the lines that led to the decision 


Please provide the populated responses based on the patient data provided.
```

Sample output:
```
{
  "MSPSS": {
    "1": {
      "Statement": "There is a special person who is around when I am in need.",
      "Response": 3  // Agree - The patient has some level of family support.
    },
    "2": {
      "Statement": "There is a special person with whom I can share my joys and sorrows.",
      "Response": 2  // Neutral - No clear indication of such a person.
    },
    "3": {
      "Statement": "My family really tries to help me.",
      "Response": 4  // Strongly Agree - Family support is indicated.
    },
    "4": {
      "Statement": "I get the emotional help and support I need from my family.",
      "Response": 3  // Agree - Family provides some emotional support.
    },
    "5": {
      "Statement": "I have a special person who is a real source of comfort to me.",
      "Response": 2  // Neutral - Cannot infer specific comfort sources.
    },
    "6": {
      "Statement": "My friends really try to help me.",
      "Response": 2  // Neutral - Limited information about friends.
    },
    "7": {
      "Statement": "I can count on my friends when things go wrong.",
      "Response": 2  // Neutral - No specific mention of friendship support.
    },
    "8": {
      "Statement": "I can talk about my problems with my family.",
      "Response": 4  // Strongly Agree - Indicates willingness to engage with family.
    },
    "9": {
      "Statement": "I have friends with whom I can share my joys and sorrows.",
      "Response": 2  // Neutral - Insufficient information about friendships.
    },
    "10": {
      "Statement": "There is a special person in my life who cares about my feelings.",
      "Response": 3  // Agree - Some indication of caring individuals, possibly family.
    },
    "11": {
      "Statement": "My family is willing to help me make decisions.",
      "Response": 4  // Strongly Agree - Family is noted to provide support.
    },
    "12": {
      "Statement": "I can talk about my problems with my friends.",
      "Response": 2  // Neutral - Insufficient information about friend interactions.
    }
  }
}
```

### Validation

Sample to validate - refer to code










