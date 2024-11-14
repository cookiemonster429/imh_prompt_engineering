from pydantic import BaseModel, conint, constr
from typing import Dict
import json  # Import the json library for pretty printing

class SubstanceUse(BaseModel):
    Smoking: conint(ge=0)  # Must be a non-negative integer
    Alcohol: conint(ge=0)

class BiologicalFactors(BaseModel):
    Predisposing: Dict[str, Dict[str, str]]  # Include questions and presence
    Precipitating: Dict[str, Dict[str, str]]
    Perpetuating: Dict[str, Dict[str, str]]
    Protective: Dict[str, Dict[str, str]]

class PsychologicalFactors(BaseModel):
    Predisposing: Dict[str, Dict[str, str]]
    Precipitating: Dict[str, Dict[str, str]]
    Perpetuating: Dict[str, Dict[str, str]]
    Protective: Dict[str, Dict[str, str]]  # Ensure this field exists

class SocialFactors(BaseModel):
    Predisposing: Dict[str, Dict[str, str]]
    Precipitating: Dict[str, Dict[str, str]]
    Perpetuating: Dict[str, Dict[str, str]]
    Protective: Dict[str, Dict[str, str]]  # Ensure this field exists

class PatientData(BaseModel):
    Filename: constr(min_length=1)
    Age: conint(ge=0)  # Age must be a non-negative integer
    Ethnicity: conint(ge=1, le=5)  # Assuming ethnicity is coded 1 to 5
    Gender: conint(ge=0, le=1)  # Assuming 0 = Female, 1 = Male
    Occupation: constr(min_length=1)  # Occupation is a string
    Past_Psychiatric_History: conint(ge=0, le=1)
    Past_Admissions_to_IMH: conint(ge=0, le=1)
    Past_Medical_History: conint(ge=0, le=1)
    Family_Medical_History: conint(ge=0, le=1)
    Diagnosis: constr(min_length=1)
    Presenting_Concerns: constr(min_length=1)
    Symptoms: conint(ge=0, le=1)
    Living_Arrangement: conint(ge=0, le=4)  # Assuming living arrangements are coded 0 to 4
    Pack_Years: conint(ge=0)
    Alcohol_Consumption: conint(ge=0, le=3)  # Assuming alcohol consumption is coded 0 to 3
    Functional_Impairment: conint(ge=0, le=3)  # Assuming functional impairment is coded 0 to 3
    Coping_Mechanisms: conint(ge=0, le=3)  # Assuming coping mechanisms coded 0 to 3
    Formulation: constr(min_length=1)
    Social_History: conint(ge=0, le=3)  # Assuming social history coded 0 to 3
    Substance_Use: SubstanceUse
    Suicidal_Ideation: conint(ge=0, le=1)  # Assuming binary coded
    Aggression: conint(ge=0, le=3)  # Assuming aggression coded 0 to 3
    Biological: BiologicalFactors
    Psychological: PsychologicalFactors
    Social: SocialFactors

