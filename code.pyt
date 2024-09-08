import tkinter as tk
from tkinter import messagebox

diseases = {
    "Common Cold": {
        "symptoms": ["runny nose", "sore throat", "cough", "congestion", "slight body aches", "sneezing"],
        "treatment": ["decongestants", "antihistamines", "cough suppressants", "pain relievers", "rest", "hydration"]
    },
    "Flu": {
        "symptoms": ["fever", "chills", "muscle aches", "cough", "congestion", "runny nose", "fatigue"],
        "treatment": ["antiviral medications", "pain relievers", "rest", "hydration"]
    },
    "COVID-19": {
        "symptoms": ["fever", "dry cough", "tiredness", "loss of taste or smell", "difficulty breathing", "chest pain"],
        "treatment": ["rest", "hydration", "pain relievers", "fever reducers", "medical attention if severe"]
    },
    "Strep Throat": {
        "symptoms": ["sore throat", "painful swallowing", "red and swollen tonsils", "fever", "headache", "rash"],
        "treatment": ["antibiotics", "pain relievers", "rest", "hydration"]
    }
}

def check_symptoms():
    input_symptoms = symptom_entry.get()
    symptoms = [symptom.strip().lower() for symptom in input_symptoms.split(',')]
    found_diseases = []

    for disease, info in diseases.items():
        matched_symptoms = set(info["symptoms"]).intersection(symptoms)
        if matched_symptoms:
            found_diseases.append((disease, matched_symptoms, info["treatment"]))

    result_text.delete(1.0, tk.END)

    if found_diseases:
        for disease, matched_symptoms, treatments in found_diseases:
            result_text.insert(tk.END, f"Disease: {disease}\n")
            result_text.insert(tk.END, f"Matched Symptoms: {', '.join(matched_symptoms)}\n")
            result_text.insert(tk.END, f"Treatments: {', '.join(treatments)}\n\n")
    else:
        messagebox.showinfo("No Match", "No matching diseases found. Please consult a doctor for a proper diagnosis.")

# Create main window
root = tk.Tk()
root.title("Symptom Checker")
root.geometry("500x400")
root.configure(bg="#f8f9fa")

# Create and place widgets
header_label = tk.Label(root, text="Symptom Checker", font=("Segoe UI", 18), bg="#f8f9fa", fg="#007bff")
header_label.pack(pady=20)

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, borderwidth=1)
frame.pack(padx=10, pady=10, fill="both", expand=True)

symptom_label = tk.Label(frame, text="Enter your symptoms (comma separated):", font=("Segoe UI", 12), bg="#ffffff")
symptom_label.pack(anchor="w")

symptom_entry = tk.Entry(frame, font=("Segoe UI", 12), width=50)
symptom_entry.pack(pady=10)

check_button = tk.Button(frame, text="Check", font=("Segoe UI", 12), bg="#007bff", fg="white", command=check_symptoms)
check_button.pack(pady=10)

result_text = tk.Text(frame, font=("Segoe UI", 12), height=10, bg="#e9ecef")
result_text.pack(pady=10, fill="both", expand=True)

# Run the application
root.mainloop()