# Sample Patient Data
patient_data = {
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
    "Coping_Mechanisms": 2,
    "Formulation": "Long history of low self-esteem issues and is constantly bothered by his lack of meaning and contribution to the world around him. This lack of control over his situation in early childhood has continued throughout adulthood. Possible auditory hallucinations to explore further.",
    "Social_History": 1,
    "Substance_Use": {
        "Smoking": 3,
        "Alcohol": 3
    },
    "Suicidal_Ideation": 1,
    "Aggression": 3,
    "Biological": {
        "Predisposing": {
            "Presence": {
                "What was their temperament at birth?": "0",
                "What do we know about their consistent personality characteristics?": "0",
                "Is there a family psychiatric history?": "1",
                "Are there toxic exposures in utero, birth complications, or developmental disorders?": "0",
                "Is there a history of concussions or traumatic brain injuries?": "0",
                "Neurodevelopmental history": "0"
            }
        },
        "Precipitating": {
            "Presence": {
                "Serious medical illness or injury?": "0",
                "Increasing use of alcohol or drugs?": "1",
                "Medication non-adherence?": "0",
                "Pregnancy or hormonal changes?": "0",
                "Sleep deprivation?": "1"
            }
        },
        "Perpetuating": {
            "Presence": {
                "Do they have a chronic illness, functional impairment caused by cognitive deficits, or a learning disorder?": "0",
                "Lack of medication optimization (suboptimal doses)": "0",
                "Lack of treatment or follow up for mental illness": "1",
                "Current substance use?": "1",
                "Chronic medical problems, chronic pain, or disability?": "0",
                "How is patient responding to hospitalization?": "0",
                "What are the degree of the symptoms right now?": "1"
            }
        },
        "Protective": {
            "Presence": {
                "Good overall health": "0",
                "Absence of family psychiatric history": "0",
                "What is their response to medications?": "1",
                "Do they have above-average intelligence, easy temperament, resiliency, specific talents or abilities?": "1",
                "No substance use is a protective factor": "0"
            }
        }
    },
    "Psychological": {
        "Predisposing": {
            "Presence": {
                "What is their attachment style?": "0",
                "How did their family act and what is the family structure?": "1",
                "Do they have problems with affect modulation?": "1",
                "Do they have a rigid or negative cognitive style?": "1",
                "Low self-image/self-esteem?": "1"
            }
        },
        "Precipitating": {
            "Presence": {
                "Cognitive: core beliefs and cognitive distortions": "1",
                "Dialectical: emotional dysregulation and dysfunction": "1",
                "Interpersonal: grief, loss, disagreement, change/transitions": "1",
                "Psychodynamic: unconscious conflicts/defenses": "1"
            }
        },
        "Perpetuating": {
            "Presence": {
                "One or more perpetuating psychological processes: chronic negative thoughts and reinforcing environment": "1",
                "Help-seeking and help-rejecting, chronic emotional dysregulation and poor distress tolerance": "1",
                "Chronic/unresolved dysfunctional relationships, interpersonal conflicts, or role transitions": "1",
                "Recurring themes throughout one’s life, chronic primitive defenses": "1",
                "What are their beliefs about self/others/world?": "1",
                "Are there self-destructive coping mechanisms, or traumatic re-enactments?": "1",
                "Ongoing poor coping skills, limited or lack of insight?": "1",
                "Personality traits that affect relationships": "0",
                "How is their attachment style playing out in this particular situation?": "0"
            }
        },
        "Protective": {
            "Presence": {
                "Do they have ability to be reflective or modulate their affect?": "1",
                "Do they have ability to mentalize (see other's perspectives)?": "1",
                "Do they have a positive sense of self, or adaptive coping mechanisms?": "1",
                "Psychologically-minded, reflective, and capacity to change thinking patterns?": "1",
                "Have they previously responded well to therapy?": "1",
                "Good coping skills, good insight?": "1"
            }
        }
    },
    "Social": {
        "Predisposing": {
            "Presence": {
                "Poverty, low socioeconomic status, teenage parenthood, or poor access to health care?": "0",
                "Childhood exposure to maternal depression, domestic violence, late adoption, temperament mismatch, or marital conflicts?": "1",
                "Immigration history, marginalization, discrimination, or racism?": "0",
                "Exposure to antisocial personality/traits": "0"
            }
        },
        "Precipitating": {
            "Presence": {
                "Loss of or separation from close family, partner, or friends": "1",
                "Interpersonal trauma": "0",
                "Work/academic/financial stressors": "1",
                "Recent immigration, loss of home, loss of a supportive service": "0",
                "Is the individual's current experience/symptoms similar to a past situation?": "1"
            }
        },
        "Perpetuating": {
            "Presence": {
                "Chronic marital/relationship discord, lack of empathy from family/friends": "0",
                "Chronically dangerous or hostile neighborhood, trans-generational problems of immigration": "0",
                "Ongoing transitions and stressors": "1",
                "Poor finances or working long hours": "1",
                "Isolation, unsafe environment": "0"
            }
        },
        "Protective": {
            "Presence": {
                "Positive relationships, supportive community, and/or extended family/friends?": "1",
                "Religious/spiritual beliefs": "0",
                "Good interpersonal supports": "1",
                "Financial/disability support": "0",
                "Has an outpatient healthcare team: GP, psychiatrist, social, or case worker?": "1"
            }
        }
    }
}

# Validate the data
try:
    validated_patient = PatientData(**patient_data)
    print("Validation successful:")
    # Use json.dumps for pretty printing
    # print(json.dumps(validated_patient.dict(), indent=2))  # Pretty-print the validated output
except Exception as e:
    print("Validation error:", e)
